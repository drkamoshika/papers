# ChatGPT Scheduled Task — Paper Watch prompt template

このファイルは、ChatGPT側に作成する本番Scheduled Taskの**指示文の原本・再現用テンプレート**です。

> 重要: このファイルを変更しても、すでにChatGPT側に作成済みのScheduled Taskの指示文は自動では更新されません。
> 本番タスクを変更する場合は、ChatGPTの「スケジュール」画面でタスク本体も編集してください。

## Task prompt

GitHub連携とWeb検索を使って、定期的な論文ウォッチを1回実行する。

対象リポジトリは `drkamoshika/papers`。

1. 最初に `config/paper_watch.yml` を読み、sources、topics、max_papers、lookback_days、summary設定を取得する。
2. `state/seen_papers.txt` を読み、既出論文のcanonical ID一覧を取得する。過去の `reports/` 全体は重複判定のためには読まない。
3. 指定された期間について、対象sourceを検索する。現在のsourceはarXivとPubMed。
4. topicsに関連する候補を広めに集め、既出IDを除外する。
5. 候補から重要度・新規性・テーマのバランスを考えて、`max_papers` 以下を選ぶ。十分に有用な新着が少ない場合、上限まで無理に埋めない。
6. 各論文について、取得できた一次情報を読み、日本語でまとめる。可能なら原論文本文を読むが、abstractしか確認できない場合は必ず `Read level: abstract` と明記する。本文未確認なのに本文を読んだように書かない。
7. 各論文のサマリには、可能な範囲で以下を含める。
   - Source
   - canonical ID
   - Published date
   - Authors
   - Journal / Category
   - URL
   - Read level
   - 目的
   - 手法
   - データ・実験
   - 主な結果（定量値があれば優先）
   - 新規性
   - 限界
   - なぜ注目したか
8. 医療AI論文では、情報が取得できる場合、study design、sample size、primary endpoint、external validation、prospective / retrospectiveも含める。
9. レポート冒頭に「今回の概況」を置き、個々の論文の列挙だけでなく、今回の新着から見える研究トレンドを短く整理する。
10. 最後に、採用した全論文のcanonical IDを次の機械可読ブロックで付ける。

```text
<!-- PAPER_IDS -->
arxiv:xxxx.xxxxx
pmid:xxxxxxxx
<!-- /PAPER_IDS -->
```

11. 完成したレポート全体を本文として、`drkamoshika/papers` にGitHub Issueを1件だけ作成する。タイトルは `[paper-report] YYYY-MM-DD ML / LLM / Medical AI` の形式にする。
12. 1論文につき1 Issueは作らない。1回の実行につき1 Issueとする。
13. GitHubリポジトリへ直接ファイルを書き込まない。Issue作成後はGitHub ActionsがMarkdown化・commitする。
14. Issue作成に成功したら、作成したIssue番号を報告する。

## Recommended schedule

本番では3日ごとを想定する。実行周期はこのファイルではなく、ChatGPT側のScheduled Task設定で管理する。
