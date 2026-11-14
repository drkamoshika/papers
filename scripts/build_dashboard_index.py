#!/usr/bin/env python3
"""Build a static search index from Markdown reports. No external dependencies."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
OUTPUT = ROOT / "docs" / "papers.json"

def field(section, names):
    for line in section.splitlines():
        m = re.match(r"^\s*[-*]\s*(?:\*\*)?([^:*]+?)(?:\*\*)?\s*:\s*(.*)$", line)
        if m and m.group(1).strip().lower() in names:
            return m.group(2).strip()
    return ""

def parse(path):
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT).as_posix()
    date = re.search(r"20\d{2}-\d{2}-\d{2}", path.name)
    if not date:
        date = re.search(r"20\d{2}-\d{2}-\d{2}", text[:700])
    report_date = date.group() if date else ""
    headings = list(re.finditer(r"^##\s+(?:\d+\.\s+)?(.+)$", text, re.M))
    papers = []
    for i, h in enumerate(headings):
        title = h.group(1).strip()
        section = text[h.end():headings[i + 1].start() if i + 1 < len(headings) else len(text)]
        link = re.search(r"https?://(?:arxiv\.org/abs/\d{4}\.\d+|pubmed\.ncbi\.nlm\.nih\.gov/\d+)", section)
        if not link:
            continue
        url = link.group()
        source = "arXiv" if "arxiv.org" in url else "PubMed"
        canonical_id = ("arxiv:" + url.rsplit("/", 1)[-1]) if source == "arXiv" else ("pmid:" + re.search(r"/(\d+)/?$", url).group(1))
        papers.append({
            "id": canonical_id, "title": title, "url": url, "source": source,
            "date": field(section, {"date", "publication date", "published online", "published"}),
            "tags": field(section, {"tags"}), "summary": field(section, {"summary"}),
            "why": field(section, {"why interesting"}), "reportDate": report_date,
            "report": rel, "details": section.strip()[:11000]
        })
    return papers

def main():
    # All reports use date-based names under reports/daily/.
    paths = []
    paths += sorted((REPORTS / "daily").glob("*.md")) if (REPORTS / "daily").exists() else []
    papers = {}
    for path in paths:
        for paper in parse(path):
            # Prefer a newer daily report when a paper is mentioned more than once.
            papers[paper["id"]] = paper
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({"papers": list(papers.values())}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Indexed {len(papers)} unique papers from {len(paths)} reports")

if __name__ == "__main__":
    main()
