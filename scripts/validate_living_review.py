#!/usr/bin/env python3
"""Validate the single living review used by the report and dashboard."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REVIEW_PATH = ROOT / "docs" / "overview.json"
LEGACY_TRENDS_PATH = ROOT / "docs" / "trends.json"
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WEEK = re.compile(r"^\d{4}-W\d{2}$")


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def require_text(value: object, label: str) -> str:
    assert isinstance(value, str) and value.strip(), f"{label} must be non-empty"
    return value


def main() -> None:
    review = load(REVIEW_PATH)
    papers = load(ROOT / "docs" / "papers.json")["papers"]
    foundations = load(ROOT / "docs" / "foundations.json")["papers"]
    corpus_ids = {paper["id"] for paper in [*papers, *foundations]}

    assert review.get("schema_version") == 3, "living review schema_version must be 3"
    assert not LEGACY_TRENDS_PATH.exists(), "docs/trends.json duplicates the canonical review"
    reviewed_at = require_text(review.get("reviewDate"), "reviewDate")
    assert DATE.fullmatch(reviewed_at), "reviewDate must be YYYY-MM-DD"
    assert review.get("corpusSnapshotDate") == reviewed_at, "corpus snapshot must match reviewDate"
    snapshot = review.get("snapshot")
    assert isinstance(snapshot, dict), "snapshot is required"
    assert snapshot.get("dailyCount") == len(papers), "dailyCount is stale"
    assert snapshot.get("foundationCount") == len(foundations), "foundationCount is stale"
    assert snapshot.get("uniqueCount") == len(corpus_ids), "uniqueCount is stale"
    latest_report = max(paper["reportDate"] for paper in papers if paper.get("reportDate"))
    assert snapshot.get("latestReportDate") == latest_report, "latestReportDate is stale"

    living = review.get("livingReview")
    assert isinstance(living, dict), "livingReview is required"
    current_week = require_text(living.get("currentWeek"), "livingReview.currentWeek")
    assert WEEK.fullmatch(current_week), "currentWeek must be YYYY-Www"
    require_text(living.get("summary"), "livingReview.summary")
    require_text(living.get("scopeNote"), "livingReview.scopeNote")
    cross_cutting = living.get("crossCutting")
    assert isinstance(cross_cutting, list) and cross_cutting, "crossCutting must not be empty"
    for item in cross_cutting:
        require_text(item.get("title"), "crossCutting.title")
        require_text(item.get("text"), "crossCutting.text")
        assert item.get("ids") and set(item["ids"]) <= corpus_ids, "crossCutting has unknown paper IDs"

    weeks = living.get("weeklyReports")
    assert isinstance(weeks, list) and weeks, "weeklyReports must not be empty"
    assert weeks[-1].get("week") == current_week, "currentWeek must match the latest weekly report"
    assert weeks[-1].get("date") == reviewed_at, "latest weekly report date must match reviewDate"

    fields = review.get("fields")
    assert isinstance(fields, list) and len(fields) == 7, "exactly seven review fields are required"
    keys = [field.get("key") for field in fields]
    assert len(set(keys)) == len(keys), "review field keys must be unique"

    required_update_text = ("state", "shift", "summary", "evidence", "boundary", "gap")
    for field in fields:
        key = require_text(field.get("key"), "field.key")
        update = field.get("currentUpdate")
        assert isinstance(update, dict), f"{key}.currentUpdate is required"
        assert update.get("reviewedAt") == reviewed_at, f"{key} update is stale"
        for name in required_update_text:
            require_text(update.get(name), f"{key}.currentUpdate.{name}")
        refs = update.get("refs")
        assert isinstance(refs, list) and refs, f"{key}.currentUpdate.refs must not be empty"
        for ref in refs:
            paper_id = require_text(ref.get("id"), f"{key} reference id")
            require_text(ref.get("title"), f"{key} reference title")
            url = require_text(ref.get("url"), f"{key} reference URL")
            parsed = urlparse(url)
            assert parsed.scheme == "https" and parsed.netloc, f"{key} reference URL must use HTTPS"
            assert paper_id in corpus_ids, f"{key} reference {paper_id} is absent from the corpus"

    print(
        f"living review valid: {len(fields)} fields, "
        f"{sum(len(field['currentUpdate']['refs']) for field in fields)} update references, "
        f"latest {current_week} ({reviewed_at})"
    )


if __name__ == "__main__":
    main()
