"""Offline regression tests: source dates must never become report dates."""
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("publication_dates", ROOT / "scripts" / "refresh_publication_dates.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class PublicationDateTests(unittest.TestCase):
    def test_arxiv_uses_original_submission_not_revision(self):
        page = b"<div>[Submitted on 14 Aug 2026 (v1), last revised 23 Aug 2026 (v2)]</div>"
        with mock.patch.object(mod, "request", return_value=page):
            key, result, error = mod.arxiv_page("arxiv:2608.14354")
        self.assertIsNone(error)
        self.assertEqual(key, "arxiv:2608.14354")
        self.assertEqual(result["date"], "2026-08-14")
        self.assertEqual(result["basis"], "arxiv-v1")

    def test_pubmed_prefers_electronic_to_print_and_indexing(self):
        xml = b"""<?xml version="1.0" encoding="UTF-8"?>
<PubmedArticleSet><PubmedArticle><MedlineCitation><PMID>42545345</PMID>
<Article><ArticleDate DateType="Electronic"><Year>2026</Year><Month>08</Month><Day>03</Day></ArticleDate>
<Journal><JournalIssue><PubDate><Year>2026</Year><Month>10</Month><Day>01</Day></PubDate></JournalIssue></Journal>
</Article></MedlineCitation><PubmedData><History>
<PubMedPubDate PubStatus="pubmed"><Year>2026</Year><Month>08</Month><Day>23</Day></PubMedPubDate>
</History></PubmedData></PubmedArticle></PubmedArticleSet>"""
        with mock.patch.object(mod, "request", return_value=xml):
            result = mod.pubmed_dates(["pmid:42545345"])
        self.assertEqual(result["pmid:42545345"]["date"], "2026-08-03")
        self.assertEqual(result["pmid:42545345"]["basis"], "pubmed-article-electronic")

    def test_unknown_date_not_replaced_with_report_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "2026-08-23_01.md"
            path.write_text(
                "# Paper Watch — 2026-08-23_01\n\n> schema_version: 1\n\n"
                "### Paper: Example\n- Canonical ID: arxiv:2608.14354\n"
                "- Publication date: 2026-08-23\n\n"
                "### Paper: Unknown\n- Canonical ID: pmid:42545345\n"
                "- Publication date: 2026-08-23\n"
                "<!-- PAPER_IDS -->\narxiv:2608.14354\npmid:42545345\n<!-- /PAPER_IDS -->\n",
                encoding="utf-8",
            )
            with mock.patch.object(mod, "REPORTS", Path(tmp)):
                files, dates, unknown = mod.apply_dates({
                    "arxiv:2608.14354": {"date": "2026-08-14", "source_url": "https://arxiv.org/abs/2608.14354"}
                })
            updated = path.read_text(encoding="utf-8")
            self.assertEqual((files, dates, unknown), (1, 2, 1))
            self.assertIn("> report_date: 2026-08-23", updated)
            self.assertIn("- Publication date: 2026-08-14", updated)
            self.assertIn("- Publication date: 未記載", updated)


if __name__ == "__main__":
    unittest.main()
