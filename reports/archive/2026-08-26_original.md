# [paper-report] 2026-08-26 ML / LLM / Medical AI

- Issue: #8
- Source: https://github.com/drkamoshika/papers/issues/8
- Created at: 2026-08-26T06:39:31Z

# Paper Watch Report — 2026-08-26

## 今回の概況

`config/paper_watch.yml` version 2 に従い、固定日数ではなく source ごとの最新件数ベースで候補を確認した。arXivでは `machine learning` を新しい順に検索し、最新15候補を確認したうえで、採用候補は個別arXivページでmetadataとabstractを再確認した。PubMedでは医療AI・LLM・機械学習に関連する未読候補を確認し、`state/seen_papers.txt` にある既出PMIDを除外した。

今回は **18本（arXiv 11本 / PubMed 7本）**を採用した。arXiv側では8月24日投稿の新着が中心で、LLMのRLにおけるcritic再評価、離散diffusion、flow-based language modeling、超長文context、few-shot時系列予測、解釈可能MLなどが目立つ。医療AIでは、術後回復のmultimodal prediction、低血糖のtimely classificationに加え、PubMed側でhuman-AI collaborationや実臨床LLM評価、EHRベースのclinical LLMなどを採用した。

既出IDは除外済み。弱い候補で20本に水増しせず、一次情報から内容を十分に確認できた18本に留めた。今回の `read_level` は全て **abstract**。

---

## 1. Best Practice Critic Optimization

- Source: arXiv
- canonical ID: arxiv:2608.23566
- Publication date: 2026-08-24（v2: 2026-08-25）
- Authors: Penghui Qi, Xiangxin Zhou, Wee Sun Lee
- Category: cs.LG, cs.AI, cs.CL
- URL: https://arxiv.org/abs/2608.23566
- read_level: abstract
- Tags: LLM, reinforcement learning, critic, GRPO, post-training
- Summary: GRPOのようなgroup-based RLがcriticを避ける一方、1 promptあたり複数responseを必要とする問題に対し、criticを安定に学習するBest Practice Critic Optimization (BPCO)を提示。1 response/promptでもgroup-based baselineに匹敵または上回る結果を報告する。
- Why interesting: critic-free RLが主流化する中、「critic自体が悪いのではなくtraining recipeが不安定だった」という実務的に重要な再評価。

### 目的
LLM RLでcritic-based trainingが不安定になる要因を切り分け、sampling効率のよいcritic-based RLを成立させる。
### 手法
DPPO、reward範囲にboundedなvalue prediction、Monte Carlo target、unnormalized advantage、length-adaptive GAEを組み合わせるBPCOを構成。
### データ・実験
数学reasoning task、1.5B〜30B-A3B MoEまでのmodelでcontrolled experiment。
### 主な結果
strong critic baselineを一貫して改善し、1 response/promptでgroup-based baselineに匹敵または上回る。rubric-based rewardでも改善。
### 新規性
criticへpolicyには見せないreference answerやgrading rubricをconditionできる点も含め、criticの情報優位を活用。
### 限界
abstractからは長期agent taskや非reasoning domainへの一般化は未確認。
### なぜ注目したか
RL post-trainingの計算コストと安定性の両方に直接効く可能性がある。

---

## 2. Provably adaptive sampling with uniform and remasking discrete diffusion models

- Source: arXiv
- canonical ID: arxiv:2608.23554
- Publication date: 2026-08-24
- Authors: Daniil Dmitriev, Zhihan Huang, Yuting Wei
- Category: cs.LG, cs.IT, math.ST, stat.ML
- URL: https://arxiv.org/abs/2608.23554
- read_level: abstract
- Tags: discrete diffusion, sampling theory, generative models, information theory
- Summary: 離散diffusionのsampling complexityをambient dimensionではなくtarget distributionのdual total correlationで特徴づけるadaptive guaranteeを示す。
- Why interesting: discrete diffusionの並列生成を理論面から支える結果で、dimension依存の悲観的なlower boundを回避できる可能性を示す。

### 目的
uniform/remasking forward processで、sampling step数が次元dに線形依存することが本質的かを検討。
### 手法
leave-one-out denoiserを使うfirst-order samplerを解析。
### データ・実験
理論解析とstructured synthetic distributionでの数値実験。
### 主な結果
log factorを除き `N = O(DTC(X0)/ε)` のstepで `O(ε_score+ε)` errorを達成できる保証。
### 新規性
discretization errorを時点間coordinateのmutual informationで正確に表現。
### 限界
大規模言語・画像生成での実測speed/quality trade-offはabstractでは未検証。
### なぜ注目したか
diffusion型生成modelのsampling効率をdistribution構造から理解する理論的基盤になる。

---

## 3. ConvergeFlow: Language Flow with Provable Convergence to Token Embeddings

- Source: arXiv
- canonical ID: arxiv:2608.23551
- Publication date: 2026-08-24
- Authors: Na Li, Yuchen Jiao, Changxiao Cai, Gen Li
- Category: cs.CL, cs.AI, cs.LG, stat.ML
- URL: https://arxiv.org/abs/2608.23551
- read_level: abstract
- Tags: language modeling, flow matching, continuous LM, diffusion
- Summary: flow trajectoryがvalid token embeddingへ収束するよう制約し、cross-entropy decoderなしで直接token predictionを可能にするConvergeFlowを提案。
- Why interesting: autoregressive以外のlanguage modelingで、continuous flowとdiscrete tokenの境界を理論保証付きで扱う。

### 目的
continuous flow LMが最終的にvalid token embeddingへ到達しないためCE decoderに依存する問題を解消。
### 手法
data predictorをtoken embeddingのconvex hullへ制約し、flow matching由来のMSEのみで学習。
### データ・実験
OpenWebTextで評価。
### 主な結果
既存continuous / discrete diffusion LMと競合する性能を報告。
### 新規性
predictor errorがあってもvalid embeddingへ収束する条件を理論化し、direct token predictionを可能にする。
### 限界
大規模scaleやinstruction-tuned LLMでの有効性は未確認。
### なぜ注目したか
non-autoregressive / continuous language modelingの設計空間を広げる研究。

---

## 4. Interpretable AI with Local Distillation

- Source: arXiv
- canonical ID: arxiv:2608.23538
- Publication date: 2026-08-24
- Authors: Erin Craig, Yiling Huang, Snigdha Panigrahi
- Category: stat.ME, cs.LG, stat.ML
- URL: https://arxiv.org/abs/2608.23538
- read_level: abstract
- Tags: interpretable ML, distillation, local models, high-stakes AI
- Summary: black-box teacherの予測をquery点ごとのsparse linear studentへlocal distillationし、accuracyを維持しつつ人間が読める局所説明を生成する。
- Why interesting: post-hoc explanationではなく「予測器そのものを局所的に単純化する」方向で解釈可能性を扱う。

### 目的
高性能black-boxと透明性のあるlinear modelの差を局所近似で埋める。
### 手法
teacher予測でlocalityを定義し、query predictionをpseudo-observationとしてstudent fitをanchor。randomized refitでfeature stabilityも評価。
### データ・実験
17 benchmark datasetとhigh-dimensional cancer gene-expression例。
### 主な結果
teacher精度に近い予測を保ちつつ、各test pointでsparse linear modelを得た。
### 新規性
locality自体をteacherから学習し、selection stabilityまで統計的に扱う。
### 限界
局所線形近似が成立しにくい非滑らかなdecision boundaryでは性能が課題になり得るが、abstractでは詳細不明。
### なぜ注目したか
医療等の高stakes predictionへの接続可能性が高い。

---

## 5. Predicting Multiple Clinical Outcomes Related to Functional Recovery and Social Isolation Among Older Adults After Lower-Limb Fracture or Hip Replacement

- Source: arXiv
- canonical ID: arxiv:2608.23531
- Publication date: 2026-08-24
- Authors: Santosh Ray, Pratik K. Mishra, Ali Abedi, Charlene H. Chu, Amir Ahmad, Shehroz S. Khan
- Category: cs.CV, cs.LG
- URL: https://arxiv.org/abs/2608.23531
- read_level: abstract
- Tags: medical AI, multimodal sensors, rehabilitation, multi-output prediction
- Summary: 術後高齢者のsensor dataから、身体機能とsocial isolationを含む5 clinical outcomesを同時予測。multi-output学習が個別予測より良好だった。
- Why interesting: 身体回復だけでなく社会的孤立を同じ予測問題に入れ、在宅rehabilitationをmultimodalに扱う。

### 目的
lower-limb fracture / hip replacement後の複合的回復trajectoryを同時推定。
### 手法
46 daily featuresを使いsingle/multi-output ML・DLを比較。
### データ・実験
MAISON-LLF、18名、最大1,008 participant-days。5 outcomesを2週ごとに評価。
### 主な結果
joint predictionがseparate predictionより良く、NODE multi-output regressorでMSE 3.96、MAE 1.02。
### 新規性
multimodal sensorと複数clinical/social outcomeのjoint modeling。
### 限界
sample size 18と小さい。
### なぜ注目したか
small-data medical AIでmulti-task structureを使う具体例として興味深い。

**Medical AI extra:** study_design=observational modeling; sample_size=18; external_validation=abstract上なし; prospective_or_retrospective=abstractから明確化不可。

---

## 6. Primal--Dual Alternating Neural Learning for Timely Classification with Performance Guarantees

- Source: arXiv
- canonical ID: arxiv:2608.23480
- Publication date: 2026-08-24
- Authors: Jiaming Qiu, Yingye Zheng, Ying-Qi Zhao
- Category: stat.ML, cs.LG, stat.ME
- URL: https://arxiv.org/abs/2608.23480
- read_level: abstract
- Tags: clinical monitoring, sequential classification, RNN, constrained optimization
- Summary: 「早く判定する価値」と「追加観測する価値」をsensitivity・specificity・monitoring costのmulti-objective problemとして定式化し、RNN + primal-dual更新で制約付きtimely classifierを学習する。
- Why interesting: 医療predictionでaccuracyだけでなく「いつ判定するか」を性能保証付きで直接扱う。

### 目的
clinical monitoringの早期判定と追加観測のtrade-offを制御可能にする。
### 手法
value recursionでoptimal decision ruleを特徴づけ、RNNでvalue processを近似、primal-dualでconstraintsを満たす。
### データ・実験
simulationとcontinuous glucose monitoringによるhypoglycemia prediction。
### 主な結果
指定したoperating characteristicsを満たしつつtimelyなdecision ruleを得たと報告。
### 新規性
sensitivity / specificity / monitoring costを明示的制約として学習。
### 限界
abstractでは実臨床prospective validationなし。
### なぜ注目したか
医療AIで重要な「判断時点」をモデル設計に組み込んでいる。

**Medical AI extra:** study_design=method development + simulation/application; primary_endpoint=timely risk classification performance; external_validation=なしとみられる; prospective_or_retrospective=不明。

---

## 7. MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters

- Source: arXiv
- canonical ID: arxiv:2608.23473
- Publication date: 2026-08-24
- Authors: ChengAo Shen, Wenchao Yu, Fangyu Wu, Dongjin Song, Hanghang Tong, Dongsheng Luo, Wei Cheng, Haifeng Chen, Jingchao Ni
- Category: cs.LG, cs.AI
- URL: https://arxiv.org/abs/2608.23473
- read_level: abstract
- Tags: agentic ML, few-shot learning, time series, synthetic data
- Summary: foundation modelをforecastに直接使うのでなく、agentがfew-shot例とtext contextからsynthetic training dataを作り、軽量な専用forecasterを自動構築するMetaCasterを提案。
- Why interesting: agentを「推論器」ではなく「小型modelを作る自動ML engineer」として使う設計。

### 目的
データが少ないtime-series taskで軽量modelを学習可能にする。
### 手法
meta-harness-optimized multi-agent data generationでtask-specific forecasterを訓練。
### データ・実験
18 datasets、23 lightweight forecasters、14 baselines。
### 主な結果
data efficiencyとcompute efficiencyを両立しつつ高品質forecastを維持。
### 新規性
agentic synthetic data generationをdeployment用小型model構築へ接続。
### 限界
synthetic data biasやdomain shiftの詳細はabstractでは不明。
### なぜ注目したか
少量データでsmall modelを作る実用的方向性。

---

## 8. RAD: Rule-Augmented Relational Anomaly Detection

- Source: arXiv
- canonical ID: arxiv:2608.23468
- Publication date: 2026-08-24
- Authors: Noah Dahle, Anne Tumlin, Ngoc Tran, Xenofon Koutsoukos, Tyler Derr
- Category: cs.LG, cs.CR, cs.DB
- URL: https://arxiv.org/abs/2608.23468
- read_level: abstract
- Tags: relational ML, anomaly detection, symbolic rules, graph learning
- Summary: relational DBをflattenせずheterogeneous graphで保持し、random-forest path由来のsymbolic ruleをgraph representationへ注入するanomaly detector。
- Why interesting: neural relational representationと人間が読めるrule evidenceを組み合わせるneuro-symbolic寄りの実装。

### 目的
multi-table relational contextに依存するanomalyを検出。
### 手法
heterogeneous graph learning + refined symbolic rule feature + reconstruction/ranking supervision。
### データ・実験
LANL cybersecurityとAmazon/H&M churn由来の3 benchmark settings。
### 主な結果
flattened tabular / relational baselinesよりanomaly rankingを改善し、AUROC/AUPRCの平均rankで最良。
### 新規性
rule injectionをrelational representationへ直接統合。
### 限界
benchmark domain数は限定的。
### なぜ注目したか
構造化企業データでの説明可能・relational anomaly detectionに応用しやすい。

---

## 9. ProxyFormer: A Dual-Stream Proxy Architecture for Ultra-Long Context and High-Resolution Generation

- Source: arXiv
- canonical ID: arxiv:2608.23463
- Publication date: 2026-08-24
- Authors: Zhongpan Tang
- Category: cs.LG
- URL: https://arxiv.org/abs/2608.23463
- read_level: abstract
- Tags: long context, transformer efficiency, KV cache, proxy tokens
- Summary: local fine-grained streamを残しつつ、global interactionだけを圧縮proxy token上で行うdual-stream architecture。超長文contextのattention/KV costを削減する。
- Why interesting: one-shot compressionで情報を捨てず、local streamを各layerに維持する点が特徴。

### 目的
sequence lengthに対するquadratic attentionとKV cache増大を抑える。
### 手法
bottom-up proxy compression → proxy上global interaction → top-down injection。proxy-only KV cacheも導入。
### データ・実験
long-context retrievalとpreliminary image generation。
### 主な結果
16GB GPUでstandard約20K tokensに対しcompression ratio 64で約0.7M tokensまでtraining可能。64K training window modelが1,048,576 tokensで92–95% multi-needle retrieval accuracy。
### 新規性
persistent local streamとproxy global streamのdual architecture。
### 限界
preliminary結果中心で、大規模LLMの総合benchmarkは未確認。
### なぜ注目したか
long-contextのmemory/compute bottleneckへの直接的architecture提案。

---

## 10. Diversity-Based Active Learning: An Evaluation of Metric Spaces for Active Learning Selection

- Source: arXiv
- canonical ID: arxiv:2608.23461
- Publication date: 2026-08-24
- Authors: Siddharth Chilamkur, Dorit S. Hochbaum
- Category: cs.LG
- URL: https://arxiv.org/abs/2608.23461
- read_level: abstract
- Tags: active learning, small data, sample selection, classification
- Summary: Greedy K-center active learningで、raw/LDA空間よりもmodel probability space + entropy weightingがしばしば有効と実証。
- Why interesting: label budgetが小さい場面で、単純なdiversity samplingをどのrepresentation空間で行うべきかを比較している。

### 目的
diversity-based active learningのmetric space選択を実証評価。
### 手法
raw feature、LDA、model-derived probability spaceを比較しentropy weightingも評価。
### データ・実験
synthetic / real-world classification datasets、Random Forest evaluator。
### 主な結果
probability space + entropy weightingがGreedy K-centerで他optionをしばしば上回る。
### 新規性
selection algorithmそのものよりrepresentation spaceの影響を明示。
### 限界
model familyやtask typeが広範かはabstractでは不明。
### なぜ注目したか
少量label環境で即応用しやすい知見。

---

## 11. Traceable Spectral Inference via Influence Functions: Efficient Data Attribution and Error Proxies for the Ariel Mission

- Source: arXiv
- canonical ID: arxiv:2608.23458
- Publication date: 2026-08-24
- Authors: Nikki Grens, Luís F. Simões, Kai Hou Yip, Theresa Lueftinger
- Category: cs.LG, astro-ph.IM, stat.ML
- URL: https://arxiv.org/abs/2608.23458
- read_level: abstract
- Tags: data attribution, influence functions, scientific ML, uncertainty
- Summary: ground truthが運用中に得られないspace mission向けに、prediction influenceを使ってtraining sample attributionとlabel-free error proxyを構築。
- Why interesting: explainabilityをfeature attributionではなく「どのtraining dataがこの予測に効いたか」に向ける実運用型研究。

### 目的
scientific MLでground truthなしにprediction reliabilityを監査。
### 手法
prediction-based influence function、ridge closed-formを利用したefficient computation、training residualからerror proxyを伝播。
### データ・実験
Ariel mission向けsimulated spectra。
### 主な結果
提案error proxyがscale/shape spectral errorと強く相関し、有害/影響大sampleの近似も可能。
### 新規性
label-free operational data attribution + error proxy。
### 限界
実mission dataでのvalidationはabstractでは未確認。
### なぜ注目したか
高stakes scientific model monitoringへ使える可能性。

---

# PubMed / Medical AI

## 12. The application of artificial intelligence in healthcare practice: A mapping review of systematic reviews

- Source: PubMed
- canonical ID: pmid:42492159
- Publication date: 2026-07-18 (online ahead of print)
- Authors: Adam Andersen, Ruiping Huang, Edward Jiusi Liu
- Journal: Artificial Intelligence in Medicine
- URL: https://pubmed.ncbi.nlm.nih.gov/42492159/
- read_level: abstract
- Tags: medical AI, mapping review, evidence synthesis, implementation
- Summary: 2019〜2026年2月のsystematic review/meta-analysisを俯瞰し、医療AIの実装領域・データ種別・研究集中を整理。368 reviewsを採用。
- Why interesting: 個別AI modelではなく、医療AI分野全体がどこまで成熟しているかを俯瞰できる。

### 目的
AI healthcare practiceのsystematic review群をmappingし、研究集中・不足領域を把握。
### 手法
PubMed/Web of Science/Scopus/IEEE Xplore/CINAHLを検索。
### データ・実験
368 systematic reviews/meta-analyses。
### 主な結果
radiology・oncology・critical careへ集中。diagnostic imaging、EHR、biomarker/labがtraining data sourceの68%。wearable/sensor dataは2022年以降増加。
### 新規性
レビューのレビューとして領域全体をmap。
### 限界
review-level synthesisであり、個々のstudy quality差を直接解決しない。
### なぜ注目したか
今後watch対象のmedical AI subdomainを見直す基礎資料になる。

**Medical AI extra:** study_design=mapping review of systematic reviews; sample_size=368 reviews; external_validation=該当なし; prospective_or_retrospective=該当なし。

---

## 13. Human-AI Collaboration in Healthcare: A Scoping Review

- Source: PubMed
- canonical ID: pmid:42323426
- Publication date: 2026-06-20
- Authors: Joshua Strong et al.
- Journal: npj Digital Medicine
- URL: https://pubmed.ncbi.nlm.nih.gov/42323426/
- read_level: abstract
- Tags: human-AI collaboration, clinical workflow, scoping review, trust
- Summary: healthcareのhuman-AI collaboration実証研究をscoping review。17,463 recordsから140 studiesを採用し、診断解釈に研究が偏ることを示した。
- Why interesting: AI単体性能ではなくhuman-AI teamとしての効果とworkflow integrationを中心に整理。

### 目的
HAICの実証エビデンスと評価方法を整理。
### 手法
Joanna Briggs Institute methodology / PRISMA-ScR。
### データ・実験
140 studies（17,463 recordsから選定）。
### 主な結果
多くの診断taskでbenefitが報告されるが、task fit、workflow integration、training、trust calibrationに依存。patient/system outcomesの長期評価は少ない。
### 新規性
human+AI unitとして評価する視点。
### 限界
短期task-level metrics中心。
### なぜ注目したか
臨床導入時にmodel accuracyだけでは不十分なことを体系的に示す。

**Medical AI extra:** study_design=scoping review; sample_size=140 studies; external_validation=該当なし。

---

## 14. Real-world evaluation of large language model for patients medical and administrative queries in nuclear medicine

- Source: PubMed
- canonical ID: pmid:42303756
- Publication date: 2026-06-17
- Authors: Arash Latifoltojar et al.
- Journal: npj Digital Medicine
- URL: https://pubmed.ncbi.nlm.nih.gov/42303756/
- read_level: abstract
- Tags: clinical LLM, real-world evaluation, patient queries, nuclear medicine
- Summary: 実患者からprospectively収集したmedical/admin queriesに対し、ChatGPT v4.1と医師・事務スタッフの回答を比較評価。
- Why interesting: benchmark問題ではなく、実際の患者問い合わせを使ったreal-world LLM evaluation。

### 目的
患者向けLLM回答がhuman responsesと比べて実用レベルか評価。
### 手法
15/17 QUEST dimensionsでmedical/admin expertsとnon-expertsがLikert評価し、question単位でbetter/equivalent/worse判定。
### データ・実験
nuclear medicineでprospectively collected patient queries。
### 主な結果
取得できたabstract情報では評価枠組みは確認できたが、個別dimensionの数値結果は今回の取得範囲では十分確認できないため記載しない。
### 新規性
real patient questions + medical/admin両側の評価。
### 限界
single specialtyでの評価。
### なぜ注目したか
LLM臨床導入をbenchmarkから実workflowへ近づけた研究。

**Medical AI extra:** study_design=prospective real-world evaluation; external_validation=single-domain evaluation; prospective_or_retrospective=prospective。

---

## 15. General-purpose large language models outperform specialized clinical AI tools on medical benchmarks

- Source: PubMed
- canonical ID: pmid:42286322
- Publication date: 2026-06-12 (Epub)
- Authors: Krithik Vishwanath et al.
- Journal: Nature Medicine
- URL: https://pubmed.ncbi.nlm.nih.gov/42286322/
- read_level: abstract
- Tags: medical LLM, clinical AI, benchmark, real clinical queries
- Summary: OpenEvidence / UpToDate Expert AIとfrontier general-purpose LLMを、MedQA、HealthBench、real clinical queriesで比較し、general-purpose modelsが全評価で上回ったと報告。
- Why interesting: 「医療特化modelなら一般modelより強い」という前提を独立比較で検証している。

### 目的
specialized clinical AI toolsとfrontier LLMの実力差を独立評価。
### 手法
3-stage evaluation: MedQA 500、HealthBench 500、real clinical queries 100。
### データ・実験
RCQで12 US clinicians、1,800 model-question annotations。
### 主な結果
frontier LLMsが3評価すべてでclinical AI toolsを上回った。clinical AI toolsはRCQでGoogle Search AI Overviewと同程度。
### 新規性
commercial clinical toolsをreal queries込みで第三者比較。
### 限界
評価対象model・US clinical contextに依存。
### なぜ注目したか
medical AIの「specializationの価値」を再考させる結果。

**Medical AI extra:** study_design=multi-stage benchmark + blinded clinician evaluation; sample_size=500+500+100 queries, 1,800 annotations; external_validation=複数benchmark + real clinical queries。

---

## 16. Integrating large language models for enhanced predictive analytics in healthcare

- Source: PubMed
- canonical ID: pmid:41927986
- Publication date: 2026 (PubMed record)
- Authors: Yuli Wang et al.
- Journal: npj Digital Medicine
- URL: https://pubmed.ncbi.nlm.nih.gov/41927986/
- read_level: abstract
- Tags: EHR, clinical LLM, predictive analytics, multi-task learning
- Summary: structured EHRをlanguage-model形式で扱い、7B LLaMA architectureをclinical/operational predictionのmulti-task engineとして利用するHopkins LLMを提案。
- Why interesting: LLMを自由文生成ではなく、structured EHRの汎用predictive engineとして使う設計。

### 目的
clinical predictive model開発・deploymentのdata handlingとtask-specific engineering負担を減らす。
### 手法
7B LLaMA architectureをpretrain/fine-tuneしてstructured EHR predictionへ適用。
### データ・実験
Johns Hopkins Health Systemの42,160 patients。
### 主な結果
複数clinical/operational prediction taskを1つのframeworkで扱えることを報告。今回取得したabstract抜粋では各taskの数値は確認不足のため記載しない。
### 新規性
structured EHRをLLM型multi-task predictive engineへ統合。
### 限界
single health system由来dataでの一般化が課題になり得る。
### なぜ注目したか
clinical foundation modelの実装形態として具体的。

**Medical AI extra:** study_design=retrospective model development/evaluation; sample_size=42,160 patients; external_validation=abstract取得範囲では不明; prospective_or_retrospective=retrospectiveとみられるがrecord本文での明示は今回未確認。

---

## 17. Artificial Intelligence in Health Care: Clinical Opportunities, Validation Trends, and Implementation Challenges (2020-2025)

- Source: PubMed
- canonical ID: pmid:42008829
- Publication date: 2026-04-20 (online ahead of print)
- Authors: Itrat Zehra, Shakir Ali, Seung Won Lee
- Journal: Journal for Healthcare Quality
- URL: https://pubmed.ncbi.nlm.nih.gov/42008829/
- read_level: abstract
- Tags: medical AI, validation, implementation, review
- Summary: 2020〜2025年の医療AIを、clinical opportunityだけでなくvalidation trendとimplementation challengeの観点から整理するreview。
- Why interesting: model性能からdeploymentへ視点を移し、実装障壁をまとめている。

### 目的
医療AIの臨床機会・validation・implementationの現状を整理。
### 手法
review。
### データ・実験
2020–2025 literatureを対象。
### 主な結果
AIはdiagnosis、prediction、workflow支援を拡大している一方、validationとimplementationが継続的課題と整理。
### 新規性
近年のdeployment trendをquality観点で俯瞰。
### 限界
reviewでありindividual modelのprospective evidenceではない。
### なぜ注目したか
研究から実運用へのgapを追う上で有用。

**Medical AI extra:** study_design=review; external_validation=該当なし。

---

## 18. The role of artificial intelligence in virtual emergency care: a systematic review

- Source: PubMed
- canonical ID: pmid:41880917
- Publication date: 2026-03-22 (Epub; journal record 2026-07-01)
- Authors: Ravi Shankar et al.
- Journal: International Journal of Medical Informatics
- URL: https://pubmed.ncbi.nlm.nih.gov/41880917/
- read_level: abstract
- Tags: emergency care, virtual care, medical AI, systematic review
- Summary: virtual emergency careにおけるAI利用をsystematic reviewし、remote/virtual settingでのclinical decision supportの位置づけを整理。
- Why interesting: AI医療の中でもdeployment条件が特殊なvirtual emergency careに焦点を当てる。

### 目的
virtual emergency careでAIが担う役割とevidenceを整理。
### 手法
systematic review。
### データ・実験
既存研究のsystematic synthesis。
### 主な結果
今回取得したPubMed abstract抜粋では詳細なincluded-study数やpooled resultを十分確認できなかったため、数値は記載しない。
### 新規性
virtual emergency careという明確なworkflow contextに限定した整理。
### 限界
一次研究のheterogeneityに依存。
### なぜ注目したか
telemedicine/virtual careでAIを組み込む際の実装文脈が分かる。

**Medical AI extra:** study_design=systematic review; external_validation=該当なし。

---

<!-- PAPER_IDS -->
arxiv:2608.23566
arxiv:2608.23554
arxiv:2608.23551
arxiv:2608.23538
arxiv:2608.23531
arxiv:2608.23480
arxiv:2608.23473
arxiv:2608.23468
arxiv:2608.23463
arxiv:2608.23461
arxiv:2608.23458
pmid:42492159
pmid:42323426
pmid:42303756
pmid:42286322
pmid:41927986
pmid:42008829
pmid:41880917
<!-- /PAPER_IDS -->
