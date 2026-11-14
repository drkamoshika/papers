# 基礎文献 — 医療・生体信号・創薬AI

> schema_version: 1
> report_date: 2026-11-14

## ダイジェスト

選定139件中、以下は原著照合・編集確認を終えた24件。選定リストだけの論文を完成済み件数には含めない。原著要旨までの記述と本文確認を区別し、Limitationsの「編者の注意」は著者の自己申告と区別する。

研究の流れと2026年論文との接続は [文献集の案内](README.md) を参照。

## 完全版レポート

### Paper: Development and evaluation of a de-identification procedure for a case register sourced from mental health electronic records
- Source: PubMed
- Canonical ID: pmid:23842533
- Publication date: 2013-07-11
- URL: https://pubmed.ncbi.nlm.nih.gov/23842533/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 精神科診療記録CRISの匿名化で、患者別辞書による識別情報の除去と運用上の保護を検証した。
- Objective: 研究利用可能な文章を残しつつ、精神科EHRに含まれる個人識別情報を除く。
- Methods: 専用項目の識別情報から辞書を作り本文中の一致をマスク。500ノートで評価し、別の70ノート（学習50、テスト20）でMISTとも比較。複数情報が残る漏洩候補も調査した。
- Data and results: 真の識別情報の適合率98.8%、再現率97.6%。別テストでCRISは100%・88.5%、MISTは95.1%・78.1%。漏洩の可能性がある1件を確認した。
- Novelty: 文字列除去のスコアに加え、複数情報の組合せとアクセス保護を含めた研究データの匿名性を評価した。
- Limitations: 著者は綴り誤りによる識別情報の残存や、匿名化後の推測可能性を認める。高い抽出性能だけでは匿名性を保証できず、セキュリティ運用との併用が必要。

### Paper: Prediction of In-hospital Mortality in Emergency Department Patients With Sepsis: A Local Big Data-Driven, Machine Learning Approach
- Source: PubMed
- Canonical ID: pmid:26679719
- Publication date: 2016-02-13
- URL: https://pubmed.ncbi.nlm.nih.gov/26679719/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 4病院のEHRを使い、敗血症患者の院内死亡予測でランダムフォレストと臨床スコアを比較した。
- Objective: 少数の事前選択変数に依存する臨床ルールを、多数の電子記録変数で改善できるか調べる。
- Methods: 2013–2014年の救急受診後に入院した成人敗血症例を後ろ向き解析。500超の変数で学習し、受診を80:20に分割してCART、回帰、既存スコアと比較した。
- Data and results: 4,676人の5,278受診。検証AUCはランダムフォレスト0.86、CART0.69、回帰0.76、CURB-65 0.73、MEDS0.71、mREMS0.72。各比較でp≤0.003。
- Novelty: 地域の実診療データから、その施設群に適した高次元予測器を作る実例を示した。
- Limitations: 著者は前向き評価と患者転帰改善の検証を求める。編者の注意: 受診単位の無作為分割であり、独立した病院への外部検証とは区別する。

### Paper: Deep Patient: An Unsupervised Representation to Predict the Future of Patients from the Electronic Health Records
- Source: PubMed
- Canonical ID: pmid:27185194
- Publication date: 2016-05-17
- URL: https://pubmed.ncbi.nlm.nih.gov/27185194/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: Deep Patientは、教師なしで学ぶ患者表現を将来の多疾患予測へ利用した初期のEHR深層学習。
- Objective: 患者記録を汎用的な特徴表現に圧縮し、疾患ごとに手作業で特徴を作る負担を減らす。
- Methods: Mount Sinaiの約70万人の集約EHRから3層の積層ノイズ除去オートエンコーダーで表現を学習。元のEHR表現や別の特徴学習法と比較した。
- Data and results: テスト患者76,214人、78疾患を複数の時間窓で評価し、比較表現より良好な予測を報告。重症糖尿病、統合失調症、各種癌で高い性能だったが、要旨に疾患別AUCの数値はない。
- Novelty: 教師なし患者表現を共有し、異なる疾患の予測器へ展開する枠組みを示した。
- Limitations: 編者の注意: 教師なしなのは表現学習であり、最終的な疾患予測全体を指さない。単一医療システムでの評価で、施設間移植や治療効果は別途検証が必要。

### Paper: Using recurrent neural network models for early detection of heart failure onset
- Source: PubMed
- Canonical ID: pmid:27521897
- Publication date: 2016-08-13
- URL: https://pubmed.ncbi.nlm.nih.gov/27521897/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 診断・処方などの時間的な順序をGRUで扱い、心不全の初回診断予測を改善した研究。
- Objective: 診療イベント間の時間関係を利用すると、時間情報を無視する従来手法より心不全発症を予測できるか検証する。
- Methods: 2000–2013年のプライマリケア患者から心不全3,884例と対照28,903人を抽出。12または18か月の観察履歴をGRUへ入力し、ロジスティック回帰、MLP、SVM、KNNと比較した。
- Data and results: 12か月履歴でAUCはGRU0.777、回帰0.747、MLP0.765、SVM0.743、KNN0.730。18か月ではGRU0.883、最良の比較法MLP0.834だった。
- Novelty: 集計された診療コードだけでなく、時刻を持つイベント列から患者の経過を学習する意義を示した。
- Limitations: 編者の注意: 12・18か月は入力する履歴の長さであり、予測の先行時間ではない。単一医療システムの症例対照設計で、実診療での陽性的中率や転帰改善は未検証。
- Publication date note: 出版社PDFのAdvance Access Publication Dateを採用。巻号の2017年3月と区別する。出典: https://academic.oup.com/jamia/article/24/2/361/2631499

### Paper: Dermatologist-level classification of skin cancer with deep neural networks
- Source: PubMed
- Canonical ID: pmid:28117445
- Publication date: 2017-01-25
- URL: https://pubmed.ncbi.nlm.nih.gov/28117445/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 大規模な皮膚画像で学習したCNNを、2つの生検確認済み二値分類で皮膚科医と比較した。
- Objective: 画像画素と疾患ラベルから直接学習し、細かな外観差のある皮膚病変を分類する。
- Methods: 2,032疾患の臨床画像129,450枚で単一CNNを学習。角化細胞癌対良性脂漏性角化症、悪性黒色腫対良性母斑で21人の専門医と比較した。
- Data and results: 両分類課題で試験対象の専門医に匹敵する性能を報告。要旨に感度・特異度やAUCの具体値は記載されていない。
- Novelty: 医療向けの手設計特徴に依存せず、多数の皮膚疾患を含む画像学習から臨床的に重要な鑑別へ展開した。
- Limitations: 編者の注意: 2つの画像分類試験の結果であり、全疾患の診療やスマートフォンによる一般利用の安全性を実証したものではない。皮膚色などの集団別性能も要旨から不明。

### Paper: Prediction of 30-Day All-Cause Readmissions in Patients Hospitalized for Heart Failure: Comparison of Machine Learning and Other Statistical Approaches
- Source: PubMed
- Canonical ID: pmid:27784047
- Publication date: 2017-02-01
- URL: https://pubmed.ncbi.nlm.nih.gov/27784047/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 心不全の30日再入院では、複数の機械学習法が従来の回帰を上回らなかった比較研究。
- Objective: 複雑な学習法が、臨床利用には不十分だった再入院予測を改善するか検証する。
- Methods: 心不全レジストリとMedicareを結合した56,477人を70:30に分割。ベイズネット、ランダムフォレスト、勾配ブースティング、回帰、LASSOを比較した。
- Data and results: 30日再入院率21.2%。検証C統計量は順に0.618、0.607、0.614、0.624、0.618で、機械学習の優越性はなかった。既存EHRモデルの移植では0.589。
- Novelty: 同じ臨床データ上で手法を比較し、アルゴリズムの高度化だけでは予測力が伸びない例を示した。
- Limitations: 編者の注意: このレジストリと予測転帰に関する陰性結果であり、機械学習全般の無効性を示さない。無作為分割での検証と新施設への移植も区別する。

### Paper: Federated learning of predictive models from federated Electronic Health Records
- Source: PubMed
- Canonical ID: pmid:29500022
- Publication date: 2018-01-12
- URL: https://pubmed.ncbi.nlm.nih.gov/29500022/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 生の診療記録を中央に集めず、分散最適化で共通の心疾患入院予測器を学習した。
- Objective: 複数の記録保有者がデータを明示的に交換せず、単一の予測モデルへ収束する方法を作る。
- Methods: L1正則化付き疎なsoft-margin SVMにcluster Primal Dual Splitting（cPDS）を開発。前年までのEHRから翌年の心疾患入院を予測し、集中型・別の分散法と比較した。
- Data and results: cPDSは比較法と同程度のAUCを保ち、集中型より速い収束を報告。別の分散法より収束が速く通信量も少ないが、要旨に絶対値や対象者数はない。
- Novelty: 後年の医療連合学習につながる、記録を各拠点に置いたまま共同最適化する設計を示した。
- Limitations: 編者の注意: 生データを送らないことだけで、更新情報からの漏洩まで防ぐ保証にはならない。通信条件や施設間の分布差を含む臨床導入性能は要旨から確定しない。

### Paper: Prediction of Incident Hypertension Within the Next Year: Prospective Study Using Statewide Electronic Health Records and Machine Learning
- Source: PubMed
- Canonical ID: pmid:29382633
- Publication date: 2018-01-30
- URL: https://pubmed.ncbi.nlm.nih.gov/29382633/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 州全体のEHRで翌年の新規高血圧を予測し、後続年の集団で性能を検証した。
- Objective: 1年以内の本態性高血圧リスクを事前に評価し、予防対象の層別化へ利用する。
- Methods: Maine州の記録から2013年823,627人でXGBoostを構築し、2014年680,810人で前向き集団の予測を検証。5つのリスク層へ分類した。
- Data and results: AUCは後ろ向き0.917、前向き0.870。翌年の診断率は最低リスク層1.19%、最高リスク層50.93%で、実時間の予測モデルを州内で導入したと報告する。
- Novelty: 州規模の共有記録と時間を分けた検証を使い、翌年発症リスクの運用を検討した。
- Limitations: 編者の注意: 前向きの予測検証や導入は、介入の無作為試験とは異なる。利用頻度・社会経済指標の関連から高血圧の因果的要因を確定できない。

### Paper: Predicting suicide attempts in adolescents with longitudinal clinical data and machine learning
- Source: PubMed
- Canonical ID: pmid:29709069
- Publication date: 2018-04-30
- URL: https://pubmed.ncbi.nlm.nih.gov/29709069/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 思春期の非致死的自殺企図を診療履歴から予測し、対照集団と校正の重要性を示した。
- Objective: 対面スクリーニングに追加負担をかけず、日常の診療情報から予防支援の候補を把握する。
- Methods: 1998–2015年の後ろ向きコホートで974企図例を、他の自傷496人、抑うつ7,059人、一般患者25,081人と比較。ランダムフォレストを楽観バイアス調整し、等張回帰で再校正した。
- Data and results: 720日前から7日前でAUCは自傷対照0.83→0.85、抑うつ対照0.87→0.90、一般患者対照0.94→0.97。各比較で回帰を上回り、再校正で評価性能が改善した。
- Novelty: 予測時点、似た症状を持つ対照、確率の校正を同時に評価し、高いAUCだけに依存しない検討を行った。
- Limitations: 編者の注意: 対照選択でAUCは大きく変わる。後ろ向きの非致死的企図予測であり、自殺死亡の予測精度や支援介入の効果を示す結果ではない。

### Paper: Scalable and accurate deep learning with electronic health records
- Source: PubMed
- Canonical ID: pmid:31304302
- Publication date: 2018-05-08
- URL: https://pubmed.ncbi.nlm.nih.gov/31304302/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: FHIR形式で診療録全体を系列化し、複数の入院転帰を予測する深層学習の基盤研究。
- Objective: 施設ごとの手作業による変数整備を減らし、未加工に近いEHRから複数の臨床イベントを予測する。
- Methods: 米国2大学病院の匿名化EHRをFHIRに基づいて表現。診療ノートも含む系列を深層学習に入力し、従来の臨床予測モデルと比較した。
- Data and results: 24時間以上入院した成人216,221人、約469億データ点。施設別AUROCは院内死亡0.93–0.94、30日予定外再入院0.75–0.76、長期入院0.85–0.86。退院診断の頻度加重AUROCは0.90。
- Novelty: 課題別の手作業による特徴量選択から、診療録全体を再利用する汎用的な患者系列表現への転換を示した。
- Limitations: 編者の注意: 2施設での予測性能は、独立した他施設への移植性や介入による患者転帰改善の証明ではない。AUROCだけでは校正や警報負担を評価できない。

### Paper: Multitask learning and benchmarking with clinical time series data
- Source: PubMed
- Canonical ID: pmid:31209213
- Publication date: 2019-06-17
- URL: https://pubmed.ncbi.nlm.nih.gov/31209213/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: MIMIC-IIIの臨床時系列から4つの共通ベンチマークを作り、医療予測の比較可能性を高めた。
- Objective: 公開データと評価課題の不足により、医療機械学習の進歩を測りにくい問題を解消する。
- Methods: 死亡、在院期間、生理学的悪化、表現型分類を定義。線形・ニューラルモデルを基準に、深い監督、多課題学習、データに合わせた構造を比較する。
- Data and results: MIMIC-IIIに由来する4課題と強い基準モデルを提供。要旨には各手法のスコアや患者数の数値は記載されていない。
- Novelty: 単一疾患の性能競争から、同一データと複数の臨床転帰を共有する再現可能な評価基盤へ進めた。
- Limitations: 編者の注意: 公開ICUデータでの比較は、一般病棟・外来や他施設での性能を保証しない。多課題学習の効果を要旨だけから一律に断定できない。

### Paper: A clinically applicable approach to continuous prediction of future acute kidney injury
- Source: PubMed
- Canonical ID: pmid:31367026
- Publication date: 2019-07-31
- URL: https://pubmed.ncbi.nlm.nih.gov/31367026/
- read_level: full_text
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 診療記録から急性腎障害を最大48時間前に継続予測し、検出率と警報負担を併記した研究。
- Objective: 悪化する患者を治療可能な時間内に特定するため、将来の急性腎障害リスクを連続的に更新する。
- Methods: 成人703,782人、入院172・外来1,062拠点の縦断EHRで深層モデルを開発。リスクに加え信頼度、関連特徴、血液検査値の将来推移を提示する。
- Data and results: 最大48時間の先行時間、真警報1件につき偽警報2件の条件で、院内急性腎障害の55.8%を予測。発症後90日以内に定期外来透析が予定された事例では90.2%を予測した。
- Novelty: 単一時点のリスク分類を超え、継続的な予測と説明・検査値推移を臨床対応の時間窓につなげた。
- Limitations: 著者はVA患者集団の偏りを指摘。女性は6.38%で、この集団での性能は低い。前向き評価・独立検証と患者転帰への効果検証が必要としている。

本文の照合箇所: [Resultsの透析転帰・集団偏り、MethodsのData Description・Ground Truth Labels](https://pmc.ncbi.nlm.nih.gov/articles/PMC6722431/)。

### Paper: A data-driven approach to predicting diabetes and cardiovascular disease with machine learning
- Source: PubMed
- Canonical ID: pmid:31694707
- Publication date: 2019-11-06
- URL: https://pubmed.ncbi.nlm.nih.gov/31694707/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: NHANESの質問票・検査情報を使い、糖尿病、前糖尿病、心血管疾患の識別を比較した。
- Objective: 検査の有無による検出性能と、疾患の識別に寄与する調査変数を調べる。
- Methods: ロジスティック回帰、SVM、ランダムフォレスト、勾配ブースティングと加重アンサンブルを評価。木の情報利得で主要変数を抽出した。
- Data and results: 検査なしの心血管AUROCは0.831。糖尿病のXGBoostは検査なし0.862、あり0.957。前糖尿病は検査なしアンサンブル0.737、ありXGBoost0.844。
- Novelty: 検査費用を伴う情報と質問票だけの条件を分け、疾患ごとに実用上の情報価値を比較した。
- Limitations: 編者の注意: 疾患の識別を将来発症予測や因果的危険因子の発見と混同しない。要旨は心血管の検査あり値をaccuracyと表記するため、AUROCとして転載しない。

### Paper: 2018 n2c2 shared task on adverse drug events and medication extraction in electronic health records
- Source: PubMed
- Canonical ID: pmid:31584655
- Publication date: 2020-01-01
- URL: https://pubmed.ncbi.nlm.nih.gov/31584655/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 2018 n2c2は薬剤・有害事象の概念抽出から関係付けまでを共通の臨床文書で評価した。
- Objective: 有害薬剤事象の抽出で到達した性能と、なお苦手な概念・関係を把握する。
- Methods: 退院要約の生テキストから概念抽出、関係分類、端から端までの3課題を設定。参加チームはBiLSTMなどの深層モデル、手作業特徴、SVM、ルール、アンサンブルを用いた。
- Data and results: 概念抽出28チーム、他の2課題は各21チーム。最高F1は0.9418、0.9630、0.8905。理由（Reasons）と有害事象（ADE）の概念・関係では性能が低かった。
- Novelty: 単独の抽出精度と関係分類精度を、実際の一連の抽出処理の精度と分けて比較した。
- Limitations: 著者は局所文脈だけではReasonsやADEを見落とすと指摘し、広い文脈や外部知識の利用を提案。全体F1の高さを全概念の高性能と解釈できない。

### Paper: Prediction of gestational diabetes based on nationwide electronic health records
- Source: PubMed
- Canonical ID: pmid:31932807
- Publication date: 2020-01-13
- URL: https://pubmed.ncbi.nlm.nih.gov/31932807/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: イスラエルの大規模妊娠EHRから、妊娠開始時点の妊娠糖尿病リスクを予測した。
- Objective: 通常24–28週に診断される妊娠糖尿病を、より早い介入が可能な段階で予測する。
- Methods: 588,622妊娠の後ろ向きデータで学習し、将来の時期とエルサレムの地理的検証群で評価。患者が回答できる9質問だけの簡易モデルも作成した。
- Data and results: 妊娠開始時AUROCは0.85、基準リスクスコアは0.68。9質問モデルは0.80。以前の妊娠時の糖負荷検査結果などが予測に寄与した。
- Novelty: 妊娠初期の縦断履歴を活用し、時期・地域を分けた検証と簡易質問票への展開を行った。
- Limitations: 著者は前向き研究と他集団の研究を求める。低リスク群で検査を省略しても安全か、母児の転帰が改善するかは予測精度だけでは示せない。

### Paper: Dynamic and explainable machine learning prediction of mortality in patients in the intensive care unit: a retrospective study of high-frequency data in electronic patient records
- Source: PubMed
- Canonical ID: pmid:33328078
- Publication date: 2020-03-12
- URL: https://pubmed.ncbi.nlm.nih.gov/33328078/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: ICU滞在中に1時間ごとに更新する90日死亡予測を、別病院のデータでも検証した。
- Objective: 入室時だけのスコアより時系列の追加で予測が改善するか、個別の予測理由も提示できるか調べる。
- Methods: デンマーク4ICUの14,190入室・11,492人でRNNを学習し、20%を内部検証に使用。第5病院5,827人で外部検証し、44特徴の寄与をSHAPで表示した。
- Data and results: 内部AUROCは入室時0.73、24時間0.82、72時間0.85、退室時0.88。外部は順に0.75、0.80、0.82、0.83で、外部退室時MCCは0.47。
- Novelty: 静的な重症度評価から、経時的なリスク更新と患者別の特徴寄与を組み合わせた予測へ進めた。
- Limitations: 編者の注意: 遅い時点ほど追加情報を使えるため、入室時モデルとの数値比較には時間条件が必要。SHAPの寄与は治療効果の因果説明ではなく、臨床ツールとして追加検証を要する。

### Paper: BEHRT: Transformer for Electronic Health Records
- Source: PubMed
- Canonical ID: pmid:32346050
- Publication date: 2020-04-28
- URL: https://pubmed.ncbi.nlm.nih.gov/32346050/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: BEHRTは患者の診療系列をTransformerで表現し、将来受診時の多数の疾患を同時予測する。
- Objective: 症状出現後の診断を補うため、過去のEHRから将来の301疾患の発生可能性を推定する。
- Methods: 約160万人の診療記録で系列モデルを学習・評価し、既存の深層EHRモデルと比較。患者・疾患表現と個別の予測解釈も検討した。
- Data and results: 課題ごとのaverage precisionで8.0–13.2%の改善を報告。要旨に疾患別の絶対スコアはなく、これはAUROCの改善値ではない。
- Novelty: Transformerによる患者系列表現、複数疾患予測、事前学習表現の転用を統合した。
- Limitations: 編者の注意: 診断・処方・測定などを取り込める設計上の柔軟性と、全種類を実証したという主張は区別する。予測改善から早期介入の有効性は確定しない。

### Paper: nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation
- Source: PubMed
- Canonical ID: pmid:33288961
- Publication date: 2020-12-07
- URL: https://pubmed.ncbi.nlm.nih.gov/33288961/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: nnU-Netはデータに合わせて前処理・ネットワーク・学習・後処理を設定する画像分割法。
- Objective: 課題ごとに専門家が分割器を設計し直す負担を減らし、安定した強い基準を提供する。
- Methods: 設計を固定パラメータ、依存関係を持つルール、実験で決める選択に整理。新しいデータとハードウェア条件に合わせて全処理を自動構成する。
- Data and results: 国際医用画像分割競技に使われた23公開データセットで、手動介入なしに多くの既存法・専用法を上回った。要旨に課題別Dice値はない。
- Novelty: 新しい層構造だけでなく、実装・前処理・学習設定を含む一式の適応設計を方法論として確立した。
- Limitations: 編者の注意: 23データでの結果を任意の画像・施設への優越性と解釈しない。自動設定でも通常の学習用計算資源と正解ラベルを要し、臨床判断の有効性とは別である。

### Paper: Med-BERT: pretrained contextualized embeddings on large-scale structured electronic health records for disease prediction
- Source: PubMed
- Canonical ID: pmid:34017034
- Publication date: 2021-05-20
- URL: https://pubmed.ncbi.nlm.nih.gov/34017034/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: Med-BERTは構造化EHRで事前学習し、少数患者での疾患予測を改善するモデル。
- Objective: 施設内の学習患者数が少ないときにも、広範な事前学習から臨床予測の精度を得る。
- Methods: BERTを構造化診療記録へ適応し、28,490,650人のEHRで文脈表現を事前学習。2つの臨床データベースにある2疾患予測課題で微調整した。
- Data and results: 要旨はAUCの改善を1.21–6.14%と報告。少数データ条件では20%超の改善、または事前学習なしで10倍の学習例を使うモデルに匹敵するAUCを報告した。
- Novelty: 自然言語の事前学習・微調整という流れを、大規模な構造化EHRの転移学習へ展開した。
- Limitations: 編者の注意: 改善率は原著の%表記を保持し、百分率ポイントへ読み替えない。10倍のデータ効率は特定実験の結果で、あらゆる疾患・施設への保証ではない。

### Paper: Identifying who has long COVID in the USA: a machine learning approach using N3C data
- Source: PubMed
- Canonical ID: pmid:35589549
- Publication date: 2022-05-16
- URL: https://pubmed.ncbi.nlm.nih.gov/35589549/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: N3Cの診療記録からlong COVID専門診療の対象になり得る患者を抽出した研究。
- Objective: 定義や症状が変化するlong COVIDについて、診療・臨床試験へつなぐ候補患者を見つける。
- Methods: 感染後90日以上の成人を基礎集団とし、97,995人の特徴と専門外来597人を使いXGBoostを学習。全体・入院・非入院の3モデルを作り、第4施設でも検証した。
- Data and results: AUROCは全体0.92、入院0.90、非入院0.85。医療利用頻度、年齢、呼吸困難などがShapley値で重要だった。
- Novelty: 確定した病名定義が乏しい段階で、専門外来の利用を代理指標として大規模EHRから候補を探索した。
- Limitations: 著者は出力を専門外来での診療を要する可能性の指標と解釈する。編者の注意: 確定診断ではなく、医療アクセスや受診行動の違いを反映する可能性がある。

### Paper: Illusory generalizability of clinical prediction models
- Source: PubMed
- Canonical ID: pmid:38207039
- Publication date: 2024-01-11
- URL: https://pubmed.ncbi.nlm.nih.gov/38207039/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 統合失調症の治療転帰モデルが、開発試験内での高性能を他の臨床試験へ移せないことを示した。
- Objective: 少数のデータや臨床状況で成功した予測器を、一般的な治療意思決定に使えるという期待を検証する。
- Methods: 抗精神病薬の複数の独立臨床試験で転帰予測を比較。試験内、別試験への適用、複数試験を統合して除外試験を予測する条件を評価した。
- Data and results: 開発試験内では高精度だったが、別試験では偶然を上回らず、複数試験の統合でも改善しなかった。要旨に試験数や精度の具体値はない。
- Novelty: 内部検証の成功と、臨床状況をまたぐ汎化の間の隔たりを独立試験群で直接検証した。
- Limitations: 編者の注意: 統合失調症治療という検証範囲の結果であり、すべての医療予測器が汎化不能とする証拠ではない。予測対象と試験条件を伴って読む必要がある。

### Paper: MySurgeryRisk: Development and Validation of a Machine-learning Risk Algorithm for Major Complications and Death After Surgery
- Source: PubMed
- Canonical ID: pmid:29489489
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/29489489/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: MySurgeryRiskは術前EHRから8種の合併症と術後死亡を予測する枠組み。
- Objective: 手術前の情報だけで、大きな術後合併症と長期死亡の患者別確率を推定する。
- Methods: 単施設の主要入院手術51,457人でモデルを開発・検証。腎障害、敗血症、血栓塞栓、長期ICU・人工呼吸、創部・神経・心血管合併症を扱い、AUCとpredictiveness curveで評価した。
- Data and results: 合併症のAUCは0.82–0.94、術後1・3・6・12・24か月の死亡は0.77–0.83。要旨は99%信頼区間も報告する。
- Novelty: 個別の術後リスク評価を、既存の術前診療情報から自動で複数転帰へ拡張した。
- Limitations: 著者は実時間の臨床業務への導入可能性に追加検証が必要とする。編者の注意: 単施設での識別性能であり、手術方針変更の利益は評価していない。
- Publication date note: 日単位の公開日は一次書誌に未記録。巻号の刊行年月は 2019 Apr。索引登録日や便宜的な月初日は公開日として採用しない。出典: https://pubmed.ncbi.nlm.nih.gov/29489489/

### Paper: Predicting Pressure Injury in Critical Care Patients: A Machine-Learning Model
- Source: PubMed
- Canonical ID: pmid:30385537
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/30385537/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 外科重症患者のEHRから褥瘡を予測し、手入力の評価尺度を補う方法を検討した。
- Objective: 費用の高い予防用ベッドなどを優先するため、褥瘡の高リスク患者を記録から特定する。
- Methods: 6,376人を学習67%、テスト33%に分割。ランダムフォレストでステージ1以上と2以上の院内褥瘡をそれぞれ予測した。
- Data and results: ステージ1以上は516人（8.1%）、2以上は257人（4.0%）。両モデルのテストAUROCは0.79だった。
- Novelty: Braden尺度などへの追加入力を必要とせず、すでにEHRにある情報でリスクを計算する。
- Limitations: 著者は独立標本での検証と特異度を調整する校正を次の課題とする。編者の注意: 予防用ベッドを割り当てた際の褥瘡減少は検証していない。
- Publication date note: 日単位の公開日は一次書誌に未記録。巻号の刊行年月は 2018 Nov。索引登録日や便宜的な月初日は公開日として採用しない。出典: https://pubmed.ncbi.nlm.nih.gov/30385537/

### Paper: GRAM: Graph-based Attention Model for Healthcare Representation Learning
- Source: PubMed
- Canonical ID: pmid:33717639
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/33717639/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: GRAMは医学オントロジーの上位概念をattentionで混合し、少数の診療コードを表現する。
- Objective: 学習例の乏しい疾患の予測と、医学知識に沿う患者・疾患表現を両立する。
- Methods: EHRの概念とその祖先概念を階層上で重み付け。2つの逐次診断予測と心不全予測で、基本RNNなどと精度・必要データ量・解釈性を比較した。
- Data and results: 希少な疾患の予測精度を10%改善。心不全では1桁少ない学習データでAUROCを3%改善と要旨は報告し、下位概念のデータ不足時に上位概念を利用する挙動を示した。
- Novelty: 知識階層を固定特徴として加えるだけでなく、データ量に応じて概念の抽象度を学習する。
- Limitations: 編者の注意: 精度・AUROCの%は原著表記で、絶対ポイントに変換しない。オントロジーとの整合は臨床上の因果説明や安全な介入を保証しない。
- Publication date note: 日単位の公開日は一次書誌に未記録。巻号の刊行年月は 2017 Aug。索引登録日や便宜的な月初日は公開日として採用しない。出典: https://pubmed.ncbi.nlm.nih.gov/33717639/

<!-- PAPER_IDS -->
pmid:23842533
pmid:26679719
pmid:27185194
pmid:27521897
pmid:28117445
pmid:27784047
pmid:29500022
pmid:29382633
pmid:29709069
pmid:31304302
pmid:31209213
pmid:31367026
pmid:31694707
pmid:31584655
pmid:31932807
pmid:33328078
pmid:32346050
pmid:33288961
pmid:34017034
pmid:35589549
pmid:38207039
pmid:29489489
pmid:30385537
pmid:33717639
<!-- /PAPER_IDS -->
