# papers — ChatGPT Scheduled Paper Watch

このリポジトリは、**OpenAI APIを使わず、Macや常時稼働サーバーも使わずに**、ChatGPTのScheduled TasksとGitHubを組み合わせて最新論文を定期調査し、Markdownとして蓄積するための仕組みです。

現在の対象は主に以下です。

- Machine Learning
- Large Language Models (LLM)
- Medical AI / Healthcare AI
- Sources: arXiv / PubMed

---

## 1. 結論: 実行トリガーだけChatGPT、運用仕様はGitHubで管理する

この仕組みでは、ChatGPT側に長い指示文を直接持たせません。

**GitHubの `config/paper_watch.yml` を唯一の運用仕様（source of truth）にし、ChatGPT Scheduled Taskは毎回そのYAMLを読んで従うだけ**にしています。

```text
ChatGPT Scheduled Task
  ├─ いつ起動するか
  └─ 「GitHubの paper_watch.yml を読んで従え」という短い指示
          |
          v
GitHub: config/paper_watch.yml
  ├─ 検索元
  ├─ 検索テーマ
  ├─ 最大論文数
  ├─ 遡及期間
  ├─ 重複除外方法
  ├─ サマリ項目
  ├─ 論文選定方針
  ├─ Issue出力方法
  └─ ChatGPTが毎回行う詳細な task_instructions
```

このため、通常の動作調整はGitHub上のYAMLを編集するだけで、次回のScheduled Taskから反映されます。

### ChatGPT側に残るもの

- タスク名
- 実行周期 / 実行時刻
- 有効 / 停止状態
- 最小限のbootstrap prompt
- 実行履歴

### GitHub側に置くもの

- エージェントの詳細な指示
- 検索条件
- 既読ID
- レポート
- IssueをMarkdown化するGitHub Actions

---

## 2. 現在の本番設定

2026-08-23時点で、本番用Scheduled Task **「最新論文ウォッチ」** をChatGPT側に作成済みです。

現在の設定:

```text
実行周期: 3日ごと
初回: 2026-08-23 15:00ごろ JST
実行方式: flexible schedule
```

時刻を厳密に15:00固定する設定ではなく、概ねその前後で実行されます。

> 注意: 実行周期そのものはChatGPTアカウント側のScheduled Taskに保存されます。GitHubのYAMLを編集しても「3日ごと」という周期自体は変わりません。

---

## 3. Scheduled Task本体には何が書かれているか

ChatGPT側の本番タスクには、現在ほぼ次の指示だけが入っています。

```text
GitHub連携を使って `drkamoshika/papers` の `config/paper_watch.yml` を毎回読み、そこに書かれた設定と `task_instructions` をこの実行の唯一の運用仕様として、論文watchを1回実行する。YAMLを読めない、内容が不正、GitHub操作が失敗した場合は推測で代替せず、失敗理由を報告する。
```

つまり、実際の検索や要約の詳細はScheduled Task側にはほとんどありません。

**詳細はすべて `config/paper_watch.yml` の `task_instructions` にあります。**

---

## 4. どこを見れば実態が分かるか

### 4.1 ChatGPT側

Web版ChatGPTのサイドバーから **「スケジュール」** を開きます。

ここで確認・変更できるもの:

- 「最新論文ウォッチ」が有効か
- 次回実行日時
- 実行周期
- Scheduled Taskに保存されているbootstrap prompt
- 過去の実行結果
- 一時停止 / 再開
- 削除

今回の検証では、Scheduled Taskの一覧確認はWeb版が最も確実でした。

### 4.2 GitHub側

実際の動作仕様は以下を見ます。

```text
config/paper_watch.yml
```

これが最重要ファイルです。

---

## 5. 何を変更したいとき、どこを編集するか

| 変更内容 | 編集場所 |
|---|---|
| 3日ごと → 毎週 | ChatGPT → スケジュール → 最新論文ウォッチ |
| 実行時刻 | ChatGPT → スケジュール |
| 一時停止 / 再開 | ChatGPT → スケジュール |
| 最大20本 → 10本 / 30本 | `config/paper_watch.yml` の `max_papers` |
| arXiv / PubMed | `config/paper_watch.yml` の `sources` |
| 検索テーマ | `config/paper_watch.yml` の `topics` |
| 遡る日数 | `config/paper_watch.yml` の `lookback_days` |
| サマリ項目 | `config/paper_watch.yml` の `summary` |
| 論文選定方針 | `config/paper_watch.yml` の `selection` |
| ChatGPTの詳細な処理手順 | `config/paper_watch.yml` の `task_instructions` |
| 既出論文一覧 | `state/seen_papers.txt` |
| Issue→Markdown変換 | `.github/workflows/import-paper-report.yml` |
| 過去レポート | `reports/` |
| GitHub操作の承認レベル | ChatGPTのApps / Plugins → GitHub |

**基本的には、周期以外はGitHubだけ見れば調整できる設計です。**

---

## 6. `config/paper_watch.yml` の役割

現在の正本です。

主な構造:

```yaml
version: 1
repository: drkamoshika/papers

sources:
  - arxiv
  - pubmed

max_papers: 20
lookback_days: 5

topics:
  - machine learning
  - large language models
  - medical AI
  - healthcare AI

summary:
  ...

deduplication:
  ...

selection:
  ...

output:
  ...

task_instructions: |
  Run one paper-watch cycle ...
```

### `max_papers`

1回の実行で採用する最大論文数。

```yaml
max_papers: 20
```

上限なので、良い論文が少なければ20本未満でもよい、という指示にしています。

### `lookback_days`

現在は3日ごとの運用に対して、取りこぼし防止のため5日分を見ます。

```yaml
lookback_days: 5
```

期間は少し重なりますが、既読IDで重複排除します。

### `topics`

広めの検索テーマ。

```yaml
topics:
  - machine learning
  - large language models
  - medical AI
  - healthcare AI
```

ここは後から自由に具体化できます。

### `summary`

論文ごとの出力項目を定義します。

現在は主に以下です。

- 目的
- 手法
- データ / 実験
- 主な結果
- 新規性
- 限界
- なぜ注目したか

加えて、医療AIでは取得できる場合に以下も含めます。

- study design
- sample size
- primary endpoint
- external validation
- prospective / retrospective

また、`Read level: full_text / abstract` を明記し、abstractしか読めなかった場合に本文を読んだように書かないルールを入れています。

### `task_instructions`

**ChatGPTエージェントへの実際の詳細指示です。**

本番の動作を変えたい場合は、ここを編集します。

例:

- 論文選定基準を変更する
- レポート冒頭の概況をもっと長くする
- 特定分野を優先する
- PubMedを多めにする
- 定量結果を必須に近づける

などはここで調整できます。

Scheduled Taskは毎回このYAMLを読み直すため、YAMLをcommitすれば**次回から新しい指示が反映されます**。

---

## 7. 全体の実行フロー

```text
OpenAI cloud

ChatGPT Scheduled Task
        |
        | 3日ごとに起動
        v
GitHubから config/paper_watch.yml を読む
        |
        | task_instructionsを取得
        v
state/seen_papers.txt を読む
        |
        v
arXiv / PubMedをWeb検索
        |
        v
最大 max_papers 本を選定
        |
        v
詳細な日本語レポートを生成
        |
        v
GitHub Issueを1件作成
[paper-report] YYYY-MM-DD ...
        |
        | issues.opened
        v
GitHub Actions
.github/workflows/import-paper-report.yml
        |
        +--> reports/issue-N.md
        |
        +--> state/seen_papers.txt 更新
        |
        v
github-actions[bot] が main に commit
```

通常運用では以下は不要です。

- Mac常時起動
- 自前サーバー
- OpenAI API key
- OpenAI API従量課金
- GitHub ActionsからLLM APIを呼ぶ処理

---

## 8. なぜGitHub Issueを中継するのか

検証では次の挙動でした。

```text
通常チャット
  -> GitHubファイル直接作成
  -> 成功

Scheduled Task
  -> GitHubファイル直接作成
  -> OpenAI側の安全チェックでブロック
```

一方、GitHub操作を `Always allow` にした後、Scheduled TaskからのIssue作成は無人実行できました。

そのため本番では、

```text
Scheduled Task
  -> GitHub Issue
  -> GitHub Actions
  -> Markdown commit
```

という構造を使います。

---

## 9. 1論文1Issueではなく「1実行1Issue」

1回20本でもIssueは1件だけ作ります。

理由:

- GitHub write操作が1回で済む
- Actionsも1回だけ
- Scheduled Taskの失敗点が少ない
- 実行時点の研究動向を1つのスナップショットとして読める
- commit履歴が実行単位になる

特に重要な論文だけ後から個別Issueに昇格させる運用は可能です。

---

## 10. 重複除外

過去の `reports/` 全文は毎回読みません。

代わりに、

```text
state/seen_papers.txt
```

にcanonical IDだけを保存します。

例:

```text
arxiv:2608.19746
arxiv:2608.17268
pmid:42545345
pmid:42373953
```

Scheduled Taskは毎回この小さなファイルだけを読み、既出IDを除外します。

この方式ならレポートが増えても重複判定の読み込み量は小さいままです。

---

## 11. GitHub Actions

```text
.github/workflows/import-paper-report.yml
```

`[paper-report]` から始まるIssueが新規作成されたときだけ動きます。

処理内容:

1. Issueを取得
2. `reports/issue-N.md` を作成
3. Issue本文を保存
4. `PAPER_IDS` ブロックからcanonical IDを抽出
5. `state/seen_papers.txt` に追加してsort/unique
6. `github-actions[bot]` がmainへcommit/push

ChatGPT Scheduled Taskはrepoへ直接Markdownを書きません。

---

## 12. 補助ファイル `config/scheduled_task_prompt.md`

このファイルは現在、正本ではありません。

Scheduled Taskに入れる短いbootstrap promptを人間向けに保存した補助資料です。

**実行仕様の正本は `config/paper_watch.yml` です。**

---

## 13. GitHub連携の権限

ChatGPTからGitHub Issueを作成するにはGitHub Plugin / Connectorが必要です。

今回の検証では、Scheduled TaskからIssueを最初に作ろうとした際にユーザー承認が必要になりました。

GitHub操作を `Always allow` にした後の再テストでは、承認なしでIssue作成できました。

もし本番タスクで「対応が必要」と表示された場合は、ChatGPTのGitHubアプリ権限を確認してください。

---

## 14. 別環境で再現する手順

### A. GitHub側

1. このリポジトリ構成を用意する
2. `config/paper_watch.yml` を用意する
3. `state/seen_papers.txt` を用意する
4. `.github/workflows/import-paper-report.yml` を配置する
5. Actionsが `contents: write` で動けることを確認する

### B. ChatGPT側

1. GitHub Plugin / Connectorを接続する
2. 対象repositoryへのアクセスを許可する
3. GitHub操作の確認設定を適切に設定する
4. 通常チャットからテストIssueを作る
5. Scheduled TaskからテストIssueを作り、無人で通るか確認する
6. 本番Scheduled Taskを作る

Scheduled Taskのpromptは次だけでよいです。

```text
GitHub連携を使って `OWNER/REPOSITORY` の `config/paper_watch.yml` を毎回読み、そこに書かれた設定と `task_instructions` をこの実行の唯一の運用仕様として、論文watchを1回実行する。YAMLを読めない、内容が不正、GitHub操作が失敗した場合は推測で代替せず、失敗理由を報告する。
```

あとは実行周期をChatGPT側で設定します。

---

## 15. 日常運用で見る場所

普段は次の3か所だけ把握しておけば十分です。

### ChatGPT → スケジュール

確認するもの:

- 次回実行
- 成功 / 失敗
- 一時停止
- 実行周期

### `config/paper_watch.yml`

変更するもの:

- 論文数
- テーマ
- 検索期間
- 要約方法
- エージェントへの詳細指示

### `reports/`

読むもの:

- 実際に保存された論文レポート

---

## 16. 現在のファイル構成

```text
papers/
├── README.md
├── config/
│   ├── paper_watch.yml              # 運用仕様の正本
│   └── scheduled_task_prompt.md     # bootstrap promptの補助資料
├── state/
│   └── seen_papers.txt              # 既読canonical ID
├── reports/
│   └── issue-*.md                   # 実行ごとのレポート
└── .github/
    └── workflows/
        └── import-paper-report.yml   # Issue -> Markdown -> commit
```

---

## 17. 現在の設計思想

このシステムでは、

```text
ChatGPT = クラウド上の実行エージェント
GitHub YAML = エージェントの設定・指示
GitHub Issue = ChatGPTからGitHubへの受け渡し
GitHub Actions = 永続化処理
Git repository = 長期記憶 / 実行履歴
```

という役割分担にしています。

Scheduled Task側をなるべく薄くすることで、**「AIに今何を指示しているか」がGitHub上で可視化され、他環境でも再現しやすい**構成にしています。
