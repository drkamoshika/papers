# 最新論文を読むための基礎文献集

調査開始日: 2026-11-14（日本時間）

## この文献集の目的

`reports/daily/` の2026年の論文を単独の新提案として読むのではなく、何を引き継ぎ、何を変え、何がまだ解決していないかを判断するための文献集である。新着順の検索ではなく、既存246件の主題を起点に、主要手法・転換点・反証や失敗の研究・評価方法を優先した。

## 範囲と今回の到達点

| 分野 | 選定 | 照合済み・公開 | 主な対象 |
|---|---:|---:|---|
| [言語モデルの学習・推論・効率化](01-language.md) | 101 | 101 | 分散表現、attention、事前学習、スケーリング、指示・選好学習、推論探索、蒸留、量子化、推論基盤 |
| [エージェント・検索・記憶・協調](02-agents.md) | 112 | 112 | 外部記憶、検索、RAG、ツール利用、計画、反省、協調、コード・Web・ロボット環境 |
| [評価・安全性・解釈可能性](03-trust.md) | 104 | 104 | 頑健性、校正、不確実性、棄権、事実性、ベンチマーク、プライバシー、公平性、注入攻撃、不整合、説明 |
| [医療・生体信号・創薬AI](04-medical.md) | 139 | 24 | EHR、画像、臨床NLP、医療言語モデル、タンパク質・分子、生体信号、外部検証・報告指針 |
| 表形式・時系列・因果推論 | 119 | 0 | 木と深層学習、表の事前学習・生成、因果効果・因果探索、分布変化、時系列予測・表現・欠損補完 |

主編の選定は延べ575件、重複排除後556件。照合済みの延べ341件、実論文322件を公開した。別冊の古典12件を加え、**公開済みは実論文334件**。未照合の主編234件は完成済みに含めない。個別状態は [catalog.json](catalog.json)、確認範囲と残件は [調査の到達点](STATUS.md) に記録する。

2026-11-14に作業を区切り、2026-11-15のユーザー指示で未照合分の調査を再開した。各分野100件以上という当初目標は現時点で未達であり、未照合の候補を要約済みとは扱わない。既存の新着論文に近い技術的な前史の整理を優先し、さらに古い起源の探索は広げない。

さらに前の出発点となる [古典12件の別冊](00-prehistory.md) は、誤差逆伝播、LSTM、Random Forests、ニューラル確率言語モデル、単語重み付け、Okapi、A*、STRIPS、TD学習、Q-learning、傾向スコア、Coxモデルを扱う。

採用範囲は原則2024年以前。主編の公開済みは2007〜2024年、別冊は1968〜2003年を扱う。サーベイや方法論的解説も一部含む。完全な系統的レビュー、すべての分野の歴史の網羅、被引用数だけによる順位付けを主張しない。

## 研究史をたどる読み順

### 1. 言語モデルの学習・推論・効率化

単語・フレーズの分散表現（word2vec）→系列変換（seq2seq、attention）→Transformer→双方向表現と生成事前学習（ELMo、BERT、T5、GPT-3）→スケーリングと計算予算（Kaplan、Chinchilla）→指示・選好学習（FLAN、InstructGPT、DPO）→推論時の探索と検証（CoT、Self-Consistency、STaR、Tree of Thoughts、process supervision）を先に読む。

別の軸として、蒸留→adapter/LoRA→QLoRA/GPTQ/AWQ、sparse attention→FlashAttention→MQA/GQA→PagedAttention・speculative decodingを読む。「小さいモデルのスコア」だけでなく、学習費用、推論費用、メモリ、利用可能な教師、モデル変更の有無を分けて比較する。

現在のIntern-S2-Mobius、TDCS、LittleLearner、SteerDistill、Deletion Tuning、frequency-aware remaskingは、それぞれ知識と推論の分離、学習順序、知識露出、量子化後の能力保持、更新表現、推論時探索の問題として位置付けられる。この接続は技術的な比較軸であり、著者による直接引用や実証済みの優位性を意味しない。

### 2. エージェント・検索・記憶・協調

Memory Networks→kNN-LM/REALM/DPR→RAG/RETRO→Self-RAG・階層検索を読み、モデル内の知識と外部の証拠を区別する。次にReAct→Toolformer/ToolLLM→Reflexion→Voyager/Generative Agents/MemGPT→AutoGen/MetaGPT→WebArena/SWE-bench/SWE-agentの順に、ツール、環境フィードバック、経験の保存、協調、実行可能な評価へと問題設定が変わる流れを追う。

現在のWikiTrace、CoReMem、FGSE、CAMP-II、Skill Adapterは「記憶を足す」だけではなく、保存する価値、根拠へ戻れるか、将来課題への転移、誤った教訓の除去、保存と参照の費用を扱う研究として読む。ReTrace/CPU-ARCは毎回の自由な推論を再利用可能な手順へ変える研究、LEAD-RLは単純な人数増加ではなく協調への貢献の学習として比較する。

### 3. 評価・安全性・解釈可能性

敵対的事例→頑健学習と証明付き防御、校正・Bayesian uncertainty→選択的予測・conformal prediction、タスク正解率→事実性・人間の選好・行動の安全性、という3本の流れを分けて読む。公平性、プライバシー、データ・モデルの報告も、平均精度では測れない性質である。

TruthfulQA/HaluEval/FActScoreとMMLU/HumanEval/GPQAは異なるものを測る。MT-Bench/Chatbot Arenaの好ましさは、事実性や安全な実行と同一ではない。AgentDojo/InjecAgentは外部入力の信頼境界を扱う。現在のVeriHarm-Bench、MemoryDojo、ScamWorld、臨床LLM judgeの監査は、タスク成功と有害な副作用、記憶の汚染、現実的な攻撃条件、評価器自身の誤りを分ける延長線上に置く。

### 4. 医療・生体信号・創薬AI

臨床NLPのルール・知識表現→EHRの表現学習とリスク予測→画像・ECG/EEGの深層学習→大規模事前学習・医療言語モデルを追う。同時に、後ろ向き内部評価→外部検証→前向き試験→現場での人間との比較という臨床エビデンスの軸を読む。これらは技術の新旧と独立であり、新しいモデルでも臨床エビデンスが強いとは限らない。

Deep Patient/BEHRT/Med-BERT、網膜・皮膚・病理の主要診断研究、ECG/EEG表現学習、AlphaFold/ProteinMPNN/RFdiffusion、TRIPOD/PROBAST/CONSORT-AI/SPIRIT-AI/DECIDE-AIを別々の目的として整理する。現在のPACE-ECG/SeeEEGは表現と施設間転移、TransXplainRRGは画像と既往歴・レポート評価、MedPsy/PECAは資源と応答制御、FITTER/DiabAgentは制約付き行動・制御の研究として読む。試験問題の点数から実患者の安全性へは飛躍しない。

### 5. 表形式・時系列・因果推論

XGBoost→TabNet/FT-Transformer/SAINT→TabPFN、CTGAN→TabDDPMなどの生成へ進む。予測、欠損補完、合成データの分布忠実度と下流効用は別の目標である。時系列はDeepAR/N-BEATS/TFT→Informer/Autoformer→DLinear/PatchTST→Chronos/TimesFM/Moirai/MOMENTなどを読み、単一データでの学習と複数データをまたぐ事前学習を区別する。

因果効果推定、因果グラフの発見、分布変化に強い予測も別問題である。表現学習による反事実推論、double machine learning、causal forest、NOTEARS、IRM/DomainBedを比較し、必要な仮定を確認する。現在のOne Table、TSPFN、TabPFN-3.5、TIGER、Mantis 2、temporal world modeling、BGCMを、データ形式の統合だけでなく何を識別・予測・生成できたかという軸で位置付ける。

## 個別論文と研究の系譜の区別

個別レポートでは既存と同じ `Summary / Objective / Methods / Data and results / Novelty / Limitations` を使う。原著要旨だけの場合は `read_level: abstract` とし、本文・付録まで確認した場合だけ `full_text` とする。要旨で不足する数値や著者自身の限界は補って断言しない。

`report_date` は調査・要約日。arXivの `Publication date` は初回提出の公開記録で、査読誌の刊行日や最終改訂日とは区別する。PubMedの電子公開日、または日付が明示された冊子刊行日を採用し、出版社に先行公開日を確認できた場合はそちらを優先する。索引登録日や便宜的な月初日は使わない。年・月までしか分からない場合は日付を「未記載」とし、判明範囲と理由を残す。

この文献集は `reports/foundations/` に保存し、[ダッシュボード](https://drkamoshika.github.io/papers/)の「基礎文献」からも全文の要約項目を読める。基礎文献の公開用データは `docs/foundations.json`。未照合候補は画面に掲載しない。新着論文用の `docs/papers.json` と定期実行の仕組みは維持する。

この文書の最新研究との接続は、技術的な問題設定を比較した編集上の解釈である。直接の引用関係を確認した場合と区別する。基礎論文を100件並べたことだけで、その分野の理解や網羅性を保証するものではない。
