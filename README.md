# papers — ChatGPT Scheduled Paper Watch

OpenAI APIを使わず、Macや常時稼働サーバーも使わずに、**ChatGPT Scheduled Tasks + GitHub + GitHub Actions** で最新論文を定期収集・要約・保存する仕組みです。

現在の主な対象:

- Machine Learning
- Large Language Models (LLM)
- Medical AI / Healthcare AI
- Sources: arXiv / PubMed

---

## 1. 全体像

この仕組みでは、**実行トリガーだけChatGPT側に置き、実際の運用仕様はGitHub側で管理**します。

```text
ChatGPT Scheduled Task
  ├─ 実行周期: 3日ごと
  └─ 「GitHubの paper_watch.yml を読んで従え」
           |
           v
config/paper_watch.yml
  ├─ 検索元
  ├─ 検索テーマ
  ├─ 候補取得数
  ├─ 最終論文数
  ├─ サマリ形式
  ├─ 重複除外方法
  ├─ GitHub出力方法
  └─ task_instructions
           |
           v
arXiv / PubMedを検索・要約
           |
           v
GitHub Issueを1件作成
           |
           v
GitHub Actions
           |
           +--> reports/issue-N.md
           +--> state/seen_papers.txt
           |
           v
mainへ自動commit
```

通常運用では以下は不要です。

- Mac常時起動
- 自前サーバー
- OpenAI API key
- OpenAI API従量課金
- GitHub ActionsからLLM APIを呼ぶ処理

---

## 2. ChatGPT側にある実体

本番用Scheduled Task名:

```text
最新論文ウォッチ
```

現在の設定:

```text
実行周期: 3日ごと
実行方式: flexible schedule
```

Scheduled Task本体のpromptは意図的に短くしています。

```text
GitHub連携を使って `drkamoshika/papers` の `config/paper_watch.yml` を毎回読み、そこに書かれた設定と `task_instructions` をこの実行の唯一の運用仕様として、論文watchを1回実行する。YAMLを読めない、内容が不正、GitHub操作が失敗した場合は推測で代替せず、失敗理由を報告する。
```

### どこで確認・変更するか

Web版ChatGPTの **「スケジュール」** を開きます。

ここで変更するもの:

- 3日ごと → 毎週などの周期
- 実行時刻
- 一時停止 / 再開
- Scheduled Task本体のbootstrap prompt
- 実行履歴

**検索方法や要約形式はここではなくGitHub側で変更します。**

---

## 3. 運用仕様の正本

最重要ファイルは次です。

```text
config/paper_watch.yml
```

ChatGPT Scheduled Taskは毎回このファイルを読み直します。

そのため、通常のチューニングはYAMLを変更してcommitするだけで次回から反映されます。

### 現在の主要設定

```yaml
sources:
  - arxiv
  - pubmed

max_papers: 20

retrieval:
  mode: latest_count
  candidates_per_source: 15
  sort: newest_first

topics:
  - machine learning
  - large language models
  - medical AI
  - healthcare AI
```

### 20本をどう選ぶか

現在は日数で区切りません。

```text
arXiv から関連する最新候補 最大15件
PubMedから関連する最新候補 最大15件
            |
            v
最大30候補
            |
            +--> seen_papers.txtで既出除外
            +--> 内容・新規性・重要度を評価
            |
            v
最終最大20本
```

3日ごとの実行で**概ね20本程度を目指す**設定ですが、弱い・無関係な論文で無理に20本へ埋めないルールです。

---

## 4. 論文の取得方法

### arXiv

`recent` / `new` の一覧ページだけには依存しません。

検証中に、検索環境から古いキャッシュの一覧が取得され、最新論文を0件と誤判定したことがあったためです。

現在は次の手順です。

```text
Web検索で新しい関連候補を発見
       |
       v
arXiv IDを取得
       |
       v
個別の arxiv.org/abs/... ページで
投稿日・authors・abstract等を確認
```

### PubMed

個別のPubMed recordを確認します。

日付は原則として:

1. electronic / online publication date
2. それがなければPubMed上のpublication date

を使います。

雑誌の「2026 Aug号」だけを根拠に新着扱いにはしません。

---

## 5. サマリ形式

各論文は**短い初期版 + 詳細版の二層構造**です。

最初に一覧性の高い形式:

```markdown
- Tags:
- Summary:
- Why interesting:
```

その直後に詳細版:

```markdown
### 目的
### 手法
### データ・実験
### 主な結果
### 新規性
### 限界
### なぜ注目したか
```

加えて以下のmetadataを可能な範囲で付けます。

- Source
- canonical ID
- Published
- Authors
- Journal / Category
- URL
- read_level: `full_text` / `abstract`

医療AIでは、取得できる場合に以下も追加します。

- study design
- sample size
- primary endpoint
- external validation
- prospective / retrospective

abstractしか確認できない場合は `read_level: abstract` とし、本文を読んだようには書きません。

---

## 6. 重複除外

過去の `reports/` 全文は毎回読みません。

既出論文は次の小さな索引だけで管理します。

```text
state/seen_papers.txt
```

例:

```text
arxiv:2608.20331
arxiv:2608.20316
pmid:42550187
```

Scheduled Taskはこのcanonical ID一覧だけを読み、既出論文を原則除外します。

これによりレポートが増えても、毎回過去レポート全部を読む必要がありません。

---

## 7. なぜGitHub Issueを中継するのか

検証では次の挙動でした。

```text
通常チャット
  -> GitHubへ直接ファイル作成
  -> 成功

Scheduled Task
  -> GitHubへ直接ファイル作成
  -> OpenAI側の安全チェックでブロック
```

一方、GitHub操作を `Always allow` にした後は、Scheduled TaskからGitHub Issueを無人作成できました。

そのため本番は次の方式です。

```text
Scheduled Task
   -> GitHub Issue
   -> GitHub Actions
   -> Markdown file
   -> commit
```

1論文1Issueではなく、**1実行につきIssueを1件**作ります。

---

## 8. GitHub Actions

Workflow:

```text
.github/workflows/import-paper-report.yml
```

`[paper-report]` から始まるIssueが作成された時だけ動きます。

処理:

1. Issue本文を取得
2. `reports/issue-N.md` を生成
3. Issue本文末尾の `PAPER_IDS` blockを抽出
4. `state/seen_papers.txt` に追加
5. sort / unique
6. `github-actions[bot]` がmainへcommit/push

---

## 9. どこを変更すれば何が変わるか

| 変更したいこと | 編集場所 |
|---|---|
| 3日ごと → 毎週 | ChatGPT → スケジュール |
| 実行時刻 | ChatGPT → スケジュール |
| 最大20本 | `config/paper_watch.yml` → `max_papers` |
| sourceごとの候補数 | `retrieval.candidates_per_source` |
| arXiv / PubMed | `sources` |
| 検索テーマ | `topics` |
| 短いサマリ項目 | `summary.quick_fields` |
| 詳細サマリ項目 | `summary.detailed_fields` |
| 医療AI追加項目 | `summary.medical_ai_extra_fields` |
| 論文選定方針 | `selection.rules` |
| エージェントの詳細指示 | `task_instructions` |
| 既出論文 | `state/seen_papers.txt` |
| Issue→Markdown処理 | `.github/workflows/import-paper-report.yml` |

**周期以外は原則GitHub側だけで調整できます。**

---

## 10. 実行結果を見る場所

### ChatGPT

```text
スケジュール → 最新論文ウォッチ
```

見るもの:

- 次回実行
- 成功 / 失敗
- 実行履歴
- 対応が必要か

### GitHub Issues

ChatGPTが生成した生のレポート。

```text
[paper-report] YYYY-MM-DD ...
```

### reports/

GitHub Actionsが永続化したMarkdown。

```text
reports/issue-6.md
reports/issue-7.md
...
```

### state/seen_papers.txt

既出canonical IDの一覧。

---

## 11. 別環境で再現する手順

### GitHub側

1. repositoryを用意
2. `config/paper_watch.yml` を配置
3. `state/seen_papers.txt` を配置
4. `.github/workflows/import-paper-report.yml` を配置
5. GitHub Actionsに `contents: write` を許可

### ChatGPT側

1. GitHub Plugin / Connectorを接続
2. 対象repositoryへのアクセスを許可
3. GitHub writeの確認設定を適切に設定
4. 通常チャットからIssue作成をテスト
5. Scheduled TaskからIssue作成をテスト
6. 本番Scheduled Taskを作成

Scheduled Taskには以下のような短いbootstrap promptだけ設定します。

```text
GitHub連携を使って `OWNER/REPOSITORY` の `config/paper_watch.yml` を毎回読み、そこに書かれた設定と `task_instructions` をこの実行の唯一の運用仕様として、論文watchを1回実行する。YAMLを読めない、内容が不正、GitHub操作が失敗した場合は推測で代替せず、失敗理由を報告する。
```

---

## 12. ファイル構成

```text
papers/
├── README.md
├── config/
│   ├── paper_watch.yml              # 運用仕様の正本
│   └── scheduled_task_prompt.md     # bootstrap prompt補助資料
├── state/
│   └── seen_papers.txt              # 既出canonical ID
├── reports/
│   └── issue-*.md                   # 実行ごとのレポート
└── .github/
    └── workflows/
        └── import-paper-report.yml   # Issue -> Markdown -> commit
```

---

## 13. 設計思想

```text
ChatGPT Scheduled Task
  = クラウド上の定期実行トリガー + agent

config/paper_watch.yml
  = エージェントの設定・指示・運用仕様

GitHub Issue
  = ChatGPTからGitHubへの受け渡し

GitHub Actions
  = 永続化処理

Git repository
  = 長期記憶・履歴・再現可能な設定
```

Scheduled Taskを薄くし、詳細をGitHubのYAMLへ寄せることで、**「今AIに何をさせているか」をGit上で確認・変更・履歴管理できる**構成にしています。
