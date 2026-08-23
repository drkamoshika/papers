# [paper-report] 2026-08-23 ML / LLM / Medical AI clean rerun

- Issue: #6
- Source: https://github.com/drkamoshika/papers/issues/6
- Created at: 2026-08-23T06:59:25Z

# Paper Watch Report — 2026-08-23

## 今回の概況

`config/paper_watch.yml` を読み直し、`state/seen_papers.txt` を空にした状態から、直近5日（2026-08-18〜2026-08-23）について arXiv / PubMed を再検索した。

前回0本になった主因は、arXivの `recent` / category一覧ページが検索環境側で古いキャッシュ（主に8月10日まで）として返っていたことだった。今回は、その一覧だけに依存せず、検索インデックスから直近候補を発見し、選定候補について個別arXivページを検索・確認する方法に切り替えた。その結果、8月18〜20日に投稿された関連論文を複数確認できた。

PubMedも検索したが、今回確認できた関連論文の多くは2026年8月号掲載でもEpubが4〜7月であり、設定された5日lookback内の新規公開として確実に扱えるものを確認できなかった。そのため今回はarXiv中心の9本を採用した。

今回の新着では、LLM/エージェント領域で「長期記憶」「AIによるAI post-training」「agentic RL」「不要知識の忘却」など、モデル単体よりも長期運用・学習・状態管理の研究が目立つ。また、医療・生命科学では、分子foundation modelや血管内治療navigationなど、foundation model / world modelを具体的な科学・医療タスクへ落とし込む研究が見られる。

## 実行条件

- Sources: arXiv / PubMed
- Topics: machine learning / large language models / medical AI / healthcare AI
- Lookback: 5 days
- Max papers: 20
- Deduplication: `state/seen_papers.txt`（clean rerun時は空）
- Selected papers: 9

---

## 1. MemFuse: Multi-Source Memory Fusion from Fragmented Observations

- Source: arXiv
- canonical ID: arxiv:2608.18704
- Published: 2026-08-19
- Authors: Chao Li, Yuanfa Li, Wenhao Wu, Xule Liu, Zhi Wang, Kun Shao
- Journal / Category: cs.CL, cs.AI
- URL: https://arxiv.org/abs/2608.18704
- read_level: abstract

### 目的
長期エージェントのmemory研究が単一の会話履歴や単一テキストsourceに偏っている問題に対し、複数application・device・user・時点に断片化した観測を、出典を失わずに統合できるかを扱う。

### 手法
Scene-to-Sensor pipelineでsource-tagged observation、evidence-grounded question、adversarial distractorを生成する `MemFuseBench` を構築。提案memory system `MemFuse` は、source-level evidenceをatomic eventとして保持するevent layerと、関連eventをcausal fusion graph上でまとめるcluster layerを持つ。

### データ・実験
MemFuseBench上で3種類のLLM settingを用いて、既存memory systemと比較評価。

### 主な結果
abstractではMemFuseが3種類すべてのLLM settingで総合的に最良で、特にcross-source evidence fusionが必要な質問で一貫した改善を示したと報告。具体的な数値はabstractには記載されていない。

### 新規性
「長期memory」を単一履歴の検索ではなく、複数source由来の断片をprovenance付きで融合する問題としてbenchmarkとsystemの両方を提示した点。

### 限界
abstractからは、実世界の異種application/device上での長期運用評価や、非常に長い時間スケールでの性能は確認できない。

### なぜ注目したか
長期agentで重要になるmemory managementを、retrievalだけでなくsource fusion・provenanceまで含めて明示的に扱っているため。

---

## 2. Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference

- Source: arXiv
- canonical ID: arxiv:2608.18982
- Published: 2026-08-19
- Authors: Blazej Banaszewski, Andrew W. Fitzgibbon
- Journal / Category: cs.LG, q-bio.BM, q-bio.QM
- URL: https://arxiv.org/abs/2608.18982
- read_level: abstract

### 目的
wet-lab実験が高コストでdata-limitedになりやすいbioassay activity predictionに対し、少量データ環境でも一般化しやすいmolecular foundation modelを構築する。

### 手法
81 million超のmoleculeを含むPM6 quantum chemistry datasetでpretrainingし、stereochemistry表現、conformer denoising、embedding decorrelation、multi-task learningを改善。downstream predictionにはprior-data-fitted modelのTabPFNを利用する。

### データ・実験
Polaris benchmarkとactivity-cliff benchmarkで既存molecular foundation modelsと比較。さらにMiniMolとCheMeleonへPFN-based downstream predictorを移植するtransfer experimentも実施。

### 主な結果
Polarisでは既存MFMに同等またはそれ以上、activity-cliff benchmarkでは既存手法に対して統計的に有意な改善を報告。PFN-based downstream strategyをMiniMol/CheMeleonに適用しても性能が向上した。

### 新規性
foundation modelのencoderだけでなく、downstreamでin-context probabilistic inferenceを行うTabPFNとの組み合わせを重視している点。

### 限界
abstractではwet-lab prospective validationや実際のdrug discovery pipelineでの有用性は確認できない。

### なぜ注目したか
少量データ下でfoundation modelをどう使うかという問題に、表現学習とdownstream probabilistic inferenceの組み合わせで答えており、small-data MLの観点でも興味深い。

---

## 3. Causal Reasoning with Bipartite Graphical Causal Models

- Source: arXiv
- canonical ID: arxiv:2608.19831
- Published: 2026-08-20
- Authors: Joris M. Mooij
- Journal / Category: cs.AI, math.PR
- URL: https://arxiv.org/abs/2608.19831
- read_level: abstract

### 目的
feedbackを含むequilibrium systemでは、従来のcausal Bayesian networkやstructural causal modelの `do(X=x)` が、どの方程式を置き換える介入か曖昧になり得る問題を扱う。

### 手法
variable nodeとequation nodeからなるbipartite graphでsystem equation構造を表現するBGCMを提案。hard interventionを「どのequationを置換し、どのvariableをどの値に固定するか」まで明示する。さらにB-separationという新しいseparation criterionと、それに基づくMarkov property / do-calculusを構成。

### データ・実験
理論研究。物理systemの詳細case studyを用いて介入意味論を示す。

### 主な結果
BGCMがCBN/SCMをstrictly generalizeしつつgraphical causal reasoningを保持できること、domain invarianceを扱うdo-calculusへ拡張できることを示す。

### 新規性
causal graphをvariable間のedgeだけでなく「equationそのもの」をnodeとして扱い、同じ値を強制する異なる物理的介入を区別できる点。

### 限界
abstractでは大規模実データへの適用や推定algorithmの実証は扱われていない。

### なぜ注目したか
MLで広く使われるcausal frameworkの表現限界に対する基礎的拡張で、特にfeedback systemへの適用可能性があるため。

---

## 4. What is Missing from AI Post-Training AI: An Empirical Analysis

- Source: arXiv
- canonical ID: arxiv:2608.19072
- Published: 2026-08-19
- Authors: Joy Jia Yin Lim, Xin Huang, Hao Peng, Yaxi Lu, Xin Cong, Zhong Zhang, Maosong Sun, Yankai Lin
- Journal / Category: cs.AI, cs.CL, cs.LG
- URL: https://arxiv.org/abs/2608.19072
- read_level: abstract

### 目的
LLM agentがLLMのpost-trainingをend-to-endで実行できるようになった一方、そのagentが本当にtraining strategy自体を途中で見直せているのかを検証する。

### 手法
公開されているpost-training trajectoryを分析し、execution-level capabilityとstrategy-level capabilityを分離。さらに、experience scaffold、人間によるguidance、追加inference computeという3種の介入を試す。

### データ・実験
複数taskのpost-training trajectoryと、GSM8K / HumanEvalなどを用いた介入experiment。

### 主な結果
experience-driven scaffoldはGSM8Kで+12.6 points、HumanEvalで+40.8 points改善したが、strategy自体は固定されたまま。human guidanceは初期strategyをredirectできるがtraining開始後はlocal adjustment loopへ戻る。追加computeも難しいtaskではほぼ改善しなかった。

### 新規性
「agentがtrainingを回せること」と「evidenceを見ながらstrategyを再設計できること」を明確に分けて評価している。

### 限界
公開trajectoryと選択されたpost-training task/modelに依存しており、すべてのAI-for-AI settingへ一般化できるとは限らない。

### なぜ注目したか
agentic research / self-improving AIの実用上のボトルネックを、単なるcoding能力やreasoning computeではなくstrategy reevaluation不足と特定しているため。

---

## 5. SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning

- Source: arXiv
- canonical ID: arxiv:2608.19842
- Published: 2026-08-20
- Authors: Dayang Liang, Lang Feng, Bo An, Yunlong Liu
- Journal / Category: cs.AI
- URL: https://arxiv.org/abs/2608.19842
- read_level: abstract

### 目的
long-horizon agentic RLで、PPOのcritic memory costや、GRPO系のmultiple rollout依存・credit assignment問題を減らす。

### 手法
policyとvalueを単一autoregressive backboneで共有し、異なるcausal boundaryでpolicy/value predictionを出力。PPO objectiveとon-policy SARSA auxiliary objectiveを独立に最適化し、trajectory-level generalized advantage estimatorも導入。

### データ・実験
ALFWorld / WebShop、Qwen2.5-1.5B / 7BでPPOおよびGRPOと比較。

### 主な結果
平均でPPOより+15.1 percentage points、GRPOより+12.1 points。separate critic modelのmemory costを除去し、PPO比でper-iteration runtimeを33.2%削減。

### 新規性
LLMのautoregressive構造を利用してpolicyとvalueを同じbackboneで持ちながら、single-rolloutでagentic RLを成立させようとする点。

### 限界
abstractで確認できるtaskはALFWorld/WebShop中心で、より大規模なreal-world agent taskへの一般化は未確認。

### なぜ注目したか
agentic RLをより低memory・低sampling costにする実装上重要な方向で、比較結果も定量的に大きい。

---

## 6. Lost in Aggregation: How Benchmarks Overlook Irreplaceable Model Strengths

- Source: arXiv
- canonical ID: arxiv:2608.18919
- Published: 2026-08-19
- Authors: Andrej Tschalzev, Stefan Lüdtke, Heiner Stuckenschmidt, Christian Bartelt
- Journal / Category: cs.LG
- URL: https://arxiv.org/abs/2608.18919
- read_level: abstract

### 目的
benchmarkで平均score/rankだけを見ると、特定datasetでしか発揮されないmodel固有の強みが埋もれる問題を検討する。

### 手法
datasetごとのbest statistically-supported performanceを `peak performance frontier` として定義し、modelをirreplaceable / sufficient / redundant / fallibleに分類する評価視点を提案。

### データ・実験
TabArena benchmarkへ適用し、従来aggregation metricとの関係を分析。

### 主な結果
一般的なaggregation metric同士は高く相関し、主として「一貫して失敗しない」能力を測る一方、dataset-level irreplaceabilityとは十分整合しないと報告。

### 新規性
benchmarkの目的を「平均的に強いmodel選び」だけでなく、「どのmodelがpeak performance frontierを拡張するか」に広げた点。

### 限界
abstractから確認できる主要適用先はtabular ML benchmarkで、他分野への一般性は今後の検証が必要。

### なぜ注目したか
foundation modelやLLMのランキングでも、平均scoreだけでは独自の能力を見落とす可能性があり、benchmark設計に直接関係する。

---

## 7. Progressive Experience Fusion for Multi-Task World Model Control in Endovascular Navigation

- Source: arXiv
- canonical ID: arxiv:2608.18647
- Published: 2026-08-19
- Authors: Harry Robertshaw, Maxence Boels, Nikola Fischer, Sebastien Ourselin, Christos Bergeles, Alejandro Granados, Thomas C Booth
- Journal / Category: cs.RO, cs.LG
- URL: https://arxiv.org/abs/2608.18647
- read_level: abstract

### 目的
mechanical thrombectomyなどのendovascular procedureで、異なるvascular anatomyとmulti-stage pathに適応できるautonomous navigation controllerを学習する。

### 手法
multi-task TD-MPC2 controllerにProgressive Experience Fusion (PEF)を導入。action-sequence dispersionに基づいてplanning horizonを変えるheuristicとpatient-specific simulationでのfine-tuningも評価。

### データ・実験
5 subtasks、10 known training anatomiesでheld-out targetを評価。さらに30 vasculaturesでtrainingし10 held-out vasculaturesへgeneralization。unseen in-vitro stroke patient vasculatureへのtransferも実施。

### 主な結果
PEFはmean success 74%で、Soft Actor-Critic 37%（p<0.001）、base TD-MPC2 65%（p=0.053）。30 vasculaturesでtrained adaptive-horizon PEFは10 held-out vasculaturesでmean success 90%。unseen in-vitro patient vasculatureではfine-tuningによりmean path ratioが63%から80%へ改善（p<0.001）。

### 新規性
world-model controlを複数vascular task/anatomyへ段階的にexperience fusionし、patient-specific adaptationまで接続した点。

### 限界
著者自身がproof-of-conceptと位置づけており、clinical deployment前にはさらなるvalidationが必要。

### なぜ注目したか
医療AIを画像診断ではなくphysical intervention / robot controlへ展開する研究で、generalizationとpatient-specific adaptationを同時に扱っている。

---

## 8. The Embodiment Gap in Robot Foundation Models

- Source: arXiv
- canonical ID: arxiv:2608.18433
- Published: 2026-08-19
- Authors: Yukiyasu Domae, Keisuke Shirai, Hanbit Oh, Ryoichi Nakajo, Tomohiro Motoda, Koshi Makihara, Masaki Murooka, Takuma Yagi, Yoshiaki Bando, Ryo Hanai
- Journal / Category: cs.RO, cs.LG
- URL: https://arxiv.org/abs/2608.18433
- read_level: abstract

### 目的
robot foundation modelがbenchmark上generalizeしても、異なる身体構造を持つ実robotで動かすには追加adaptationが必要という問題を整理する。

### 手法
`embodiment gap` という概念を定義し、何がembodiment間でreuseでき、target robotで何を実装・adaptする必要があるかをtwo-axis mapで整理。semantic/perception sharing、robot data/interface sharing、cross-embodiment correspondence learningの3方向をsurveyする。

### データ・実験
survey / conceptual framework。新しいreporting frameworkも提示。

### 主な結果
success rateだけでは見えないtarget robotへのadaptation workを比較するため、どの構造をshareし、どのstageでadaptationするかを明示するreporting frameworkを提案。

### 新規性
robot foundation modelのgeneralizationを単純なscaling問題ではなく、deployment時に残る“embodiment gap”として定式化した点。

### 限界
surveyであり、新しい単一modelの定量benchmarkを提示する研究ではない。

### なぜ注目したか
foundation modelをphysical systemへ展開する際、「model性能」と「実機deployment可能性」が別問題であることを整理している。

---

## 9. Towards Reversible Forgetting: Managing Obsolete Knowledge in Continual Enterprise AI Agents

- Source: arXiv
- canonical ID: arxiv:2608.18177
- Published: 2026-08-18
- Authors: Nilutpaul Sarker Yash, Tirtho Roy, Ushashi Bhattacharjee
- Journal / Category: cs.LG, cs.MA
- URL: https://arxiv.org/abs/2608.18177
- read_level: abstract

### 目的
continual learningで「忘却＝失敗」とみなす考え方に対し、policy・workflow・market conditionが変化するenterprise agentではobsolete knowledgeを保持し続けること自体がriskになる問題を扱う。

### 手法
active / dormant / retiredの3 memory statesと、dormantからのreactivationを持つ `reversible forgetting` を提案。Hysteretic Reversible Memory Controllerでrelevance evidenceを蓄積し、非対称threshold、shadow-mode reactivation、policy-gated retirementを行う。

### データ・実験
abstract上は主としてconceptual frameworkとcontroller design。financeを例として説明。

### 主な結果
定量的benchmark resultはabstractには示されていない。obsolete informationの影響を抑えつつ、一時的なsuppressionとpermanent erasureを分離する設計を提示。

### 新規性
agent memoryを「記憶する/消す」の二値ではなく、後から復活可能なdormant stateを含むlife-cycleとして設計している点。

### 限界
abstractからは大規模enterprise deploymentや長期実験による定量検証は確認できない。

### なぜ注目したか
長期agentではmemory追加だけでなく「何をいつ忘れるか」が重要であり、MemFuseのようなmemory統合研究と対になるテーマだから。

---

## PubMed確認メモ

PubMedでもmachine learning / artificial intelligence / large language model / healthcare AIを検索した。しかし今回確認できた関連論文の多くは「2026 Aug issue」であってもEpubが4〜7月で、2026-08-18〜23の5日lookback内に新規公開されたものとして一次情報で確実に確認できなかった。このため今回の採用リストには含めていない。

今後はPubMedについて、`publication date`、`electronic publication date`、`index date` のどれをlookback判定に使うかをYAMLで明文化すると安定する。

<!-- PAPER_IDS -->
arxiv:2608.18704
arxiv:2608.18982
arxiv:2608.19831
arxiv:2608.19072
arxiv:2608.19842
arxiv:2608.18919
arxiv:2608.18647
arxiv:2608.18433
arxiv:2608.18177
<!-- /PAPER_IDS -->
