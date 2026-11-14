"""Regression tests for canonical Markdown parsing and schema invariants."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("index", ROOT / "scripts" / "build_dashboard_index.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def fixture():
    return """# Paper Watch — 2026-11-14
## 完全版レポート
### Paper: Example title
- Source: arXiv
- Canonical ID: arxiv:2611.12705
- Publication date: 2026-11-09
- URL: https://arxiv.org/abs/2611.12705
- read_level: abstract
- Tags: LLM, agent
- Summary: 要旨
- Objective: 目的
- Methods: 方法
- Data and results: 結果
- Novelty: 新規性
- Limitations: 限界
<!-- PAPER_IDS -->
arxiv:2611.12705
<!-- /PAPER_IDS -->
"""

class SchemaTests(unittest.TestCase):
    def parse(self, text):
        return mod.canonical(text, "reports/daily/2026-11-14.md", "2026-11-14")
    def test_valid(self):
        result = self.parse(fixture())
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "arxiv:2611.12705")
        self.assertEqual(result[0]["tags"], ["LLM", "agent"])
    def test_missing_field_fails(self):
        with self.assertRaises(ValueError):
            self.parse(fixture().replace("- Methods: 方法\n", ""))
    def test_duplicate_id_fails(self):
        x = fixture()
        block = x[x.index("### Paper:"):x.index("<!-- PAPER_IDS -->")]
        x = x.replace("<!-- PAPER_IDS -->", block + "<!-- PAPER_IDS -->")
        with self.assertRaises(ValueError):
            self.parse(x)
    def test_ids_mismatch_fails(self):
        with self.assertRaises(ValueError):
            self.parse(fixture().replace("arxiv:2611.12705\n<!-- /PAPER_IDS -->", "arxiv:2611.99999\n<!-- /PAPER_IDS -->"))
    def test_url_mismatch_fails(self):
        with self.assertRaises(ValueError):
            self.parse(fixture().replace("https://arxiv.org/abs/2611.12705", "https://arxiv.org/abs/2611.99999"))
    def test_schema_declared_without_papers_fails(self):
        with self.assertRaises(ValueError):
            self.parse("# Paper Watch\n> schema_version: 1\n")

if __name__ == "__main__":
    unittest.main()
