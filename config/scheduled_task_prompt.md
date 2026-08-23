# Scheduled Task bootstrap prompt

このファイルは補助説明です。**本番の実行仕様の正本は `config/paper_watch.yml` です。**

Scheduled Task本体には、できるだけ固定で短い次の指示だけを入れます。

```text
GitHub連携を使って `drkamoshika/papers` の `config/paper_watch.yml` を毎回読み、そこに書かれた設定と `task_instructions` をこの実行の唯一の運用仕様として、論文watchを1回実行する。YAMLを読めない、内容が不正、GitHub操作が失敗した場合は推測で代替せず、失敗理由を報告する。
```

この設計では、検索テーマ、検索元、最大論文数、遡及日数、重複除外、サマリ形式、Issueの作り方、エージェントの詳細な手順はすべて `config/paper_watch.yml` で管理します。

ChatGPT側に残る設定は基本的に以下だけです。

- タスク名
- 実行周期 / 実行時刻
- 上記の短いbootstrap prompt
- 有効 / 停止状態

したがって通常の動作調整は `config/paper_watch.yml` を編集するだけで、次回実行から反映されます。
