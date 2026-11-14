# Paper Watch Markdown schema v1

The machine-readable source of truth is [`paper.schema.json`](paper.schema.json); this document defines its Markdown serialization. This is the **required contract** for `reports/daily/YYYY-MM-DD.md`. The Markdown is the human-readable record; `scripts/build_dashboard_index.py` validates and converts it to `docs/papers.json`. No external LLM or manual reformatting is required.

## Required structure

```md
# Paper Watch — 2026-11-14

## ダイジェスト

日本語の概況と注目論文の紹介。自由文可。ただし論文詳細と混在させない。

## 完全版レポート

### Paper: Example paper title

- Source: arXiv
- Canonical ID: arxiv:2611.12705
- Publication date: 2026-11-09
- URL: https://arxiv.org/abs/2611.12705
- read_level: abstract
- Tags: LLM, agent, evaluation
- Summary: 日本語で1〜3文
- Objective: 研究課題
- Methods: モデル・アルゴリズム・実験設計
- Data and results: データ規模、比較対象、主要な定量結果
- Novelty: 従来研究との差分
- Limitations: 制約・外部妥当性・未検証事項

<!-- PAPER_IDS -->
arxiv:2611.12705
<!-- /PAPER_IDS -->
```

## Invariants

1. Every paper has **exactly one** `### Paper: TITLE` heading. No other section uses that prefix.
2. Every paper has all **12 fixed English keys** shown above, exactly once each, on separate `- Key: value` lines. Do not embed key/value metadata in prose, a table, or multi-key lines.
3. The canonical ID is `arxiv:YYYY.NNNNN` (4 or 5 digits after the dot) or `pmid:NNNNNNNN` (6–9 digits). IDs must be unique within the daily report.
4. The URL must be the corresponding arXiv abstract or PubMed record URL. Do not substitute publisher landing pages for this field; link to publisher in the prose if needed.
5. `read_level` is one of `bibliographic`, `abstract`, `full_text`. Never claim full text was read when only the abstract was read.
6. `Publication date` uses ISO `YYYY-MM-DD`; if not verified, write `未記載`. The report date and paper publication date are distinct.
7. Missing descriptive fields use `未記載`, **not invented text**. For medical AI, put study design, sample size, endpoint, external validation, and prospective/retrospective evidence in Methods / Data and results / Limitations as supported by the source.
8. The final `PAPER_IDS` block lists exactly the same canonical IDs as the paper sections, once each. The parser fails the build on mismatch or duplicate.
9. Each paper should be factually verified at its primary source before being marked `abstract` or `full_text`.
10. Narrative synthesis belongs in the digest or a separate heading, **not inside a paper's fixed fields**. No repeated partial updates or appendix-only paper records.

## Indexing and migration

- The dashboard reads only `docs/papers.json`, which is validated against `docs/paper.schema.json` and automatically regenerated when a daily report changes.
- Existing legacy daily reports remain readable via a backward-compatibility parser; new reports MUST use this schema.
- The 2026-11-14 original is preserved at `reports/archive/2026-11-14_original.md`; its normalized report has **148 distinct parseable paper IDs**, not the previously asserted 154. The missing six were not fabricated to meet the count.
- If validation fails, GitHub Actions must fail rather than silently dropping papers.
- Deduplication across days is by canonical ID, with richer metadata preferred over a later but poorer record.

## Validation

Run `python -m pip install jsonschema` then `python scripts/build_dashboard_index.py`. A valid canonical report must produce one indexed record per unique paper ID and fail on invalid IDs, mismatched URLs, missing required fields, duplicates, or inconsistent PAPER_IDS.
