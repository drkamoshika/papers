# papers — GitHub Actions Paper Watch

arXiv / PubMedから関連論文を毎日検索し、GitHub Actions runner内でローカル実行するQwenで選定・要約して、Gmailへ**ダイジェスト＋完全版全文**を送る自動論文watchです。外部LLM APIは使いません。

ChatGPT Scheduled Tasks、Notion、GitHub Issue中継は使いません。

## 全体像

```text
GitHub Actions（毎朝 07:00 Asia/Tokyo）
        |
        v
config/paper_watch.yml
        |
        +--> state/seen_papers.txt を読み既出除外
        |
        +--> arXiv API / PubMed E-utilities
        |
        +--> Ollama + Qwen3 4B（runner内ローカル実行）
        |
        +--> Gmail SMTP
        |      └─ ダイジェスト + 完全版レポート
        |
        +--> 送信成功後のみ seen_papers.txt 更新
        |
        v
github-actions[bot] が seen_papers.txt をcommit
```

## 運用仕様の正本

`config/paper_watch.yml` が唯一の運用仕様です。

主な変更箇所:

- `topics`: 検索テーマ
- `retrieval.candidates_per_source`: sourceごとの候補数
- `max_papers`: 最終採用上限
- `llm.model`: Actions runner内でローカル実行するモデル
- `summary.*`: 要約項目
- `selection.rules`: 選定方針
- `task_instructions`: レポート生成・運用指示

## 実行スケジュール

Workflow:

`.github/workflows/paper-watch.yml`

通常実行:

- 毎日 07:00
- timezone: `Asia/Tokyo`

手動実行:

GitHub → **Actions** → **Paper Watch** → **Run workflow**

## 初回セットアップ

GitHub repositoryの

**Settings → Secrets and variables → Actions → Repository secrets**

に次の2つだけ登録します。

### GMAIL_ADDRESS

送信元かつ送信先にする自分のGmailアドレス。

### GMAIL_APP_PASSWORD

Gmail SMTP用のGoogleアプリ パスワード。

通常のGoogleアカウントパスワードは登録しません。Googleアカウントで2段階認証を有効にしたうえで、アプリ パスワードを生成して登録します。

LLM用APIキーは不要です。WorkflowがOllamaをインストールし、`qwen3:4b` をGitHub Actions runner内にダウンロードしてローカル実行します。

## 実行順序と安全性

重要な順序は固定しています。

```text
seen読み込み
  ↓
候補取得
  ↓
ローカルQwenで選定
  ↓
可能ならarXiv PDF / PMC本文取得
  ↓
ローカルQwenでレポート生成
  ↓
Gmail送信
  ↓ 成功した場合のみ
seen_papers.txt更新
  ↓
commit / push
```

Gmail送信に失敗した場合、その論文IDはseenに追加されません。

## 重複管理

既出論文は以下だけで管理します。

`state/seen_papers.txt`

例:

```text
arxiv:2609.30217
pmid:42759856
```

過去メールや過去レポート全文を毎回読み返しません。

## 論文取得

### arXiv

arXiv APIをsubmittedDate降順で取得します。

採用後は個別arXivページへの到達確認とPDF取得を試し、PDFから十分な本文を抽出できた場合は `read_level: full_text` とします。失敗時はabstractへフォールバックします。

### PubMed

NCBI E-utilitiesで新しいPubMed recordを取得します。

PMCIDがある採用論文はPMC本文取得を試し、十分に抽出できた場合は `read_level: full_text`、それ以外は `abstract` とします。

## Gmailの内容

1通のメール内に両方入ります。

1. **ダイジェスト**
   - 今回の概況
   - 注目論文 最大5本
2. **完全版レポート**
   - 全採用論文
   - Tags / Summary / Why interesting
   - 目的 / 手法 / データ・実験 / 主な結果 / 新規性 / 限界 / なぜ注目したか
   - medical AI追加項目
3. **PAPER_IDS**
   - 重複管理用canonical ID

## ファイル構成

```text
papers/
├── README.md
├── requirements.txt
├── config/
│   └── paper_watch.yml
├── scripts/
│   └── paper_watch.py
├── state/
│   └── seen_papers.txt
├── reports/
│   └── ...                    # 過去方式の履歴。新規生成はしない
└── .github/
    └── workflows/
        └── paper-watch.yml
```

## 失敗時

Workflowは推測で処理を続けず失敗します。

主な確認箇所:

- Actions logの `Check required secrets`
- arXiv / PubMed retrieval
- Ollama / Qwenローカル推論
- Gmail SMTP
- 最後のgit push

一回失敗してもworkflow自体は無効化されず、次回スケジュールで再実行されます。

## 研究領域マップ・動向レビュー

ダッシュボードの「研究マップ・動向レビュー」は、従来の全体マップと週次の研究動向レビューを統合した単一のリビングレビューです。

- 公開画面: https://drkamoshika.github.io/papers/?view=map
- 文章版: `reports/overviews/README.md`
- 正本データ: `docs/overview.json`
- 週次の変更記録: `reports/weekly/YYYY-Www.md`

週次処理は別の `trends.json` や累積レポートを生成せず、正本と7つの分野別詳細を更新します。更新契約と検証方法は `docs/LIVING_REVIEW.md` に記載しています。
