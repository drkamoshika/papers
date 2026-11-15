# 最新論文を読むための基礎文献集

調査開始日: 2026-11-14（日本時間）。最終更新: 2026-11-15。次イベント予測と神経科学の2分野を追加。

## この文献集の目的

`reports/daily/` の2026年の論文を単独の新提案として読むのではなく、何を引き継ぎ、何を変え、何がまだ解決していないかを判断するための文献集である。新着順の検索ではなく、既存246件の主題を起点に、主要手法・転換点・反証や失敗の研究・評価方法を優先した。

## 範囲と今回の到達点

| 分野 | 選定 | 照合済み・公開 | 主な対象 |
|---|---:|---:|---|
| [言語モデルの学習・推論・効率化](01-language.md) | 101 | 101 | 分散表現、attention、事前学習、スケーリング、指示・選好学習、推論探索、蒸留、量子化、推論基盤 |
| [エージェント・検索・記憶・協調](02-agents.md) | 112 | 112 | 外部記憶、検索、RAG、ツール利用、計画、反省、協調、コード・Web・ロボット環境 |
| [評価・安全性・解釈可能性](03-trust.md) | 104 | 104 | 頑健性、校正、不確実性、棄権、事実性、ベンチマーク、プライバシー、公平性、注入攻撃、不整合、説明 |
| [医療・生体信号・創薬AI](04-medical.md) | 139 | 139 | EHR、画像、臨床NLP、医療言語モデル、タンパク質・分子、生体信号、外部検証・報告指針 |
| [表形式・時系列・因果推論](05-structured.md) | 119 | 119 | 木と深層学習、表の事前学習・生成、因果効果・因果探索、分布変化、時系列予測・表現・欠損補完 |
| [次イベント予測・点過程](06-next-event.md) | 100 | 100 | 条件付き強度、待ち時間、長期生成、業務ログ、LLM、時間知識グラフ、校正・評価 |
| [神経科学とAI](07-neuroscience.md) | 106 | 106 | ハエ・マウス・人間のコネクトーム、脳ネットワーク、集団活動、学習則、記憶、脳とAIの表現 |

主編の選定は延べ781件、重複除外で762件。照合・公開済みの主編は762件。古典別冊12件を含め、**公開済みは実論文774件**。選定済み主編の未照合は0件。個別状態は[catalog.json](catalog.json)、確認範囲は[STATUS.md](STATUS.md)に記録する。

2026-11-14に作業を区切り、2026-11-15の指示で再開し、選定済みの主編全件を照合した。従来5分野に加え、次イベント予測100件と神経科学106件を照合し、7分野それぞれ100件以上を公開した。既存の新着論文に近い技術的な前史の整理を優先し、さらに古い起源の探索は広げていない。

さらに前の出発点となる [古典12件の別冊](00-prehistory.md) は、誤差逆伝播、LSTM、Random Forests、ニューラル確率言語モデル、単語重み付け、Okapi、A*、STRIPS、TD学習、Q-learning、傾向スコア、Coxモデルを扱う。

従来の5分野は原則2024年以前。今回追加する次イベント予測・神経科学は基礎から2026-11-15までに確認できた近年の接続研究も含む。従来5分野の公開済みは1995〜2024年、追加2分野は1971〜2026年、別冊は1968〜2003年を扱う。サーベイや方法論的解説も一部含む。完全な系統的レビュー、すべての分野の歴史の網羅、被引用数だけによる順位付けを主張しない。

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

### 6. 次イベント予測・点過程

まず、予測対象を「次の種類」「次の時刻」「ある時間窓内の件数」「将来の事象列全体」に分ける。Poisson過程の基準→Hawkesの自己・相互励起→RMTPP/Neural Hawkes→SAHP/Transformer Hawkes→Intensity-Free/TriTPP→DualTPP/ADD-THIN/EventFlowと読み、履歴の表現、待ち時間分布、長期誤差、並列生成が何を変えたかを見る。

LLMとの接続はTPP-LLM、Byte-token Enhanced Language Models、時間認識の強化、意味知識を利用する予測を扱う。業務ログの次活動、完了までの残り時間、時間知識グラフの将来リンクは、時刻と種類を同時に出すTPPと同じ課題ではない。比較では情報がいつ利用可能だったか、時間で分けた評価、反復パターンの単純な基準、校正、尤度と予測誤差の違いを確認する。

### 7. 神経科学とAI

脳の配線、活動、行動、学習の4層を分けて読む。ハエは幼虫の全脳→成虫のhemibrain・全脳FlyWire→細胞型・ネットワーク統計→配線に制約された活動・感覚運動モデルへ進む。人間はMRIによる巨視的ネットワークと、電子顕微鏡で得る局所のシナプス地図を区別する。マウスの機能・構造を結ぶMICrONSもこの接続に位置付ける。

別の軸で、低次元の集団活動→潜在力学系→課題を解く人工ニューラル網と脳応答の比較→言語モデルと脳の表現を読む。学習は予測誤差、dopamine、海馬と新皮質の相補的学習、replay、STDP、feedback alignment・樹状突起・spiking networkの信用割当をつなぐ。配線の一致、活動の予測、行動の再現、意識・感情の説明は異なる到達点であり、ある層の成功から他の層まで実証されたとは扱わない。

## 追加2分野を比較して読むための軸

次の表は個別論文を横断した編集上の整理で、すべての著者が同じ分類を用いるという意味ではない。各論文の一次資料と確認箇所は個別レポートへ残す。

| 次イベント予測で何を問うか | 入口となる研究 | 比較するときの要点 |
|---|---|---|
| 次に何が・いつ起きるか | RMTPP → Neural Hawkes → SAHP/THP | 事象の種類と待ち時間を同時に予測するか、片方を既知としていないか |
| 強度をどう表すか | Fully Neural Network、Intensity-Free、IFIB、AutoSTPP | 強度・累積ハザード・同時密度のどれを直接学ぶか、積分が正確か近似か、必要な制約を満たすか |
| 長い将来の列をどう生成するか | DualTPP → TriTPP → ADD-THIN → EventFlow | 次事象の精度、窓内件数、列分布の距離、長期simulationの校正を区別する |
| 欠けた履歴・集約観測でどう学ぶか | Short Doubly-Censored、Interval-censored、Neural Hawkesの欠測議論 | 真の未観測列を推論するか、集約された平均挙動を当てるか、不完全な列を直接学ぶか |
| LLMの意味情報は役立つか | TPP-LLM → Language-TPP/Byte-token → DescribeEvent | 種別の説明と事象ごとの文章を区別。意味なし記号の基準、時間符号、追加調整、遅延と費用を比較する |
| 業務ログ・時間graphの大きいモデルは必要か | SNAP、GenTKG、History repeats Itself、David vs. Goliath | 情報が豊かな課題での利得と、反復・頻度だけで解ける課題を分ける。履歴重複と未来情報の漏洩を調べる |
| 予測が確率として信用できるか | PIT diagnostics、Comparative evaluation、EarthquakeNPP | NLL/MAE/ACCだけでなく、proper score、期間内生成、分野の強い基準法を用いる |

読み始める順は、[Neural TPPのレビュー](https://arxiv.org/abs/2104.03528)で定義をそろえ、[RMTPP](https://www.kdd.org/kdd2016/subtopic/view/recurrent-temporal-point-process)と[Neural Hawkes](https://arxiv.org/abs/1612.09328)で履歴の表現を理解し、[Intensity-Free](https://arxiv.org/abs/1909.12127)と[ADD-THIN](https://arxiv.org/abs/2311.01139)で設計の変化を追う。その後[TPP-LLM](https://arxiv.org/abs/2410.02062)、[Language-TPP](https://arxiv.org/abs/2502.07139)、[DescribeEvent](https://arxiv.org/abs/2610.19021)へ進む。[EarthquakeNPP](https://arxiv.org/abs/2410.08226)と[次活動予測の一般化の再検討](https://arxiv.org/abs/2309.09618)を並行して読むと、モデルの大型化と確かな進歩を分けて評価しやすい。

| 神経科学で何を観測するか | 入口となる研究 | AIへの接点と解釈の境界 |
|---|---|---|
| 細胞とシナプスの配線 | 幼虫全脳、hemibrain、FlyWire、2026年male CNS/BANC | 学習architectureを拘束する資源。全脳・全中枢という呼称でも標本欠損・分割誤差・電気シナプスなどの範囲を確認する |
| 構造と活動の対応 | MICrONS、Connectome-constrained networks、Shiuらの感覚運動モデル | 配線を固定して課題学習する方式と、学習せず単純なneuronモデルを走らせる方式を区別する |
| 人間の大規模network | HCP、Yeoの分割、rich club、DMN/gradient、CPM | MRIの領域間結合はシナプス地図ではない。motion、空間自己相関、tractographyの偽経路を考慮する |
| 集団での計算と表現 | GPFA → dPCA/LFADS/TCA → neural population geometry/CEBRA | 潜在変数の抽出、課題labelの利用、単一trialの予測、因果的な機構説明を区別する |
| 学習と記憶 | CLS → replay → EWC、STDP → 三因子rule → feedback alignment/e-prop | 記憶保持と信用割当の計算を説明する。生体に似た実装が可能なことと、実脳がその算法を使うことは別 |
| 予測・報酬・navigation | dopamine prediction error、distributional RL、predictive map、TEM、grid-like agents | 報酬の平均・分布、状態遷移、空間metricなど、何の未来を表すかを確認する |
| 言語と脳 | task-optimized models、Schrimpf/Caucheteux、semantic decoder | 脳応答への線形mapping、説明可能分散、意味の再構成、逐語転写を区別する |

ハエ関係は[2024年の成虫全脳地図](https://pubmed.ncbi.nlm.nih.gov/39358518/)→[細胞型](https://pubmed.ncbi.nlm.nih.gov/39358521/)・[network統計](https://pubmed.ncbi.nlm.nih.gov/39358527/)→[課題学習による活動予測](https://pubmed.ncbi.nlm.nih.gov/39261740/)と[感覚運動モデル](https://pubmed.ncbi.nlm.nih.gov/39358519/)を組にして読む。人間については[構造から機能結合を予測する研究](https://pubmed.ncbi.nlm.nih.gov/19188601/)→[個人のfingerprint](https://pubmed.ncbi.nlm.nih.gov/26457551/)→[gradient](https://pubmed.ncbi.nlm.nih.gov/27791099/)と[行動予測protocol](https://pubmed.ncbi.nlm.nih.gov/28182017/)を読み、[局所皮質のEM地図](https://pubmed.ncbi.nlm.nih.gov/38723085/)と測定scaleの違いを確認する。

両分野の接点は、spike列を点過程で扱うこと、予測誤差が学習信号となること、過去の経験が将来の状態分布を表すことにある。[微分可能な点過程によるSNN学習](https://arxiv.org/abs/2106.00901)、[報酬の発生と時刻の誤差](https://pubmed.ncbi.nlm.nih.gov/10195164/)、[海馬のpredictive map](https://pubmed.ncbi.nlm.nih.gov/28967910/)、[分布的なdopamine符号](https://pubmed.ncbi.nlm.nih.gov/31942076/)を橋渡しにできる。これらの関連は問題設定の比較であり、LLM・脳・点過程が同一の機構という主張ではない。

## 個別論文と研究の系譜の区別

個別レポートでは既存と同じ `Summary / Objective / Methods / Data and results / Novelty / Limitations` を使う。原著要旨だけの場合は `read_level: abstract` とし、本文・付録まで確認した場合だけ `full_text` とする。要旨で不足する数値や著者自身の限界は補って断言しない。

`report_date` はレポートの作成日で、論文公開日ではない。文献集の追記・最終更新日は上記およびSTATUSに記載する。arXivの `Publication date` は初回提出の公開記録で、査読誌の刊行日や最終改訂日とは区別する。PubMedの電子公開日、または日付が明示された冊子刊行日を採用し、出版社に先行公開日を確認できた場合はそちらを優先する。索引登録日や便宜的な月初日は使わない。年・月までしか分からない場合は日付を「未記載」とし、判明範囲と理由を残す。[公開日が日単位で未確認の文献](DATE_NOTES.md)に一覧と根拠をまとめた。

この文献集は `reports/foundations/` に保存し、[ダッシュボード](https://drkamoshika.github.io/papers/)の「基礎文献」からも全文の要約項目を読める。基礎文献の公開用データは `docs/foundations.json`。未照合候補は画面に掲載しない。新着論文用の `docs/papers.json` と定期実行の仕組みは維持する。

この文書の最新研究との接続は、技術的な問題設定を比較した編集上の解釈である。直接の引用関係を確認した場合と区別する。基礎論文を100件並べたことだけで、その分野の理解や網羅性を保証するものではない。
