# [paper-report] 2026-09-01 ML / LLM / Medical AI

- Issue: #10
- Source: https://github.com/drkamoshika/papers/issues/10
- Created at: 2026-09-01T06:24:01Z

# Paper Watch Report — 2026-09-01

## 今回の概況

`config/paper_watch.yml` version 2 を正本として実行した。`state/seen_papers.txt` の既出canonical IDを除外し、arXiv / PubMedそれぞれで最新側の関連候補を探索した。

今回のarXiv探索では、検索インデックスから既出IDより新しい候補を個別arXivページまで確実に検証できなかった。設定では「recent/new一覧だけを信用せず個別ページで検証する」ことが必須なので、推測でarXiv論文を補完していない。一方、PubMedでは未読の原著・実装研究を複数確認できたため、技術的内容と臨床的含意を優先して10本を採用した。

今回目立ったテーマは、(1) LLMをEHRや救急・周術期workflowに組み込む臨床実装、(2) multimodal / multi-agentによる患者コミュニケーションやrisk prediction、(3) RAGを用いた診断支援のtask-specificな限界、(4) LLM推論効率のKV-cache最適化、(5) machine learningによる生理信号・空間疫学予測である。

- Sources searched: arXiv / PubMed
- Candidate retrieval: latest relevant candidates, newest first, up to 15 per source
- Deduplication: `state/seen_papers.txt`
- Selected papers: 10
- arXiv selected: 0（新規候補を個別一次ページまで確実に検証できず）
- PubMed selected: 10
- Read level: すべて abstract

---

## 1. Subgroup Differences in Agreement Between an Algorithm Guided Large Language Model and Routine Emergency Department Triage

- Source: PubMed
- canonical ID: pmid:42642916
- Publication date: 2026-08-26
- Authors: Ali Halıcı, Ezgi Cesur, Fikret Çelik
- Journal: Medical Science Monitor
- URL: https://pubmed.ncbi.nlm.nih.gov/42642916/
- read_level: abstract
- Tags: emergency medicine, triage, LLM, safety, subgroup analysis
- Summary: 1,960件の成人救急受診で、標準化promptからLLMに5段階triageを割り当てさせ、routine ED triageとの一致度とsubgroup差を評価した。5段階accuracyは71.3%、weighted κ=0.824。urgent/non-urgentではAUC 0.768、sensitivity 0.630、specificity 0.906だった。
- Why interesting: 単純な平均精度ではなく、年齢・糖尿病・外傷などで「低くtriageしてしまう」discordanceが偏る点を示しており、臨床LLMの安全性評価として実務的。

### 目的
救急triageでLLMをdecision supportとして使う場合、routine triageとの一致だけでなく、患者subgroupごとのdiscordanceが安全上問題にならないかを調べる。

### 手法
1960成人ED visitを後ろ向き解析。年齢、性別、主訴、comorbidity、vital signs、GCSを入力し、LLMがEmergency Severity Indexベースの5段階categoryを出力。routine triageと比較した。

### データ・実験
single-system retrospective study、n=1,960。urgent/non-urgent classificationと5-level agreementを評価し、lower/higher acuity discordanceをprespecified subgroupで解析。

### 主な結果
5-level accuracy 71.3%、weighted κ=0.824。urgent/non-urgent AUC 0.768、sensitivity 0.630、specificity 0.906。LLMのlower-acuity discordance 9.8%、higher-acuity discordance 18.9%。lower-acuity assignmentは高齢者、trauma、diabetesで多かった。

### 新規性
LLM triageの評価をglobal accuracyからsubgroup-specific safety discordanceへ広げた点。

### 限界
routine triage自体がgold standardではなく、local practiceとのagreementを測っている。prospective outcome validationが未実施。

### なぜ注目したか
医療AIの公平性・安全性で重要な「どの患者群で外しやすいか」を具体的に示しているため。

**Medical AI extra:** study_design=retrospective; sample_size=1,960 ED visits; primary_endpoint=triage agreement / urgent classification performance; external_validation=なし; prospective_or_retrospective=retrospective.

---

## 2. A bimodal large language model reduces misalignment in patient education: A double-blinded randomized trial

- Source: PubMed
- canonical ID: pmid:42607666
- Publication date: 2026-08-17
- Authors: Peixing Wan et al.
- Journal: Med
- URL: https://pubmed.ncbi.nlm.nih.gov/42607666/
- read_level: abstract
- Tags: multimodal LLM, patient education, audio, randomized trial, communication
- Summary: textだけでなくaudio cueも統合するbimodal LLM「Dolphin」を構築し、16,583 patient education cases由来64,200 utterancesで評価。555患者のdouble-blind randomized trialでは、text-only LLMより満足度、suggestion acceptance、proactive disclosureが高く、7日以内のunplanned recontactも少なかった。
- Why interesting: 「医療LLMは言語が正しければよい」ではなく、音声に含まれる感情cueまで使ってmisalignmentを減らすという、multimodal clinical communicationの強い実証研究。

### 目的
text-only LLMが見落とす非言語的感情情報をaudioから取り込み、患者教育でのemotional / semantic misalignmentを減らせるか検証する。

### 手法
text+audioのDolphinを構築し、emotion recognition、semantic consistency、ablation、expert rating、double-blind randomized trialでtext-only comparatorと比較。

### データ・実験
64,200 utterances、16,583 cases、6 departments、3 centers。randomized trialは555 patients。

### 主な結果
text-only LLMではemotional misalignment 36.7%、semantic misalignment 28.3%。Dolphinはemotion recognition 0.886 vs 0.713、semantic consistency 84.9% vs 82.1%。RCTでは満足度98.6% vs 93.8%、suggestion acceptance 76.1% vs 58.9%、proactive disclosure 44.6% vs 26.5%、7-day unplanned recontact 12.9% vs 22.9%。

### 新規性
患者教育LLMにaudio-derived nonverbal signalを組み込み、communication outcomeまでrandomized trialで評価した点。

### 限界
特定言語・医療環境での研究で、他地域・疾患・長期outcomeへの一般化は未確認。

### なぜ注目したか
multimodal LLMが臨床価値を生む具体例として、benchmarkではなく患者level outcomeを示しているため。

**Medical AI extra:** study_design=double-blind randomized trial + model development; sample_size=64,200 utterances / 16,583 cases, trial n=555; primary_endpoint=alignment and patient-education outcomes; external_validation=3-center evaluation; prospective_or_retrospective=prospective randomized componentあり.

---

## 3. A large language model-driven multidisciplinary AI agent system predicts delirium in emergency critically ill patients

- Source: PubMed
- canonical ID: pmid:42594876
- Publication date: 2026-08-13
- Authors: Wen Shang, Tongyue Shi, Qingbian Ma, Guilan Kong
- Journal: Cell Reports Medicine
- URL: https://pubmed.ncbi.nlm.nih.gov/42594876/
- read_level: abstract
- Tags: multi-agent, delirium, emergency medicine, RAG, risk prediction
- Summary: DeLiriuMAgentsは、ML risk model、救急・神経・精神科のLLM virtual specialists、RAG medical evidenceを統合したmulti-agent delirium prediction system。MIMIC-IVでderivation/internal validation、PKU 2病院とeICU-CRDでexternal validationした。
- Why interesting: 「LLMが単独で診断する」のではなく、予測モデル・専門家agent・evidence retrievalを分業させ、外部validationまで行っている。

### 目的
救急重症患者でのdelirium早期予測を、解釈可能かつinteractiveなmulti-agent clinical consultationとして実装する。

### 手法
data-driven ML risk prediction + emergency medicine / neurology / psychiatry virtual specialists + RAG evidenceを統合し、最終decisionを形成。

### データ・実験
MIMIC-IVでdevelopment/internal validation。Peking Universityの2病院cohortとeICU-CRDでexternal validation。

### 主な結果
accuracy/sensitivity/specificityはMIMIC-IVで0.749/0.762/0.747、PKUで0.731/0.708/0.736、eICU-CRDで0.670/0.708/0.665。chart reviewとclinician evaluationでreportのinterpretability/usefulnessも評価。

### 新規性
複数専門領域LLM agentとtraditional ML、RAGを一つの臨床prediction pipelineに統合している点。

### 限界
external cohortでperformance低下があり、実運用でのimpactやprospective trialはabstract上未確認。

### なぜ注目したか
agentic medical AIが「会話」ではなくrisk prediction workflowへ入る具体的実装で、外部validationもあるため。

**Medical AI extra:** study_design=model development + multicohort validation; sample_size=abstractに総n記載なし; primary_endpoint=delirium prediction performance; external_validation=PKU 2 hospitals + eICU-CRD; prospective_or_retrospective=database/cohort validation, prospective trialではない.

---

## 4. An Electronic Health Record-Integrated, Large Language Model-Powered Tool to Triage Surgical Patients

- Source: PubMed
- canonical ID: pmid:42623072
- Publication date: 2026-08-03
- Authors: Jane Wang et al.
- Journal: JAMA Network Open
- URL: https://pubmed.ncbi.nlm.nih.gov/42623072/
- read_level: abstract
- Tags: EHR, LLM, surgery, triage, human-in-the-loop, prospective implementation
- Summary: Stanford Health CareでEHR-integrated LLM tool「SCM Navigator」をprospectiveに運用し、6,193 surgical casesをtriage。hospitalist comanagement適応の同定でsensitivity 0.94、specificity 0.74を示した。
- Why interesting: retrospective benchmarkではなく、実際のEHR workflowへhuman-in-the-loopで組み込み、臨床医feedbackをreferenceとしてprospective評価している。

### 目的
hospitalist surgical comanagement対象患者のmanual identificationをLLMで自動化できるか検証する。

### 手法
preoperative documentation、structured data、perioperative morbidity criteriaを使い、LLMがappropriate / not appropriate / possibly appropriateを出力。医師reviewを必須とした。

### データ・実験
Stanford Health Care、2025-09〜2026-02のprospective unblinded quality improvement study。6,193 surgical cases、16 attending中14名参加。

### 主な結果
1,582 cases (25.5%)をhospitalist consultation推奨。医師判断をreferenceにsensitivity 0.94、specificity 0.74。false negative 19件中、LLM misclassificationと判断されたのは2件。

### 新規性
EHR-native、human-in-the-loopのLLM screeningをprospective operational settingで評価した点。

### 限界
single health system、referenceがphysician judgmentであり、hard clinical outcomeへの効果は未確立。

### なぜ注目したか
医療LLMの価値が「診断精度」ではなくworkflow automationとして現れる実例で、導入設計も現実的。

**Medical AI extra:** study_design=prospective quality improvement; sample_size=6,193 surgical cases; primary_endpoint=sensitivity/specificity for SCM eligibility; external_validation=なし; prospective_or_retrospective=prospective.

---

## 5. Noninvasive Intracranial Pressure Estimation Using Subspace System Identification and Machine Learning Algorithms: A Learning-to-Rank Approach

- Source: PubMed
- canonical ID: pmid:42585053
- Publication date: 2026-08-12
- Authors: Anni Zhao et al.
- Journal: IEEE Transactions on Biomedical Engineering
- URL: https://pubmed.ncbi.nlm.nih.gov/42585053/
- read_level: abstract
- Tags: machine learning, intracranial pressure, physiological signals, system identification, critical care
- Summary: ABP、cerebral blood velocity、R-R intervalなどの非侵襲signalからmean ICPを推定するため、subspace system identificationとranking-constrained optimizationを統合したML frameworkを提案した。
- Why interesting: deep learning一辺倒ではなく、生理系のsystem identificationとlearning-to-rank制約を組み合わせたmedical MLで、方法論的に面白い。

### 目的
侵襲的measurementを必要とするICPを、非侵襲的physiological signalsから推定する。

### 手法
subspace system identificationでcerebral hemodynamics modelを構築し、signal featureとestimation errorのmappingをranking constraints付きconvex optimizationで学習。

### データ・実験
複数clinical setting由来のdatabaseをtrain/test split。ABP、CBv、R-R intervalを利用。

### 主な結果
test entriesの31.88%が2 mmHg以内、34.07%が2–6 mmHgのestimation error。proof-of-conceptとしてfeasibilityを示した。

### 新規性
system identificationとranking-constrained MLを非侵襲ICP estimationへ組み合わせた点。

### 限界
accuracyはまだ臨床実装に十分とは言えず、cohort diversity、multicenter/prospective validationが必要と著者自身が指摘。

### なぜ注目したか
physiology-informed MLの実例で、単純なblack-box predictionとは異なるアプローチだから。

**Medical AI extra:** study_design=proof-of-concept model development; sample_size=abstractに総n記載なし; primary_endpoint=ICP estimation error; external_validation=複数settingを含むが独立prospective validationではない; prospective_or_retrospective=database-based.

---

## 6. Retrieval-Augmented Generation-Enabled Multimodal Large Language Model for Histopathologic Grading of Cutaneous Squamous Cell Carcinoma and Melanocytic Nevi

- Source: PubMed
- canonical ID: pmid:42588739
- Publication date: 2026-08-06
- Authors: Joshua Mijares et al.
- Journal: Cancers
- URL: https://pubmed.ncbi.nlm.nih.gov/42588739/
- read_level: abstract
- Tags: RAG, multimodal LLM, pathology, dermatology, task-specific validation
- Summary: Claude 4.5 Opus + ChromaDB RAGで、60 cSCCと67 melanocytic neviをgrading。同じRAG architectureでもcSCC concordance 90.0% (κ=0.85)に対し、nevus dysplasiaは44.8% (κ=0.072)と大きく差が出た。
- Why interesting: 「RAGを付ければ医療LLMが安定する」という単純な期待に反し、同一architectureでもtask definitionの曖昧さ・human agreementの低さに強く依存することを示す。

### 目的
RAG-assisted multimodal LLMが皮膚病理gradingをどこまでreference dermatopathologistに一致させられるか検証する。

### 手法
task-specific literatureをChromaDBでretrieveし、Claude 4.5 Opusにgrounding。各caseを3回評価しmajority resultを採用。

### データ・実験
60 cSCC cases、67 melanocytic nevus cases。

### 主な結果
cSCC: concordance 90.0%、κ=0.85。nevus: concordance 44.8%、κ=0.072。severely dysplastic nevusは0/6でconcordant classificationなし。

### 新規性
同じRAG/LLM frameworkを、human inter-rater reliabilityが異なる2 pathology tasksに並列適用し、task dependencyを明瞭に示した。

### 限界
case数が限定的で、single reference gradingや実臨床diagnostic workflowへのprospective integrationは未評価。

### なぜ注目したか
医療AIではmodel architectureだけでなく、target labelの曖昧さ自体が性能上限を決めることを示す好例。

**Medical AI extra:** study_design=retrospective diagnostic concordance study; sample_size=127 cases; primary_endpoint=concordance / Cohen's kappa; external_validation=なし; prospective_or_retrospective=retrospective.

---

## 7. AdaK: adaptive KV cache budget estimation framework for analyzing long-context large language model inference

- Source: PubMed
- canonical ID: pmid:42620545
- Publication date: 2026-08-05
- Authors: Tianjun Shao
- Journal: Frontiers in Artificial Intelligence
- URL: https://pubmed.ncbi.nlm.nih.gov/42620545/
- read_level: abstract
- Tags: LLM inference, KV cache, long context, efficiency, sparse attention
- Summary: long-context LLMのKV cache budgetを固定値ではなく動的に推定するAdaKを提案。entropy threshold、task-aware lookup table、lightweight policy networkの3戦略を評価し、16 settingsでfixed k=2048比最大17.9%の推定cache reductionを報告。
- Why interesting: long-context推論のメモリ問題を「cacheをどう削るか」ではなく「どのbudgetまで安全に削れそうかを事前推定する」問題として分離している。

### 目的
resource-constrained hardwareでlong-context LLMを動かす際のKV cache memory負荷を、task/modelに応じてadaptiveに見積もる。

### 手法
entropy-based thresholding、task-aware lookup table、lightweight policy networkの3 budget estimatorを設計。

### データ・実験
Qwen3-4B、Qwen3-8B、Mistral-7Bを含む16 settings。

### 主な結果
fixed k=2048 baselineに対し、estimated KV cache reduction最大17.9%。budget estimatorをdownstream sparse-attention kernelからdecoupleできる設計を提案。

### 新規性
cache compression mechanismそのものではなく、dynamic budget ceiling estimationを独立moduleとして扱う点。

### 限界
abstractで示されるのはbudget estimationで、実kernel上のend-to-end latency/quality trade-offは限定的。

### なぜ注目したか
長文LLMの実運用で重要なmemory costを、モデル変更なしで制御する方向だから。

---

## 8. Digital twin-supported behavioral intention in mothers of young children to prevent childhood obesity: a large language model-based intervention study

- Source: PubMed
- canonical ID: pmid:42626192
- Publication date: 2026-08-06
- Authors: Kenji Nakamura et al.
- Journal: Frontiers in Artificial Intelligence
- URL: https://pubmed.ncbi.nlm.nih.gov/42626192/
- read_level: abstract
- Tags: digital twin, LLM, preventive medicine, nutrition, behavior change
- Summary: childhood overweight digital twinと、nutrition guidance向けにfine-tuneしたLlama 3-70Bを組み合わせ、121 mothersでrisk visualization + chat consultationを評価。fine-tuned modelは30問中appropriate responseが18→27へ改善し、参加者の受容性・behavioral intentionも高かった。
- Why interesting: risk predictionモデルとLLM counselingを一体化し、「予測した後どう行動につなげるか」まで設計している。

### 目的
childhood obesity riskを個別visualizationし、LLMによるsupportive guidanceを組み合わせることで、保護者の予防行動意図を高められるか探索する。

### 手法
Tohoku Medical Megabank由来のpublished overweight-risk modelと、Japanese food composition dataでsupervised fine-tuneしたLlama 3-70Bを統合。

### データ・実験
nutrition QA 30問を3 registered dietitiansが評価。子どもを持つ女性121名がdigital twin visualizationとsingle chat-based testを体験。

### 主な結果
off-the-shelf Llama 3-70Bは30問中18 appropriate、fine-tuned modelは27。core acceptability itemsは5点中平均4.9超。121名中112名がrecommended lifestyle changesをfeasibleと認識。

### 新規性
predictive digital twinとconversational LLMをprecision prevention interventionとして統合した点。

### 限界
single-session、self-reported behavioral intention中心で、actual behavior/weight outcomeへの効果は未検証。

### なぜ注目したか
medical AIのpredictionをpatient-facing interventionへつなげる設計として興味深い。

**Medical AI extra:** study_design=feasibility/intervention study; sample_size=121 participants; primary_endpoint=appropriateness / acceptability / behavioral intention; external_validation=なし; prospective_or_retrospective=prospective single-session evaluation.

---

## 9. Leveraging a Large Language Model in Competency Development: Advancing Standardization and Optimizing Operational Efficiency

- Source: PubMed
- canonical ID: pmid:42607036
- Publication date: 2026-08-17
- Authors: Allison Wild, Tina Cheek
- Journal: Journal for Nurses in Professional Development
- URL: https://pubmed.ncbi.nlm.nih.gov/42607036/
- read_level: abstract
- Tags: LLM, nursing, workflow automation, standardization, operational efficiency
- Summary: nursing professional developmentのorientation competency standardizationにLLMを導入し、manual standardization effortを76%削減したと報告。
- Why interesting: clinical diagnosisではなく、医療組織のknowledge/workflow standardizationでLLMのROIを定量化した実装例。

### 目的
複数hospital/systemでorientation competencyを迅速にstandardizeする際のmanual workloadをLLMで削減する。

### 手法
advanced technology teamと連携してLLM-based workflowを構築し、導入前後のoperational metricsを評価。

### データ・実験
abstractでは詳細なcase数・model architectureは記載なし。

### 主な結果
manual standardization effortを76%削減。

### 新規性
LLMの医療活用をclinical decision supportではなくprofessional development operationsへ展開し、efficiency metricを示した点。

### 限界
abstractの情報量が少なく、品質維持、error rate、generalizabilityの詳細は不明。

### なぜ注目したか
LLM導入の価値が患者診療以外のhealth-system operationsにも広がっていることを示すため。

**Medical AI extra:** study_design=postimplementation operational evaluation; sample_size=abstractに記載なし; primary_endpoint=manual standardization effort; external_validation=なし; prospective_or_retrospective=implementation evaluation.

---

## 10. Avian influenza risk mapping in India using machine learning

- Source: PubMed
- canonical ID: pmid:42620513
- Publication date: 2026-08-05
- Authors: Satish S Gaikwad, T R Arun, Basavaraj Shrinivasa, Pragya Yadav, Babasaheb Tandale
- Journal: Frontiers in Veterinary Science
- URL: https://pubmed.ncbi.nlm.nih.gov/42620513/
- read_level: abstract
- Tags: machine learning, spatial epidemiology, One Health, uncertainty, influenza
- Summary: 2006–2024のIndia HPAI outbreak recordsと94 predictorsを用い、H3 hexagon上でspatial risk mapping。8 base classifiersはいずれもAUC>0.76、Gaussian-process stacked meta-learnerはAUC 0.853で、Random Forest 0.851との差は小さく非有意だったが、uncertainty layerを提供した。
- Why interesting: 単に最良AUCを競うのではなく、surveillance planningに使えるprediction uncertaintyを同時に地図化している点が実用的。

### 目的
Indiaにおけるavian influenza surveillanceを支援するnational relative spatial risk mapとuncertainty mapを構築する。

### 手法
2006-01〜2024-04のoutbreak records、buffered pseudo-absence、H3 resolution-7、94 environmental/livestock/land-cover/anthropogenic predictors。5-fold spatial block CVで8 classifiersとGaussian-process stackingを評価。

### データ・実験
national outbreak surveillance data、spatial cross-validation。

### 主な結果
全base classifier AUC>0.76。GPR stack AUC 0.853、Random Forest AUC 0.851/Brier 0.155/ECE 0.079で差は非有意。GPR posterior SDはensemble disagreementとr=0.74。東部、北東部、沿岸部、南部の一部をpriority areaとして同定。

### 新規性
spatial risk predictionとmodel uncertaintyを同時にsurveillance layerとして提供する点。

### 限界
passive-surveillance bias、multicollinearity、prospective validation未実施。

### なぜ注目したか
public / One Health領域で、uncertainty-aware MLを意思決定へ直接つなげる好例だから。

**Medical AI extra:** study_design=retrospective spatial epidemiology/modeling; sample_size=outbreak-record countはabstractに明記なし; primary_endpoint=spatial risk prediction performance; external_validation=prospective external validationなし; prospective_or_retrospective=retrospective.

---

<!-- PAPER_IDS -->
pmid:42642916
pmid:42607666
pmid:42594876
pmid:42623072
pmid:42585053
pmid:42588739
pmid:42620545
pmid:42626192
pmid:42607036
pmid:42620513
<!-- /PAPER_IDS -->
