# [paper-report] 2026-08-29 ML / LLM / Medical AI

- Issue: #9
- Source: https://github.com/drkamoshika/papers/issues/9
- Created at: 2026-08-29T06:23:36Z

# Paper Watch Report — 2026-08-29

## 今回の概況

`config/paper_watch.yml` version 2 に従い、arXiv / PubMed それぞれで新しい側から関連候補を探索し、`state/seen_papers.txt` に登録済みのcanonical IDを除外した。今回は最大20本の枠に対し、**arXiv 12本 / PubMed 8本、計20本**を採用した。

arXivでは2026-08-27投稿の新着が厚く、test-time adaptation、agent skillの永続化、RLVRの探索・能力統合、低コストpretraining、LLM内部表現の監査など、モデルを「学習済みの固定物」として使うより、推論時・運用時にどう適応・監査するかを扱う研究が目立った。PubMedでは、精神病リスク評価、肺炎抗菌薬選択、抗菌薬stewardship RAG、LLM研究の再現性監査、医療コミュニケーション訓練、放射線治療計画・画像生成、核医学画像高速化など、臨床ワークフローに近い評価が多い。

全論文について、先に **Tags / Summary / Why interesting** を置き、その後に **目的 / 手法 / データ・実験 / 主な結果 / 新規性 / 限界 / なぜ注目したか** を記載する。今回の `read_level` はすべて `abstract` とした。

---

# arXiv

## 1. CritICL: Inference-Time Weak-to-Strong Generalization from Small Language Model Failure Modes

- Source: arXiv
- canonical ID: arxiv:2608.27455
- Publication date: 2026-08-27
- Authors: Yufan Wu, Yinghui He, Zhengyi Hu, Lang Wei, Ruichen Li, Qifan Yang, Ting Zhu
- Category: cs.CL
- URL: https://arxiv.org/abs/2608.27455
- read_level: abstract
- Tags: test-time adaptation, weak-to-strong, ICL, inference efficiency
- Summary: 小型モデルが失敗するパターンを構造化して強いモデルの推論時ガイダンスへ変換するCritICLを提案。追加学習なしで、標準ICLや高コストなtest-time scalingより少ない生成回数・tokenで改善を狙う。
- Why interesting: 「弱いモデルの答え」ではなく「弱いモデルがどう失敗するか」を情報資源として使う点が面白い。

### 目的
推論時に高性能モデルを適応させる際、弱いモデルから得られる失敗情報を有効活用できるかを検証する。
### 手法
弱いモデルのfailure modeを抽出してprompt/contextへ組み込むstatic / dynamic CritICLを構成し、強いモデルの推論を誘導する。
### データ・実験
複数のreasoning taskでstandard ICLおよびtest-time scaling系手法と比較。
### 主な結果
abstractでは標準ICLを一貫して上回り、test-time scalingに競合または優越しつつgeneration数とtoken costを削減したと報告。
### 新規性
weak-to-strong transferをtrainingではなくinference-time failure-mode transferとして扱う点。
### 限界
failure mode抽出の品質や、非常に異なるmodel family間での一般性はabstractだけでは不明。
### なぜ注目したか
小型モデルを単なる安価な代替ではなく、強モデルを改善する診断器として使う設計だから。

---

## 2. WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

- Source: arXiv
- canonical ID: arxiv:2608.27454
- Publication date: 2026-08-27
- Authors: Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu
- Category: cs.AI, cs.CL
- URL: https://arxiv.org/abs/2608.27454
- read_level: abstract
- Tags: LLM agent, skill evolution, persistent memory, knowledge base
- Summary: agentの経験を一過性のtrajectoryで終わらせず、永続wikiと実行可能skillへコンパイルし、両者を共進化させるWikiSkillを提案。
- Why interesting: agent memoryを「検索する履歴」ではなく、再利用可能な知識とskillへ編集する方向に進めている。

### 目的
長期agentが過去経験を蓄積しても、それが再利用可能なskillとして成長しにくい問題を扱う。
### 手法
経験をpersistent wikiへ構造化し、その知識からexecutable skillを生成・更新するループを設計。
### データ・実験
複数benchmarkと複数model settingで既存skill-evolution手法と比較。
### 主な結果
abstractではstate-of-the-art skill evolution手法を上回り、獲得skillが異なるmodel / familyへもtransferしたと報告。
### 新規性
knowledge baseとskill libraryを別々に持つのではなく、相互更新させる点。
### 限界
長期間のwiki肥大化、誤知識修正、現実のtool環境での安全性は未確認。
### なぜ注目したか
長期agentの「経験をどう資産化するか」に直接答える設計だから。

---

## 3. TTPO: Test-Time Policy Optimization

- Source: arXiv
- canonical ID: arxiv:2608.27448
- Publication date: 2026-08-27
- Authors: Aozhe Wang, Zhengxi Lu, Jianze Wang, Shangke Lv, Ying Liu, Weiming Lu, Jun Xiao, Yueting Zhuang, Hua Yang, Qianglong Chen, Yongliang Shen
- Category: cs.CL
- URL: https://arxiv.org/abs/2608.27448
- read_level: abstract
- Tags: test-time training, policy optimization, reasoning, self-supervision
- Summary: test-timeに複数rolloutの一致・不一致を利用してpolicyを最適化するTTPOを提案。教師ラベルなしで推論能力をその場で更新する。
- Why interesting: test-time computeを「たくさん考える」だけでなく「その場でpolicy更新する」方向へ拡張している。

### 目的
正解ラベルがないtest-time環境でも、モデル自身のrolloutから学習signalを作りpolicyを改善する。
### 手法
一致rolloutを利用するobjectiveと、不一致groupを扱うRL objective、token-level selectionを組み合わせる。
### データ・実験
5つのcompetition-level reasoning benchmarkで評価。
### 主な結果
Qwen3-1.7Bで一例として38.0%から45.2%へ改善。thinkingなし設定でもtaskにより+25.2〜+36.4 pointsの改善を報告。
### 新規性
label-free test-time policy updateをrollout agreementから構成する点。
### 限界
test-time更新の計算量、誤ったconsensusによるdrift、継続利用時の安定性はabstractでは不明。
### なぜ注目したか
test-time scalingとonline adaptationの境界を縮める研究だから。

---

## 4. Boosting LLM Exploration via Weak-Model Guidance in RLVR

- Source: arXiv
- canonical ID: arxiv:2608.27420
- Publication date: 2026-08-27
- Authors: Xingyu Shen, Huishuai Zhang, Peng Li, Yinchun Wang, Dongyan Zhao
- Category: cs.CL
- URL: https://arxiv.org/abs/2608.27420
- read_level: abstract
- Tags: RLVR, exploration, weak model, entropy collapse
- Summary: RLVRで探索が早期に狭まる問題に対し、弱いモデルの部分reasoning prefixを注入してtarget modelを異なる探索軌道へ誘導する。
- Why interesting: 弱モデルをteacherではなくexploration perturbationとして使うため、強モデルの多様性を保つ発想が明快。

### 目的
RLVR training中のentropy collapseと探索不足を緩和する。
### 手法
weak modelが生成した部分的reasoning prefixをtarget modelのrollout開始条件として利用。
### データ・実験
複数reasoning benchmarkで通常RLVRと比較し、sampling数kを変えて分析。
### 主な結果
abstractではkが増えるほど改善が目立ち、追加SFT・複雑なreward設計なしで探索性と性能を改善。
### 新規性
weak modelの不完全reasoningを探索多様性のseedとして利用。
### 限界
weak model選択依存性やprefix品質が悪い場合の悪影響は未確認。
### なぜ注目したか
RLの探索問題をmodel hierarchyで解くシンプルな介入だから。

---

## 5. Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms

- Source: arXiv
- canonical ID: arxiv:2608.27409
- Publication date: 2026-08-27
- Authors: Siye Wu, Kai Yang, Yuchen Cai, Xin Xu, Peng-Yuan Wang, Jiaxuan Wang, Jiashun Liu, Jiafei Lyu, Yangkun Chen, Saiyong Yang, Yanghua Xiao
- Category: cs.CL
- URL: https://arxiv.org/abs/2608.27409
- read_level: abstract
- Tags: RLVR, model merging, capability fusion, multi-domain reasoning
- Summary: domain別RLVRで獲得した能力をMerge、mixed RL、MOPDなどで統合し、どの融合方法が能力保持に効くかを比較。
- Why interesting: 「専門モデルをどう統合するか」を平均scoreだけでなくdomain別の差として丁寧に見ている。

### 目的
別domainで個別に強化したreasoning能力を一つのmodelへ統合する最適な方法を比較する。
### 手法
parameter merge、mixed reinforcement learning、policy distillation系を横断評価。
### データ・実験
複数domain / benchmarkでsingle-domain RLVR modelと統合modelを比較。
### 主な結果
平均差は手法間で1.4 points以内でも、個別benchmarkでは最大8.6 points差。single-sample accuracyは改善する一方、solution coverage自体の増加は明確でないと報告。
### 新規性
融合手法の平均値だけでなく、domain別trade-offとcoverageまで分析。
### 限界
対象model規模・domain構成が変わった場合の一般性は未確認。
### なぜ注目したか
複数RL specialistを運用する際の実践的な設計判断に直結する。

---

## 6. How Language Models Organize and Structure Moral Knowledge

- Source: arXiv
- canonical ID: arxiv:2608.27402
- Publication date: 2026-08-27
- Authors: Orion Reblitz-Richardson
- Category: cs.CL, cs.AI, cs.LG
- URL: https://arxiv.org/abs/2608.27402
- read_level: abstract
- Tags: interpretability, representation, moral knowledge, probing
- Summary: LLM内部で複数のmoral foundationがどのように表現されるかをlinear probeと方向ベクトルで分析し、独立性と共通成分の両方を示す。
- Why interesting: alignmentを出力評価だけでなく「内部で価値概念がどう幾何学的に配置されるか」から見る研究。

### 目的
moral conceptが単一軸なのか、複数独立軸なのか、内部representation構造を調べる。
### 手法
6種類のmoral foundation向けlinear probeとrepresentation directionを構築。
### データ・実験
moral dilemma等の入力でdirection間類似性・合成性を分析。
### 主な結果
directionはほぼ独立しつつ共通moral componentも持ち、平均pairwise cosine 0.26（非moral比較0.013）。dilemma directionの合成はmismatch baselineの2.7倍と報告。
### 新規性
価値判断をpre-resolved labelではなく複数概念間の構造・conflictとして解釈。
### 限界
probeが因果的表現を捉えているか、model間一般性は要検証。
### なぜ注目したか
alignment / interpretabilityを内部表現から理解する具体的な手掛かりになる。

---

## 7. Making Clinical Language Models Auditable: Concept-Guided Fine-Tuning for Robust Prediction

- Source: arXiv
- canonical ID: arxiv:2608.27397
- Publication date: 2026-08-27
- Authors: Jin Mu, Guanhua Chen
- Category: cs.CL, cs.AI
- URL: https://arxiv.org/abs/2608.27397
- read_level: abstract
- Tags: medical AI, clinical NLP, sparse autoencoder, auditability
- Summary: SAE featureを臨床conceptへ対応づけ、artifact latentを抑制しながらfine-tuningするCASTを提案。prediction精度とconcept-level audit trailを両立する。
- Why interesting: 医療LMの説明可能性をpost-hoc説明だけでなく、fine-tuning時のfeature制御に組み込んでいる。

### 目的
clinical LMがdataset artifactへ依存する問題を抑えつつ、予測根拠をconcept単位で監査可能にする。
### 手法
SAE latentをLLM-assisted labelingとICD-10 constraintでconcept化し、確認済みartifact latentを抑制してfine-tuning。
### データ・実験
MIMIC-IV discharge noteのmortality predictionで評価。
### 主な結果
abstractでは対応するfine-tuned encoder baselineを上回り、LLM baselineとも競合しつつfeature-level audit trailを提供。
### 新規性
concept discovery、artifact suppression、attributionを同一training frameworkに統合。
### 限界
単一EHR source中心で、外部施設validationはabstractで確認できない。
### なぜ注目したか
医療AIの性能と監査可能性を同時に設計する実用的方向だから。

**Medical AI extra:** study_design=model development / retrospective EHR evaluation; sample_size=abstract記載なし; primary_endpoint=mortality prediction; external_validation=明示なし; prospective_or_retrospective=retrospective.

---

## 8. LeVJEPA: Efficient & Scalable Video Pretraining without the Heuristics

- Source: arXiv
- canonical ID: arxiv:2608.27395
- Publication date: 2026-08-27
- Authors: Lukas Kuhn, Lucas Maes, Giuseppe Serra, Quentin Le Lidec, Yann LeCun, Randall Balestriero, Florian Buettner
- Category: cs.CV, cs.AI
- URL: https://arxiv.org/abs/2608.27395
- read_level: abstract
- Tags: video pretraining, JEPA, self-supervised learning, efficiency
- Summary: 複雑なheuristicを減らした単一encoder型video pretrainingを提案し、V-JEPA2より大幅に少ないcomputeで競合性能を狙う。
- Why interesting: video foundation modelで「性能を上げる複雑さ」より「単純化してscaleする」方向を示している。

### 目的
video representation learningをより単純・低計算量でscale可能にする。
### 手法
single encoder + projectorとcollapse-free LeJEPA objective、SIGRegを利用。
### データ・実験
V-JEPA2等とmatched-epoch / matched-FLOPs比較。
### 主な結果
matched epochsで5.6〜20.8倍少ないpretraining compute、matched FLOPsでImageNet-1K +7.6 pointsを報告。
### 新規性
多数のvideo-specific heuristicを外し、単純なpredictive representation objectiveへ寄せる。
### 限界
downstream video-specific task全体での優位性や大規模scale時の再現性はabstractだけでは不明。
### なぜ注目したか
foundation modelの計算効率と設計簡素化の両方に関わるため。

---

## 9. CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases

- Source: arXiv
- canonical ID: arxiv:2608.27391
- Publication date: 2026-08-27
- Authors: Sil Hamilton, Albert Yu Sun, Oscar J. Romero, Carl-Leander Henneking, David Mimno, Bishan Yang, Igor Labutov
- Category: cs.AI, cs.CL, cs.IR, cs.LG
- URL: https://arxiv.org/abs/2608.27391
- read_level: abstract
- Tags: enterprise QA, temporal knowledge, long context, benchmark
- Summary: 企業内情報の時間変化と組織規模を模した大規模QA benchmark。最大10,000人規模のsynthetic企業と23万超documentsを用意する。
- Why interesting: enterprise RAG/agent評価で、単純なstatic corpusではなく組織規模と時間変化を含めている。

### 目的
現実的な企業knowledge environmentでLLM QA性能が規模拡大にどう劣化するか測る。
### 手法
複数のsynthetic company、temporal document、ground-truth QAを生成。
### データ・実験
4企業、12〜10,000 employees相当、230k超documents、5 LLMを評価。
### 主な結果
組織・context規模が現実的になるほど性能が悪化すると報告。
### 新規性
enterprise QAにtemporal driftとorganizational scaleを体系的に導入。
### 限界
synthetic corporationが実企業のアクセス権・ノイズ・文化をどこまで再現するかは不明。
### なぜ注目したか
長期運用RAG/agentの現実的stress testとして有用そうだから。

---

## 10. Puro-2B: Poor Lab's Qwen2-1.5B Trained on RTX 5090 within $5090

- Source: arXiv
- canonical ID: arxiv:2608.27370
- Publication date: 2026-08-27
- Authors: Kairong Luo, Jiarui Cui, Yaorui Yin, Shengqi Chen, Yiming Yang, Linxiang Gao, Yanmohan Wang, Mingzhe Zhang, Kaiyue Wen, Kaifeng Lyu, Wenguang Chen
- Category: cs.CL, cs.LG
- URL: https://arxiv.org/abs/2608.27370
- read_level: abstract
- Tags: pretraining, low-cost training, FP8, consumer GPU
- Summary: consumer RTX 5090とFP8を使い、1.4T tokensまで2B級モデルをscratch pretrainingする公開recipeを提示。
- Why interesting: foundation model pretrainingを大規模cluster前提から引き下げ、研究室レベルで再現可能にしようとしている。

### 目的
限られた予算・consumer GPUでもcompetitiveな小型LMをscratchから学習できるか検証。
### 手法
FP8 training、data/training recipe、compute-cost optimizationを組み合わせる。
### データ・実験
Puro-2B系列を最大1.4T tokensまでpretrainしQwen2/2.5 1.5B級と比較。
### 主な結果
最良runはcompute cost $6.9K未満でQwen2.5-1.5Bへ接近。scaling-law分析では約$4.4KでQwen2-1.5B相当を予測。
### 新規性
consumer hardware前提でtraining recipe・costを明示した点。
### 限界
電力・開発時間・data preparationを含む総コストや他hardwareでの再現性は別途確認が必要。
### なぜ注目したか
小規模研究環境でのfrom-scratch学習の実現可能性を具体的数字で示すため。

---

## 11. Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO

- Source: arXiv
- canonical ID: arxiv:2608.27351
- Publication date: 2026-08-27
- Authors: Yunpeng Ba, Zhi Zheng, Yue Xie, Jiaqing Li, Xialiang Tong, Tao Zhong, Mingxuan Yuan, Zhichao Lu, Xuyang Wu, Zhenkun Wang
- Category: cs.LG
- URL: https://arxiv.org/abs/2608.27351
- read_level: abstract
- Tags: evolution strategies, reasoning, GRPO, post-training
- Summary: LLM reasoning post-trainingでEvolution StrategiesをGRPOと比較し、Pass@1だけでなくPass@Kのsolution coverageに強みがあることを分析。
- Why interesting: RL系post-trainingが平均成功率を上げてもreasoning diversityを狭める可能性に対し、ESという別系統の最適化を示す。

### 目的
ESがLLM reasoningでどのような能力・coverageを獲得するかGRPOと比較する。
### 手法
gradient-free ES trainingとGRPO、さらにsequential GRPO→ESを評価。
### データ・実験
複数reasoning benchmarkでPass@1 / Pass@K等を比較。
### 主な結果
ESはPass@1を改善しつつGRPOより広いPass@K coverageを示し、sequential combinationも有効と報告。
### 新規性
LLM reasoningのpost-trainingをsolution coverage観点でESと比較。
### 限界
ESのsample efficiencyや大規模modelでのcompute costはabstractでは十分分からない。
### なぜ注目したか
RLVR以外のreasoning optimizationに実用的な選択肢を提示するため。

---

## 12. INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment

- Source: arXiv
- canonical ID: arxiv:2608.27348
- Publication date: 2026-08-27
- Authors: Yutong Zhang, Jianshuo Dong, Peng Xu, Long Wang, Jie Zhang, Tianwei Zhang, Xiaoping Zhang, Han Qiu
- Category: cs.CL
- URL: https://arxiv.org/abs/2608.27348
- read_level: abstract
- Tags: agent safety, misalignment, intent monitoring, tool use
- Summary: agentにintent-targeted toolを用意し、そのtoolを呼ぶ確率をintent signalとして使う監視手法を提案。
- Why interesting: CoTを読んで判定するjudge方式ではなく、agent行動そのものに監査用signalを埋め込む発想。

### 目的
長いagent trajectoryのどの時点でmisaligned intentが形成されたかを密に追跡する。
### 手法
intentごとの専用toolをenvironmentに追加し、tool-call probabilityをjudge-free signalとして取得。
### データ・実験
agentic misalignment scenarioでCoT-based monitoring等と比較。
### 主な結果
abstractではCoT監視を補完し、重要なintervention stepをより直接特定できると報告。
### 新規性
monitoringを外部judgeではなくaction-space設計へ組み込む点。
### 限界
agentが監視toolの存在を学習・回避する可能性や実tool環境への影響は要検証。
### なぜ注目したか
agent安全性をruntime instrumentationとして設計する方向が実装に近いため。

---

# PubMed

## 13. Large language models can supplement the assessment of clinical high risk for psychosis

- Source: PubMed
- canonical ID: pmid:42560867
- Publication date: 2026-08-06 (online ahead of print)
- Authors: Luz Maria Alliende, Rob Voigt, Maeve Hoffman, Gregory P Strauss, Lauren M Ellman, Elaine F Walker, Philip Corlett, Jason Schiffman, Scott W Woods, Albert Powers, Steven M Silverstein, James A Waltz, Richard Zinbarg, Shuo Chen, Trevor F Williams, Joshua Kenney, James M Gold, Vijay A Mittal
- Journal: Journal of Psychopathology and Clinical Science
- URL: https://pubmed.ncbi.nlm.nih.gov/42560867/
- read_level: abstract
- Tags: medical AI, psychiatry, LLM, clinical risk prediction
- Summary: 2,077件のpsychosis-risk interview assessor notesからModernBERT、LLaMA-4、GPT-4.1 miniでリスク指標を抽出し、CHR判定と将来conversion予測への追加価値を評価。
- Why interesting: 構造化検査だけでなく、既に臨床で残される自由記述noteからリスク情報を補助的に取り出す現実的な使い方。

### 目的
clinical high risk for psychosis (CHR)の評価をNLP/LLMで補助できるか検証。
### 手法
encoder modelとzero/few-shot decoder LLMをassessor notesへ適用し、gold-standard CHR rating、SHARP/NAPLS score、conversion predictionと比較。
### データ・実験
Structured Interview for Psychosis-risk Syndromes 2,077 interviews。
### 主な結果
ModernBERTがCHR分類accuracy 82.67%、κ=.63。positive分類はSHARP +0.69 SD、NAPLS +0.85 SDと関連（p<.001）。decoder risk scoreも既存risk scoreと有意に関連し、一部conversion modelを追加改善。
### 新規性
専門的transcript preprocessingではなくassessor notesという利用しやすい入力でrisk signalを抽出。
### 限界
単一consortium由来で、prospective deploymentや別医療圏でのgeneralizationは未確認。
### なぜ注目したか
臨床noteをLLMで補助screeningに使う、導入可能性の高いユースケースだから。

**Medical AI extra:** study_design=retrospective/proof-of-concept observational analysis; sample_size=2,077 interviews; primary_endpoint=CHR classification / risk association; external_validation=明示なし; prospective_or_retrospective=retrospective.

---

## 14. Enhancing antimicrobial stewardship using a retrieval-augmented generation large language model for infectious disease management

- Source: PubMed
- canonical ID: pmid:42561260
- Publication date: 2026-08-03 (PubMed record; collection 2026)
- Authors: Hugo Morales, Cristian Rocha, Luan Matheus Trindade Dalmazo, Lucas de Azevedo Takara, Mateus Cichelero, Bruno Guerra, Jessica Andrade-Silva, Paula Tuma, Moacyr Silva Júnior
- Journal: Einstein (São Paulo)
- URL: https://pubmed.ncbi.nlm.nih.gov/42561260/
- read_level: abstract
- Tags: medical AI, RAG, antimicrobial stewardship, clinical guideline
- Summary: Hospital Israelita Albert Einsteinの抗菌薬guideをRAG化し、institutional protocolへ沿った回答検索とusabilityを評価。
- Why interesting: general medical knowledgeではなく、施設内guidelineをgrounding sourceにしてprotocol adherenceを狙う実装。

### 目的
抗菌薬治療guideへのアクセスと遵守をRAG-LLMで標準化する。
### 手法
document processing、query processing、LLM、prompt managementの4 moduleとvector databaseでRAG systemを構築。
### データ・実験
institutional antimicrobial protocolを用い、retrieval accuracy、System Usability Scale、user perception等で評価。
### 主な結果
SUS score 82、適切なantimicrobial protocolを83%でretrieval。
### 新規性
施設固有stewardship protocolを外部knowledgeとしてLLMへ直接grounding。
### 限界
single-institution guideline中心で、患者outcome改善や多施設clinical effectivenessは未確認。
### なぜ注目したか
RAGの医療応用として「正しいローカル規則へ従わせる」という用途が明確だから。

**Medical AI extra:** study_design=system development/evaluation; sample_size=abstractに明示なし; primary_endpoint=retrieval accuracy/usability; external_validation=なし; prospective_or_retrospective=not clearly specified in abstract.

---

## 15. Large Language Model-Based Clinical Decision Support for Antibiotic Selection and Dose Recommendation in Hospitalized Patients With Pneumonia: Multicenter Retrospective Study

- Source: PubMed
- canonical ID: pmid:42550965
- Publication date: 2026-08-04
- Authors: Yang Zhang, Li Li, Chunting Tan, Mengyuan Ji, Xican Tian, Xiangdong Mu, Jun Li, Yu Gu, Honglei Liu
- Journal: JMIR Medical Informatics
- URL: https://pubmed.ncbi.nlm.nih.gov/42550965/
- read_level: abstract
- Tags: medical AI, LLM, antibiotics, RAG, knowledge graph
- Summary: pneumonia入院患者で、類似症例retrieval + guideline knowledge graph + clinician rule constraintを組み合わせたLLMに抗菌薬選択とdose recommendationを行わせ、多施設外部validation。
- Why interesting: LLMを自由生成させず、clinical ruleとretrievalを組み合わせ、外部施設で性能を検証している。

### 目的
肺炎患者の抗菌薬選択・用量提案を制約付きLLMで支援し、cross-site generalizabilityを評価。
### 手法
dual-branch retrieval、guideline knowledge graph、clinician-defined rules、hybrid-context reasoning。DeepSeek-V3、GLM-4.6、GPT-4oを比較。
### データ・実験
中国2病院331患者。development 233、external validation 98。
### 主な結果
DeepSeek-V3 full pipelineはexternal validationで抗菌薬選択F1 0.8605 / Jaccard 0.8571、選択+用量ではF1 0.8503 / Jaccard 0.8469。rule triggerとevidenceも提示。
### 新規性
case retrieval、guideline KG、hard clinical constraintsを一つのmedication pipelineへ統合。
### 限界
2施設・肺炎に限定され、prospective prescribing impactや安全性は未評価。
### なぜ注目したか
医療LLM研究として外部validationとtraceable evidenceの両方があるため。

**Medical AI extra:** study_design=multicenter retrospective study; sample_size=331 (233 development, 98 external validation); primary_endpoint=antibiotic selection/dosing F1 and Jaccard; external_validation=yes, second-hospital cohort; prospective_or_retrospective=retrospective.

---

## 16. Reporting Quality of Large Language Model Studies: A Cross-Sectional Audit of High-Ranking Radiology and Medical Imaging Journals

- Source: PubMed
- canonical ID: pmid:42551868
- Publication date: 2026-08-04 (online ahead of print)
- Authors: Ismail Mese, Saime Turgut Gunes, Ozge Coskun, Ali Keles, Tuba Banaz, Muhammed Faruk Kazanbas, Burak Kocak
- Journal: Korean Journal of Radiology
- URL: https://pubmed.ncbi.nlm.nih.gov/42551868/
- read_level: abstract
- Tags: medical AI, LLM evaluation, reproducibility, reporting quality
- Summary: 2025年の上位radiology/imaging誌に掲載されたLLM研究102本をMI-CLEAR-LLMで監査し、再現性に必要な情報がどこまで報告されているか評価。
- Why interesting: LLM性能そのものではなく、研究結果を再現・比較できるレベルで報告されているかを定量化している。

### 目的
radiology LLM研究のreporting transparencyをMI-CLEAR-LLMで監査。
### 手法
Q1誌のeligible studiesをquota-based samplingし、複数reviewerのconsensusでchecklist adherenceを採点。
### データ・実験
201 eligible studies中102研究を最終分析。
### 主な結果
平均adherence 51.2%±14.7%。input data type 100%、test-data independence 80.2%に対し、prompt execution setup 29.4%、stochasticity management 33.1%、training-data cutoff date 9.8%、prompt wording rationale 15.6%。journal差p=0.011。
### 新規性
医療LLM研究の再現性不足を項目別・journal別に定量化。
### 限界
radiology/imaging Q1誌と2025年論文に限定。
### なぜ注目したか
LLM研究を読む際、scoreより先に何を報告すべきかを示す実務的なauditだから。

**Medical AI extra:** study_design=cross-sectional reporting audit; sample_size=102 studies; primary_endpoint=MI-CLEAR-LLM adherence; external_validation=not applicable; prospective_or_retrospective=retrospective literature audit.

---

## 17. Large language model-based simulated patient training for heart failure palliative care communication: a pilot study

- Source: PubMed
- canonical ID: pmid:42553746
- Publication date: 2026-07-22 (eCollection 2026 Aug)
- Authors: Risa Kishikawa, Hiroyuki Morita, Satoshi Kodera
- Journal: European Heart Journal - Digital Health
- URL: https://pubmed.ncbi.nlm.nih.gov/42553746/
- read_level: abstract
- Tags: medical education, LLM, simulated patient, palliative care
- Summary: advanced heart failureのpalliative care communicationを日本語LLM simulated patientで訓練し、自動framework-based feedbackを返すweb appのpilot評価。
- Why interesting: medical LLMを診断支援ではなく、反復可能な対話訓練環境として使う具体的応用。

### 目的
LLM simulated patientによるcommunication trainingのfeasibilityと自己効力感への初期signalを確認。
### 手法
single-armで1 sessionのLLM patient interactionとNURSE/SHARE等に基づくfeedbackを実施。
### データ・実験
10 sessions。平均7.6±2.0 dialogue turns。
### 主な結果
palliative communication knowledge +1.7（adjusted p<0.01）、confidence +1.2（adjusted p=0.03）。model response約3秒、feedback約17秒。
### 新規性
患者simulatorとstructured feedback generatorを同一LLM training appへ統合。
### 限界
10 sessions、controlなし、self-reported outcome中心。
### なぜ注目したか
低コストで繰り返せる医療コミュニケーション教育として実装距離が近い。

**Medical AI extra:** study_design=single-arm pilot; sample_size=10 sessions; primary_endpoint=change in self-efficacy; external_validation=no; prospective_or_retrospective=prospective interventional pilot.

---

## 18. Image-based evaluation of a commercial AI synthetic CT generator for brain and prostate MR-only radiotherapy

- Source: PubMed
- canonical ID: pmid:42547906
- Publication date: 2026 Aug
- Authors: Morgan Aire, Carson Matthews, Joshua Jones, David Duong, Christopher Schneider, Sotirios Stathakis, Olivia Shay, Krystal Kirby
- Journal: Journal of Applied Clinical Medical Physics
- URL: https://pubmed.ncbi.nlm.nih.gov/42547906/
- read_level: abstract
- Tags: medical imaging, synthetic CT, radiotherapy, commercial AI
- Summary: FDA 510(k) clearedのTheraPanacea synthetic CTをbrain/prostate MR-only planningで画像・幾何学的に評価。
- Why interesting: research prototypeでなくcommercial cleared AIを、implantやboneなど失敗しやすい条件まで含めて検証している。

### 目的
sCTのHU fidelityとgeometryをreference CTに対して定量評価。
### 手法
paired CT/MRからsCT生成し、soft tissue、bone、contour geometry、landmark、implantを比較。
### データ・実験
brain 20 + prostate 20患者、計40 retrospective cases。
### 主な結果
soft-tissue mean HU差<50 HU、central ROI多くで<20 HU。centroid shift<2 mm、MDA<5 mm、bony landmark<1 mm。一方bone HU compressionはfemoral head最大347±14 HU、sacrum455±50 HU、dental implantは約9000 HU過小評価。
### 新規性
commercial sCTの平均性能だけでなくimplant/bone failure modeを明確化。
### 限界
image-based evaluation中心で、institutional dosimetric validationは別途必要。
### なぜ注目したか
臨床導入前QAで「どこが危ないか」を具体的に示すため。

**Medical AI extra:** study_design=retrospective evaluation study; sample_size=40 patients; primary_endpoint=HU/geometric agreement; external_validation=明示なし; prospective_or_retrospective=retrospective.

---

## 19. AI-assisted VMAT planning incorporating deep learning-based dose prediction for head and neck cancer

- Source: PubMed
- canonical ID: pmid:42503595
- Publication date: 2026 Aug
- Authors: Seiji Tomori, Kakutaro Narazaki, Shun Tasaka
- Journal: Journal of Applied Clinical Medical Physics
- URL: https://pubmed.ncbi.nlm.nih.gov/42503595/
- read_level: abstract
- Tags: radiotherapy planning, deep learning, human-in-the-loop, head and neck cancer
- Summary: deep-learning dose predictionを使うRatoGuideでHNC VMAT planを作成し、複雑症例ではphysicistがhotspotを手修正するhuman-in-the-loop workflowを評価。
- Why interesting: 「完全自動化」ではなく、AIが苦手な不規則症例を人が補正する現実的運用を定量評価。

### 目的
HNCの典型・複雑解剖でAI-assisted planningのrobustnessとquality standardizationを評価。
### 手法
AI dose prediction→dose-derived ring contour→optimization。Dmax>115%ならplannerがmanual fine-tuning。
### データ・実験
11患者、12 VMAT plans。経験豊富なplannerのclinical planと比較。
### 主な結果
PTV coverageは同等でOAR sparing改善。spinal cord PRV Dmax 27.50→23.97 Gy。初期hotspot 3例は手修正でcriteria達成。planning time約2時間→30分。
### 新規性
AI planと人間介入の役割境界を複雑症例で明示。
### 限界
小規模単施設、prospective clinical outcome未評価。
### なぜ注目したか
human-in-the-loop medical AIの実際の時間短縮と安全補正が見えるため。

**Medical AI extra:** study_design=retrospective feasibility/planning comparison; sample_size=11 patients / 12 plans; primary_endpoint=dosimetric plan quality and planning time; external_validation=no; prospective_or_retrospective=retrospective.

---

## 20. Scanner-agnostic artificial intelligence approach for fast bone scintigraphy

- Source: PubMed
- canonical ID: pmid:42482648
- Publication date: 2026 Aug
- Authors: Vinicius de Oliveira Menezes, Cleiton Cavalcante Queiroz, Antônio Augusto Silva Oliveira, Aurílio José Dos Santos Filho, Allisson Francisco de Morais, Adriano de Oliveira Vigário, Maria Eduarda Flamini, Felipe Alves Mourato, Tsang Ing Ren, Marcos Antônio Dórea Machado
- Journal: Journal of Applied Clinical Medical Physics
- URL: https://pubmed.ncbi.nlm.nih.gov/42482648/
- read_level: abstract
- Tags: nuclear medicine, denoising, multicenter AI, prospective validation
- Summary: scanner-specific retrainingを不要にするadaptive-diffusion U-Netで、骨シンチのhalf-time / half-dose画像をreconstruct。multi-vendor retrospective dataに加え、未学習scannerを含むprospective validationを実施。
- Why interesting: 医療画像AIで重要なscanner/domain shiftを、未学習vendorを含むprospective testで正面から評価している。

### 目的
撮像時間・doseを半減してもdiagnostic image qualityを維持し、scannerごとの再学習を不要にする。
### 手法
U-Net backbone + trainable isotropic diffusion layer。10〜70% countへPoisson thinningして学習。
### データ・実験
retrospective 3,635 studies / 4 camera models、quantitative test 182 scans。prospective 60 patients、そのうち20はtraining未使用Philips BrightView。3 blinded physicians評価。
### 主な結果
50% countsでSSIM 0.903±0.045→0.963±0.032、PSNR 30.50±4.13→40.85±4.55 dB、LPIPS 0.05±0.01→0.03±0.01（p<0.001）。double-speed DL imageのLikert 4.4±0.7 vs standard 4.5±0.5、診断discrepancyなし。
### 新規性
multi-vendor + unseen scanner prospective validationを伴うscanner-agnostic denoising。
### 限界
prospective cohortは60人で、長期workflow・rare pathologyへの一般性は追加検証が必要。
### なぜ注目したか
医療AIのexternal generalizationをかなり実践的な形で検証しているため。

**Medical AI extra:** study_design=multicenter retrospective development + prospective validation; sample_size=3,635 retrospective, 182 quantitative test, 60 prospective (20 unseen scanner); primary_endpoint=image quality / diagnostic fidelity; external_validation=yes, unseen scanner and multi-vendor; prospective_or_retrospective=both.

---

<!-- PAPER_IDS -->
arxiv:2608.27455
arxiv:2608.27454
arxiv:2608.27448
arxiv:2608.27420
arxiv:2608.27409
arxiv:2608.27402
arxiv:2608.27397
arxiv:2608.27395
arxiv:2608.27391
arxiv:2608.27370
arxiv:2608.27351
arxiv:2608.27348
pmid:42560867
pmid:42561260
pmid:42550965
pmid:42551868
pmid:42553746
pmid:42547906
pmid:42503595
pmid:42482648
<!-- /PAPER_IDS -->
