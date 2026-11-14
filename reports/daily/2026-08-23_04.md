# [paper-report] 2026-08-23 ML / LLM / Medical AI

- Issue: #4
- Source: https://github.com/drkamoshika/papers/issues/4
- Created at: 2026-08-23T06:47:42Z

# Paper Watch Report — 2026-08-23

## 今回の概況

今回は `config/paper_watch.yml` の設定に従い、arXiv / PubMedを対象に、過去5日を中心として機械学習・LLM・医療AIの新着を探索した。既出IDは `state/seen_papers.txt` で除外した。

今回は上限20本まで無理に埋めず、一次情報を十分確認でき、かつ技術的に意味のある6本を採用した。今回目立った流れは3つある。

1. **LLM/agentの長期記憶を、単なる履歴保存ではなく「複数ソースの断片統合」として扱う研究**。MemFuseはこの問題を明示的なbenchmarkとmemory graphとして定式化している。
2. **小規模データでの学習効率を、foundation model + in-context probabilistic inferenceで改善する流れ**。Monroeは分子表現とTabPFNを組み合わせ、創薬の少量データ問題に直接踏み込んでいる。
3. **医療AIは精度競争から運用・監視・根拠の品質へ**。PubMed側では、LLMの画像検査選択、実環境でのAI監視registry、外科計画用3D再構成など、臨床実装を強く意識した研究が目立った。

---

# arXiv

## 1. Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference

- Source: arXiv
- canonical ID: `arxiv:2608.18982`
- Published: 2026-08-19
- Authors: Blazej Banaszewski, Andrew W. Fitzgibbon
- Category: molecular foundation model / drug discovery / machine learning
- URL: https://arxiv.org/abs/2608.18982
- Read level: full_text

### 目的
創薬ではwet-labで得られるbioassayデータが高コストで少量になりやすく、少数サンプルでの分子活性予測が難しい。この研究は、大規模な分子事前学習とin-context probabilistic inferenceを組み合わせ、data-scarceな下流タスクへの適応性能を高めることを狙う。

### 手法
Monroeはgraph transformer系の分子encoderを用い、ステレオ化学を明示的にgraphへ符号化する。事前学習ではuncertainty weightingによるmulti-task loss、conformer denoising、embedding decorrelationを導入する。下流では通常のfine-tuningではなく、固定encoderのembeddingをTabPFNへ渡し、in-contextでposterior-predictive distributionを出す。

### データ・実験
PM6の約8,100万分子とPCBAの約156万分子を利用。事前学習は合計1,152 taskで行われた。評価はPolarisとMoleculeACEを中心に実施し、既存のMolFormer、MiniMol、CheMeleonなどと比較している。事前学習は4基のH100 GPUで約26時間。

### 主な結果
Polarisでは既存MFMと同等以上、activity-cliff benchmarkでは従来法に対して有意な改善を報告。さらにTabPFN型の下流予測器を既存のMiniMol / CheMeleonへ適用しても性能向上し、`MiniMol_PFN` と `CheMeleon_PFN` が新しい強いbaselineになった。

### 新規性
「大規模分子encoder」だけでなく、**分子表現を固定した上でTabPFNによりin-context adaptationする**点が重要。few-shot / small-dataな創薬問題に対し、fine-tuningしない適応を成立させている。

### 限界
論文の評価は主に既存benchmark上であり、wet-labのprospective validationまでは行っていない。また、分子foundation modelとして強い一方、clinical / translationalな有効性は今後の検証が必要。

### なぜ注目したか
少量データで既存foundation modelをどう活かすかという問題にかなり直結している。特に「大規模事前学習 + 小規模下流データ + in-context predictor」という構成は、LLM以外のfoundation modelでも応用可能性が高い。

---

## 2. Causal Reasoning with Bipartite Graphical Causal Models

- Source: arXiv
- canonical ID: `arxiv:2608.19831`
- Published: 2026-08-20
- Authors: Joris M. Mooij
- Category: causal inference / graphical models / machine learning theory
- URL: https://arxiv.org/abs/2608.19831
- Read level: full_text

### 目的
既存のCausal Bayesian NetworkやStructural Causal Modelでは、feedbackを含む平衡系で「同じ変数値を強制する異なる介入」が区別できない場合がある。この曖昧さを扱える一般的なcausal graphical frameworkを作ることが目的。

### 手法
変数nodeと方程式nodeを分けた**bipartite graphical causal model (BGCM)** を導入する。介入を単なる `do(X=x)` ではなく、どの方程式を置き換え、どの変数を、どの値へ固定するかまで明示する。さらにB-separationという新しいgraphical separation criterionと、それに基づくdo-calculusを定式化する。

### データ・実験
理論研究で、主に物理系のcase studyを使って、標準SCMでは曖昧になる介入をBGCMで区別できることを示す。

### 主な結果
BGCMはCBN/SCMを包含しつつ、cyclic / equilibrium systemでも介入意味論を保てると主張。functional determinismをgraphical separationへ明示的に取り込むことで、domain invariance reasoningも可能になる。

### 新規性
因果モデルのgraphを「変数間」ではなく「変数と方程式の二部グラフ」として扱う点。これにより、同じ `X=x` でも異なる実世界介入を区別できる。

### 限界
現時点では理論frameworkが中心で、大規模な実データbenchmarkや一般的なcausal discovery pipelineとの統合は今後の課題。

### なぜ注目したか
LLM / agentだけでなく、AIが科学・医療でreasoningするにはcausal semanticsの扱いが重要。feedbackやequilibriumを持つ生命科学・生理学系では特に意味がありそう。

---

## 3. MemFuse: Multi-Source Memory Fusion from Fragmented Observations

- Source: arXiv
- canonical ID: `arxiv:2608.18704`
- Published: 2026-08-19
- Authors: Chao Li, Yuanfa Li, Wenhao Wu, Xule Liu, Zhi Wang, Kun Shao
- Category: LLM agents / long-term memory / benchmark
- URL: https://arxiv.org/abs/2608.18704
- Read level: abstract

### 目的
長期agent memoryの既存研究は単一のtext historyを前提にすることが多いが、実際には情報はアプリ・端末・ユーザー・時刻を跨いで断片化される。この分散観測をsource provenanceを失わず統合する問題を扱う。

### 手法
`MemFuseBench` を提案し、Scene-to-Sensor pipelineでsource-tagged observation、evidence-grounded question、adversarial distractorを生成する。MemFuse本体はatomic eventを保持するevent layerと、関連eventをcausal fusion graph上でまとめるcluster layerの二層memory構造を持つ。

### データ・実験
複数LLM設定で、temporal reasoning、cross-source evidence fusion、noise robustnessを評価するbenchmarkを構築。

### 主な結果
著者らによれば、評価したmemory systemの中でMemFuseが3種類すべてのLLM設定において最良のoverall performanceを達成し、特にcross-source evidence fusionを必要とする質問で一貫した改善を示した。

### 新規性
長期記憶を「何を保存するか」だけでなく、**複数source間で断片をどう統合し、なおかつ元sourceへtrace backできるか**としてbenchmark化した点。

### 限界
今回確認できたのはabstractであり、benchmark規模・具体的な数値差・baseline詳細は本文未確認。

### なぜ注目したか
長期agentを実用化する際、Gmail・Calendar・Slack・Webなど複数sourceを横断してmemoryを作る必要があるため、かなり実運用に近い問題設定。

---

# PubMed

## 4. Comparative Analysis of Large Language Model Performance in Appropriate Diagnostic Imaging Modality Selection

- Source: PubMed
- canonical ID: `pmid:42107669`
- Published: 2026 Aug issue
- Authors: James R Rybczyk, Kanhai S Amin, Varun Chamarty, Peyton Fletcher, Edward R Melnick, Howard P Forman
- Journal: Journal of the American College of Radiology
- URL: https://pubmed.ncbi.nlm.nih.gov/42107669/
- Read level: abstract

### 目的
ACRのcriteriaに基づく適切な画像検査選択において、複数frontier LLMの性能とclinical reasoningを比較する。

### 手法
OpenEvidence、GPT-5 Thinking、GPT-5、Claude Opus 4.1、Claude Sonnet 4.5、Gemini 2.5 Pro、Gemini 2.5 Flashの7モデルを比較。ACR guidelineを基に50のclinical vignetteを作成し、imaging appropriateness、technical specificity、clinical rationale、citation qualityをblind reviewerが評価。

### データ・実験
- Study design: comparative evaluation
- Sample size: 50 clinical vignettes
- 評価: 4 performance domains + readability + word count
- Reviewer: 2名blind、必要時3人目

### 主な結果
画像選択そのものは各LLMとも比較的高スコアで、大きな差は見られなかった。一方、citation qualityには大きな差があり、Gemini 2.5 Proは80%、Gemini 2.5 Flashは76%のpromptでhallucinated citationを含んだと報告されている。citation qualityでは他モデルより有意に低かった（P < .001）。

### 新規性
単なるmedical QA accuracyではなく、**検査選択 + rationale + citation validity**を同時に評価している。

### 限界
50 vignetteという比較的小規模なtext-based評価であり、実患者・prospective clinical workflowでの検証ではない。

### なぜ注目したか
医療LLMでは「答えが合っている」だけでは不十分で、根拠citationの信頼性が独立した重大問題であることを具体的に示している。

---

## 5. ACR's Assess-AI: A Registry for Real-World Performance Monitoring of Clinical Imaging Artificial Intelligence

- Source: PubMed
- canonical ID: `pmid:42066927`
- Published: 2026 Aug issue
- Authors: Laura P Coombs, Laura Brink, Woojin Kim, Christoph Wald, Kendall Schmidt, Mike Tilkin, Keith Dreyer, Tessa S Cook, Bernardo Bizzo
- Journal: Journal of the American College of Radiology
- URL: https://pubmed.ncbi.nlm.nih.gov/42066927/
- Read level: abstract

### 目的
画像AIの導入後に、実環境で性能が維持されているかを継続監視するnational registry `Assess-AI` の設計と機能を示す。

### 手法
施設からde-identified AI output、radiology report text、DICOM metadataを収集し、ACR Connect経由で集約。LLM prompting pipelineでradiology reportからsurrogate labelを抽出し、AI outputとのconcordanceを中央で計算する。結果はdashboardで可視化し、discordant caseは施設側で再同定してreviewできる。

### データ・実験
- Study design: registry / post-deployment monitoring framework
- 対象use case: intracranial hemorrhage, pulmonary embolism, pneumothorax, large-vessel occlusion, bone age, cervical spine fracture など
- Prospective/retrospective: abstract上では明示的なtrial designではなく、実運用registryの報告

### 主な結果
施設単位でdata completeness、longitudinal concordance、benchmarkとの比較、demographic/technical factor別discordanceを追跡可能。local adjudicationによるroot-cause analysisも設計に含まれる。

### 新規性
医療AIを「開発時benchmark」ではなく**導入後に継続監視するインフラ**として扱っていること。さらにLLMをsurrogate labelingに使い、registry規模でground-truth生成コストを下げる設計になっている。

### 限界
abstractでは大規模outcome改善や患者予後への効果までは示していない。LLM由来surrogate label自体の誤差管理も重要な論点になる。

### なぜ注目したか
医療AIが研究からdeploymentへ移るにつれ、model drift・施設差・population shiftの監視が不可欠になる。このregistryはその実装例として重要。

---

## 6. Development of an Artificial Intelligence-Driven Three-Dimensional Reconstruction Model of Renal Vasculature for Surgical Planning in Robot-Assisted Partial Nephrectomy

- Source: PubMed
- canonical ID: `pmid:42430567`
- Published: 2026 Aug issue
- Authors: Davide Brusa, Riccardo Bertolo, Francesco Ditonno, Greta Pettenuzzo, Lorenzo Pierangelo Treccani, Alessandro Veccia, Filippo Caudana, Francesco Fontana, Maria Angela Cerruto, Alessandro Antonelli
- Journal: International Journal of Medical Robotics and Computer Assisted Surgery
- URL: https://pubmed.ncbi.nlm.nih.gov/42430567/
- Read level: abstract

### 目的
robot-assisted partial nephrectomyの術前計画を支援するため、造影CTから腎血管を自動segmentationし3D reconstructionを生成するdeep learning pipelineを実装・内部検証する。

### 手法
3D SegResNetを用い、arterial / portal phaseのCTからrenal vascular structureをsegmentationする。manual segmentationをground truthとし、spatial normalization、isotropic resampling、augmentation、pre/post-processingを組み込む。

### データ・実験
- Study design: single-centre internal validation
- Sample size: 97 CT scans
- Training: 68 scans
- Independent held-out test: 29 scans
- 対象: 2019年1月〜2025年9月にrenal massで治療された患者
- External validation: なし
- Prospective / retrospective: abstractの記述からは既存症例を用いたretrospective datasetと解釈されるが、本文未確認のため断定しない

### 主な結果
abstractでは自動segmentationと3D reconstructionの実装・内部validationが報告されている。今回取得した検索結果では詳細な定量metricの全文は確認できなかったため、数値は記載しない。

### 新規性
診断classificationではなく、**手術前の解剖理解・planningに直接つながる3D reconstruction**へAIを使っている。

### 限界
single-centreかつ97症例で、external validationがない。手術時間、合併症、margin、腎機能などclinical outcome改善まで示されたかはabstractのみでは判断できない。

### なぜ注目したか
医療AIが「画像を分類する」段階から、医師のplanning workflowそのものを支援する方向へ移っている例として分かりやすい。

---

## 今回の採用数

- arXiv: 3本
- PubMed: 3本
- 合計: 6本
- 上限: 20本

十分に一次情報を確認できない候補や、既出論文、テーマとの関連が弱いものは上限まで埋めるためには採用しなかった。

<!-- PAPER_IDS -->
arxiv:2608.18982
arxiv:2608.19831
arxiv:2608.18704
pmid:42107669
pmid:42066927
pmid:42430567
<!-- /PAPER_IDS -->
