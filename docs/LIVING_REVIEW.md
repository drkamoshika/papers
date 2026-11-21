# 研究領域マップ・動向レビューの更新仕様

「全体マップ」と「研究動向レビュー」は、同じ7分野を別々に説明していたため、`docs/overview.json` を正本とする単一の更新型レビューへ統合した。

## 正本と公開先

- 構造化データ: `docs/overview.json`
- ダッシュボード: `docs/index.html?view=map`
- 文章版の入口: `reports/overviews/README.md`
- 分野別の詳細章: `reports/overviews/01-language.md` 〜 `07-neuroscience.md`
- 週ごとの変更記録: `reports/weekly/YYYY-Www.md`

`docs/trends.json` は持たない。旧 `docs/trends.html` は既存リンクを壊さないための転送専用で、本文やデータを持たない。

## 毎週更新する内容

1. その週に追加された論文を7分野へ配置し、既存の系譜・比較・到達点との関係を確認する。
2. 各分野の `currentUpdate` を更新する。必須項目は、現在地、理解の変化、全体像、今回の根拠、まだ言えないこと、次の課題、重要文献。
3. 大きな進展がない分野も削除せず、「変更なし」と判断した根拠と隣接研究の扱いを記録する。
4. `livingReview.crossCutting` に分野横断の関係、`weeklyReports` に週次記録を追加する。
5. `reports/weekly/YYYY-Www.md` を保存し、文章版の該当分野にも新しい証拠で変わった箇所を反映する。
6. `python scripts/validate_living_review.py` を実行する。

新着を別レビューとして積み上げるのではなく、過去の理解が維持されたか、修正されたか、反証されたかを明示する。異なる課題の指標を直接比較せず、実験結果・編者の統合的解釈・未検証の仮説を区別する。

## 週次自動化への指示

週次処理は `reports/trends/overview.md` や `docs/trends.json` を生成しない。上記の正本、分野別の文章版、週次変更記録だけを更新する。公開前に検証スクリプトを通し、7分野の更新日、重要文献ID、HTTPSの一次資料リンク、最新週との整合を確認する。
