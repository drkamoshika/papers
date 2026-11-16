# 医療・生体信号・創薬AI：基礎から現在へのレビュー

レビュー日: 2026-11-16。収録論文の公開日上限: 2026-11-12。

画像や診療記録から特徴を学ぶ段階から、事前学習した表現を使い、文章・生体信号・分子を横断して支援する段階へ進んだ。現在の到達点は用途ごとに異なり、診療現場の効果は精度の高いベンチマークとは分けて評価する必要がある。

収録基礎文献 139件／本レビューで引用する基礎文献 18件・新着論文 8件。分野横断の文献を含み、件数は引用IDの集合から計算。

## いま何ができるか

画像の領域抽出、記録の構造化、生体信号解析、分子・タンパク質の候補探索で有用性を示す。

医学試験の高得点や記録の読解から、自律診療・個別予後予測・治療効果までは確定しない。 [1](https://pubmed.ncbi.nlm.nih.gov/33288961/) [2](https://pubmed.ncbi.nlm.nih.gov/42957896/) [3](https://pubmed.ncbi.nlm.nih.gov/43019548/)

## 基礎からの積み上げ

### 画像と患者記録から表現を学ぶ

U-Netは領域の切り出し、Deep Patientは電子カルテの表現学習を進めた。nnU-Netはデータセットごとの設定を体系化し、設計の自動化と再現可能な比較を重視した。 [4](https://arxiv.org/abs/1505.04597) [5](https://pubmed.ncbi.nlm.nih.gov/27185194/) [1](https://pubmed.ncbi.nlm.nih.gov/33288961/)

### タスクごとの学習から事前学習へ

BEHRTとMed-BERTは診療記録の系列、RETFoundは眼底画像、ECG研究は心電図を扱う。データの種類ごとに事前学習した表現を別の課題へ移す流れだが、施設や機器の差も持ち越す。 [6](https://pubmed.ncbi.nlm.nih.gov/32346050/) [7](https://pubmed.ncbi.nlm.nih.gov/34017034/) [8](https://pubmed.ncbi.nlm.nih.gov/37704728/) [9](https://pubmed.ncbi.nlm.nih.gov/32903191/)

### 分子とタンパク質を探索する

AlphaFoldは構造予測、ProteinMPNNは配列設計、RFdiffusionは構造・機能を狙う生成設計へと対象を広げた。計算上の候補を作ることと、生体内での有効性・安全性を確かめることは別の段階になる。 [10](https://pubmed.ncbi.nlm.nih.gov/34265844/) [11](https://pubmed.ncbi.nlm.nih.gov/36108050/) [12](https://pubmed.ncbi.nlm.nih.gov/37433327/)

### 実臨床の評価を設計する

TRIPOD、CONSORT-AI、DECIDE-AIは、予測モデルの報告、介入試験、早期の臨床評価をそれぞれ支える。外部検証や人とAIの組合せを評価しなければ、モデル精度から診療への貢献を判断しにくい。 [13](https://pubmed.ncbi.nlm.nih.gov/25569120/) [14](https://pubmed.ncbi.nlm.nih.gov/32908283/) [15](https://pubmed.ncbi.nlm.nih.gov/35585198/) [16](https://pubmed.ncbi.nlm.nih.gov/34152373/)

## 到達点・適用条件・残る境界

### 医用画像・生体信号を解析する — 比較が蓄積

できていること: 領域抽出、所見の検出、心電図などの分類で、対象のデータと手順を定めた評価が積み重なっている。

条件: 施設・装置・患者層を分けた外部検証と、判定の閾値、医療者と組み合わせた効果を確認する。

残る境界: 単施設の高精度から、異なる施設での安全性や患者転帰の改善は推定できない。 [1](https://pubmed.ncbi.nlm.nih.gov/33288961/) [9](https://pubmed.ncbi.nlm.nih.gov/32903191/) [16](https://pubmed.ncbi.nlm.nih.gov/34152373/) [15](https://pubmed.ncbi.nlm.nih.gov/35585198/)

### 臨床記録を構造化し、人の確認を支援する — 前向き評価の例あり

できていること: 診療記録から有害事象などを抽出し、人による確認と組み合わせて注釈時間や一致度を改善した例がある。

条件: 対象イベント・重症度・時間関係を分けて測り、後ろ向き検証、サイレント運用、人との比較を区別する。

残る境界: 注釈支援の改善から、自律的な治療判断や患者の長期予後の改善までは言えない。 [2](https://pubmed.ncbi.nlm.nih.gov/42957896/) [17](https://arxiv.org/abs/2611.01527)

### 将来の患者状態を予測する — 用途ごとの検証が必要

できていること: 電子カルテや生体信号から特定の将来イベントを予測するモデルが作られている。

条件: 予測時点で使える情報だけを入力し、時系列・施設外検証、校正、単純な持続予測との比較を行う。

残る境界: 現時点の状態を正しく整理できるLLMでも、数か月後の個別予後が当たるとは限らない。 [18](https://pubmed.ncbi.nlm.nih.gov/31367026/) [6](https://pubmed.ncbi.nlm.nih.gov/32346050/) [3](https://pubmed.ncbi.nlm.nih.gov/43019548/)

### 創薬・タンパク質設計を支援する — 実験検証を伴う研究

できていること: 構造予測や候補生成を使って、実験へ進める候補を絞り、設計と検証の循環を作れる。

条件: 結合・機能・毒性・合成可能性など、目的に対応した実験を設計する。

残る境界: 構造がもっともらしいことや試験管内の機能から、治療薬としての有効性・臨床成功率は導けない。 [10](https://pubmed.ncbi.nlm.nih.gov/34265844/) [11](https://pubmed.ncbi.nlm.nih.gov/36108050/) [12](https://pubmed.ncbi.nlm.nih.gov/37433327/) [19](https://pubmed.ncbi.nlm.nih.gov/42984375/)

## 直近研究の位置づけ

### 有害事象抽出：人の作業まで測った例

免疫治療の有害事象抽出では、後ろ向きの現時点イベント検出F1は0.92、重症度分類は0.66。3か月の前向きサイレント運用では二値F1が0.72〜0.79で、スタッフのクロスオーバー試験では注釈時間を2.71分短縮した。異なる指標・段階の数値を一つの精度にまとめない。 [2](https://pubmed.ncbi.nlm.nih.gov/42957896/)

### 膝関節症：現在の評価から将来予測への壁

単施設の追跡完了111人で、既に膝関節症のある患者について医師との診断一致は105/111。一方、6か月後のWOMAC予測誤差はLLM 5.92〜6.58、医師3.86、持続予測5.43。高い診断一致を一般的な診断精度や予後予測能力へ広げない。 [3](https://pubmed.ncbi.nlm.nih.gov/43019548/)

### 医学的評価器：課題を替えると信頼性が変わる

10 LLMを3種の医療評価に用いた研究では、全課題で上位3位に入るモデルはなかった。最重症トリアージで重大な過小評価が報告され、別課題で良い評価器をそのまま転用できないことが示された。 [20](https://pubmed.ncbi.nlm.nih.gov/42995166)

## 次の課題（編者の整理）

### 支援が現場の結果を改善するか

人の確認を残した業務時間・判断品質の改善と、患者転帰の改善を段階別に検証する。モデル単体の結果だけで判断しない。 [15](https://pubmed.ncbi.nlm.nih.gov/35585198/) [2](https://pubmed.ncbi.nlm.nih.gov/42957896/)

### 外部施設と将来時点に耐えられるか

施設・時点・患者層をまたいだ校正と、監視・更新後の性能を確かめる必要がある。 [16](https://pubmed.ncbi.nlm.nih.gov/34152373/) [21](https://pubmed.ncbi.nlm.nih.gov/38207039/) [22](https://pubmed.ncbi.nlm.nih.gov/42066927)

## 分野間の接点（編者の整理）

- [表形式・時系列・因果推論](https://drkamoshika.github.io/papers/?view=map&topic=structured): EHRの予後予測は表・時系列の問題でもあり、観察データから治療の介入効果を推定する問題とは区別する。 [6](https://pubmed.ncbi.nlm.nih.gov/32346050/) [23](https://arxiv.org/abs/2611.15009)

- [次イベント予測・点過程](https://drkamoshika.github.io/papers/?view=map&topic=events): 診断・投薬・合併症の次イベントと発生時刻を扱うには、点過程の評価と観察の欠落・打ち切りの扱いが重要になる。 [24](https://arxiv.org/abs/1612.09328) [3](https://pubmed.ncbi.nlm.nih.gov/43019548/)

- [神経科学とAI](https://drkamoshika.github.io/papers/?view=map&topic=neuroscience): EEGの表現学習と脳の機構理解は接点を持つが、信号を分類できることと脳回路を説明できることは別である。 [25](https://arxiv.org/abs/2611.17031) [26](https://pubmed.ncbi.nlm.nih.gov/39358519/)

## 読む順番

1. [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1505.04597)

2. [BEHRT: Transformer for Electronic Health Records](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32346050)

3. [Highly accurate protein structure prediction with AlphaFold](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34265844)

4. [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A35585198)

5. [An agentic AI system enhances clinical detection of immune-related adverse events in a multi-phase validation study](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42957896)

6. [Performance of a Large Language Model for Predicting Clinical and Radiographic Outcomes in Knee Osteoarthritis: Single-Center Prospective Observational Study](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A43019548)

7. [Large language models are unstable as autonomous medical evaluators across clinical tasks](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42995166)

## 参考文献と確認範囲

1. [nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation](https://pubmed.ncbi.nlm.nih.gov/33288961/) — 2020-12-07 / pmid:33288961 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A33288961)

2. [An agentic AI system enhances clinical detection of immune-related adverse events in a multi-phase validation study](https://pubmed.ncbi.nlm.nih.gov/42957896/) — 2026-10-29 / pmid:42957896 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42957896) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://pubmed.ncbi.nlm.nih.gov/42957896/)

3. [Performance of a Large Language Model for Predicting Clinical and Radiographic Outcomes in Knee Osteoarthritis: Single-Center Prospective Observational Study](https://pubmed.ncbi.nlm.nih.gov/43019548/) — 2026-11-12 / pmid:43019548 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A43019548) / 今回の再確認: 2026-11-16、出版社本文の関連箇所、[一次資料](https://medinform.jmir.org/2026/1/e107092/)

4. [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597) — 2015-05-18 / arxiv:1505.04597 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1505.04597)

5. [Deep Patient: An Unsupervised Representation to Predict the Future of Patients from the Electronic Health Records](https://pubmed.ncbi.nlm.nih.gov/27185194/) — 2016-05-17 / pmid:27185194 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A27185194)

6. [BEHRT: Transformer for Electronic Health Records](https://pubmed.ncbi.nlm.nih.gov/32346050/) — 2020-04-28 / pmid:32346050 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32346050)

7. [Med-BERT: pretrained contextualized embeddings on large-scale structured electronic health records for disease prediction](https://pubmed.ncbi.nlm.nih.gov/34017034/) — 2021-05-20 / pmid:34017034 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34017034)

8. [A foundation model for generalizable disease detection from retinal images](https://pubmed.ncbi.nlm.nih.gov/37704728/) — 2023-09-13 / pmid:37704728 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A37704728)

9. [Deep Learning for ECG Analysis: Benchmarks and Insights from PTB-XL](https://pubmed.ncbi.nlm.nih.gov/32903191/) — 2021-05-11 / pmid:32903191 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32903191)

10. [Highly accurate protein structure prediction with AlphaFold](https://pubmed.ncbi.nlm.nih.gov/34265844/) — 2021-07-15 / pmid:34265844 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34265844)

11. [Robust deep learning-based protein sequence design using ProteinMPNN](https://pubmed.ncbi.nlm.nih.gov/36108050/) — 2022-09-15 / pmid:36108050 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A36108050)

12. [De novo design of protein structure and function with RFdiffusion](https://pubmed.ncbi.nlm.nih.gov/37433327/) — 2023-07-11 / pmid:37433327 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A37433327)

13. [Transparent reporting of a multivariable prediction model for individual prognosis or diagnosis (TRIPOD): the TRIPOD statement](https://pubmed.ncbi.nlm.nih.gov/25569120/) — 2015-01-07 / pmid:25569120 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A25569120)

14. [Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension](https://pubmed.ncbi.nlm.nih.gov/32908283/) — 2020-09-09 / pmid:32908283 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32908283)

15. [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://pubmed.ncbi.nlm.nih.gov/35585198/) — 2022-05-18 / pmid:35585198 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A35585198)

16. [External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients](https://pubmed.ncbi.nlm.nih.gov/34152373/) — 2021-06-21 / pmid:34152373 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34152373)

17. [From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents](https://arxiv.org/abs/2611.01527) — 2026-11-01 / arxiv:2611.01527 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.01527)

18. [A clinically applicable approach to continuous prediction of future acute kidney injury](https://pubmed.ncbi.nlm.nih.gov/31367026/) — 2019-07-31 / pmid:31367026 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A31367026)

19. [From Generative Molecular Design to Agentic Artificial Intelligence in Drug Discovery](https://pubmed.ncbi.nlm.nih.gov/42984375/) — 2026-11-12 / pmid:42984375 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42984375)

20. [Large language models are unstable as autonomous medical evaluators across clinical tasks](https://pubmed.ncbi.nlm.nih.gov/42995166) — 2026-11-06 / pmid:42995166 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42995166) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://pubmed.ncbi.nlm.nih.gov/42995166)

21. [Illusory generalizability of clinical prediction models](https://pubmed.ncbi.nlm.nih.gov/38207039/) — 2024-01-11 / pmid:38207039 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A38207039)

22. [ACR's Assess-AI: A Registry for Real-World Performance Monitoring of Clinical Imaging Artificial Intelligence](https://pubmed.ncbi.nlm.nih.gov/42066927) — 2026-04-29 / pmid:42066927 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42066927)

23. [From Forecasting to World Modeling: Can Temporal Foundation Models Recover Causal Response?](https://arxiv.org/abs/2611.15009) — 2026-11-11 / arxiv:2611.15009 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.15009) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.15009v1)

24. [The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process](https://arxiv.org/abs/1612.09328) — 2016-12-29 / arxiv:1612.09328 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1612.09328)

25. [Your Vision Foundation Model Is Secretly an EEG Foundation Model](https://arxiv.org/abs/2611.17031) — 2026-11-12 / arxiv:2611.17031 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17031) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.17031v1)

26. [A Drosophila computational brain model reveals sensorimotor processing](https://pubmed.ncbi.nlm.nih.gov/39358519/) — 2024-10-02 / pmid:39358519 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A39358519)

## このレビューの範囲

母集団はこのライブラリの収録論文。全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断的レビューです。

基礎文献・新着論文は収録先の区別です。基礎文献側にも2026年の研究が含まれるため、古さや新しさは個々の公開日で確認できます。

技術の系譜、分野間の接点、次の課題は編者の整理であり、論文間の直接の引用関係や、商用普及の程度を確定するものではありません。

個別論文の確認範囲は要旨または本文の関連箇所です。今回、代表的な22件の一次資料を追加で照合しました。全件の全文再精読や独立再現を意味しません。

実験の数字は論文の報告値です。異なるデータ・分割・指標の数値を統一順位へ変換していません。

[7分野の全体マップ](https://drkamoshika.github.io/papers/?view=map)
