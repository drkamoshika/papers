# papers — ChatGPT Scheduled Paper Watch

このリポジトリは、**OpenAI APIを使わず、Macや常時稼働サーバーも使わずに**、ChatGPTのScheduled Taskで最新論文を定期調査し、その結果をGitHubへMarkdownとして蓄積するための実験・運用リポジトリです。

現在の対象は主に以下です。

- Machine Learning
- Large Language Models (LLM)
- Medical AI / Healthcare AI
- Sources: arXiv / PubMed

---

## 1. 全体構成

この仕組みでは、ChatGPTのScheduled TaskからGitHubリポジトリへ直接ファイルを書き込ませません。

Scheduled TaskからのGitHubファイル直接書き込みは安全チェックでブロックされる場合がある一方、GitHub Issue作成は許可設定後に無人実行できることを確認できました。そのため、**GitHub Issueを安全な中継点**として利用します。

```text
ChatGPT Scheduled Task（OpenAIクラウド）
        |
        | 1. GitHubから設定を読む
        | 2. arXiv / PubMedの新着を検索
        | 3. 論文を選定・要約
        | 4. GitHub Issueを1件作成
        v
GitHub Issue
  [paper-report] YYYY-MM-DD ...
        |
        | issues.opened
        v
GitHub Actions
  .github/workflows/import-paper-report.yml
        |
        +--> reports/issue-N.md を生成
        |
        +--> state/seen_papers.txt を更新
        |
        v
github-actions[bot] が main に commit
```

このため、通常運用では以下は不要です。

- Macの常時起動
- 自前サーバー
- OpenAI API key
- OpenAI APIの従量課金
- GitHub ActionsからLLM APIを呼ぶ処理

---

## 2. どこに何が設定されているか

この仕組みは、**GitHub側の設定**と**ChatGPT側の設定**の2か所に分かれています。

### GitHub側

#### `config/paper_watch.yml`

論文ウォッチの設定値です。

現在は以下を持ちます。

- `sources`: arXiv / PubMed
- `max_papers`: 1回のレポートに含める最大論文数
- `lookback_days`: 何日前まで遡って候補を探すか
- `topics`: 検索テーマ
- `summary.fields`: 論文ごとにまとめる項目
- `deduplication`: 既出論文の判定方法

`max_papers` を変更すれば、例えば20本から10本、30本へ変更できます。

> Note: 現在の `lookback_days: 14` は初回試験用です。3日ごとの本番運用なら、4〜7日程度に短くして重複除外を併用するのが合理的です。

#### `.github/workflows/import-paper-report.yml`

GitHub IssueをMarkdownへ変換してcommitするGitHub Actionsです。

以下のIssueだけを処理します。

```text
[paper-report] ...
```

処理内容は次の通りです。

1. Issueが新規作成される
2. `reports/issue-N.md` を作成
3. Issueタイトル、URL、作成日時、本文を保存
4. Issue本文末尾の `PAPER_IDS` ブロックから論文IDを抽出
5. `state/seen_papers.txt` に追記・重複排除
6. `github-actions[bot]` がcommit/push

#### `reports/`

各実行の最終レポートが保存されます。

現在はIssue番号を使い、次の形式です。

```text
reports/issue-2.md
reports/issue-3.md
...
```

Issue番号を使うことでファイル名の衝突を避けています。必要なら将来 `YYYY-MM-DD.md` 形式へ変更できます。

#### `state/seen_papers.txt`

既出論文判定用の**小さな索引**です。

過去の `reports/` を毎回すべて読ませると、レポートが増えるほどChatGPT側の読み込み量も増えます。そのため、過去レポート本文を全走査する方式は採用しません。

代わりに、以下のようなcanonical IDだけを保存します。

```text
arxiv:2608.19746
arxiv:2608.17268
pmid:42545345
pmid:42373953
```

数千本の論文を蓄積しても、このファイルは非常に小さいため、Scheduled Taskは毎回これだけを読めば既出判定できます。

### ChatGPT側

GitHubリポジトリには保存されない設定があります。

#### GitHub Plugin / Connector

ChatGPTのGitHub連携を接続し、このリポジトリへのアクセスを許可します。

今回の検証では、GitHubの操作確認を `Always allow` にした後、Scheduled TaskからGitHub Issueを無人作成できました。

#### Scheduled Task

**実行周期とエージェントへの指示そのものはChatGPT側に保存されます。**

つまり、3日ごとのスケジュールは `.github/workflows/` や `config/` には存在しません。

別環境へ再現する場合は、GitHubリポジトリをcloneするだけではなく、ChatGPT側でもScheduled Taskを作る必要があります。

Scheduled Tasksの一覧・編集は、現状Web版ChatGPTから確認するのが確実です。

---

## 3. 1論文1Issueではなく「1実行1Issue」にする理由

現在は、**1回の定期実行につきGitHub Issueを1件だけ作成**します。

例えば1回20本なら、1つのIssue本文に20本をまとめます。

この方式を推奨する理由は次の通りです。

- 20本ならIssueが20件ではなく1件で済む
- GitHub write操作の回数が少ない
- Scheduled Taskの失敗点が少ない
- GitHub Actionsも1回だけ実行される
- 「2026-08-23時点で何が注目だったか」というスナップショットとして読みやすい
- 1実行単位でcommit履歴が残る

一方、特定論文について後から議論・タスク管理したくなった場合だけ、重要論文を個別Issueへ昇格させる運用が適しています。

---

## 4. 論文ごとのサマリ形式

初回試験では短い `Summary` と `Why interesting` が中心でしたが、本番ではもう少し情報量を増やします。

推奨フォーマットは以下です。

```markdown
## 1. Paper title

- Source: arXiv / PubMed
- ID: arxiv:xxxx.xxxxx / pmid:xxxxxxxx
- Published: YYYY-MM-DD
- Authors: ...
- Journal / Category: ...
- URL: ...
- Read level: abstract / full text

### 目的
この研究が何を解こうとしているか。

### 手法
モデル、アルゴリズム、研究デザイン、比較方法など。

### データ・実験
データセット、症例数、benchmark、評価指標など。

### 主な結果
重要な定量結果を優先して記載する。

### 新規性
既存研究と比べて何が新しいか。

### 限界
著者が述べている限界、またはabstractから明確に判断できる制約。
推測で限界を作らない。

### なぜ注目したか
ML / LLM / 医療AIの流れの中で、なぜ読む価値があるか。
```

医療論文では可能な範囲で以下も含めます。

- study design
- sample size
- primary endpoint
- external validationの有無
- prospective / retrospective

ただし本文へアクセスできずabstractしか確認できない場合は、`Read level: abstract` と明記し、本文を読んだように書かないことを重要なルールとします。

---

## 5. 既出論文の扱い

### 採用しない方式

```text
毎回 reports/ 以下を全部読む
```

これは実行回数が増えるほど読み込み量が増えるため採用しません。

### 採用する方式

```text
state/seen_papers.txt
```

だけを読む方式です。

Scheduled TaskがGitHub Issueを作成するとき、本文の最後に次の機械可読ブロックを付けます。

```text
<!-- PAPER_IDS -->
arxiv:2608.19746
arxiv:2608.17268
pmid:42545345
<!-- /PAPER_IDS -->
```

GitHub Actionsはここから `arxiv:` / `pmid:` の行だけを抽出して `state/seen_papers.txt` に保存します。

次回Scheduled Taskは、検索結果のcanonical IDが `state/seen_papers.txt` に存在する場合、その論文を原則除外します。

### バージョン更新について

arXivは同じ論文IDでversionが更新される場合があります。現在はcanonical ID単位で既出扱いにする想定です。

将来、重大なversion updateも拾いたい場合は、例えば

```text
arxiv:2608.19746:v2
```

のようにversionも管理する方式へ変更できます。

---

## 6. Scheduled Taskの推奨指示

本番用タスクでは、概ね以下を指示します。

```text
GitHubリポジトリ drkamoshika/papers を使って定期論文ウォッチを実行する。

1. config/paper_watch.yml を読む。
2. state/seen_papers.txt が存在すれば読む。
3. 設定されたsourcesだけを対象に最新論文を検索する。
   現在は arXiv と PubMed。
4. topicsを検索テーマとして使う。
5. lookback_days の期間を中心に新着候補を集める。
6. arXiv IDまたはPMIDがseen_papers.txtにある論文は原則除外する。
7. 重要度・新規性・テーマとの関連性を考慮して max_papers 件まで選ぶ。
8. 各論文を日本語で要約する。

各論文について最低限以下を含める。
- Source
- canonical ID
- Published
- Authors
- Journal / Category
- URL
- Read level (abstract / full text)
- 目的
- 手法
- データ・実験
- 主な結果
- 新規性
- 限界
- なぜ注目したか

abstractしか確認できない場合は、その範囲を超えて推測しない。
可能なら定量結果を含める。

最後に今回の全体傾向を短くまとめる。

GitHubには論文ごとではなく、1実行につき1件だけIssueを作成する。
Issue titleは次の形式にする。

[paper-report] YYYY-MM-DD ML / LLM / Medical AI

Issue本文の最後に次の形式でcanonical ID一覧を付ける。

<!-- PAPER_IDS -->
arxiv:...
pmid:...
<!-- /PAPER_IDS -->

リポジトリファイルへ直接commitしない。
GitHub Issue作成までをChatGPT側で行い、その後のMarkdown化とcommitはGitHub Actionsに任せる。
```

### 実行周期

本番候補は**3日ごと**です。

3日ごとに実行する場合、検索期間は4〜7日程度にして少し重複期間を持たせ、`seen_papers.txt` で既出を除く方式が扱いやすいです。

---

## 7. 新しい環境で再現する手順

### Step 1: GitHubリポジトリを用意

新しいGitHubリポジトリを作成します。

最低限、以下を用意します。

```text
repo/
├── README.md
├── config/
│   └── paper_watch.yml
├── state/
│   └── seen_papers.txt      # 初回は空でもよい
├── reports/                 # Actionsが作成
└── .github/
    └── workflows/
        └── import-paper-report.yml
```

### Step 2: ChatGPTへGitHub Pluginを接続

ChatGPT Web版でGitHub連携を追加し、対象リポジトリへのアクセスを許可します。

無人Issue作成を行う場合、GitHub write操作のpermission設定を確認します。

### Step 3: 手動IssueでGitHub Actionsを確認

次のタイトルでIssueを1件作ります。

```text
[paper-report] workflow test
```

Issue本文は適当なMarkdownで構いません。

成功するとActionsが起動し、

```text
reports/issue-N.md
```

が自動commitされます。

### Step 4: ChatGPT通常チャットからIssue作成を確認

ChatGPTに次のように頼みます。

```text
GitHubの owner/repo に
[paper-report] ChatGPT integration test
というIssueを作って。
```

これが通ればGitHub連携自体は動いています。

### Step 5: Scheduled TaskでIssue作成を確認

数分後に一度だけIssueを作成するScheduled Taskを設定します。

ここで手動承認が必要になる場合は、Plugin permissionを確認します。

### Step 6: 論文ウォッチScheduled Taskを作成

上記「Scheduled Taskの推奨指示」を使い、希望する周期を設定します。

重要なのは、**Scheduled TaskはGitHubリポジトリ内ではなくChatGPTアカウント側に存在する**点です。

---

## 8. 現在までに確認できたこと

実際の検証では以下を確認済みです。

### 通常チャット → GitHubファイル直接作成

成功。

### Scheduled Task → GitHubファイル直接作成

安全チェックでブロックされた。

そのため本番方式には採用しない。

### Scheduled Task → GitHub Issue作成

GitHub Pluginのpermission設定後、無人実行に成功。

### GitHub Issue → GitHub Actions → Markdown → commit

成功。

### arXiv / PubMed検索 → 約20論文のサマリ → Issue → Markdown保存

初回pilotで成功。

---

## 9. 現在の本番化ステータス

GitHub側の受け皿は動作しています。

```text
ChatGPT -> Issue -> Actions -> Markdown -> commit
```

まで動作確認済みです。

一方、**3日ごとの本番Scheduled Taskはまだ固定運用として設定していません。**

今後はサマリ形式、検索キーワード、検索期間、論文数を数回試してから本番タスクを固定する方針です。

---

## 10. 今後の改善候補

- `lookback_days` を本番用に4〜7日へ変更
- arXiv / PubMedの件数配分を設定可能にする
- topicごとの上限を設定する
- review / original research / benchmarkなど論文種別の扱いを設定する
- 高重要度論文だけ個別Issueへ昇格する
- `reports/YYYY-MM-DD.md` のような日付ベースファイル名へ変更する
- arXiv version updateを追跡する
- 月次・四半期単位で過去レポートを横断したtrend summaryを作る

---

## 11. 設計上の考え方

このリポジトリは、GitHub ActionsにAI処理をさせる仕組みではありません。

AI処理はChatGPTのScheduled Taskが担当し、GitHub Actionsは**保存処理だけ**担当します。

```text
ChatGPT = 調査・選定・要約
GitHub Issue = 安全な受け渡し
GitHub Actions = deterministicな保存処理
GitHub Repository = 長期アーカイブ
```

この分離により、OpenAI APIを使わず、ローカルマシンも使わずに、クラウドだけで定期的な論文ウォッチを蓄積できます。
