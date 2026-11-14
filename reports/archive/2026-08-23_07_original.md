# [paper-report] 2026-08-23 ML / LLM / Medical AI — latest-count v2

- Issue: #7
- Source: https://github.com/drkamoshika/papers/issues/7
- Created at: 2026-08-23T07:08:42Z

# Paper Watch Report — 2026-08-23

## 今回の概況

`config/paper_watch.yml` version 2 に従い、今回は固定日数ではなく、**arXiv / PubMed それぞれについて関連する最新候補を新しい側から10件ずつ確認**した。候補取得後に `state/seen_papers.txt` のcanonical IDで既出を除外し、技術的な内容・新規性・テーマのバランスを見て最終的に13本を採用した。

arXivでは、categoryの `recent/new` 一覧だけに依存せず、検索で最新候補を発見し、採用候補は個別arXivページでmetadataとabstractを確認した。今回の新着では、agent memory、tool use、post-training、model routing、semantic cacheなど、LLMを「単体モデル」ではなく長期運用するための設計が目立つ。また医療AIでは、患者向け医療レポート解釈、EHR foundation-style modeling、医療画像再構成、精神健康評価など、実運用を意識した研究が多い。

各論文は、以前の読みやすい **Tags / Summary / Why interesting** を先に置き、その後に詳細版の **目的 / 手法 / データ・実験 / 主な結果 / 新規性 / 限界 / なぜ注目したか** を併記する。

## 実行条件

- Sources: arXiv / PubMed
- Candidate retrieval: latest 10 per source, newest first
- Candidate window: 日数制限なし
- Max final papers: 20
- Selected papers: 13
- Deduplication: `state/seen_papers.txt`
- Read level: 今回はすべて abstract（PubMedの一部は公開抄録・PMC情報を併用）

---

# arXiv

## 1. G-CARL: Grounded Checklist-Aligned Reward Learning for Patient-Oriented Medical Report Interpretation

- Source: arXiv
- canonical ID: arxiv:2608.20331
- Published: 2026-08-20
- Authors: Shiao Xie, Siyu Chen, Jianwei Lv, Bo Yuan, Yujin Wang, Xiandong Li
- Category: cs.CL, cs.AI
- URL: https://arxiv.org/abs/2608.20331
- read_level: abstract
- Tags: medical AI, multimodal LLM, reinforcement learning, patient communication
- Summary: 患者が医療レポートを理解するためのopen-ended multimodal taskを定義し、医学的事実性と患者ごとの要求充足を同時に最適化するG-CARLを提案。multi-source retrievalによるclaim verificationと、instance-specific checklistをrewardとして組み合わせる。
- Why interesting: 医療LLMを単なる診断QAではなく、「正確で、患者に合わせて説明する」実運用タスクとして定式化している点が重要。

### 目的
患者向け医療レポート解釈では、医学的に正しいだけでなく、質問内容や会話履歴に応じて分かりやすく説明する必要がある。この二つを同時に満たす学習枠組みを作る。

### 手法
Patient-oriented Medical Report Interpretation (PMRI)を新タスクとして定義。G-CARLはmulti-source retrievalでatomic claimを検証し、患者の要求に合わせたweighted checklistでcoverageを評価するreward learningを行う。

### データ・実験
実世界データに基づくMMedReport benchmarkを構築し、clinician-designedの3次元評価プロトコルで既存post-training手法と比較。

### 主な結果
abstractでは、overall quality、claim-level precision、checklist recallで既存post-training baselineを一貫して上回り、臨床家のpairwise preferenceでもより正確かつ患者ニーズに合うと報告。

### 新規性
factualityと患者個別のcommunicative alignmentを、異なる検証可能性を持つreward signalとして分離しながらjoint optimizationする点。

### 限界
abstractからは、実臨床で患者が直接利用した場合の安全性、長期的な理解度や意思決定への影響までは確認できない。

### なぜ注目したか
医療AIで重要な「正しさ」と「患者向け説明」を同時に扱う、臨床導入に近いpost-training設計だから。

**Medical AI extra:** study_design=model/benchmark development; external_validation=abstract上では明確な外部臨床validationなし。

---

## 2. Pandora's AI Model Routing Box: Efficient Allocation with Costly Value Estimation

- Source: arXiv
- canonical ID: arxiv:2608.20316
- Published: 2026-08-20
- Authors: Adam Fisch, Shubhendu Trivedi, Fantine Huot, William W. Cohen, Michael Kaisers, Mirella Lapata, Kate Larson, Jacob Eisenstein
- URL: https://arxiv.org/abs/2608.20316
- read_level: abstract
- Tags: model routing, inference efficiency, value of information, multi-model systems
- Summary: 複数のAIモデルや推論設定から、どれにqueryを割り当てるかというrouting問題を「価値推定そのものにもコストがかかる」Pandora's Box問題として定式化。高価な評価器を必要な場合だけ呼ぶrouting policyを導出する。
- Why interesting: model routingの問題を「どのモデルが強いか」だけでなく、「それを見積もるためにいくら払うか」まで含めて最適化している。

### 目的
specialist modelを使い分けるheterogeneous AI systemで、routing qualityを維持しながらvalue estimationのコストを減らす。

### 手法
Gaussian signal model下でvalue-of-informationを閉形式で計算するPandora's Routerを提案。さらに各specialistが自己評価コストを払うか決めるdecentralized版Pandora's Bidderを設計。

### データ・実験
multi-LLM benchmark、retrieval-augmented specialist、inference-time reasoning量の異なるLLMという3domainで評価。

### 主な結果
Pandora's Routerはexhaustive estimationに近いrouting qualityを維持しながら、高価なestimatorの問い合わせ回数を大幅に削減したと報告。

### 新規性
routing前の「性能予測」自体をcostly inspectionとして扱い、情報価値で評価精度と計算費用を選択する点。

### 限界
Gaussian signalなどの仮定が実際の複雑なrouterにどこまで適合するか、abstractだけでは不明。

### なぜ注目したか
複数モデル・複数推論強度を使い分けるagentic systemが増える中、運用コストを理論的に扱う実用性の高い研究。

---

## 3. Explainable Transformer Models for Clinical Prediction Tasks on Structured Electronic Health Records

- Source: arXiv
- canonical ID: arxiv:2608.20315
- Published: 2026-08-20
- Authors: Jun Ni Du, Lukas Adamek, Maxim Kryukov, Flavio Dormont, Ziv Bar-Joseph, Sven Jager, Brandon Rufino
- Category: cs.LG
- URL: https://arxiv.org/abs/2608.20315
- read_level: abstract
- Tags: medical AI, EHR, transformer, explainability
- Summary: 75 million patientsのde-identified EHRでpretrainしたBERT-LERを提案。検査値をpercentile binningでtoken化し、Integrated Gradientsで入力event単位の説明を付ける。
- Why interesting: EHR foundation modelで、数値laboratory dataの扱いと説明可能性を一つのframeworkに統合している。

### 目的
structured EHR predictionで、検査値の定量情報を失わず、かつ予測根拠を臨床eventレベルで説明できるモデルを作る。

### 手法
BERT-style timeline modelにlaboratory valueのpercentile-based tokenizationを導入。Integrated Gradientsを用いてtoken-level attributionを生成する。

### データ・実験
75 million patientsのde-identified EHRでpretraining。public EHRShot benchmarkとreal-world asthma severity progression studyで評価。

### 主な結果
EHRShotとasthma taskで公開benchmark modelと競合し、laboratory-related taskではしばしば上回った。attributionは既知のclinical risk factorと整合したと報告。

### 新規性
EHR sequence modelingで、laboratory value representationとinput-grounded explainabilityを同時に扱う点。

### 限界
大規模pretraining dataの施設・患者populationへの依存、説明のcausal validity、prospective clinical impactはabstractでは未確認。

### なぜ注目したか
医療AIの実装では予測精度だけでなく説明可能性が重要であり、非常に大規模なEHR pretrainingと組み合わせているため。

**Medical AI extra:** study_design=model development + benchmark/real-world retrospective evaluation; sample_size=pretraining 75 million patients; external_validation=public EHRShotを使用するが臨床prospective external validationとは別。

---

## 4. MidTool: Mid-training Data Synthesis for Agentic Tool Use

- Source: arXiv
- canonical ID: arxiv:2608.20314
- Published: 2026-08-20
- Authors: Fengqing Jiang, Yite Wang, Boyi Liu, Zhaoyang Wang, Canwen Xu, Zhewei Yao, Radha Poovendran, Yuxiong He
- URL: https://arxiv.org/abs/2608.20314
- read_level: abstract
- Tags: LLM agent, tool use, mid-training, MCP
- Summary: API、MCP skill、document workflowなどからtool-use supervisionを合成するMidTool-Mixを作り、Qwen3 4B/8Bをmid-training。その後SFT/RLを行うと、BFCL、tau2-Bench、MCP Universeでbaselineより改善した。
- Why interesting: tool useをpost-trainingだけに任せず、mid-training段階で獲得すべき基礎能力として扱っている。

### 目的
LLM agentのgeneral tool use能力を、post-training以前のmid-training段階で体系的に形成できるか検証する。

### 手法
web/PDF/codeに加え、real-world tool APIs、MCP skills、document-grounded workflowからtraining dataを構築。tool affordance recognition、argument grounding、tool-call composition、incomplete information recoveryを学習する。

### データ・実験
Qwen3-4B-Base / 8B-BaseをMidTool-Mixでmid-trainし、その後SFTとRL。BFCL、tau2-Bench、MCP Universeで評価。

### 主な結果
SFT/RLの両post-training設定でbaselineより一貫してdownstream tool-use performanceが向上したと報告。

### 新規性
agentic tool use向けの専用mid-training corpus constructionを、MCPまで含む現実的tool surfaceで構築した点。

### 限界
abstractではdata contamination、実際の長期agent workflowでのfailure recovery、tool security面の評価は不明。

### なぜ注目したか
MCPを含むtool ecosystemが広がる中、agent能力をどのtraining stageで獲得させるかという重要な設計問題を扱うため。

---

## 5. Phantom Gains: Auditing Self-Improvement Against a Measured Null

- Source: arXiv
- canonical ID: arxiv:2608.20290
- Published: 2026-08-20
- Authors: Cheng Xu, Nan Yan, Liming Chen, M-Tahar Kechadi
- Category: cs.AI, cs.CL
- URL: https://arxiv.org/abs/2608.20290
- read_level: abstract
- Tags: self-improvement, LoRA, evaluation, statistical auditing
- Summary: Qwen3-8Bの3 roundsのLoRA self-trainingを、同一pipelineを通すfrozen controlと比較し、「個々の問題を獲得/喪失した」というself-improvement評価が測定ノイズで簡単に作られることを示す。
- Why interesting: self-improving AIの研究で、平均scoreではなくtransition-level analysisを使う際に、control nullが必須だと強く警告している。

### 目的
model self-improvementの細粒度評価で観測されるgain/lossが、本当の能力変化なのか測定artifactなのかを検証する。

### 手法
rank-32 LoRA self-trainingをfrozen controlと同一pipelineで比較。single greedy decodeなど7種類のmeasurement failureを監査し、pooled baselineに対するper-problem exact test + FDR controlを提案。

### データ・実験
Qwen3-8B、複数self-training / external distillation arm、held-out replicateを使ったpre-registered audit。

### 主な結果
controlなしでは複数の指標が誤ったself-improvementを示した。提案exact testではheld-out controlで偽陽性を検出せず、external distillationの一部gainはself-trainingと異なるpatternを示した。

### 新規性
self-improvement評価の「null」を別実験ではなく、同一study内のfrozen baseline replicateから直接測るaudit framework。

### 限界
Qwen3-8Bや特定self-training regimeでの結果が、より大規模model・別taskへどこまで一般化するかは未確認。

### なぜ注目したか
AIがAIを改善する研究では評価artifactを能力向上と誤認するリスクが高く、その検証設計そのものを扱うため。

---

## 6. Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization

- Source: arXiv
- canonical ID: arxiv:2608.20281
- Published: 2026-08-20
- Authors: Qian Kou, Xiaofeng Shi, Xiaosong Qiu, Hua Zhou
- Category: cs.CL, cs.AI
- URL: https://arxiv.org/abs/2608.20281
- read_level: abstract
- Tags: post-training, knowledge internalization, retrieval-free QA, continual learning
- Summary: 固定document corpusをparametric knowledgeとして内部化するため、Inject→Align→Recoverの3段階post-trainingを提案。domain QAを上げつつgeneral capabilityを回復する。
- Why interesting: RAGではなく「知識そのものをmodelへ入れる」場合に、domain adaptationとgeneral能力維持のtrade-offを明示的に分解している。

### 目的
bounded document collectionをretrievalなしで答えられるようにmodel内部へ取り込みつつ、general capabilityの劣化を抑える。

### 手法
Injectでcontinuation/rewrite/instruction-conditioned reconstruction、Alignでanswer-only QA、Recoverでdomain-adapted modelとbase instruction modelをmerge。

### データ・実験
Common Corpus / CCI、Llama / Phi / Qwen / SmolLM familyで比較。

### 主な結果
main comparisonでは8つのdataset-model settingのうち7つでVanilla SFTを4 metricすべてで上回り、平均domain QA +3.6 points、general performance +12.1 pointsを報告。

### 新規性
knowledge injection、behavior alignment、general ability recoveryを別stageに分離したpost-training design。

### 限界
固定corpus internalizationは更新頻度が高いknowledgeやprovenance要求にはRAGより不利な可能性があるが、abstractではその運用trade-offは十分扱われていない。

### なぜ注目したか
「RAGかfine-tuningか」の中間にある、document knowledgeを安全にparametric化する設計として実用的。

---

## 7. Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads, Capacities, and Encoders

- Source: arXiv
- canonical ID: arxiv:2608.20280
- Published: 2026-08-20
- Authors: Yash Kulkarni, Shubham Harkare, Arvind Suresh Yogesh Babu
- Category: cs.DB, cs.LG
- URL: https://arxiv.org/abs/2608.20280
- read_level: abstract
- Tags: semantic cache, LLM inference, efficiency, retrieval
- Summary: FIFO/LRU/LFU/ARC/GDSFなど7種類のsemantic cache eviction policyを18設定で比較。LFUが最も強い単純defaultだが、より大きな問題は「semantic hitの多くが実際にはanswer-substitutableでない」ことだと示す。
- Why interesting: cache hit rateが高くても実際の再利用可能率は非常に低い可能性を定量化しており、LLM servingの評価指標そのものを見直す研究。

### 目的
LLM semantic cacheでどのeviction policyが有効か、統一protocolで比較する。

### 手法
CLEVER frameworkでFIFO, LRU, LFU, ARC, GDSF, streaming SISO, semantic-redundancy policyを3 corpora × 3 capacities × 2 encodersで評価。

### データ・実験
18 settings。さらにcache hitが本当にanswer-substitutableか品質監査。

### 主な結果
どのpolicyもLFUを最大0.041 percentage points以上改善できなかった。一方、raw hit rate 51–60%がquality-adjustedでは1.1–2.2%まで低下するsettingを確認。

### 新規性
eviction algorithmの微差より、semantic hit validityの方が支配的という評価視点。

### 限界
使用corpus・threshold・encoderに依存するため、production trafficでの再現性は追加検証が必要。

### なぜ注目したか
agent/LLM servingのtoken cost最適化でsemantic cacheは有望だが、dashboard上のhit rateをそのまま価値とみなせないことを示すため。

---

## 8. Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents

- Source: arXiv
- canonical ID: arxiv:2608.20274
- Published: 2026-08-20
- Authors: Yiyang Feng, Biddut Sarker Bijoy, Niranjan Balasubramanian, Jiawei Zhou
- URL: https://arxiv.org/abs/2608.20274
- read_level: abstract
- Tags: LLM agent, skill memory, transfer learning, long-term memory
- Summary: agentが過去taskから誘導したskillを再利用する際、whole-task skillはno-memory baselineより悪化しやすい一方、subtask-levelかつtext形式のskillは平均的にtransferを改善した。
- Why interesting: 「memoryをretrievalできる」ことと「memoryが役に立つ」ことは別で、skillの粒度と表現形式がtransferabilityを左右すと示す。

### 目的
LLM agentがexperienceから生成したskillが、別taskへいつ有効にtransferするのかを体系的に調べる。

### 手法
task-level vs subtask-level、text vs codeの2軸でskill inductionを比較。specificityとabstractnessを組み合わせたskill utility scoreも提案。

### データ・実験
複数task間でinduced skillをtransferし、no-memory baselineと比較。

### 主な結果
task-level skillは多くの場合performanceを低下させ、subtask-level skillは平均的に改善。text skillはcode skillよりtransferしやすい。utility scoreはtask executionなしでもsuccessと相関。

### 新規性
memory retrieval性能ではなく、skill representationのtransfer utilityを事前診断するmetricを提案した点。

### 限界
abstractからは非常に長期のskill accumulationでutility scoreが維持されるか、skill間conflictをどう扱うかは不明。

### なぜ注目したか
長期agentのknowledge/skill memory設計に直結し、単純に過去experienceを貯めればよいわけではないことを示しているため。

---

# PubMed

## 9. Deep learning image reconstruction improves visualization of arterial phase hyperenhancement and washout appearance on dual-energy CT for hepatocellular carcinoma: a non-inferiority study

- Source: PubMed
- canonical ID: pmid:42550187
- Published: 2026-08-04 (online ahead of print)
- Authors: Baiming Wu, Jin Cui, Yan Lei, Meiqi Wan, Zhixi Luo, Yunxuan Xie, Jinran Chen, Enming Cui
- Journal: Abdominal Radiology
- URL: https://pubmed.ncbi.nlm.nih.gov/42550187/
- read_level: abstract
- Tags: medical imaging, deep learning reconstruction, dual-energy CT, hepatocellular carcinoma
- Summary: HCCのdual-energy CTでDLIRを使い、low-energy VMIの画質とLI-RADS主要所見の視認性を改善。DLIR-H/50-keVが最適で、APHEとwashout検出はMRIに対してnon-inferiorとされた。
- Why interesting: AIを診断分類器としてではなく、画像再構成そのものに使い、MRIが使いにくい状況でCTの臨床価値を上げようとしている。

### 目的
DLIR-based DECTがHCC評価の画像品質と主要LI-RADS所見の可視化を改善できるか検証する。

### 手法
single-center retrospective analysis of a prospective cohort。40/50/60/74-keV VMIをASiR-V、DLIR-H、DLIR-Mで再構成し、objective/5-point subjective metricsを比較。最適protocolをMRIとnon-inferiority比較。

### データ・実験
2024年6月〜2025年7月登録患者。各患者につき3 phase × 各energy/algorithm combinationで36 image sets。

### 主な結果
DLIR-H/50–60-keVがobjective metricで最良。DLIR-H/50-keVがoptimal protocolとなり、APHEとnonperipheral washout検出でMRIに対するnon-inferiorityを示した。

### 新規性
deep learning reconstructionとdual-energy low-keV imagingを組み合わせ、HCCの診断的visual featureまでMRIと比較した点。

### 限界
single-centerで、abstractではsample sizeが明示されていない。MRI代替としての広範なgeneralizationにはmulticenter validationが必要。

### なぜ注目したか
医療AIをworkflowの一部として実装しやすい「画像再構成」に適用し、臨床的endpointへ接続しているため。

**Medical AI extra:** study_design=single-center retrospective analysis of prospective cohort; primary_endpoint=image quality + LI-RADS feature visualization; external_validation=no; prospective_or_retrospective=retrospective analysis。

---

## 10. Large language model applications for real-time clinical mental health assessment: Current potential and future directions

- Source: PubMed
- canonical ID: pmid:42545345
- Published: 2026-08-03 (online ahead of print)
- Authors: Katie Aafjes-van Doorn, Francine Cheng Ty, Antonia Yuxin Hua, Chunlin An, Anna Van Meter
- Journal: Journal of Psychopathology and Clinical Science
- URL: https://pubmed.ncbi.nlm.nih.gov/42545345/
- read_level: abstract
- Tags: medical LLM, mental health, clinical assessment, scoping review
- Summary: LLMが患者と直接対話してscreening/diagnosis/symptom monitoringを行う研究をpreregistered scoping reviewで整理。該当したのは10研究のみで、structured interview、domain adaptation、clinical reference standardを使う研究ほど良い傾向だった。
- Why interesting: 医療LLMの中でも「医師向けQA」ではなく、患者との継続的なassessment interfaceという用途を扱う。

### 目的
LLMによるdirect mental health assessmentの現状、独自の強み、臨床利用へ向けた研究課題を整理する。

### 手法
中国語・英語文献を含むpreregistered scoping review。screening、diagnosis、symptom monitoringでLLMが患者/参加者を直接評価する研究を対象。

### データ・実験
criteriaを満たした研究は10件。4件がdiagnostic interviewing/classification、5件がsymptom/severity assessment、1件がmultimodal depression assessment。

### 主な結果
evidenceはrecentかつheterogeneous。structured interviewing logic、domain-specific adaptation、clinically anchored reference standardsを使うtoolで比較的強いperformanceが報告されたが、validationは限定的。

### 新規性
LLMのmental health利用を、一般的なchatbotやtherapy supportではなくdirect clinical assessmentに限定してレビューしている。

### 限界
研究数が10件と少なく、early-stage/nonjournal publicationが多い。現時点ではclinical evaluationのreplacementではなくsupport toolと位置づけられる。

### なぜ注目したか
LLMがreal-time / longitudinal assessmentへ向かう際の現在地とvalidation不足を明確に示しているため。

**Medical AI extra:** study_design=preregistered scoping review; sample_size=10 studies; external_validation=review対象研究では限定的。

---

## 11. Deep learning maps local brain aging in relation to cognition across human adulthood

- Source: PubMed
- canonical ID: pmid:42546187
- Published: 2026-08-03 (Epub; issue 2026-08-11)
- Authors: Nikhil N Chaudhari, Owen M Vega Huerta, Samayan Bhattacharya, Nahian F Chowdhury, Andrei Irimia; Alzheimer's Disease Neuroimaging Initiative
- Journal: PNAS
- URL: https://pubmed.ncbi.nlm.nih.gov/42546187/
- read_level: abstract
- Tags: deep learning, neuroimaging, brain age, Alzheimer's disease
- Summary: global brain ageを単一値で出す代わりに、T1 MRIからvoxel-level local brain ageを推定。14,748人の認知正常者で学習し、MCI/ADではfrontotemporal領域のaccelerated agingが進行することを示した。
- Why interesting: black-boxなglobal scoreから、解剖学的にどこが老化しているかを可視化できるbiomarkerへ進めている。

### 目的
global brain ageでは隠れるregional aging patternを推定し、認知機能やAD progressionとの関連を調べる。

### 手法
T1-weighted MRIからvoxel-level local brain age (LBA)を推定するdeep-learning architectureを構築。

### データ・実験
multiple sitesのcognitively normal 14,748 participantsでtraining。MCIとAD cohortに適用し、regional agingとcognitionを比較。

### 主な結果
正常成人でもfrontal/temporal lobesがparietal/occipitalより相対的にadvanced agingを示し、MCI→ADでfrontotemporal agingが進行。AD vulnerabilityの高い領域のLBA deviationがcognitive performanceと関連。

### 新規性
brain ageをvoxelwiseにlocalizeし、neuroanatomical agingとfunctional outcomeを結びつけた点。

### 限界
MRI cohort/scan protocol依存や、clinical prospective predictionとしてのutilityはabstractでは未確認。

### なぜ注目したか
医療画像AIの出力を解釈可能なspatial biomarkerへ近づけており、AD早期評価への応用可能性がある。

**Medical AI extra:** study_design=multisite imaging model development/validation; sample_size=14,748 cognitively normal participants for training; prospective_or_retrospective=observational imaging analysis。

---

## 12. Personalized Prediction of Acute and Chronic Postsurgical Pain — the role of Multidomain Biosignatures, Machine Learning-Based Integration, and Standardized Outcome Definitions

- Source: PubMed
- canonical ID: pmid:42543469
- Published: 2026-08-03
- Authors: Georg Winter, Richard D. Urman, Markus M. Luedi, Andrea Stieger
- Journal: Current Pain and Headache Reports
- URL: https://pubmed.ncbi.nlm.nih.gov/42543469/
- read_level: abstract
- Tags: machine learning, pain prediction, personalized medicine, clinical risk
- Summary: postsurgical pain predictionの現状をreviewし、単一risk factorや既存multivariate modelでは個人risk stratificationに不十分と整理。multidomain biosignatureとML integrationを今後の重要方向として挙げる。
- Why interesting: 医療MLでありがちな「予測モデルを作る」より前に、どのmodalitiesを統合しどうclinical actionへつなげるかという設計問題を強調している。

### 目的
acute/chronic postsurgical painのpersonalized predictionについて、既存modelの限界と今後必要なmethodologyを整理する。

### 手法
narrative review。clinical、psychological、psychophysical、surgical predictorとmultivariate prognostic modelを概観。

### データ・実験
review articleのため独自patient cohortなし。

### 主な結果
個別predictorは十分でなく、既存multivariate modelも最大でmoderate discrimination、high risk of bias。APSP/CPSPともexternally validated predictive modelは現時点で存在しないと整理。

### 新規性
multidomain biosignature、ML integration、standardized outcome definitionを一つのpersonalized prediction frameworkとして位置づける。

### 限界
narrative reviewであり、新規modelのvalidation studyではない。提案方向の有効性は今後のprospective studyが必要。

### なぜ注目したか
医療AIで重要な「モデル性能」から「臨床で介入可能なrisk stratification」へのギャップを明確にしているため。

**Medical AI extra:** study_design=narrative review; external_validation=既存モデルには外部validationなしと報告。

---

## 13. A Machine Learning and Large Language Model Tool for Systematic Literature Reviews of Health Economic Evidence: A Validation Study

- Source: PubMed
- canonical ID: pmid:42525208
- Published: 2026-07-29 (online ahead of print)
- Authors: Lisa M Bloudek, Allie B Cichewicz, Kush Patel, Sean D Sullivan, Kevin M Kallmes
- Journal: Pharmacoeconomics
- URL: https://pubmed.ncbi.nlm.nih.gov/42525208/
- read_level: abstract
- Tags: LLM, machine learning, systematic review, health economics
- Summary: health economic systematic reviewをML screener + LLM criteria screenerで再現。title/abstract screeningは95%以上のaccuracyだったが、full-text screeningは80%未満に落ち、複雑なmodel structureのdata extractionも弱かった。
- Why interesting: LLMを研究workflowへ入れた際、どの工程は自動化でき、どこは人間validationが必要かを具体的な数字で示している。

### 目的
economic evaluationのsystematic literature reviewでAI-assisted search/screening/extractionの効率とaccuracyを検証する。

### 手法
既存のmanual SLRを、ML-based Robot ScreenerとLLM-based Smart Screenerを含むNested Knowledge platformで再現し、人間による元レビューと比較。

### データ・実験
元SLRのPubMed article 43件を基準に評価。screening、full-text判定、data extraction、time savingを比較。

### 主な結果
AI searchは元SLRのPubMed 43件中22件（51%）をretrieval。title/abstract screening accuracy >95%、full-text screening <80%。time savingはdata extractionで約20%、title/abstract screening/searchで最大約60%。

### 新規性
clinical trialではなく、表現が不均一で解釈依存度の高いhealth-economic model reviewでAI workflowを実務的にvalidationした点。

### 限界
commercial platform評価で利益相反があり、単一review replication。complex modeling assumptionの抽出・解釈では依然human oversightが必要。

### なぜ注目したか
LLM agentに論文調査を任せる今回の仕組み自体にも直結し、「abstract screeningは強いがfull-text解釈は難しい」という境界を定量的に示しているため。

**Medical AI extra:** study_design=validation study; sample_size=manual SLRの43 PubMed articlesを基準; external_validation=single replicated review。

---

## 今回のまとめ

今回の方式では、日付windowに依存せずsourceごとの最新候補を一定件数見るため、arXiv list pageのcacheやPubMedのissue date / Epub dateのずれに引っ張られにくくなる。一方で、毎回同じ最新候補が残る可能性があるため、`seen_papers.txt` のcanonical ID除外は引き続き重要。

サマリ形式については、短い `Summary / Why interesting` が一覧性を担保し、その後の詳細セクションが研究内容を後から読み返すためのknowledgeとして機能する。この二層構造を今後の標準形式とする。

<!-- PAPER_IDS -->
arxiv:2608.20331
arxiv:2608.20316
arxiv:2608.20315
arxiv:2608.20314
arxiv:2608.20290
arxiv:2608.20281
arxiv:2608.20280
arxiv:2608.20274
pmid:42550187
pmid:42545345
pmid:42546187
pmid:42543469
pmid:42525208
<!-- /PAPER_IDS -->
