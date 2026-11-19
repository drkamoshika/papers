# 研究動向・リビングレポート
> updated_at: 2026-11-19
> version: 1（初回レビュー）
> source_corpus: 既存基礎774件＋日次278件（登録延べ1,052件）

## 読み方と根拠の範囲
基礎774件と日次278件＝登録延べ1,052件を対象とし、既存の2026-11-18全体レビュー（基礎774件・日次264件、代表192件）を継承しつつ、2026-11-17〜19に追加された日次14件の抄録・日次詳細と主要な原著ページを照合した。**1,052報の全文を今回一から精読したものではない**。論文集の既存レビューは一部代表文献のみ一次資料を再確認しており、本文未確認の結果は各日次レポートの確認レベルに従う。11月19日時点の初回試作で、対象週の残りの日の論文は未収録。

これは論文を日付順に並べたニュースではなく、**研究テーマごとに問題設定・手法の流れ・現在できること・未解決課題**を継続更新するための文書。評価課題が違う論文の結果をランキングしない。推論・研究機会は編者の仮説として扱う。前回の7テーマ技術詳説は[全体マップ](https://drkamoshika.github.io/papers/?view=map)と[詳細レビュー](https://github.com/drkamoshika/papers/blob/main/reports/overviews/README.md)に保存されている。今回の初回版はそれを置き換えず、そこに2026-11-19までの動向と研究上の見取り図を重ねる。

## 全体の見取り図
**共通の問いは『モデルが何を知っているか』ではなく『必要な証拠があり、それを使える形で保持し、何を根拠に安全に判断・実行できるか』。**
言語モデルの実行トレース、協調エージェントの証拠引継ぎ、医療AIの増分価値、イベントモデルの将来整合性は、それぞれ違う問題に見えても、入力・状態・制約・検証・意思決定という層に分けると比較できる。これは編者による方法論的整理であり、文献間に直接の引用・実証的連鎖があることを主張するものではない。

## 7テーマの累積レビュー
### 1. 言語モデルの学習・推論・効率化
**現在の到達点 — 推論手順を実行可能な形にする段階**
Transformer、事前学習、指示調整、選好学習、推論時探索という発展を経て、現在のボトルネックは「推論を長く生成すること」から「何を検証し、どの実行を信じるか」へ移っている。検証器付き探索やアダプタ切替は、重みの一律拡大とは別の改良経路である。

**最新の更新（2026-11-19）**
ARCHERは自然言語の思考列を型付きの電卓呼び出し・検証を含む行動列へ変換して小型モデルを訓練し、比較対象に対する数学ベンチマークの改善を報告した。Self-Disagreementは自ら生成した反論へ応じる訓練を扱い、LoRAWeaverは追加学習なしのアダプタ選択を試みる。これらは学習段階、推論時制御、運用時ルーティングという異なる制御点を操作する。

**論文の比較と解釈上の境界**
ARCHERの評価は主に数学、Self-Disagreementは対話的な正誤維持、LoRAWeaverは特定のモデル・タスク群である。改善率を同じ尺度で合算できない。生成した手順の監査可能性と、その手順が実際の判断の因果過程を反映することも異なる。

**次に解くべき研究課題**
実行トレース、外部検証器、自己反論を同じ課題・同じ推論予算で比較し、どの失敗類型にどの制御が効くかを層別化する。検証器自体の誤り、呼び出し回数、遅延を必ず測る。

**代表文献と元資料**
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (`arxiv:1706.03762`)
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) (`arxiv:2106.09685`)
- [Learning When Diffusion Language Models Should Regenerate](https://arxiv.org/abs/2611.17320) (`arxiv:2611.17320`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-15.md)
- [Benchmarks Don't Talk Back: Learning Through Self-Disagreement](https://arxiv.org/abs/2611.17563) (`arxiv:2611.17563`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-17.md)
- [LoRAWeaver: Directional Adapter Routing in LoRA Representation Space](https://arxiv.org/abs/2611.17340) (`arxiv:2611.17340`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-17.md)
- [ARCHER: From Rationale Imitation to Executable Reasoning in Small Language Models](https://arxiv.org/abs/2611.18494) (`arxiv:2611.18494`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-18.md)
- [Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers](https://arxiv.org/abs/2611.21449) (`arxiv:2611.21449`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-18.md)

関連する既存の詳説：[言語モデルの学習・推論・効率化](https://drkamoshika.github.io/papers/?view=map&topic=language)

### 2. エージェント・検索・記憶・協調
**現在の到達点 — 協調の情報損失が定量化され始めた**
RAG、ReAct、記憶、マルチエージェントは、単発のモデルを環境に接続するための異なる機構である。局所的な成功が増えても、情報が引き継がれなければ全体の正確性は落ちる。分業の利益は並列性と責任分離にあるが、証拠の連結、更新された状態、最終統合の品質を別途測る必要がある。

**最新の更新（2026-11-19）**
Multi-Agent Memory Inconsistencyは、必須委譲により矛盾する主張の両方を取得する割合が50.2%から68.7%に増えた一方、矛盾検出率が16.2%から13.2%へ下がったと報告。取得できた証拠対のうちワーカー報告へ両方が残ったのは35.2%。以前のCoLFAの失敗位置特定、DeliverBenchの依存成果物評価と合わせ、問題を取得・受渡し・統合・検証へ分解する方向が見える。

**論文の比較と解釈上の境界**
この値は限られた文書レビューの制御された矛盾事例であり、あらゆるエージェントタスクで分業が劣るという一般則ではない。エージェント数ではなく、情報経路の構造と予算が効果を左右する。

**次に解くべき研究課題**
単独、独立並列、共有メモリ、証拠対を必ず保持する構造化ハンドオフを同じ予算で比較する。各段で情報保持率、矛盾検出率、最終納品の整合性と費用を計測する。

**代表文献と元資料**
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) (`arxiv:2005.11401`)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (`arxiv:2210.03629`)
- [DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://arxiv.org/abs/2611.03412) (`arxiv:2611.03412`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-14.md)
- [CoLFA: Collaboration-Guided Lightweight Failure Attribution for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2611.14980) (`arxiv:2611.14980`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-15.md)
- [Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents](https://arxiv.org/abs/2611.22245) (`arxiv:2611.22245`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-19.md)

関連する既存の詳説：[エージェント・検索・記憶・協調](https://drkamoshika.github.io/papers/?view=map&topic=agents)

### 3. 評価・安全性・解釈可能性
**現在の到達点 — 正解率から証拠・安定性・介入へ**
平均正答率やAUROCだけでは、校正、棄権方策、根拠の保持、再現性、隠れた情報経路を捉えられない。内部活性化を用いた評価はモデル内の表現を記述できるが、それが回答の因果的な理由かは介入により別途確かめる必要がある。

**最新の更新（2026-11-19）**
Tracing Knowledge and Reasoningは16モデル・24ベンチマークを内部表現から比較した。Rubric-Based AESは631回答・103基準・15モデルなどを使い人間採点との一致を測る。Weight-Space Programmingの追試は、重み生成の一部成功と重み読解の限界を切り分ける。Self-Disagreementは反論への頑健性を直接訓練する。新規報告の多くは『評価対象を細分化する』という流れに位置づく。

**論文の比較と解釈上の境界**
説明の妥当性と介入の因果性、採点一致と実環境での安全性、リスク閾値の指定と本当の閾値遵守は区別すべき。モデルの検証結果だけで下流の実行システムが安全とは言えない。

**次に解くべき研究課題**
評価対象を正解・校正・継続実行の整合性・証拠来歴に分解し、個別の閾値を固定して見せかけの棄権と実際の選択的予測を比較する。説明文の変化ではなく、介入時の行動変化も検査する。

**代表文献と元資料**
- [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) (`arxiv:2211.09110`)
- [Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702) (`arxiv:2307.13702`)
- [Abstention Is Not Threshold Compliance: Stated Scoring Rules in Open Language Models](https://arxiv.org/abs/2611.14661) (`arxiv:2611.14661`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-15.md)
- [Tracing Knowledge and Reasoning in LLM](https://arxiv.org/abs/2611.17461) (`arxiv:2611.17461`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-17.md)
- [Rubric-Based AES with LLM Ensembles: Scoring of Student Responses in Critical Online Reasoning Using Ensembles of LLMs](https://arxiv.org/abs/2611.21422) (`arxiv:2611.21422`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-18.md)
- [Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers](https://arxiv.org/abs/2611.21449) (`arxiv:2611.21449`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-18.md)
- [Benchmarks Don't Talk Back: Learning Through Self-Disagreement](https://arxiv.org/abs/2611.17563) (`arxiv:2611.17563`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-17.md)

関連する既存の詳説：[評価・安全性・解釈可能性](https://drkamoshika.github.io/papers/?view=map&topic=trust)

### 4. 医療・生体信号・創薬AI
**現在の到達点 — 探索的識別と臨床価値の間を厳密に分ける**
医療AIではデータ取得・症例抽出・診断・予後予測・介入を同一の『高精度』で語れない。診断や記述支援の性能が高くても、将来状態の予測と患者アウトカムの改善は別課題。施設差、時間分割、校正、患者単位の安定性、外部検証という関門が残る。

**最新の更新（2026-11-19）**
尿中揮発性成分AIの多がん種検出は10がん種491例と健常200例の多施設症例対照・内部検証研究で、一般集団スクリーニングでの有用性を示したものではない。血算由来の複雑な指標のレビューは数学的重複と既存測定値への増分価値を問う。Compliance by DesignはLLMを定量分析の設計・説明に用いつつ、解析仕様と検証可能な実行を分離する提言で、効果量を実証した臨床試験ではない。

**論文の比較と解釈上の境界**
尿アッセイは陽性・陰性の事前有病率や外部の患者集団への移転が未解決。血算指標レビューは実証的な治療効果ではない。AIに解析を説明させるだけでは監査可能性や統計的妥当性の保証にはならない。

**次に解くべき研究課題**
新規バイオマーカーは『元の変数のみ→複合特徴→新規センサー』の増分利益を、施設外・時期外・患者中心の指標で評価する。LLMは文章化と仮説形成を担い、実行可能な統計仕様・ログ・コード検証を別系統で固定する。

**代表文献と元資料**
- [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://pubmed.ncbi.nlm.nih.gov/35585198/) (`pmid:35585198`)
- [Performance of a Large Language Model for Predicting Clinical and Radiographic Outcomes in Knee Osteoarthritis: Single-Center Prospective Observational Study](https://pubmed.ncbi.nlm.nih.gov/43019548/) (`pmid:43019548`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-15.md)
- [Artificial Intelligence-Based Urine Volatomic Assay for Multi-Cancer Detection: A Multicentric Case-Control Discovery and Internal Validation Study](https://pubmed.ncbi.nlm.nih.gov/43006187/) (`pmid:43006187`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-17.md)
- [Evaluating mathematical complexity and incremental clinical value in complete blood count-derived indices](https://pubmed.ncbi.nlm.nih.gov/43031444/) (`pmid:43031444`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-17.md)
- [Compliance by Design: Governing AI-Augmented Quantitative Analysis in Clinical and Translational Research](https://pubmed.ncbi.nlm.nih.gov/42954875/) (`pmid:42954875`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-19.md)
- [Large language models are unstable as autonomous medical evaluators across clinical tasks](https://pubmed.ncbi.nlm.nih.gov/42995166) (`pmid:42995166`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-06.md)

関連する既存の詳説：[医療・生体信号・創薬AI](https://drkamoshika.github.io/papers/?view=map&topic=medical)

### 5. 表形式・時系列・因果推論
**現在の到達点 — 複雑なモデルより情報の観測設計が争点**
XGBoostなどの木の基準、TabPFNなどの事前学習、時系列基盤モデルは用途ごとに利益が異なる。予測誤差を小さくするだけで、因果効果や機構が識別できるわけではない。教師信号、観測窓、分布外テスト、何を入力できるかが優先される。

**最新の更新（2026-11-19）**
微生物群集の機構推定では、ランダムな群集と培地の組み合わせが、機構の識別可能性を左右し、LASSOのような単純手法でも役割を回復できると報告。コウモリの反響定位音では単発の分類より音列の情報が識別に寄与。V-JEPA-LMでは凍結された動画表現に速度情報が存在しても、適切な教師信号なしでは言語側が読み出さないことを示した。

**論文の比較と解釈上の境界**
微生物の実験設計、コウモリの制御環境、動画ベンチマークという別領域の結果を同一の性能改善として扱わない。因果的な識別可能性、表現の可読性、時系列の予測精度は異なる数学的対象。

**次に解くべき研究課題**
入力摂動・情報取得の能動設計・出力検証を別要素として比較する。ラベル精度に加えて時系列の校正と長期の整合性を測り、モデルを高度化する前に観測の識別可能性を検証する。

**代表文献と元資料**
- [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754) (`arxiv:1603.02754`)
- [TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second](https://arxiv.org/abs/2207.01848) (`arxiv:2207.01848`)
- [Chronos: Learning the Language of Time Series](https://arxiv.org/abs/2403.07815) (`arxiv:2403.07815`)
- [From Forecasting to World Modeling: Can Temporal Foundation Models Recover Causal Response?](https://arxiv.org/abs/2611.15009) (`arxiv:2611.15009`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-14.md)
- [V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations](https://arxiv.org/abs/2611.17831) (`arxiv:2611.17831`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-18.md)
- [Deep learning reveals persistent individual signatures in bat echolocation calls of the greater leaf-nosed bat](https://pubmed.ncbi.nlm.nih.gov/42864600/) (`pmid:42864600`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-19.md)
- [Learning the mechanism of collective microbial function via random community-media pairing](https://pubmed.ncbi.nlm.nih.gov/42869071/) (`pmid:42869071`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-19.md)

関連する既存の詳説：[表形式・時系列・因果推論](https://drkamoshika.github.io/papers/?view=map&topic=structured)

### 6. 次イベント予測・点過程
**現在の到達点 — 次イベントの精度と長期系列の整合性が分岐点**
頻度基準・Markov的遷移からHawkes過程、ニューラル点過程、待ち時間分布、系列拡散まで、予測対象はラベル・時刻・個数・系列全体と拡張されている。ここへLLMを足す意味は意味情報の増分にあり、単に言語モデルが巨大なこと自体は根拠にならない。

**最新の更新（2026-11-19）**
11月17〜19日の14件には、新たな点過程の直接比較研究は採用されていない。ただしInteractive Program Inductionは情報が足りないときに識別力の高い問い合わせを選ぶ設計、ARCHERは推論結果を実行可能な行動に変える設計、V-JEPA-LMは観測表現から必要な動的情報を読み出す設計を示す。長期イベント生成の制約・観測計画を考える際の隣接知見として重要。

**論文の比較と解釈上の境界**
行動トレースはイベントの発生時刻を予測したものではなく、動画の速度認識も点過程の強度校正を実証しない。関連づけは編者の方法論的な仮説である。

**次に解くべき研究課題**
まず独立なラベル頻度/直近遷移、強度型・待ち時間型、LLM併用を同じ情報量で比較する。長期生成には発生数・発生間隔・論理条件・観測可能なセンサー系列の整合性を別々に測る。ハード制約とソフト修正の費用/成功率を分離する。

**代表文献と元資料**
- [The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process](https://arxiv.org/abs/1612.09328) (`arxiv:1612.09328`)
- [Intensity-Free Learning of Temporal Point Processes](https://arxiv.org/abs/1909.12127) (`arxiv:1909.12127`)
- [David vs. Goliath in Next Activity Prediction: Argmax vs. LSTM, Transformer, and LLM](https://arxiv.org/abs/2606.15868) (`arxiv:2606.15868`)
- [Can LLMs Access their World Knowledge for Event Prediction?](https://arxiv.org/abs/2610.19021) (`arxiv:2610.19021`)
- [Interactive Program Induction with Language Model Priors](https://arxiv.org/abs/2611.18485) (`arxiv:2611.18485`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-18.md)
- [ARCHER: From Rationale Imitation to Executable Reasoning in Small Language Models](https://arxiv.org/abs/2611.18494) (`arxiv:2611.18494`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-18.md)
- [V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations](https://arxiv.org/abs/2611.17831) (`arxiv:2611.17831`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-18.md)

関連する既存の詳説：[次イベント予測・点過程](https://drkamoshika.github.io/papers/?view=map&topic=events)

### 7. 神経科学とAI
**現在の到達点 — 構造地図から動的な機構仮説へ**
電子顕微鏡の局所接続、MRIの広域相関、神経集団の低次元動態、機能的結合は測るものが異なる。ハエの全脳回路地図など大規模な構造資源は確立したが、接続図だけから内的状態・学習・感情・全行動を復元できるわけではない。

**最新の更新（2026-11-19）**
今回14件には神経回路の構造・機能を直接更新する重要論文は採用されていない。コウモリの個体音響識別は非侵襲センシングと個体差の分析として隣接するが、神経回路の解明を示した研究ではない。そのためトレンドの解釈を強引に変更しない。

**論文の比較と解釈上の境界**
ハエ・マウス・ヒトでデータの単位、解像度、収録範囲が異なる。構造の一致や活動の相関から機構の因果性まで言えない。

**次に解くべき研究課題**
ニューロンの接続・活動・行動を同時に持つ標本で、学習や内的状態を変える介入を行い、構造からの予測を検証する。個体をまたいだ再現性と観測の交絡を計測する。

**代表文献と元資料**
- [Neuronal wiring diagram of an adult brain](https://pubmed.ncbi.nlm.nih.gov/39358518/) (`pmid:39358518`)
- [A Drosophila computational brain model reveals sensorimotor processing](https://pubmed.ncbi.nlm.nih.gov/39358519/) (`pmid:39358519`)
- [Functional connectomics spanning multiple areas of mouse visual cortex](https://pubmed.ncbi.nlm.nih.gov/40205214/) (`pmid:40205214`)
- [Semantic reconstruction of continuous language from non-invasive brain recordings](https://pubmed.ncbi.nlm.nih.gov/37127759/) (`pmid:37127759`)
- [Deep learning reveals persistent individual signatures in bat echolocation calls of the greater leaf-nosed bat](https://pubmed.ncbi.nlm.nih.gov/42864600/) (`pmid:42864600`) — [元日次レポート](https://github.com/drkamoshika/papers/blob/main/reports/daily/2026-11-19.md)

関連する既存の詳説：[神経科学とAI](https://drkamoshika.github.io/papers/?view=map&topic=neuroscience)

## 分野間の接点と研究テーマ候補
**(A) 観測→意味→制約付き生成:** センサ・数値の表現に含まれる情報を、イベント系列に必要な意味へ射影し、その系列が元観測と整合するかを外部で検証する。表現可読性・長期予測・制約充足・修正費用を別指標で評価する。

**(B) 知識・証拠の受渡し:** RAGやマルチエージェントの検索段階から最終決定まで、根拠を引用可能な単位で渡し、情報の脱落や矛盾検出の失敗を計測する。モデルと通信機構の寄与を分離する。

**(C) 予測から支援へ:** 医療や業務イベントのリスク予測で識別・校正・予測幅の評価を揃え、介入による実際の転帰変化との違いを検証する。反実仮想は観察予測のみから導けない。

## 更新履歴
- 2026-11-19 初回。既存の7テーマ・1,038件のレビューを継承し、11月17〜19日の14件を加え、登録延べ1,052件を対象とする動向地図へ更新。[第2026-W47週レビュー](../weekly/2026-W47.md)。

## 週次スナップショット
- [2026-W47（11月19日時点の初回）](../weekly/2026-W47.md)

## 品質と再検証メモ
すべての登録文献を今回独立に全文再読したわけではない。既存の7テーマレビューの一次確認は限定的な代表文献に対するものであり、ほとんどは収録済みの抄録・本文要約の信頼性に依存する。更新の際は出典・確認レベル・観測条件・数値の分母を明示する。今回の新規論文は各日次レポートにあるcanonical IDとリンクへ遡れる。