#!/usr/bin/env python3
"""Verify paper publication dates against arXiv/PubMed and update Markdown.

The REPORT DATE is the date in reports/daily/YYYY-MM-DD*.md, independent of
the PUBLICATION DATE obtained from source metadata. This script never copies
one into the other. Unverified dates are removed rather than presented as fact.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports" / "daily"
CACHE = ROOT / "docs" / "publication-dates.json"
PAPER = re.compile(r"^### Paper: .+$", re.M)
CANON = re.compile(r"^- Canonical ID: (arxiv:\d{4}\.\d{4,5}|pmid:\d{6,9})$", re.M)
PUB = re.compile(r"^- Publication date: .*$", re.M)
USER_AGENT = "PaperWatchDateVerifier/1.0 (public research metadata; https://github.com/drkamoshika/papers)"
ATOM = "{http://www.w3.org/2005/Atom}"


def request(url: str) -> bytes:
    """GET primary-source metadata, with bounded retries."""
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/xml,text/html,*/*"})
            with urllib.request.urlopen(req, timeout=18) as response:
                return response.read()
        except (OSError, urllib.error.HTTPError) as exc:
            last = exc
            if isinstance(exc, urllib.error.HTTPError) and exc.code in (400, 401, 403, 404):
                break
            time.sleep(2 ** attempt)
    raise RuntimeError(f"{url}: {last}")


def validated(date_text: str) -> str:
    date = dt.date.fromisoformat(date_text)
    if date > dt.date.today() + dt.timedelta(days=1) or date.year < 1800:
        raise ValueError(f"implausible publication date {date_text}")
    return date.isoformat()


def entry(date: str, url: str, basis: str) -> dict:
    return {"date": validated(date), "source_url": url, "basis": basis}


def arxiv_atom(ids: list[str]) -> dict[str, dict]:
    """Bulk arXiv v1 submitted/published dates from official Atom API."""
    result = {}
    for offset in range(0, len(ids), 40):
        batch = ids[offset:offset + 40]
        query = urllib.parse.urlencode({
            "id_list": ",".join(x.split(":", 1)[1] for x in batch),
            "start": 0,
            "max_results": len(batch),
        })
        url = "https://export.arxiv.org/api/query?" + query
        try:
            root = ET.fromstring(request(url))
            for item in root.findall(ATOM + "entry"):
                paper_id = (item.findtext(ATOM + "id") or "").split("/")[-1]
                paper_id = re.sub(r"v\d+$", "", paper_id)
                pub = item.findtext(ATOM + "published") or ""
                key = "arxiv:" + paper_id
                if key in batch and re.fullmatch(r"\d{4}-\d{2}-\d{2}.*", pub):
                    result[key] = entry(pub[:10], f"https://arxiv.org/abs/{paper_id}", "arxiv-v1")
        except (ValueError, ET.ParseError, RuntimeError) as exc:
            print(f"arXiv API batch {offset // 40 + 1}: {exc}; using primary abstract pages")
        if offset + 40 < len(ids):
            time.sleep(3)
    return result


def arxiv_page(key: str) -> tuple[str, dict | None, str | None]:
    paper_id = key.split(":", 1)[1]
    url = f"https://arxiv.org/abs/{paper_id}"
    try:
        text = request(url).decode("utf-8", errors="replace")
        # arXiv explicitly shows original submission, not the latest revision.
        match = re.search(r"Submitted on\s+(\d{1,2})\s+([A-Za-z]{3})\s+(\d{4})", text, re.I)
        if not match:
            # An arXiv paper with revisions still identifies its earliest [v1] timestamp.
            match = re.search(r"\[v1\][^<]{0,70}?\b(\d{1,2})\s+([A-Za-z]{3})\s+(\d{4})", text, re.I)
        if not match:
            return key, None, "submission date not located on arXiv abstract page"
        date = dt.datetime.strptime(" ".join(match.groups()), "%d %b %Y").date().isoformat()
        return key, entry(date, url, "arxiv-v1"), None
    except (ValueError, RuntimeError) as exc:
        return key, None, str(exc)


def xml_date(node: ET.Element | None) -> str | None:
    if node is None:
        return None
    y, m, d = [(node.findtext(k) or "").strip() for k in ("Year", "Month", "Day")]
    if not (y and m and d):
        return None
    try:
        if m.isalpha():
            m = str(dt.datetime.strptime(m[:3].title(), "%b").month)
        return validated(f"{int(y):04d}-{int(m):02d}-{int(d):02d}")
    except ValueError:
        return None


def pubmed_dates(ids: list[str]) -> dict[str, dict]:
    """Batch PubMed XML; prefer online publication over print/indexing dates."""
    results = {}
    for offset in range(0, len(ids), 100):
        group = ids[offset:offset + 100]
        params = urllib.parse.urlencode({
            "db": "pubmed",
            "id": ",".join(k.split(":", 1)[1] for k in group),
            "retmode": "xml",
            "tool": "paper_watch_publication_dates",
        })
        root = ET.fromstring(request("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + params))
        for item in root.findall(".//PubmedArticle"):
            pmid = (item.findtext("./MedlineCitation/PMID") or "").strip()
            key = "pmid:" + pmid
            if key not in group:
                continue
            paper_url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            article = item.find("./MedlineCitation/Article")
            if article is None:
                continue
            choices: list[tuple[str | None, str]] = []
            for node in article.findall("./ArticleDate"):
                choices.append((xml_date(node), "pubmed-article-electronic"))
            for node in item.findall("./PubmedData/History/PubMedPubDate"):
                status = (node.attrib.get("PubStatus") or "").lower()
                if status in {"epublish", "aheadofprint", "ecollection"}:
                    choices.append((xml_date(node), "pubmed-" + status))
            choices.append((xml_date(article.find("./Journal/JournalIssue/PubDate")), "pubmed-journal-issue"))
            for node in item.findall("./PubmedData/History/PubMedPubDate"):
                if (node.attrib.get("PubStatus") or "").lower() == "ppublish":
                    choices.append((xml_date(node), "pubmed-print"))
            for date, basis in choices:
                if date:
                    results[key] = entry(date, paper_url, basis)
                    break
        if offset + 100 < len(ids):
            time.sleep(1)
    return results


def collect_records() -> tuple[dict[str, dict], dict[str, str]]:
    files = {}
    for path in sorted(REPORTS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        starts = list(PAPER.finditer(text))
        for i, start in enumerate(starts):
            end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
            section = text[start.start():end]
            m = CANON.search(section)
            if not m:
                raise ValueError(f"{path}: Paper section missing canonical ID")
            if not PUB.search(section):
                raise ValueError(f"{path}: missing Publication date for {m.group(1)}")
            files.setdefault(m.group(1), []).append(path)
    return files


def apply_dates(records: dict[str, dict]) -> tuple[int, int, int]:
    changed_files, changed_dates, unknown = 0, 0, 0
    for path in sorted(REPORTS.glob("*.md")):
        original = path.read_text(encoding="utf-8")
        match_date = re.search(r"\d{4}-\d{2}-\d{2}", path.name)
        if not match_date:
            raise ValueError(f"report has no report date in filename: {path}")
        report_date = match_date.group()
        body = original
        if re.search(r"^> report_date:", body, re.M):
            body = re.sub(r"^> report_date:.*$", f"> report_date: {report_date}", body, count=1, flags=re.M)
        elif re.search(r"^> schema_version:", body, re.M):
            body = re.sub(r"^(> schema_version:.*)$", r"\1\n> report_date: " + report_date, body, count=1, flags=re.M)
        else:
            body = re.sub(r"^# .+$", lambda m: m.group() + f"\n\n> report_date: {report_date}", body, count=1, flags=re.M)
        starts = list(PAPER.finditer(body))
        for i in reversed(range(len(starts))):
            start = starts[i].start()
            end = starts[i + 1].start() if i + 1 < len(starts) else len(body)
            section = body[start:end]
            match = CANON.search(section)
            if not match:
                raise ValueError(f"missing paper ID: {path}")
            key = match.group(1)
            new_date = records.get(key, {}).get("date") or "未記載"
            old_date = PUB.search(section)
            if not old_date:
                raise ValueError(f"missing Publication date: {key}")
            if old_date.group().split(": ", 1)[-1].strip() != new_date:
                changed_dates += 1
            if new_date == "未記載":
                unknown += 1
            section = PUB.sub(lambda m: "- Publication date: " + new_date, section, count=1)
            body = body[:start] + section + body[end:]
        if body != original:
            path.write_text(body, encoding="utf-8")
            changed_files += 1
    return changed_files, changed_dates, unknown


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write verified dates to canonical Markdown and cache")
    parser.add_argument("--refresh", action="store_true", help="Re-query even previously verified metadata")
    args = parser.parse_args()

    files = collect_records()
    ids = sorted(files)
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {"schema_version": 1, "records": {}}
    records = cache.get("records", {})
    if args.refresh:
        records = {}
    records = {k: v for k, v in records.items() if k in files and v.get("date") and v.get("source_url")}
    pending = [k for k in ids if k not in records]
    errors = {}
    pubmed = [k for k in pending if k.startswith("pmid:")]
    arxiv = [k for k in pending if k.startswith("arxiv:")]
    if pubmed:
        try:
            records.update(pubmed_dates(pubmed))
        except (RuntimeError, ValueError, ET.ParseError) as exc:
            errors["pubmed-batch"] = str(exc)
            print("PubMed batch error:", exc)
    if arxiv:
        records.update(arxiv_atom(arxiv))
        missing = [k for k in arxiv if k not in records]
        if missing:
            # Fallback: individual official arXiv pages, bounded concurrency.
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                futures = {executor.submit(arxiv_page, key): key for key in missing}
                for future in concurrent.futures.as_completed(futures):
                    key, record, error = future.result()
                    if record:
                        records[key] = record
                    else:
                        errors[key] = error
    if not records:
        raise RuntimeError("Could not verify ANY paper publication dates. Refusing to alter the reports.")
    for key in ids:
        if key not in records and key not in errors:
            errors[key] = "Primary-source exact publication date not available"
    print(f"Primary-source verified: {len(records)} / {len(ids)}; unresolved: {len(ids)-len(records)}")
    for key in sorted(errors)[:20]:
        print("Unresolved:", key, errors[key])
    if not args.apply:
        print("Dry run; pass --apply to save verified dates.")
        return
    changed_files, changed_dates, unknown = apply_dates(records)
    cache_content = {"schema_version": 1, "policy": "arXiv v1 submitted date; PubMed earliest exact electronic publication date, then exact journal issue date; NEVER reportDate.", "records": dict(sorted(records.items())), "unresolved": dict(sorted(errors.items()))}
    CACHE.write_text(json.dumps(cache_content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {changed_dates} publication-date fields in {changed_files} Markdown files; {unknown} sections have unverified dates.")


if __name__ == "__main__":
    main()
