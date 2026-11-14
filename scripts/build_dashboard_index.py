#!/usr/bin/env python3
"""Deterministic Markdown -> JSON index. Canonical schema v1 + legacy fallback."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports" / "daily"
OUTPUT = ROOT / "docs" / "papers.json"
SCHEMA = ROOT / "docs" / "paper.schema.json"
ID = re.compile(r"^(?:arxiv:\d{4}\.\d{4,5}|pmid:\d{6,9})$")
URL = re.compile(r"https?://(?:arxiv\.org/abs/\d{4}\.\d{4,5}|pubmed\.ncbi\.nlm\.nih\.gov/\d+)")
CANON = re.compile(r"^### Paper: (.+)$", re.M)
KEYS = {
    "Source": "source", "Canonical ID": "id", "Publication date": "date",
    "URL": "url", "read_level": "read_level", "Tags": "tags",
    "Summary": "summary", "Objective": "objective", "Methods": "methods",
    "Data and results": "results", "Novelty": "novelty",
    "Limitations": "limitations",
}
REQUIRED = ("id", "title", "url", "source", "read_level")
EMPTY = {"", "未記載", "不明", "N/A"}
def canonical(text, report, date):
    starts = list(CANON.finditer(text))
    if not starts:
        if "schema_version: 1" in text:
            raise ValueError(f"{report}: schema v1 declared but no Paper sections")
        return None
    rows = []
    for i, m in enumerate(starts):
        body = text[m.end(): starts[i + 1].start() if i + 1 < len(starts) else len(text)]
        body = body.split("<!-- PAPER_IDS -->", 1)[0]
        row = {"title": m.group(1).strip(), "report": report, "reportDate": date}
        for line in body.splitlines():
            match = re.match(r"^- ([A-Za-z][A-Za-z0-9_ ]*):\s*(.*)$", line)
            if match and match.group(1) in KEYS:
                k = KEYS[match.group(1)]
                if k in row:
                    raise ValueError(f"{report}: duplicate {k} in {row['title']}")
                row[k] = match.group(2).strip()
        missing = set(KEYS) - {key for key, val in KEYS.items() if val in row}
        if missing:
            raise ValueError(f"{report}: missing schema keys {sorted(missing)} in {row['title']}")
        for k in REQUIRED:
            if row.get(k, "") in EMPTY:
                raise ValueError(f"{report}: missing {k} in {row['title']}")
        if not ID.fullmatch(row["id"]):
            raise ValueError(f"{report}: invalid ID {row['id']}")
        expected = ("https://arxiv.org/abs/" + row["id"][6:]) if row["id"].startswith("arxiv:") else ("https://pubmed.ncbi.nlm.nih.gov/" + row["id"][5:] + "/")
        if row["url"].rstrip("/") != expected.rstrip("/"):
            raise ValueError(f"{report}: URL does not match ID {row['id']}")
        if row["read_level"] not in ("abstract", "full_text", "bibliographic"):
            raise ValueError(f"{report}: invalid read_level {row['id']}")
        row["tags"] = [t.strip() for t in row.get("tags", "").split(",") if t.strip() and t.strip() != "未記載"]
        for k in ("date", "summary", "objective", "methods", "results", "novelty", "limitations"):
            if row.get(k, "") in EMPTY:
                row[k] = None
        if row["date"] is not None and not re.fullmatch(r"20\\d{2}-\\d{2}-\\d{2}", row["date"]):
            raise ValueError(f"{report}: invalid date {row['date']}")
        row["why"] = row.get("novelty") or ""
        row["details"] = "\n".join(f"{k}: {row.get(v,'')}" for k, v in KEYS.items() if k not in ("Source", "Canonical ID", "URL"))
        rows.append(row)
    if len(rows) != len({x["id"] for x in rows}):
        raise ValueError(f"{report}: duplicate IDs within report")
    block = re.search(r"<!-- PAPER_IDS -->(.*?)<!-- /PAPER_IDS -->", text, re.S)
    if not block:
        raise ValueError(f"{report}: missing PAPER_IDS block")
    ids = [s.strip() for s in block.group(1).splitlines() if s.strip()]
    if set(ids) != {x["id"] for x in rows} or len(ids) != len(rows):
        raise ValueError(f"{report}: PAPER_IDS mismatch")
    return rows

def legacy(text, report, date):
    # Backward compatibility for earlier daily reports; new reports MUST use canonical.
    headings = list(re.finditer(r"^##\s+(?:\d+\.\s+)?(.+)$", text, re.M))
    rows = []
    for i, m in enumerate(headings):
        body = text[m.end():headings[i + 1].start() if i + 1 < len(headings) else len(text)]
        url = URL.search(body)
        if not url:
            continue
        u = url.group()
        arxiv = "arxiv.org" in u
        cid = "arxiv:" + u.rsplit("/", 1)[-1] if arxiv else "pmid:" + re.search(r"/(\d+)/?$", u).group(1)
        def fld(key):
            x = re.search(r"^- (?:\*\*)?" + re.escape(key) + r"(?:\*\*)?:\s*(.+)$", body, re.M | re.I)
            return x.group(1).strip() if x else ""
        rows.append({"id":cid,"title":m.group(1).strip(),"url":u,
                     "source":"arXiv" if arxiv else "PubMed","date":fld("Date") or fld("Publication date") or None,
                     "tags":[t.strip() for t in fld("Tags").split(",") if t.strip()],"summary":fld("Summary") or None,"why":fld("Why interesting"),
                     "objective":None,"methods":None,"results":None,"novelty":fld("Why interesting") or None,"limitations":None,
                     "read_level":fld("read_level") or "abstract",
                     "reportDate":date,"report":report,"details":body.strip()[:11000]})
    return rows

def build():
    rows = {}
    paths = sorted(REPORTS.glob("*.md"))
    for path in paths:
        text = path.read_text(encoding="utf-8")
        report = path.relative_to(ROOT).as_posix()
        m = re.search(r"20\d{2}-\d{2}-\d{2}", path.name)
        date = m.group() if m else ""
        parsed = canonical(text, report, date)
        if parsed is None:
            parsed = legacy(text, report, date)
        for row in parsed:
            old = rows.get(row["id"])
            if old is None:
                rows[row["id"]] = row
            else:
                # Prefer richer content, never overwrite with an empty/shorter summary.
                score = lambda p: sum(len(p.get(k) or "") for k in ("summary", "objective", "methods", "results", "novelty", "limitations"))
                if score(row) > score(old):
                    rows[row["id"]] = row
    # Validate the generated data against the single machine-readable contract.
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise RuntimeError("Install jsonschema: pip install jsonschema") from exc
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for paper in rows.values():
        validator.validate({k: paper.get(k) for k in schema["properties"]})
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({"schema_version":1,"papers":list(rows.values())}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Indexed {len(rows)} unique papers from {len(paths)} reports")

if __name__ == "__main__":
    build()
