# papers — ChatGPT Scheduled Paper Watch

このリポジトリは、**OpenAI APIを使わず、Macや常時稼働サーバーも使わずに**、ChatGPTのクラウド実行とGitHubを組み合わせて最新論文を定期調査し、Markdownとして蓄積するための実験・運用リポジトリです。

現在の主な対象は次のとおりです。

- Machine Learning
- Large Language Models (LLM)
- Medical AI / Healthcare AI
- Sources: arXiv / PubMed

---

## 1. まず重要: 実態は「ChatGPT Workそのもの」ではなく Scheduled Tasks が中心

この仕組みの実行主体は、正確には **ChatGPTのScheduled Tasks（スケジュール済みタスク）** です。

ChatGPT WorkからScheduled Taskを作成・利用することはできますが、この仕組みは「Work専用のコード」が動いているわけではありません。

役割を分けると次のようになります。

```text
ChatGPT Scheduled Task
  = いつ実行するか / 何をするか / Web検索 / GitHubアプリ操作

GitHub repository
  = 検索条件 / 既読ID / 出力レポート / GitHub Actions
```

つまり、本番運用時にクラウド上で3日ごとに起動するのはChatGPTのScheduled Taskです。

Codex AutomationやMac上のCodexを使っているわけではありません。

OpenAI公式のScheduled Tasks説明:
https://help.openai.com/ja-jp/articles/10291617-scheduled-tasks-in-chatgpt

ChatGPT WorkとCodexの説明:
https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex

---

## 2. 現在どこまで実装済みか

### 実装済み

- ChatGPTとGitHubの接続
- GitHub Issueの無人作成テスト
- `[paper-report]` IssueをGitHub ActionsでMarkdown化する処理
- `reports/` への自動commit
- `state/seen_papers.txt` による既出論文ID管理
- arXiv / PubMedから20本選んだpilotレポートの作成
- 検索条件を `config/paper_watch.yml` に分離
- 本番Scheduled Task用の指示文テンプレートを `config/scheduled_task_prompt.md` に保存

### まだ実装していないもの

**3日ごとに繰り返す本番の論文ウォッチScheduled Taskは、まだChatGPT側に作成していません。**

初回20本のpilotレポートは、このチャット上で手動実行したものです。

したがって、現時点でこのリポジトリを見ても「3日ごと」という設定がGitHub内に存在しないのは正常です。

---

## 3. 全体の実行フロー

本番では次の流れになります。

```text
OpenAI cloud

ChatGPT Scheduled Task
        |
        | 起動周期: 3日ごと（ChatGPT側で設定）
        |
        | 1. GitHubから config/paper_watch.yml を読む
        | 2. state/seen_papers.txt を読む
        | 3. arXiv / PubMedをWeb検索
        | 4. 候補を選定・要約
        | 5. GitHub Issueを1件作成
        v

GitHub repository: drkamoshika/papers

Issue
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

- Macの常時起動
- 自前サーバー
- OpenAI API key
- OpenAI APIの従量課金
- GitHub ActionsからLLM APIを呼ぶ処理

---

## 4. ChatGPT側の「実体」はどこにあるのか

GitHubだけを見ても、このシステム全体は把握できません。

ChatGPT側には次の2つの状態があります。

### 4.1 Scheduled Task本体

本番タスクを作成すると、ChatGPTアカウント側に以下が保存されます。

- タスク名
- 実行周期
- 次回実行日時
- タスクへの指示文（prompt）
- 有効 / 一時停止状態
- 過去の実行結果
- タスクに関連付けられたチャット

### どこで見るか

ChatGPTのサイドバーから **「スケジュール」** を開きます。

Web版ではここから、

- タスク一覧
- 次回実行日時
- 過去の回答
- タスクの編集
- 一時停止 / 再開
- 削除

を確認できます。

今回の検証では、Web版の「スケジュール」画面が最も確実に確認できました。

OpenAI公式にも、Scheduledページから既存タスクの回答・次回実行・編集・一時停止・再開・削除を管理できると記載されています。

### 4.2 GitHubアプリの接続と権限

ChatGPTからGitHub Issueを作るため、GitHubアプリ / Plugin / Connectorを接続しています。

ChatGPTの **設定 → Apps / Plugins → GitHub** 付近から、接続状態や権限を確認します。

今回の検証では、GitHub操作を `Always allow` に設定した後、Scheduled TaskからIssueを無人作成できました。

アプリ権限によってはScheduled Taskが「対応が必要」となり、ユーザー承認待ちで停止することがあります。

---

## 5. Scheduled Taskの指示文はどこにあるのか

実際に実行される指示文は、**ChatGPT側のScheduled Task本体に保存されます**。

GitHubのREADMEやconfigを変更しても、ChatGPT側のタスクpromptそのものが自動で書き換わるわけではありません。

ただし、再現性を確保するため、このリポジトリにも原本を保存します。

```text
config/scheduled_task_prompt.md
```

このファイルは、

- 別のChatGPTアカウントで再構築するとき
- タスクを作り直すとき
- 現在の指示設計をGitHub上で確認したいとき

のための**canonical template**です。

### 重要

```text
GitHub側の scheduled_task_prompt.md
        ↓
   自動同期しない
        ↓
ChatGPT側のScheduled Task prompt
```

したがって、本番タスク作成後に根本的な指示を変える場合は、

1. `config/scheduled_task_prompt.md` を更新
2. ChatGPTの「スケジュール」でタスク本体も編集

という2段階になります。

一方、検索テーマや最大論文数などは後述の `paper_watch.yml` を毎回読む設計なので、GitHub側だけ変更すれば反映できます。

---

## 6. 何を変更したいとき、どこを触ればいいか

| 変更したい内容 | 変更場所 |
|---|---|
| 3日ごと → 毎週など実行周期 | ChatGPT → スケジュール → 該当タスク |
| タスクを一時停止 / 再開 | ChatGPT → スケジュール |
| タスクの根本的な指示 | ChatGPT → スケジュール → タスク編集 |
| 指示文の再現用原本 | `config/scheduled_task_prompt.md` |
| 最大論文数 20 → 10 / 30 | `config/paper_watch.yml` の `max_papers` |
| 検索テーマ | `config/paper_watch.yml` の `topics` |
| arXiv / PubMedなど検索元 | `config/paper_watch.yml` の `sources` |
| 遡る日数 | `config/paper_watch.yml` の `lookback_days` |
| サマリ項目 | `config/paper_watch.yml` の `summary` |
| 既出論文一覧 | `state/seen_papers.txt` |
| IssueからMarkdownへの変換処理 | `.github/workflows/import-paper-report.yml` |
| 過去レポート | `reports/` |
| GitHub操作の承認レベル | ChatGPTのGitHubアプリ設定 |

この設計では、**普段のチューニングはなるべくGitHub側のconfigだけで済む**ようにします。

Scheduled Taskのpromptは「毎回configを読む」という比較的固定の役割にしておくのがポイントです。

---

## 7. GitHub側の設定ファイル

### `config/paper_watch.yml`

論文ウォッチの可変設定です。

現在は概ね以下を持ちます。

```yaml
sources:
  - arxiv
  - pubmed

max_papers: 20
lookback_days: 14

topics:
  - machine learning
  - large language models
  - medical AI
  - healthcare AI
```

加えてサマリ項目や重複排除方式を定義しています。

本番を3日ごとに回すなら、`lookback_days` は4〜7日程度にして、多少期間を重ねながらcanonical IDで重複排除する方法が安全です。

### `config/scheduled_task_prompt.md`

ChatGPT Scheduled Taskに入れる指示文の原本です。

実際のScheduled Taskを別環境で作り直す場合は、この内容を基準にします。

### `state/seen_papers.txt`

既出論文判定用の軽量インデックスです。

```text
arxiv:2608.19746
arxiv:2608.17268
pmid:42545345
pmid:42373953
```

過去の `reports/` を毎回全文走査しないために使います。

数千本蓄積しても本文レポートよりはるかに小さいため、Scheduled Taskは毎回このファイルだけ読めば既出判定できます。

### `.github/workflows/import-paper-report.yml`

GitHub IssueをMarkdownへ変換してcommitするActionsです。

`[paper-report]` から始まるIssueだけ処理します。

処理内容:

1. Issueを受け取る
2. `reports/issue-N.md` を作る
3. Issue本文を保存
4. `PAPER_IDS` ブロックからcanonical IDを抽出
5. `state/seen_papers.txt` を更新・重複排除
6. `github-actions[bot]` がcommit/push

---

## 8. なぜChatGPTからGitHubへ直接Markdownを書かないのか

検証では次の違いがありました。

```text
通常のChatGPTチャット
  -> GitHub create_file
  -> 成功

Scheduled Task
  -> GitHub create_file
  -> 安全チェックでブロック
```

一方で、GitHub Issue作成は権限設定後にScheduled Taskから実行できました。

そのため、Issueを中継点にしています。

```text
Scheduled Task
  -> GitHub Issue
  -> GitHub Actions
  -> Markdown
```

この構造は直接writeより1段増えますが、Scheduled Task側の権限制約とGitHub側の自動処理をきれいに分離できます。

---

## 9. 1論文1Issueではなく「1実行1Issue」

現在は、**1回の定期実行につきIssueを1件だけ作成**します。

例えば20本なら1つのIssue本文に20本をまとめます。

理由:

- GitHub write操作が1回で済む
- Actionsも1回で済む
- 失敗ポイントが減る
- 「その実行時点の研究動向」というスナップショットになる
- commit履歴も実行単位で分かりやすい

後から特に重要な論文だけ、個別Issueへ昇格させる運用は可能です。

---

## 10. 論文ごとのサマリ形式

本番では短いSummaryだけでなく、次の情報を可能な範囲で取得します。

```markdown
## Paper title

- Source
- canonical ID
- Published
- Authors
- Journal / Category
- URL
- Read level: abstract / full text

### 目的
何を解こうとしているか。

### 手法
モデル、アルゴリズム、研究デザイン、比較方法など。

### データ・実験
データセット、症例数、benchmark、評価指標など。

### 主な結果
重要な定量結果を優先。

### 新規性
既存研究と比べて何が新しいか。

### 限界
一次情報から確認できる範囲のみ。推測で作らない。

### なぜ注目したか
今回の研究動向の中での意味。
```

医療AIでは、取得できる場合に次も含めます。

- study design
- sample size
- primary endpoint
- external validation
- prospective / retrospective

本文にアクセスできずabstractしか読めない場合は、必ず `Read level: abstract` と明記します。

---

## 11. 本番Scheduled Taskを作るときの手順

1. ChatGPTでGitHubアプリが接続済みであることを確認する
2. GitHubアプリが `drkamoshika/papers` にアクセスできることを確認する
3. 必要ならGitHub操作権限を設定する
4. ChatGPTの「スケジュール」を開く
5. 新しいScheduled Taskを作成する
6. 指示文には `config/scheduled_task_prompt.md` の内容を使う
7. 実行周期を「3日ごと」に設定する
8. 作成後、タスク詳細画面で次回実行日時と指示内容を確認する
9. 初回実行後、GitHub Issueが作られたことを確認する
10. Actionsが `reports/` と `state/seen_papers.txt` を更新したことを確認する

---

## 12. 別環境で再現する方法

このGitHubリポジトリだけでは、ChatGPT側のScheduled TaskとGitHub OAuth接続は復元されません。

別のChatGPTアカウント・環境では次が必要です。

```text
GitHub repository
    +
GitHub Plugin / Connector接続
    +
GitHub権限設定
    +
ChatGPT Scheduled Task作成
```

再現手順:

1. このrepositoryを利用可能にする
2. ChatGPTでGitHubを接続する
3. repositoryへのアクセスを許可する
4. `config/paper_watch.yml` を確認する
5. `config/scheduled_task_prompt.md` を確認する
6. ChatGPTのスケジュール画面から新規タスクを作る
7. prompt templateをタスクへ設定する
8. 3日ごとの周期を設定する
9. テスト実行する
10. Issue → Actions → reportsへのcommitを確認する

---

## 13. ChatGPTのタスクを削除・編集するときの注意

Scheduled TaskはGitHub Actionsとは独立しています。

- Scheduled Taskを停止しても、GitHub Actionsファイルは残る
- GitHub Actionsを削除しても、Scheduled Taskは起動し続ける可能性がある
- GitHub接続を解除すると、Scheduled TaskはIssue作成に失敗する
- アプリ操作で追加承認が必要になると、タスクが対応待ち / 一時停止になる可能性がある
- 関連付けられたScheduled Taskのチャットを削除すると、タスクが一時停止する場合がある

問題が起きたら、まずChatGPTの「スケジュール」でタスク実行結果を確認し、次にGitHubのIssues / Actionsを見ると切り分けやすいです。

---

## 14. トラブルシューティングの見る順番

### 論文レポートが作られない

1. ChatGPT → スケジュール
   - タスクが有効か
   - 最終実行が成功したか
   - 「対応が必要」になっていないか

2. GitHub → Issues
   - `[paper-report]` Issueが作られたか

3. GitHub → Actions
   - `Import paper report issue` が実行されたか

4. GitHub → `reports/`
   - `issue-N.md` が作られたか

5. GitHub → `state/seen_papers.txt`
   - IDが追記されたか

この順番で見ると、ChatGPT側の問題かGitHub側の問題かを切り分けやすいです。

---

## 15. 現在の主なファイル構成

```text
papers/
├── README.md
├── config/
│   ├── paper_watch.yml
│   └── scheduled_task_prompt.md
├── state/
│   └── seen_papers.txt
├── reports/
│   └── issue-2.md
└── .github/
    └── workflows/
        └── import-paper-report.yml
```

---

## 16. 設計方針

この仕組みでは、役割を次のように分離します。

```text
ChatGPT Scheduled Task
= reasoning / Web調査 / 要約 / Issue作成

config/paper_watch.yml
= 頻繁に変えたい検索条件

state/seen_papers.txt
= 軽量な長期状態

GitHub Issue
= ChatGPTからGitHubへの受け渡し

GitHub Actions
= deterministicなファイル生成とcommit

reports/
= 人間が読む長期アーカイブ
```

この分離により、OpenAI APIや常時稼働PCを使わず、処理の実態をできるだけGitHub上にも可視化・再現できる構成を目指します。
