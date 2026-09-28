#!/usr/bin/env python3
from __future__ import annotations

import io
import json
import os
import re
import smtplib
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from copy import deepcopy
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import markdown
import requests
import yaml
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "paper_watch.yml"
UA = "drkamoshika-paper-watch/1.0 (GitHub Actions)"


class PaperWatchError(RuntimeError):
    pass


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    required = [
        "sources",
        "max_papers",
        "retrieval",
        "topics",
        "summary",
        "deduplication",
        "output",
        "selection",
        "task_instructions",
    ]
    missing = [k for k in required if k not in cfg]
    if missing:
        raise PaperWatchError(f"Invalid config; missing keys: {', '.join(missing)}")
    if cfg["deduplication"].get("seen_file") != "state/seen_papers.txt":
        raise PaperWatchError(
            "This runner only permits state/seen_papers.txt as the deduplication state file."
        )
    if cfg["output"].get("mode") != "gmail_only":
        raise PaperWatchError("This runner expects output.mode=gmail_only.")
    return cfg


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise PaperWatchError(f"Missing required environment variable/secret: {name}")
    return value


def seen_path(cfg: dict[str, Any]) -> Path:
    path = (ROOT / cfg["deduplication"]["seen_file"]).resolve()
    allowed = (ROOT / "state" / "seen_papers.txt").resolve()
    if path != allowed:
        raise PaperWatchError(f"Refusing to use unexpected seen-file path: {path}")
    return path


def read_seen(cfg: dict[str, Any]) -> set[str]:
    path = seen_path(cfg)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("", encoding="utf-8")
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def text_of(elem: ET.Element | None) -> str:
    if elem is None:
        return ""
    return " ".join("".join(elem.itertext()).split())


def request_get(
    url: str, *, params: dict[str, Any] | None = None, timeout: int = 45
) -> requests.Response:
    r = requests.get(
        url, params=params, headers={"User-Agent": UA}, timeout=timeout
    )
    r.raise_for_status()
    return r


def arxiv_candidates(cfg: dict[str, Any]) -> list[dict[str, Any]]:
    n = int(cfg["retrieval"]["candidates_per_source"])
    query = " OR ".join(f'all:"{topic}"' for topic in cfg["topics"])
    r = request_get(
        "https://export.arxiv.org/api/query",
        params={
            "search_query": query,
            "start": 0,
            "max_results": n,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        },
    )
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(r.content)
    out: list[dict[str, Any]] = []
    for entry in root.findall("a:entry", ns):
        raw_id = text_of(entry.find("a:id", ns)).rstrip("/").split("/")[-1]
        arxiv_id = re.sub(r"v\d+$", "", raw_id)
        if not arxiv_id:
            continue
        out.append(
            {
                "source": "arxiv",
                "canonical_id": f"arxiv:{arxiv_id}",
                "title": text_of(entry.find("a:title", ns)),
                "abstract": text_of(entry.find("a:summary", ns)),
                "authors": [
                    text_of(x.find("a:name", ns))
                    for x in entry.findall("a:author", ns)
                ],
                "publication_date": text_of(entry.find("a:published", ns))[:10],
                "updated_date": text_of(entry.find("a:updated", ns))[:10],
                "journal_or_category": ", ".join(
                    x.attrib.get("term", "")
                    for x in entry.findall("a:category", ns)
                    if x.attrib.get("term")
                ),
                "url": f"https://arxiv.org/abs/{arxiv_id}",
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                "read_level": "abstract",
            }
        )
    return out


def pubmed_query(topics: list[str]) -> str:
    terms: list[str] = []
    for topic in topics:
        t = topic.lower()
        if t == "medical ai":
            terms.append(
                '(medical[Title/Abstract] AND ("artificial intelligence"[Title/Abstract] '
                'OR "machine learning"[Title/Abstract] OR "large language model"[Title/Abstract]))'
            )
        elif t == "healthcare ai":
            terms.append(
                '(healthcare[Title/Abstract] AND ("artificial intelligence"[Title/Abstract] '
                'OR "machine learning"[Title/Abstract] OR "large language model"[Title/Abstract]))'
            )
        elif "large language model" in t:
            terms.append(
                '("large language model"[Title/Abstract] OR '
                '"large language models"[Title/Abstract] OR LLM[Title/Abstract])'
            )
        else:
            terms.append(f'"{topic}"[Title/Abstract]')
    return "(" + " OR ".join(terms) + ")"


def pubmed_date(article: ET.Element) -> str:
    electronic = article.find(".//Article/ArticleDate[@DateType='Electronic']")
    if electronic is not None:
        y = text_of(electronic.find("Year"))
        m = text_of(electronic.find("Month")).zfill(2)
        d = text_of(electronic.find("Day")).zfill(2)
        if y:
            return "-".join(x for x in [y, m, d] if x)

    hist = article.find(".//PubmedData/History/PubMedPubDate[@PubStatus='epublish']")
    if hist is not None:
        y = text_of(hist.find("Year"))
        m = text_of(hist.find("Month")).zfill(2)
        d = text_of(hist.find("Day")).zfill(2)
        if y:
            return "-".join(x for x in [y, m, d] if x)

    pd = article.find(".//JournalIssue/PubDate")
    if pd is not None:
        medline = text_of(pd.find("MedlineDate"))
        if medline:
            return medline
        y = text_of(pd.find("Year"))
        m = text_of(pd.find("Month"))
        d = text_of(pd.find("Day"))
        return " ".join(x for x in [y, m, d] if x)
    return ""


def pubmed_candidates(cfg: dict[str, Any]) -> list[dict[str, Any]]:
    n = int(cfg["retrieval"]["candidates_per_source"])
    q = pubmed_query(cfg["topics"])
    s = request_get(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
        params={
            "db": "pubmed",
            "term": q,
            "retmax": n,
            "sort": "pub date",
            "retmode": "json",
        },
    ).json()
    ids = s.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []

    time.sleep(0.35)
    r = request_get(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
        params={"db": "pubmed", "id": ",".join(ids), "retmode": "xml"},
    )
    root = ET.fromstring(r.content)
    by_id: dict[str, dict[str, Any]] = {}

    for item in root.findall(".//PubmedArticle"):
        pmid = text_of(item.find(".//MedlineCitation/PMID"))
        if not pmid:
            continue

        abstract_parts = []
        for part in item.findall(".//Article/Abstract/AbstractText"):
            label = part.attrib.get("Label")
            text = text_of(part)
            if text:
                abstract_parts.append(f"{label}: {text}" if label else text)

        authors = []
        for a in item.findall(".//Article/AuthorList/Author"):
            collective = text_of(a.find("CollectiveName"))
            if collective:
                authors.append(collective)
                continue
            last = text_of(a.find("LastName"))
            initials = text_of(a.find("Initials"))
            name = " ".join(x for x in [last, initials] if x)
            if name:
                authors.append(name)

        pmcid = ""
        for aid in item.findall(".//PubmedData/ArticleIdList/ArticleId"):
            if aid.attrib.get("IdType") == "pmc":
                pmcid = text_of(aid)
                break

        by_id[pmid] = {
            "source": "pubmed",
            "canonical_id": f"pmid:{pmid}",
            "title": text_of(item.find(".//Article/ArticleTitle")),
            "abstract": "\n".join(abstract_parts),
            "authors": authors,
            "publication_date": pubmed_date(item),
            "journal_or_category": text_of(item.find(".//Article/Journal/Title")),
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "pmcid": pmcid,
            "read_level": "abstract",
        }

    return [by_id[x] for x in ids if x in by_id]


def call_local_model(model: str, prompt: str, *, timeout: int = 3600) -> str:
    prefix = "/no_think\n" if True else ""
    proc = subprocess.run(
        ["ollama", "run", model],
        input=prefix + prompt,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    if proc.returncode != 0:
        raise PaperWatchError(
            f"Local Ollama model failed with exit code {proc.returncode}: "
            f"{proc.stderr[-4000:]}"
        )
    text = proc.stdout.strip()
    if not text:
        raise PaperWatchError(f"Local Ollama model returned an empty response: {model}.")
    return text


def parse_json_object(text: str) -> dict[str, Any]:
    stripped = re.sub(
        r"^```(?:json)?\s*|\s*```$",
        "",
        text.strip(),
        flags=re.I | re.S,
    )
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start < 0 or end <= start:
        raise PaperWatchError("Selection model did not return a JSON object.")
    try:
        return json.loads(stripped[start : end + 1])
    except json.JSONDecodeError as e:
        raise PaperWatchError(f"Could not parse selection JSON: {e}") from e


def select_papers(
    cfg: dict[str, Any], candidates: list[dict[str, Any]]
) -> list[str]:
    max_papers = int(cfg["max_papers"])
    model = cfg.get("llm", {}).get("model", "qwen3:4b")
    compact = [
        {
            "canonical_id": x["canonical_id"],
            "source": x["source"],
            "title": x["title"],
            "publication_date": x["publication_date"],
            "journal_or_category": x.get("journal_or_category", ""),
            "abstract": x.get("abstract", ""),
        }
        for x in candidates
    ]

    prompt = f"""
You are selecting papers for a Japanese research paper-watch.

Selection rules from the canonical YAML:
{json.dumps(cfg["selection"]["rules"], ensure_ascii=False, indent=2)}

Configured topics:
{json.dumps(cfg["topics"], ensure_ascii=False)}

Maximum papers: {max_papers}

Choose only from the candidate list below. Prefer recent, technically substantive,
potentially influential work and keep a reasonable balance across ML, LLM,
medical AI, and healthcare AI when the candidates permit. Do not fill the quota
with weak or irrelevant work.

Return ONLY a JSON object exactly like:
{{"selected_ids":["arxiv:xxxx.xxxxx","pmid:12345678"]}}

Candidate papers:
{json.dumps(compact, ensure_ascii=False)}
""".strip()

    obj = parse_json_object(call_local_model(model, prompt, timeout=1800))
    selected = obj.get("selected_ids")
    if not isinstance(selected, list) or not all(
        isinstance(x, str) for x in selected
    ):
        raise PaperWatchError("Selection JSON has no valid selected_ids array.")
    if len(selected) > max_papers:
        raise PaperWatchError("Selection model returned more than max_papers.")

    candidate_ids = {x["canonical_id"] for x in candidates}
    invalid = [x for x in selected if x not in candidate_ids]
    if invalid:
        raise PaperWatchError(
            f"Selection model returned IDs outside candidate pool: {invalid}"
        )
    return list(dict.fromkeys(selected))


def sample_text(text: str, limit: int) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text

    first = limit * 2 // 5
    middle = limit // 5
    last = limit - first - middle
    mid_start = max(0, len(text) // 2 - middle // 2)

    return (
        text[:first]
        + "\n\n[... middle of full text sampled ...]\n\n"
        + text[mid_start : mid_start + middle]
        + "\n\n[... end of full text sampled ...]\n\n"
        + text[-last:]
    )


def extract_arxiv_full_text(paper: dict[str, Any], char_limit: int) -> str:
    # Individual arXiv page reachability check, then PDF parsing.
    request_get(paper["url"], timeout=45)
    pdf = request_get(paper["pdf_url"], timeout=90).content
    reader = PdfReader(io.BytesIO(pdf))
    chunks: list[str] = []

    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        if text:
            chunks.append(text)

    return sample_text("\n".join(chunks), char_limit)


def extract_pmc_full_text(pmcid: str, char_limit: int) -> str:
    if not pmcid:
        return ""

    time.sleep(0.35)
    r = request_get(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
        params={"db": "pmc", "id": pmcid, "retmode": "xml"},
        timeout=60,
    )
    root = ET.fromstring(r.content)
    body = root.find(".//body")
    if body is None:
        return ""

    paragraphs = []
    for elem in body.iter():
        if elem.tag.rsplit("}", 1)[-1] in {"title", "p"}:
            text = text_of(elem)
            if text:
                paragraphs.append(text)

    return sample_text("\n".join(paragraphs), char_limit)


def enrich_selected(
    cfg: dict[str, Any], papers: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    limit = int(
        cfg.get("runner", {}).get("max_full_text_chars_per_paper", 30000)
    )
    enriched: list[dict[str, Any]] = []

    for paper in papers:
        item = deepcopy(paper)
        full_text = ""

        try:
            if item["source"] == "arxiv":
                full_text = extract_arxiv_full_text(item, limit)
            elif item["source"] == "pubmed" and item.get("pmcid"):
                full_text = extract_pmc_full_text(item["pmcid"], limit)
        except Exception as e:
            print(
                f"WARNING: full-text retrieval failed for "
                f"{item['canonical_id']}: {e}",
                file=sys.stderr,
            )

        if len(full_text.strip()) >= 2000:
            item["read_level"] = "full_text"
            item["full_text_excerpt"] = full_text
        else:
            item["read_level"] = "abstract"

        enriched.append(item)

    return enriched


def report_prompt(
    cfg: dict[str, Any], papers: list[dict[str, Any]]
) -> str:
    digest_n = int(cfg["output"].get("gmail_digest_top_papers", 5))
    paper_ids_format = cfg["output"].get("paper_ids_block_format", "")

    return f"""
Create the complete Japanese paper-watch email/report using ONLY the supplied
verified paper metadata and text. Do not invent numerical results, limitations,
study details, authors, dates, or claims not supported by the supplied material.

Canonical task instructions:
{cfg["task_instructions"]}

Summary fields:
quick_fields = {json.dumps(cfg["summary"]["quick_fields"], ensure_ascii=False)}
detailed_fields = {json.dumps(cfg["summary"]["detailed_fields"], ensure_ascii=False)}
medical_ai_extra_fields = {json.dumps(cfg["summary"]["medical_ai_extra_fields"], ensure_ascii=False)}

Rules:
{json.dumps(cfg["summary"]["rules"], ensure_ascii=False, indent=2)}

Email structure MUST be:
1. "## ダイジェスト"
   - include "### 今回の概況"
   - then up to {digest_n} especially notable papers, concise
2. horizontal separator
3. "# 完全版レポート"
   - start again with "## 今回の概況"
   - then every selected paper
   - for each paper include Source, canonical ID, publication date, authors when
     available, journal/category when available, URL, and read_level
   - for each paper first include Tags, Summary, Why interesting
   - immediately follow with 目的, 手法, データ・実験, 主な結果, 新規性,
     限界, なぜ注目したか
   - for medical/healthcare AI include study design, sample size,
     primary endpoint, external validation, prospective/retrospective when
     supported
4. End with the exact PAPER_IDS block containing every selected canonical ID,
   one per line, and nothing except canonical IDs between the marker lines.

Configured PAPER_IDS example:
{paper_ids_format}

Important: read_level is already determined by the runner. If
read_level=abstract, do not imply full text was read. If read_level=full_text,
you may use the provided sampled full text plus abstract.

Selected verified papers:
{json.dumps(papers, ensure_ascii=False)}
""".strip()


def extract_report_ids(report: str) -> list[str]:
    match = re.search(
        r"<!-- PAPER_IDS -->(.*?)<!-- /PAPER_IDS -->",
        report,
        flags=re.S,
    )
    if not match:
        raise PaperWatchError("Generated report is missing the PAPER_IDS block.")

    ids = re.findall(
        r"^(?:arxiv:[0-9.]+|pmid:\d+)\s*$",
        match.group(1),
        flags=re.M,
    )
    return [x.strip() for x in ids]


def generate_report(
    cfg: dict[str, Any],
    papers: list[dict[str, Any]],
    selected_ids: list[str],
) -> str:
    model = cfg.get("llm", {}).get("model", "qwen3:4b")

    report = call_local_model(
        model,
        report_prompt(cfg, papers),
        timeout=5400,
    )

    report_ids = extract_report_ids(report)
    if report_ids != selected_ids and set(report_ids) != set(selected_ids):
        raise PaperWatchError(
            "Report PAPER_IDS do not match selected IDs. "
            f"selected={selected_ids}, report={report_ids}"
        )

    return report


def send_gmail(cfg: dict[str, Any], report: str) -> None:
    address = require_env("GMAIL_ADDRESS")
    password = require_env("GMAIL_APP_PASSWORD").replace(" ", "")
    today = datetime.now(ZoneInfo("Asia/Tokyo")).date().isoformat()

    subject = (
        f'{cfg["output"].get("gmail_subject_prefix", "[paper-watch]")} '
        f"{today} ML / LLM / Medical AI"
    )

    msg = EmailMessage()
    msg["From"] = address
    msg["To"] = address
    msg["Subject"] = subject
    msg.set_content(report)

    html_body = markdown.markdown(
        report,
        extensions=["tables", "fenced_code", "sane_lists"],
    )
    msg.add_alternative(
        f"<html><body>{html_body}</body></html>",
        subtype="html",
    )

    host = cfg.get("runner", {}).get("smtp_host", "smtp.gmail.com")
    port = int(cfg.get("runner", {}).get("smtp_port", 465))

    with smtplib.SMTP_SSL(host, port, timeout=60) as smtp:
        smtp.login(address, password)
        smtp.send_message(msg)


def update_seen(cfg: dict[str, Any], selected_ids: list[str]) -> None:
    path = seen_path(cfg)
    existing_lines = [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    existing = set(existing_lines)
    additions = [x for x in selected_ids if x not in existing]
    if not additions:
        return

    path.write_text(
        "\n".join(existing_lines + additions) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    cfg = load_config()

    # Fail before network work if required Gmail secrets are absent.
    require_env("GMAIL_ADDRESS")
    require_env("GMAIL_APP_PASSWORD")

    seen = read_seen(cfg)
    candidates: list[dict[str, Any]] = []

    if "arxiv" in cfg["sources"]:
        candidates.extend(arxiv_candidates(cfg))
    if "pubmed" in cfg["sources"]:
        candidates.extend(pubmed_candidates(cfg))

    unseen = [
        item
        for item in candidates
        if item["canonical_id"] not in seen
    ]
    if not unseen:
        print("No unseen candidates found; nothing to send.")
        return

    selected_ids = select_papers(cfg, unseen)
    if not selected_ids:
        print("No papers selected after relevance/quality filtering; nothing to send.")
        return

    by_id = {item["canonical_id"]: item for item in unseen}
    selected = [by_id[paper_id] for paper_id in selected_ids]
    enriched = enrich_selected(cfg, selected)

    report = generate_report(cfg, enriched, selected_ids)

    # Critical ordering: email first; persistent state only after successful send.
    send_gmail(cfg, report)
    update_seen(cfg, selected_ids)

    print(
        f"SUCCESS: sent Gmail report and updated seen state "
        f"for {len(selected_ids)} papers."
    )
    print("Selected IDs:")
    for paper_id in selected_ids:
        print(f"  {paper_id}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        raise
