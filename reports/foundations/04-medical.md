# 基礎文献 — 医療・生体信号・創薬AI

> schema_version: 1
> report_date: 2026-11-15

## ダイジェスト

選定139件中、以下は原著照合・編集確認を終えた139件。選定リストだけの論文を完成済み件数には含めない。原著要旨までの記述と本文確認を区別し、Limitationsの「編者の注意」は著者の自己申告と区別する。

研究の流れと2026年論文との接続は [文献集の案内](README.md) を参照。

## 完全版レポート

### Paper: Unlocking clinical data from narrative reports: a study of natural language processing
- Source: PubMed
- Canonical ID: pmid:7702231
- Publication date: 1995-05-01
- URL: https://pubmed.ncbi.nlm.nih.gov/7702231/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 胸部X線レポートから6所見を抽出し、NLPと医師の間の不一致を医師間の不一致と比較した。
- Objective: 文章に含まれる病態の自動検出が、医師による記録解釈にどこまで近いか調べる。
- Methods: 入院時レポート200件で、汎用NLP、内科医6人、放射線科医6人、一般人6人、他3手法を比較。1文書あたりの不一致所見数と、医師多数決への感度・特異度を測った。
- Data and results: 医師間の平均距離0.24、NLP対医師0.26で有意差なし。NLPの感度81%、特異度98%、医師平均は85%・98%。一般人と他手法の不一致は大きかった。
- Novelty: 人の解釈自体に不一致があることを踏まえ、自動抽出の妥当性を相対的に評価した。
- Limitations: 著者も胸部画像レポートの6所見に限定された領域とする。編者の注意: 画像の診断研究ではなく文章の抽出研究で、他の記録形式への一般化は未確定。

### Paper: Use of natural language processing to translate clinical information from a database of 889,921 chest radiographic reports
- Source: PubMed
- Canonical ID: pmid:12091676
- Publication date: 2002-07-01
- URL: https://pubmed.ncbi.nlm.nih.gov/12091676/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 約89万件の胸部X線レポートを構造化し、抽出精度と大規模な所見分布を検証した。
- Objective: 文章の画像診断記録を研究用データベースへ変換し、コード情報より豊かな病態把握を得る。
- Methods: 単一都市部大学病院の10年分、251,186人の889,921レポートをNLPでコード化。150件を手動確認し、24状態の頻度・併存と既報の疫学傾向を比較した。
- Data and results: 手動比較で感度0.81、特異度0.99。別の気胸確認ではNLP感度1.00対退院会計コード0.17、特異度は双方0.996。肺癌の右左比3:2など既報との一致も報告した。
- Novelty: 小標本の抽出評価に加え、大規模な文章由来データの内的・外的な整合性を検証した。
- Limitations: 編者の注意: 疫学的な傾向の一致は各記録の正確さを保証しない。単施設の画像報告書が対象であり、実画像の診断や未記録疾患の検出を行うものではない。
- Publication date note: RSNAの掲載履歴Published online: Jul 1 2002を採用。推測の月初日ではなく出版社の明示日。出典: https://pubs.rsna.org/doi/10.1148/radiol.2241011118

### Paper: Automated encoding of clinical documents based on natural language processing
- Source: PubMed
- Canonical ID: pmid:15187068
- Publication date: 2004-06-07
- URL: https://pubmed.ncbi.nlm.nih.gov/15187068/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: MedLEEの構造化出力をUMLSコードと修飾情報へ写像し、文章の検索可能性を高めた。
- Objective: 臨床文書の所見を最も具体的な概念コードへ、自動で修飾情報も保持して変換する。
- Methods: MedLEEが抽出する所見・修飾を照合してコードを生成。再現率と適合率を別々の無作為150文で測り、7専門家の参照と比較した。
- Data and results: 全用語のコード再現率0.77、対応UMLSコードのある用語では0.83。用語抽出の再現率0.84、コード適合率0.89で、専門家間の性能範囲に近かった。
- Novelty: 単語にコードを貼るだけでなく、構造化された臨床所見と関連修飾をコード化へ接続した。
- Limitations: 編者の注意: 再現率・適合率は異なる文集合で測定され、文書全体の正確さとは異なる。辞書にコードがない用語の扱いと他施設への適用は別途検討が必要。

### Paper: Noninvasive brain-actuated control of a mobile robot by human EEG
- Source: PubMed
- Canonical ID: pmid:15188874
- Publication date: 2004-06-30
- URL: https://pubmed.ncbi.nlm.nih.gov/15188874/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 非侵襲EEGの3状態分類とロボット側の自律性を組み合わせ、室間の移動制御を実演した。
- Objective: 遅いと考えられていた非侵襲信号でも、移動ロボットの複雑な動きを制御できるか調べる。
- Methods: 非同期EEG解析と機械学習で3つの精神状態を認識し、高度なロボティクスと統合。2人が思考のみで複数の部屋を移動させ、手動制御と比較した。
- Data and results: 2被験者が移動を達成し、手動制御との性能比0.74を報告。要旨に比の詳細な定義、所要時間、試行数はない。
- Novelty: 連続した低位の運動指令を脳から送る代わりに、EEGの少数状態とロボット制御を組み合わせた。
- Limitations: 編者の注意: 2人の実演であり、患者集団や屋外環境の一般的な実用性は未検証。0.74を分類精度74%へ読み替えない。
- Publication date note: IEEEのDate of Publication: 30 June 2004を採用。出典: https://ieeexplore.ieee.org/abstract/document/1300798/authors

### Paper: Causal protein-signaling networks derived from multiparameter single-cell data
- Source: PubMed
- Canonical ID: pmid:15845847
- Publication date: 2005-04-22
- URL: https://pubmed.ncbi.nlm.nih.gov/15845847/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 単一細胞の多項目測定と分子介入から、シグナル伝達の因果ネットワークを推定した。
- Objective: 細胞内経路の方向付きの影響を、個別の既知経路に限定せずデータから再構成する。
- Methods: 数千の一次ヒト免疫細胞で複数のリン酸化タンパク質・リン脂質を同時計測。分子介入の情報とベイズネットワークを使い、経路の結び付きを推定した。
- Data and results: 既報の関係の多くを回復し、新しい経路間の因果関係を予測して実験確認した。要旨に辺ごとの精度や測定項目数はない。
- Novelty: 集団平均の相関ではなく、単一細胞の多変量分布と介入を因果探索へ接続した代表例。
- Limitations: 編者の注意: 因果解釈は介入の特異性、測定した変数、ネットワーク仮定に依存する。免疫細胞の条件下での結果を全組織・全シグナルへ一般化しない。

### Paper: Natural language processing to extract medical problems from electronic clinical documents: performance evaluation
- Source: PubMed
- Canonical ID: pmid:16359928
- Publication date: 2005-12-05
- URL: https://pubmed.ncbi.nlm.nih.gov/16359928/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: MetaMapと否定検出から問題リスト候補を抽出し、施設用語への調整の効果を測った。
- Objective: 診療文章から病態を拾い、患者の問題リストをより完全で新しい状態に保つ。
- Methods: UMLS MetaMap Transfer（MMTx）とNegExを使い、施設で頻用される80の問題を抽出。既定の辞書データと用途に絞った独自サブセットを比較した。
- Data and results: 既定では再現率0.740、適合率0.756。独自サブセットで速度が上がり、再現率は0.896へ有意に改善、適合率の低下は非有意だった。
- Novelty: 概念辞書と否定文の解釈を組み合わせ、施設に合わせた語彙範囲の調整が有効と示した。
- Limitations: 編者の注意: 対象は施設で選んだ80病態で、自由な全疾患抽出ではない。問題リスト候補の抽出性能と、医師が承認した最終リストの正確さは異なる。

### Paper: Machine learning for real-time single-trial EEG-analysis: from brain-computer interfacing to mental state monitoring
- Source: PubMed
- Canonical ID: pmid:18031824
- Publication date: 2007-09-29
- URL: https://pubmed.ncbi.nlm.nih.gov/18031824/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: BBCIの前処理・分類と、文字入力・覚醒度監視への応用を概説した方法論的論文。
- Objective: 個人内外の変動が大きいEEGを、少ない利用者訓練で実時間の単試行解析へ使う。
- Methods: Berlin BCIの信号処理・機械学習を説明し、Hex-o-Spell文字入力と実時間の覚醒度モニタリング実験を紹介した。
- Data and results: Hex-o-Spellで毎分6–8文字の通信速度を報告。覚醒度監視の結果も提示するが、要旨に対象数・精度の具体値はない。
- Novelty: BCIの分類器だけでなく、少ない利用者訓練で使う実時間の対話用途へ結び付けた。
- Limitations: 編者の注意: 手法・応用の概説を含み、単一の無作為比較試験ではない。文字入力速度は課題と利用者に依存し、医療診断や長期使用の有効性は示さない。

### Paper: EEG-based neonatal seizure detection with Support Vector Machines
- Source: PubMed
- Canonical ID: pmid:20713314
- Publication date: 2010-08-14
- URL: https://pubmed.ncbi.nlm.nih.gov/20713314/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 新生児の連続EEGで、発作検出率と毎時の偽警報数の交換関係を示したSVM検出器。
- Objective: 患者ごとの専用学習なしに、NICUでの発作確認を支援する。
- Methods: 多チャネルEEG区間をSVMで分類し、2段階の後処理で時間的精度・頑健性を改善。発作のある正期産新生児17人、計267時間で事象単位評価を行った。
- Data and results: 平均検出率は偽警報毎時1件で約89%、2件で約96%、4件で約100%。見逃しと偽検出の原因も分析した。
- Novelty: 区間accuracyに限らず、臨床の警報負担に直結する事象検出率と毎時誤警報を提示した。
- Limitations: 編者の注意: 正期産で発作を持つ17人の評価で、早産児や発作のない大集団での性能は別途必要。検出100%という値も毎時4件の偽警報条件を伴う。

### Paper: Automatic classification of artifactual ICA-components for artifact removal in EEG signals
- Source: PubMed
- Canonical ID: pmid:21810266
- Publication date: 2011-08-02
- URL: https://pubmed.ncbi.nlm.nih.gov/21810266/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: ICAで分けたEEG成分を6特徴の線形分類器で判定し、アーチファクト除去を自動化した。
- Objective: 目・筋由来などの妨害成分を、人や電極配置が変わっても取り除く。
- Methods: TDSEPで成分分離し、周波数・空間・時間特徴からLPMで選択。12人の640注釈成分で学習、1,080成分でテストし、別ERP18人とBCI80人でも汎化を評価した。
- Data and results: 6特徴だけで専門家間の不一致の水準に近い性能を報告。異なる研究・電極設定でも動作したが、要旨の数値結果は一部欠落しており誤り率は補わない。
- Novelty: 個人のアーチファクト専用記録に依存せず、解釈しやすい少数の線形特徴で成分を選別した。
- Limitations: 編者の注意: 成分の判定一致は、必要な脳信号を失わない保証ではない。適用先での電極、課題、専門家ラベルの差を点検する必要がある。

### Paper: Automated identification of postoperative complications within an electronic medical record using natural language processing
- Source: PubMed
- Canonical ID: pmid:21862746
- Publication date: 2011-08-24
- URL: https://pubmed.ncbi.nlm.nih.gov/21862746/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 術後合併症を診療文書から抽出すると、退院コードだけの監視より多くの事例を拾えた。
- Objective: 患者安全上のイベントを、行政コードに加えて自由記載から把握する価値を調べる。
- Methods: VHA6施設の入院手術患者2,974人を横断解析。記録レビューを基準に、透析を要する腎不全、血栓塞栓、敗血症、肺炎、心筋梗塞をNLPと退院コード指標で比較した。
- Data and results: 感度はNLP対コードで腎不全82%対38%、肺炎64%対5%、敗血症89%対34%、心筋梗塞91%対89%。双方とも高い特異度だが、NLPは相対的に低かった。
- Novelty: 診断コードに記録されにくい合併症を、文章を使う追加監視経路で捕捉した。
- Limitations: 編者の注意: 過去の合併症を同定する研究であり、発症前の予測ではない。VHAの記録に基づく感度向上と、特異度低下・確認作業の増加を併せて評価する必要がある。

### Paper: Fast and accurate modeling of molecular atomization energies with machine learning
- Source: PubMed
- Canonical ID: pmid:22400967
- Publication date: 2012-01-31
- URL: https://pubmed.ncbi.nlm.nih.gov/22400967/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 核電荷と原子位置から分子の原子化エネルギーを回帰し、量子計算を近似した初期研究。
- Objective: 分子のSchrödinger方程式を毎回解く代わりに、低い計算負担でエネルギーを推定する。
- Methods: 有機分子の幾何と元素情報を入力し、hybrid密度汎関数理論による原子化エネルギーを非線形回帰で学習。7,000超の分子で交差検証した。
- Data and results: 平均絶対誤差は約10kcal/mol。分子の原子化ポテンシャルエネルギー曲線の予測も示した。
- Novelty: 量子化学の計算結果を分子間で学ぶ統計的な近似器へ置き換える方向を示した。
- Limitations: 編者の注意: 正解も特定の密度汎関数計算であり、実験値への誤差と同じではない。学習外の元素・分子規模・構造での精度は別途必要。

### Paper: Risk prediction models: II. External validation, model updating, and impact assessment
- Source: PubMed
- Canonical ID: pmid:22397946
- Publication date: 2012-03-07
- URL: https://pubmed.ncbi.nlm.nih.gov/22397946/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 臨床予測器の外部検証、現地への更新、導入効果の検証を段階として整理した方法論文。
- Objective: モデルを作った後、臨床で使うまでに必要な評価と調整を明確にする。
- Methods: 循環器領域の実例を使い、新しい患者での予測評価、施設条件や新因子に合わせる更新、意思決定・患者転帰に対するimpact studyを解説した。
- Data and results: 外部検証で確率予測の妥当性を確認し、その後に利用による診療・転帰・費用効果を調べる枠組みを提示。要旨に統合した効果量はない。
- Novelty: モデル開発の成功から臨床導入へ直結せず、移植・更新・介入の評価を分ける道筋を示した。
- Limitations: 編者の注意: 方法論的な概説で、特定モデルの有効性を保証しない。外部予測性能がよくても、導入後の行動変化や患者への利益は実測が必要。

### Paper: The feasibility of using natural language processing to extract clinical information from breast pathology reports
- Source: PubMed
- Canonical ID: pmid:22934236
- Publication date: 2012-06-30
- URL: https://pubmed.ncbi.nlm.nih.gov/22934236/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 3施設の多数の乳房病理報告を構造化し、同じ診断や否定の多様な表現を分析した。
- Objective: 自由記載の乳房病理情報を、研究や意思決定支援に使える形式へ変換できるか調べる。
- Methods: 76,000超の報告をNLPで解析し、手術日・左右・記録番号で表へ整理。診断ごとの表現を調べ、専門家コードと感度・特異度を比較した。
- Data and results: 浸潤性乳管癌の表現124通り、小葉癌95通り、乳管癌がない表現は4,000超。専門家との比較で感度99.1%、特異度96.5%だった。
- Novelty: 大規模な複数施設の病理文章で、表現と否定の多様性を定量的に示しながら構造化した。
- Limitations: 編者の注意: 要旨には性能評価用標本数や診断別誤差はない。全報告数をそのまま手動検証数と読み替えず、別施設の文章への適用は再評価が必要。

### Paper: External validation of a Cox prognostic model: principles and methods
- Source: PubMed
- Canonical ID: pmid:23496923
- Publication date: 2013-03-06
- URL: https://pubmed.ncbi.nlm.nih.gov/23496923/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 公開されたCox予後モデルを、得られる情報の量に応じて外部検証する統計手順。
- Objective: 基準生存関数が明示されないことの多いCoxモデルで、識別と校正を適切に評価する。
- Methods: 予後指数のみ、指数とリスク群のKaplan–Meier曲線、さらに基準生存曲線がある3段階を区別。基準生存関数の近似と確率プロットを提案し、乳癌2データで例示した。
- Data and results: 開発群と検証群を分け、識別と校正の評価を実演。絶対確率の校正には最も詳しい第3段階の情報が必要と説明する。
- Novelty: 係数だけの移植で済ませず、公開情報不足が外部検証のどの部分を制約するか明示した。
- Limitations: 編者の注意: 欠けた基準関数の近似には情報と仮定が要る。乳癌の実例の結果を他疾患のモデル性能と扱わず、比例ハザード等のモデル仮定も確認する。

### Paper: Improving case definition of Crohn's disease and ulcerative colitis in electronic medical records using natural language processing: a novel informatics approach
- Source: PubMed
- Canonical ID: pmid:23567779
- Publication date: 2013-04-04
- URL: https://pubmed.ncbi.nlm.nih.gov/23567779/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 炎症性腸疾患の症例同定に、診断コードと診療ノートのNLP特徴を組み合わせた。
- Objective: 行政コードだけでは一貫しなかったCrohn病・潰瘍性大腸炎のEHR上の症例定義を改善する。
- Methods: 2大学施設でICD-9コードを持つ患者を抽出し、各疾患600人の記録レビューを基準に開発・検証。コード・処方・文章特徴をadaptive LASSO回帰で選択した。
- Data and results: 確認症例はCrohn病399人、潰瘍性大腸炎378人。統合AUC0.95・0.94に対しコードのみ0.89・0.86。同じ精度で6–12%多くの患者を分類できた。
- Novelty: コード化データと自由記載を相補的に使い、研究コホートの症例数と精度を両立した。
- Limitations: 編者の注意: 既に少なくとも1つ診断コードがある集団の症例同定であり、一般集団での新規診断や発症予測ではない。コードのない症例の捕捉性能は分からない。
- Publication date note: 出版社版PDFに明記されたPublished online 4 April 2013を採用。巻号の2013年6月と区別。出典: https://academic.oup.com/ibdjournal/article-pdf/19/7/1411/23424044/ibd1411.pdf

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

### Paper: A new framework to enhance the interpretation of external validation studies of clinical prediction models
- Source: PubMed
- Canonical ID: pmid:25179855
- Publication date: 2014-08-30
- URL: https://pubmed.ncbi.nlm.nih.gov/25179855/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 外部検証の結果を、開発群と検証群の患者構成差を踏まえて解釈する3段階の枠組み。
- Objective: 同じ『外部検証』でも、再現性の確認と大きく異なる集団への移植を区別する。
- Methods: case-mixの違いで集団の関連性を定量化し、性能を解釈、必要なら更新する。深部静脈血栓症モデルを3つの異なる検証標本で例示した。
- Data and results: 1標本は主に再現性、2標本は移植性を検証した。各群の性能は適切で、大幅な更新を要しなかった。要旨にAUC・校正の具体値はない。
- Novelty: 単一のスコア差を良否判定せず、患者構成の違いとモデルの更新を一連の解釈に含めた。
- Limitations: 編者の注意: 提案の実例は1疾患モデルである。case-mixの差だけですべての性能変化を説明できず、測定・治療・ラベルの違いも確認が必要。

### Paper: External validation of new risk prediction models is infrequent and reveals worse prognostic discrimination
- Source: PubMed
- Canonical ID: pmid:25441703
- Publication date: 2014-10-23
- URL: https://pubmed.ncbi.nlm.nih.gov/25441703/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 新規予測器の外部検証は少なく、独立検証では識別性能が落ちる傾向を調べたレビュー。
- Objective: 新規リスク予測モデルは開発集団では高い識別精度を出しやすいが、別集団で確かめなければ予測を持ち運べるか分からない。モデル発表後、実際にどの程度の外部検証が行われ、成績は開発時からどう変わったのかを定量化した。
- Methods: 選定された127の新規予測モデルを追跡し、後続研究に外部集団での検証があるか、その著者が開発者と独立しているか、開発時と検証時のAUCがどれくらい異なるかを比較した。時間を追った外部検証の実施確率も調べ、単に『検証した論文がある』だけではなく検証者の独立性を区別した。
- Data and results: 127モデル中32（25%）に何らかの外部検証があり、開発者と異なる著者による検証は22（17%）。モデル発表後5年以内に独立検証される確率は16%。外部集団でのAUCの中央値は開発時より0.05低かった。モデルの性能上昇報告と、未知集団でも同じ精度を保つことの間には実質的な隔たりがあった。
- Novelty: 外部検証の不足を定性的に批判するだけでなく、モデル開発と検証の実績・独立性・識別性能低下を同時に計測した。未知データでの性能を議論する際、最初の高精度より再現性と分布移動への頑健性を重視すべきという根拠になる。
- Limitations: 対象年代・研究領域に限定した調査で、2026年の全予測研究にそのまま検証率を当てはめられない。外部AUCの低下は患者構成の違いにも依存し、原モデルが必ず過学習していたことだけを意味しない。

### Paper: Transparent Reporting of a multivariable prediction model for Individual Prognosis or Diagnosis (TRIPOD): explanation and elaboration
- Source: PubMed
- Canonical ID: pmid:25560730
- Publication date: 2015-01-06
- URL: https://pubmed.ncbi.nlm.nih.gov/25560730/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: TRIPODの解説文書は、予測モデル報告に必要な22項目の理由と適切な記載例を説明する。
- Objective: 診断・予後モデルの開発、検証、更新を読者が評価できるよう、報告を透明にする。
- Methods: TRIPODの各項目を詳しく解説し、既刊論文の良い報告例とともに、バイアスや臨床有用性を判断するための情報を示した。
- Data and results: 22項目の意味・根拠・例を提供。新しい予測器の精度を試験した論文ではなく、報告と研究設計を支える方法論文書である。
- Novelty: 短いチェックリストを実際の執筆・査読へ使えるよう、項目ごとの理由と実例へ展開した。
- Limitations: 編者の注意: 報告が完全でも研究のバイアスや臨床利益が自動的に解消するわけではない。2015年版の解説として読み、後年のAI拡張とは区別する。

### Paper: Transparent reporting of a multivariable prediction model for individual prognosis or diagnosis (TRIPOD): the TRIPOD statement
- Source: PubMed
- Canonical ID: pmid:25569120
- Publication date: 2015-01-07
- URL: https://pubmed.ncbi.nlm.nih.gov/25569120/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: TRIPOD声明は診断・予後の多変量予測モデルを透明に報告する22項目を定めた。
- Objective: 予測モデルの研究論文では、どの患者を対象にどの入力情報を使い、欠測や内部検証をどう扱ったのかが省略されることがあり、読者が妥当性を再評価できない。診断・予後モデルに共通して必要な報告内容を揃えることが目的である。
- Methods: 既存の報告指針と実証研究から候補項目を収集し、Web調査と2011年の3日間の専門家会議、その後の運営委員会の反復検討を通じて合意を形成した。機械学習か回帰かといったモデル種類でなく、研究の目的、対象集団、候補予測因子、欠測、モデル構築・性能評価、解釈などの報告手続きを対象にしている。
- Data and results: 診断・予後のモデル開発、外部検証、更新研究で共有できる22項目のTRIPODチェックリストを策定し、説明文書を提示した。新規患者で予測のAUCや転帰が改善した『介入効果』の報告ではなく、第三者が手続きと結果を検証できるようにするための報告標準が成果である。
- Novelty: モデルの精度を比較する論文の再現性と評価可能性を改善するため、研究デザイン・欠測・校正・外部検証などを明示させる共通の枠組みを提供した。論文要約でも性能の数字だけでなく、評価の条件を残す重要性を示す。
- Limitations: 報告指針を満たすことは、手法が正しい、過学習がない、患者に利益があると証明することと異なる。TRIPODは論文の内容を透明化するルールであり、モデルの性能を保証する採点尺度ではない。

### Paper: An overview of the BIOASQ large-scale biomedical semantic indexing and question answering competition
- Source: PubMed
- Canonical ID: pmid:25925131
- Publication date: 2015-04-30
- URL: https://pubmed.ncbi.nlm.nih.gov/25925131/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: BioASQの初回競技は医学索引付けと、根拠検索から回答生成までを共通基盤で評価した。
- Objective: 医学の自然言語質問に対し、論文・オントロジーを使って簡潔で理解可能な回答を返す技術を比較する。
- Methods: 2013年競技でPubMed新規文書のMeSH自動付与とQAを設定。QAは専門家が作った開発29問・テスト282問で、exact回答と段落形式のideal回答などを評価した。
- Data and results: 索引付け12チーム46実行のうち1チームがNLMのMTIを継続的に上回った。QAは3チーム11実行で、ideal回答の手動評価が良好と報告。要旨に数値スコアはない。
- Novelty: 索引、文書・断片・知識検索、短答、要約を、医学QAの一連の構成要素として共通評価した。
- Limitations: 編者の注意: 初回競技の限られた質問と参加数の結果である。医学専門家向けQAの性能を患者への個別助言の安全性と同一視できない。

### Paper: U-Net: Convolutional Networks for Biomedical Image Segmentation
- Source: arXiv
- Canonical ID: arxiv:1505.04597
- Publication date: 2015-05-18
- URL: https://arxiv.org/abs/1505.04597
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: U-Netは文脈を集める縮小経路と位置を復元する拡大経路を持つ、少数注釈向け画像分割器。
- Objective: 大量の正解画像を用意しにくい生体画像で、精密な画素単位の分割を学習する。
- Methods: 対称的な縮小・拡大構造をend-to-endで訓練し、強いデータ拡張で注釈例を活用。電子顕微鏡の神経構造と、位相差・DIC細胞画像で評価した。
- Data and results: ISBIの神経構造分割で先行するsliding-window CNNを上回り、2015細胞追跡競技の対象カテゴリでも優勝。512×512画像を当時のGPUで1秒未満に分割した。
- Novelty: 分類用CNNを画素ごとに繰り返す処理から、文脈と精密な位置をまとめて出力する分割構造へ進めた。
- Limitations: 編者の注意: 少数注釈でも対象の代表性と拡張の妥当性は必要。競技成績と当時のGPU速度を任意の臨床画像や計算環境へ一般化しない。

### Paper: Challenges in clinical natural language processing for automated disorder normalization
- Source: PubMed
- Canonical ID: pmid:26187250
- Publication date: 2015-07-14
- URL: https://pubmed.ncbi.nlm.nih.gov/26187250/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: DNorm-Cは臨床文章の多様な疾患表現を抽出し、対応する標準概念へ正規化する。
- Objective: 医学論文より臨床記録で疾患抽出・正規化が難しい理由と、語彙的な改善方法を調べる。
- Methods: 語彙の豊かさを比較し、CRFで言及範囲を認識、pairwise learning to rankで語の変形と概念の対応を学習。ShARe/CLEF臨床文章で評価した。
- Data and results: 範囲のみの厳密F1は0.753、範囲と概念の一致は0.672。改善は各0.039、0.036。認識誤りは正規化誤りの4倍超で、略語が頻繁な原因だった。
- Novelty: 抽出と概念対応の誤りを分解し、臨床特有の語彙変動を学習する正規化法を提案した。
- Limitations: 高再現率版では正規化再現率0.744に上がる一方、適合率が下がる。編者の注意: 標準語彙に概念がない例もあり、辞書照合だけで解消できる問題ではない。

### Paper: Searching molecular structure databases with tandem mass spectra using CSI:FingerID
- Source: PubMed
- Canonical ID: pmid:26392543
- Publication date: 2015-09-21
- URL: https://pubmed.ncbi.nlm.nih.gov/26392543/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: CSI:FingerIDは質量スペクトルから分子指紋を推定し、構造データベースを検索する。
- Objective: 未知の代謝物が多数残る非標的メタボローム解析で、小分子の同定を改善する。
- Methods: tandem MSから観測を説明するfragmentation treeを作り、機械学習で構造fingerprintを予測。その指紋でPubChemなどの分子構造データベースを検索する。
- Data and results: 計算による代謝物同定で競合法を大きく上回ったと報告。要旨に正解率、候補順位、標本数はない。
- Novelty: スペクトルから直接構造を生成するのではなく、学習した構造指紋を介して既知構造候補を探索する。
- Limitations: 編者の注意: 検索可能な候補データベースへの依存があり、候補にない分子の確定構造決定とは異なる。スペクトル条件や異性体の識別性能も確認が必要。

### Paper: Deep Residual Learning for Image Recognition
- Source: arXiv
- Canonical ID: arxiv:1512.03385
- Publication date: 2015-12-10
- URL: https://arxiv.org/abs/1512.03385
- read_level: full_text
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: ResNetは入力からの差分を学ぶ残差構造により、非常に深い画像ネットワークを訓練可能にした。
- Objective: 深さを増すと最適化が難しくなる問題を減らし、表現の深さによる精度改善を得る。
- Methods: 層の変換を入力に対する残差として定式化。ImageNetで152層まで、CIFAR-10で100・1,000層を分析し、物体検出にも転用した。
- Data and results: 残差ネットのアンサンブルはImageNetテストのtop-5 error3.57%でILSVRC2015分類優勝。COCO検出では28%の相対改善を報告した。
- Novelty: 深層化を単なる層追加から、恒等経路に対する修正を学ぶ最適化しやすい構造へ変えた。医用画像のbackboneにもつながる。
- Limitations: 編者の注意: 3.57%はアンサンブルのtop-5誤り率で、単一モデルのtop-1精度ではない。一般画像の結果であり、医療診断の有効性を直接示さない。

本文の照合箇所: [Section 4.1の比較とTable 5に対応するtop-5 error・アンサンブル条件](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)。

### Paper: Locality Sensitive Deep Learning for Detection and Classification of Nuclei in Routine Colon Cancer Histology Images
- Source: PubMed
- Canonical ID: pmid:26863654
- Publication date: 2016-02-04
- URL: https://pubmed.ncbi.nlm.nih.gov/26863654/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 大腸癌病理で核中心を検出し、近隣の予測を利用して核の種類を分類する方法。
- Objective: 細胞の多様性が大きいH&E画像で、核の精密な分割なしに位置と分類を推定する。
- Methods: SC-CNNで核中心付近に高確率が集まるよう回帰し、CNNとNeighboring Ensemble Predictorで分類。4クラス、2万超の注釈核を含む大腸腺癌画像で比較した。
- Data and results: 検出と分類の組合せで、比較した近年の手法中で最良の平均F1を報告。要旨にF1の具体値やクラス別結果はない。
- Novelty: 核の境界分割を前提にせず、空間的制約付き中心検出と近隣を使う分類を接続した。
- Limitations: 編者の注意: 大腸腺癌の注釈画像での結果であり、他臓器や染色条件の変化に対する性能は要旨から不明。定量的組織解析の臨床利益は将来の可能性である。

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

### Paper: Lung Pattern Classification for Interstitial Lung Diseases Using a Deep Convolutional Neural Network
- Source: PubMed
- Canonical ID: pmid:26955021
- Publication date: 2016-02-29
- URL: https://pubmed.ncbi.nlm.nih.gov/26955021/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 間質性肺疾患のCTパッチを、手作業特徴に代えてCNNで7パターンに分類した。
- Objective: 肺の複雑な組織パターンを自動識別し、鑑別診断支援につながる特徴学習を評価する。
- Methods: 2×2カーネルの5畳み込み層、LeakyReLU、平均poolingと3全結合層を使用。複数施設・機器の120CTから14,696パッチを抽出し、正常やすりガラス影など7クラスで比較した。
- Data and results: 分類性能は約85.5%と報告。要旨は旧来手法に対する有効性を述べるが、クラス別性能や患者単位の診断精度は示さない。
- Novelty: 一般画像の特徴設計を転用するだけでなく、肺パターン分類用の深い畳み込み表現を設計した。
- Limitations: 著者は3次元化と鑑別診断システムへの統合を今後の課題とする。パッチ分類をCT全体の疾患診断と同一視できず、患者単位の分割条件も本文確認が必要。

### Paper: Deep Patient: An Unsupervised Representation to Predict the Future of Patients from the Electronic Health Records
- Source: PubMed
- Canonical ID: pmid:27185194
- Publication date: 2016-05-17
- URL: https://pubmed.ncbi.nlm.nih.gov/27185194/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: Deep Patientは、教師なしで学ぶ患者表現を将来の多疾患予測へ利用した初期のEHR深層学習。
- Objective: 電子カルテの診断名・処方・検査などは高次元で不均一なため、疾患ごとに手作業で特徴量を設計して予後モデルを作る方法は再利用しにくい。疾患ラベルを直接与えなくても、患者の過去の医療記録全体から将来の複数疾患の予測に使える共通表現を学習できるかを検証した。
- Methods: Mount Sinai系の約70万人の集約EHRを利用し、3層の積層ノイズ除去オートエンコーダで患者記録を圧縮する。ノイズを加えた入力から元の記録を復元する教師なし学習で中間表現を獲得した後、その表現を別の教師あり予測器の入力へ渡す二段階構成。元の診療コードをそのまま入力する場合や別の特徴学習手法を対照として、78種類の疾患と複数の予測時間窓を評価した。
- Data and results: テスト対象は76,214人で、78疾患の発症予測について比較表現に対して広く良好な成績を報告した。重症糖尿病・統合失調症・複数のがんで高い予測性能と述べる一方、確認した要旨には疾患別の詳細なAUC差の一覧はない。重要なのは単一疾患の分類器ではなく、複数タスクへ共用できる表現を一度獲得した点にある。
- Novelty: 深層モデルで予測器を直接作るのではなく『ラベルなしの多数の診療履歴から患者表現を先に学ぶ』ことを前面に出した初期の重要研究。少数ラベルの医療予測へ表現を再利用できる可能性を示すが、学習データの規模による利益とモデル構造による利益は区別する必要がある。
- Limitations: 教師なしなのは患者表現の獲得段階であり、転帰予測や評価にラベルが一切不要だったわけではない。単一医療システムの蓄積データであり、施設間移植、時期外の校正、医療介入による患者転帰改善は未実証。

### Paper: Deep learning as a tool for increased accuracy and efficiency of histopathological diagnosis
- Source: PubMed
- Canonical ID: pmid:27212078
- Publication date: 2016-05-23
- URL: https://pubmed.ncbi.nlm.nih.gov/27212078/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 前立腺生検と乳癌リンパ節の病理で、良性スライドを自動除外する支援の可能性を示した。
- Objective: 癌病理診断の増大する作業量に対し、精度と効率を両立する深層学習の利用を検討する。
- Methods: 前立腺癌の同定とセンチネルリンパ節の乳癌転移検出という2事例で、追加免疫染色や人の介入なしの自動解析を評価した。
- Data and results: 検証した癌含有スライドおよび微小・大転移をすべて検出し、良性・正常スライドの30–40%を除外できた。要旨に全対象数や信頼区間はない。
- Novelty: 全診断を置き換える用途に限らず、明らかな陰性例の選別で読影負担を減らす設計を示した。
- Limitations: 編者の注意: 『すべて検出』は研究標本内の結果で、母集団での感度100%を保証しない。実診療の作業時間や見逃しへの影響は追加評価が必要。

### Paper: V-Net: Fully Convolutional Neural Networks for Volumetric Medical Image Segmentation
- Source: arXiv
- Canonical ID: arxiv:1606.04797
- Publication date: 2016-06-15
- URL: https://arxiv.org/abs/1606.04797
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: V-Netは体積全体を分割し、Diceに基づく目的関数で前景・背景の不均衡に対処する。
- Objective: 臨床で多い3次元画像を2次元断面に分けず、少数注釈から一体で解析する。
- Methods: 前立腺MRIを入力する3次元の全畳み込みモデルをend-to-endで学習。Dice目的、ランダム非線形変形、histogram matchingを利用した。
- Data and results: 難しいテスト画像で良好な分割と先行法より短い処理を報告。要旨に絶対Dice・実行時間・対象数はない。
- Novelty: 3次元表現と領域の重なりを直接最適化する損失を統合し、小さな前景領域の分割へ対応した。
- Limitations: 編者の注意: 前立腺MRIの評価で、全臓器や撮像条件での性能を保証しない。Diceを改善しても境界の臨床上重要な誤りを別途確認する必要がある。

### Paper: 3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation
- Source: arXiv
- Canonical ID: arxiv:1606.06650
- Publication date: 2016-06-21
- URL: https://arxiv.org/abs/1606.06650
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 3D U-Netは一部の断面にしか注釈がない立体画像から、密な3次元分割を学習する。
- Objective: 全断面のラベル付けを避け、立体的な構造を活かした画像分割を可能にする。
- Methods: U-Netの2次元演算を3次元へ置換し、学習中に弾性変形で拡張。対象画像の一部を注釈する半自動用途と、代表的な疎注釈データで学ぶ全自動用途を評価した。
- Data and results: 形状の変動が大きいXenopus腎臓で、両用途に良好な分割を報告。事前学習を使わず訓練できたが、要旨にDiceや標本数はない。
- Novelty: 2次元の少数例学習を、疎な断面注釈からの体積全体の密な学習へ拡張した。
- Limitations: 編者の注意: 疎注釈でも代表的な学習データは必要で、注釈なし学習ではない。対象画像の注釈を使う半自動成績と、未見画像の全自動成績を区別する。

### Paper: Using recurrent neural network models for early detection of heart failure onset
- Source: PubMed
- Canonical ID: pmid:27521897
- Publication date: 2016-08-13
- URL: https://pubmed.ncbi.nlm.nih.gov/27521897/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 診断・処方などの時間的な順序をGRUで扱い、心不全の初回診断予測を改善した研究。
- Objective: 医療コードの出現回数を集計するモデルでは、直近に起こった診療イベントと数年前の既往を同様に扱いやすく、時間経過による状態変化を表現しにくい。診断・処方などの連続する診療履歴をRNNで扱うことで、心不全の初回診断をどれだけ早く捉えられるかを比較する。
- Methods: 2000〜2013年のプライマリケア記録から心不全患者3,884人と対照28,903人を抽出。診療イベント列を12か月または18か月の観察窓にまとめてGRUベースの再帰型ネットワークで処理し、ロジスティック回帰、MLP、SVM、k近傍法と同じ予測課題で比較した。観察履歴の長さと、心不全の発症まで残る時間を混同しないことが重要。
- Data and results: 12か月履歴ではAUROCがGRU 0.777、ロジスティック回帰0.747、MLP0.765、SVM0.743、k近傍0.730。18か月履歴ではGRU 0.883に対し最良の対照MLPが0.834。履歴を長くした条件で差が広がり、時間順序を使う価値の一端を示す。ただし観察期間や各群の構成が変わると指標の比較条件も変わる。
- Novelty: 深層学習を単に表の分類へ適用するのでなく、経過そのものを入力単位にした。患者の過去イベントが将来の診断を予測する際、順序を保持する構造が集計表現を上回る場合を具体的に提示する。
- Limitations: 症例対照のオフライン評価で、実診療の有病率での陽性的中率や、誰にどの時点で検査を追加すれば利益があるかは評価されていない。時間モデルのAUROCが上がったことを介入の因果効果や長期校正の良好さと同一視できない。
- Publication date note: 出版社PDFのAdvance Access Publication Dateを採用。巻号の2017年3月と区別する。出典: https://academic.oup.com/jamia/article/24/2/361/2631499

### Paper: Molecular graph convolutions: moving beyond fingerprints
- Source: PubMed
- Canonical ID: pmid:27558503
- Publication date: 2016-08-24
- URL: https://pubmed.ncbi.nlm.nih.gov/27558503/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 分子を固定fingerprintへ変換する代わりに、グラフから特徴を学ぶ初期の畳み込み法。
- Objective: 手設計の分子指紋が捨てる情報を減らし、予測に必要な構造特徴をデータから選ぶ。
- Methods: 原子、結合、距離などを符号化した無向分子グラフにgraph convolutionを適用し、固定fingerprintを使う手法と比較した。
- Data and results: 分子グラフからの表現学習の可能性を示す一方、すべてのfingerprint法を上回らないと明記。要旨にデータ数や指標値はない。
- Novelty: 下流モデルだけを学ぶ枠組みから、分子構造の表現自体も学ぶグラフ学習へ移行した。
- Limitations: 著者自身が固定fingerprintへの一律の優越性を否定する。編者の注意: 構造からの活性予測と、候補化合物の実験的な薬効確認は別である。

### Paper: Densely Connected Convolutional Networks
- Source: arXiv
- Canonical ID: arxiv:1608.06993
- Publication date: 2016-08-25
- URL: https://arxiv.org/abs/1608.06993
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: DenseNetは前の全層の特徴を後の層へ渡し、特徴再利用と勾配伝達を強める。
- Objective: 深いCNNの学習を効率化し、少ないパラメータで高い認識性能を得る。
- Methods: L層でL(L+1)/2の直接接続を持ち、各層がそれ以前の特徴mapを入力に使う。CIFAR-10/100、SVHN、ImageNetで評価した。
- Data and results: 多くのベンチマークで当時の比較法より高い性能と計算効率を報告。要旨にモデル別のパラメータ数、演算量、誤り率はない。
- Novelty: 層の出力を後段へ密に共有し、特徴を作り直す負担と勾配消失を抑える構造を示した。
- Limitations: 編者の注意: パラメータ削減は実行時メモリや速度の同率改善を意味しない。一般画像の分類結果から、医用画像の精度・施設間汎化は推論できない。

### Paper: Improved Automated Detection of Diabetic Retinopathy on a Publicly Available Dataset Through Integration of Deep Learning
- Source: PubMed
- Canonical ID: pmid:27701631
- Publication date: 2016-10-01
- URL: https://pubmed.ncbi.nlm.nih.gov/27701631/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 同じ公開眼底データで、深層学習を加えた糖尿病網膜症検出器を従来版と比較した。
- Objective: 元のIowa Detection Programの感度を保ちながら特異度を改善できるか検証する。
- Methods: 学習に用いなかったMessidor-2と網膜専門医3人の既存合意基準を使用し、紹介を要する網膜症についてIDx-DR X2.1を評価した。
- Data and results: 感度96.8%、特異度87.0%、陰性的中率99.0%、AUC0.980。偽陰性は6/874、重症非増殖・増殖網膜症や黄斑浮腫の見逃しはなかった。感度差は非有意、特異度は従来版より有意に高かった。
- Novelty: 基本的な検出器を揃えた比較で、深層学習部品の追加が特異度へ与える効果を評価した。
- Limitations: 編者の注意: 同じ公開データ上の既報との比較であり、前向き導入試験ではない。陰性的中率は有病率に依存し、失明予防効果はこの結果だけでは示せない。

### Paper: Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs
- Source: PubMed
- Canonical ID: pmid:27898976
- Publication date: 2016-11-29
- URL: https://pubmed.ncbi.nlm.nih.gov/27898976/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 眼底写真から紹介を要する糖尿病網膜症を検出し、閾値による感度と特異度の変化を示した。
- Objective: 糖尿病網膜症の眼底スクリーニングでは、専門医が判読する負担が大きい。画像から『紹介を要する糖尿病網膜症』を自動検出できるかを、多数の医師の参照ラベルと独立画像群で評価する。AUCだけでなく、高感度を選んだときどの程度の特異度を保てるかが実運用上の問題となる。
- Methods: 128,175枚の眼底写真を用いてCNNを学習し、開発と独立したEyePACS-1（9,963枚）・Messidor-2（1,748枚）で評価。複数の眼科医の判定に基づき紹介対象の状態を定義し、AUCのほか、高感度を優先する閾値と高特異度を優先する閾値を設定して感度・特異度の交換条件を検証した。
- Data and results: EyePACS-1でAUC 0.991、Messidor-2で0.990。高感度の動作点では感度97.5%／96.1%、特異度93.4%／93.9%を示した。これはテスト画像の定義された判読課題で高精度だったことを意味し、実際の受診者で撮影不可能な画像や病院の検査経路を含む全体の患者利益を測定したわけではない。
- Novelty: 深層学習による眼科画像診断で、開発データとは別の画像セットを使い、紹介判断に必要な操作閾値まで定量化した代表的研究。AUROCだけでなく、臨床上重視する感度と、不要な紹介が増える特異度のトレードオフを見る設計は他の医療AIにも通用する。
- Limitations: 独立画像セットでの内部的な診断性能であり、前向きの診療介入によって眼疾患の予後が改善したことを示さない。撮影品質・対象集団・施設や装置の差による分布変化を現場で監視し続ける必要がある。
- Publication date note: 著者所属機関が公開する出版社版PDFのPublished Online November 29, 2016を採用。12月13日の巻号・訂正日と区別。出典: https://storage.googleapis.com/gweb-research2023-media/pubtools/3679.pdf

### Paper: A novel deep learning approach for classification of EEG motor imagery signals
- Source: PubMed
- Canonical ID: pmid:27900952
- Publication date: 2016-11-30
- URL: https://pubmed.ncbi.nlm.nih.gov/27900952/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 運動イメージEEGの時空間・周波数情報をCNNと積層オートエンコーダーで分類した。
- Objective: BCIの運動イメージ信号で、手設計の分類法に対する深層学習の改善を調べる。
- Methods: 時間・周波数・電極位置を組み合わせた入力を作り、1次元畳み込みとmax-poolingで特徴抽出。CNN単体やSAEに加え、CNNの特徴をSAEで分類する構成を評価した。
- Data and results: BCI Competition IVの2bでκ=0.547。競技の優勝法に対して9%の改善と報告するが、要旨は改善を絶対ポイントと定義しない。
- Novelty: 複数の信号軸を含む入力と、畳み込み特徴・深い分類器の組合せをBCIへ導入した。
- Limitations: 編者の注意: 単一競技データのオフライン分類であり、実時間BCIの情報伝達速度や新規利用者への適応能力は要旨から確認できない。

### Paper: Accurate De Novo Prediction of Protein Contact Map by Ultra-Deep Learning Model
- Source: PubMed
- Canonical ID: pmid:28056090
- Publication date: 2017-01-05
- URL: https://pubmed.ncbi.nlm.nih.gov/28056090/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 深い残差モデルで残基接触を予測し、相同配列が少ない場合の構造推定を改善した。
- Objective: 従来の共進化解析で難しかった接触予測を、配列保存性との統合で高精度化する。
- Methods: 1次元残差モデルで系列を変換し、その出力と進化カップリング・残基対情報を2次元残差モデルへ入力。CASP11、CAMEO難例、膜タンパク質の計579例で検証した。
- Data and results: 上位Lの長距離接触精度は0.47、CCMpred0.21、MetaPSICOV0.30。接触制約でTM-score>0.6の折り畳みは203/579、比較法79・62例だった。
- Novelty: 残基対を独立に扱わず、深い2次元モデルで接触パターンと系列・構造の関係を学んだ。
- Limitations: 編者の注意: 接触の順位精度と完成構造の精度は異なる。正しい折り畳みは全例ではなく、相同配列が少なくても性能が不変という結果ではない。

### Paper: Natural language processing to extract symptoms of severe mental illness from clinical text: the Clinical Record Interactive Search Comprehensive Data Extraction (CRIS-CODE) project
- Source: PubMed
- Canonical ID: pmid:28096249
- Publication date: 2017-01-17
- URL: https://pubmed.ncbi.nlm.nih.gov/28096249/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: CRIS-CODEは精神科退院要約から広い症状群を抽出し、病名をまたぐ症状の分布を調べた。
- Objective: 重症精神疾患の主要症状を診療文書から取り出し、二次研究に利用できるようにする。
- Methods: 精神科医が50症状を選び、TextHunterとCRISで抽出器を開発。重症精神疾患7,962人の23,128要約と、その他7,575人の13,496要約で分布を記述した。
- Data and results: 性能不良の4症状を除いた46症状でF1中央値0.88。重症疾患患者の87%、その他の60%から症状を抽出し、多くの症状が診断を横断した。
- Novelty: 単独症状や病名の抽出から、複数の症状領域を横断して再利用できる臨床表現型へ広げた。
- Limitations: 編者の注意: 単一提供者の英語退院要約であり、記録されない症状は把握できない。抽出された言及を現在症状や診断の確定と混同しない。

### Paper: Dermatologist-level classification of skin cancer with deep neural networks
- Source: PubMed
- Canonical ID: pmid:28117445
- Publication date: 2017-01-25
- URL: https://pubmed.ncbi.nlm.nih.gov/28117445/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 大規模な皮膚画像で学習したCNNを、2つの生検確認済み二値分類で皮膚科医と比較した。
- Objective: 悪性黒色腫などの皮膚病変を画像から識別する際、疾患ごとに専門的な特徴量を手設計する代わりに、多数の疾患と画像から学習したCNNで専門家に近い鑑別ができるかを検証した。
- Methods: 2,032種類の疾患を含む臨床画像129,450枚で一つの深層畳み込みモデルを訓練。生検で病変が確定した、角化細胞癌対良性脂漏性角化症、悪性黒色腫対良性母斑という2つの二値分類を試験し、臨床経験を持つ皮膚科医21名の判定と比較した。
- Data and results: 2つの生検確認済み鑑別課題で、モデルは対象の皮膚科医に匹敵する性能と報告。要旨にすべての感度・特異度の絶対数値を確認できないため補っていない。結果は二つの設定された画像分類での対照比較であり、あらゆる皮膚疾患を診察できたという実験ではない。
- Novelty: 一般的な画像学習を多数の皮膚疾患へ適用し、手設計した診断特徴に依存せず臨床的に重要な二値鑑別へ転用した。患者を診る医師の情報量と、モデルが利用した画像の情報量を揃えた比較かを考える重要性も示す。
- Limitations: 臨床画像による限定的な2課題のオフライン評価で、スマートフォン経由のスクリーニングや幅広い皮膚色・撮影環境での安全性を直接検証していない。

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

### Paper: A Dataset and a Technique for Generalized Nuclear Segmentation for Computational Pathology
- Source: PubMed
- Canonical ID: pmid:28287963
- Publication date: 2017-03-06
- URL: https://pubmed.ncbi.nlm.nih.gov/28287963/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 多施設・多臓器の核境界データと、画素・物体両方の誤りを評価する分割基盤を提供した。
- Objective: 密集・接触する核や外観の多様性に対応し、病理画像の核分割を比較可能にする。
- Methods: 医師が質を確認した21,000超のH&E核境界を公開。物体と画素の誤りを統合する指標と、接触・重複核の境界を重視する深層分割法を提案した。
- Data and results: 複数病院・患者・病態・臓器の画像を収集し、多様なテスト画像で良好な分割を報告。要旨に具体的なスコアや外部施設別結果はない。
- Novelty: 核分割アルゴリズムに加え、汎化を促す公開注釈と統一した評価指標を揃えた。
- Limitations: 編者の注意: 多様な収集元は汎化の期待を高めるが、任意のH&E画像で調整不要という保証ではない。注釈基準と臓器別誤差を確認する必要がある。

### Paper: DeepSleepNet: A Model for Automatic Sleep Stage Scoring Based on Raw Single-Channel EEG
- Source: PubMed
- Canonical ID: pmid:28678710
- Publication date: 2017-06-28
- URL: https://pubmed.ncbi.nlm.nih.gov/28678710/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: DeepSleepNetは生の単一チャネルEEGから特徴と睡眠段階間の遷移を学習する。
- Objective: 睡眠知識を使う手設計特徴を減らし、異なる記録条件でも自動睡眠判定を行う。
- Methods: CNNで時間位置に依存しにくい特徴、双方向LSTMで段階遷移を学習し、2段階で訓練。異なる導出・標準を持つMASSとSleep-EDFで評価した。
- Data and results: accuracy/macro-F1はMASS86.2%/81.7%、Sleep-EDF82.0%/76.9%。比較法は各85.9%/80.5%、78.9%/73.7%だった。
- Novelty: 信号特徴と前後の睡眠段階の文脈を統合し、同じ構造・学習手順を複数データへ使った。
- Limitations: 編者の注意: 同じ設計で各データを学習できることと、学習なしの機器間転移は異なる。双方向の文脈を使う処理を、未来情報なしの実時間判定と混同しない。

### Paper: Deep learning with convolutional neural networks for EEG decoding and visualization
- Source: PubMed
- Canonical ID: pmid:28782865
- Publication date: 2017-08-07
- URL: https://pubmed.ncbi.nlm.nih.gov/28782865/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 生EEGから運動課題を読むCNNの学習法と、周波数・空間特徴の可視化を検討した。
- Objective: 手設計の特徴を使わずEEGを識別し、モデルが何を利用したか理解できるようにする。
- Methods: 想像・実行課題に複数CNN構造を比較し、batch normalization、ELU、cropped trainingの効果を評価。学習特徴を周波数帯と頭皮上の位置で可視化した。
- Data and results: 平均分類accuracyはFBCSP82.1%、深層CNN84.0%。α・β・高γ帯のパワー変化をCNNが利用することを確認した。
- Novelty: EEG向け学習設計と特徴可視化をセットにし、生信号の表現学習を従来法と比較した。
- Limitations: 編者の注意: 運動関連課題の復号であり、疾患診断の精度ではない。モデル入力への寄与の可視化を、生物学的な脳機構の因果解明と同一視しない。

### Paper: Challenges in adapting existing clinical natural language processing systems to multiple, diverse health care settings
- Source: PubMed
- Canonical ID: pmid:28419261
- Publication date: 2017-09-01
- URL: https://pubmed.ncbi.nlm.nih.gov/28419261/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 既存の内視鏡NLPを4つの医療環境へ移す作業で、想定以上の調整負担が生じた。
- Objective: 臨床NLPの高精度な試作品を、異なる施設へ展開する際の障害を明らかにする。
- Methods: 2013–2015年の内視鏡・病理報告を使い、地域、診療形態、報酬構造、EHRの異なる4環境で品質測定システムを適応した。
- Data and results: 適応は成功したが、コーパス整備、報告形式、独特の表現の違いにより時間と労力が予想を大きく超えた。要旨には工数や精度の数値はない。
- Novelty: 抽出器単体の性能より、実際の複数施設への移植過程と必要な組織知識を分析対象にした。
- Limitations: 編者の注意: 1種類の品質測定用途の経験で、すべてのNLPの移植費用を定量化する研究ではない。著者は地域のEHR専門家、現実的な期間、反復開発の必要性を示す。

### Paper: Deep convolutional neural network for the automated detection and diagnosis of seizure using EEG signals
- Source: PubMed
- Canonical ID: pmid:28974302
- Publication date: 2017-09-27
- URL: https://pubmed.ncbi.nlm.nih.gov/28974302/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 13層CNNでEEGを正常・発作前・発作に分類する自動解析を検討した。
- Objective: 視覚的なEEG確認の負担と判定の変動を減らす、機械的な信号分類器を開発する。
- Methods: EEG信号へ13層の深い畳み込みモデルを適用し、正常、preictal、seizureの3クラスを識別した。要旨に患者数や学習・テストの分割法はない。
- Data and results: accuracy88.67%、specificity90.00%、sensitivity95.00%を報告。クラス別の詳細や患者間汎化は要旨から確認できない。
- Novelty: 手作業の判別特徴に代わり、深層CNNをEEGの発作関連状態の分類に利用した。
- Limitations: 編者の注意: 区間分類の性能を長時間の連続記録での発作予告・警報性能へ換算できない。患者独立分割と偽警報頻度が不明なため、臨床的な検出能力は確定しない。

### Paper: MoleculeNet: a benchmark for molecular machine learning
- Source: PubMed
- Canonical ID: pmid:29629118
- Publication date: 2017-10-31
- URL: https://pubmed.ncbi.nlm.nih.gov/29629118/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: MoleculeNetは分子学習の公開データ、指標、基準実装を揃え、手法比較を標準化した。
- Objective: 異なるデータで評価されていた分子予測法を、共通の条件で比較可能にする。
- Methods: 複数の公開分子データを整備して評価指標を定め、既存の特徴量・学習法をDeepChemの実装として提供した。
- Data and results: 学習可能な表現が広く高性能だった一方、少数データ・強いクラス不均衡では難しさが残る。量子・生物物理課題ではアルゴリズム選択より物理に即した特徴が重要な場合があった。
- Novelty: 個別の分子モデル提案に加え、課題をまたいで特徴表現と学習器を比較する基盤を作った。
- Limitations: 編者の注意: 要旨にデータセット数や具体的スコアはない。学習表現が常に最善とは結論しておらず、評価分割やデータの希少性を伴って比較する必要がある。

### Paper: DeepLoc: prediction of protein subcellular localization using deep learning
- Source: PubMed
- Canonical ID: pmid:29036616
- Publication date: 2017-11-01
- URL: https://pubmed.ncbi.nlm.nih.gov/29036616/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: DeepLocはタンパク質の全配列を読み、細胞内の局在と膜結合性を予測する。
- Objective: 注釈済み相同配列に頼れない新規タンパク質や配列変異でも、配列だけで性質を推定する。
- Methods: RNNで全長配列を処理し、attentionで局在に重要な領域を捉える。厳しい基準で実験注釈を選んだUniProtデータで学習・評価した。
- Data and results: 10カテゴリの局在accuracy78%、膜結合対可溶性92%。相同情報を使う手法を含む比較法を上回った。
- Novelty: 相同タンパク質の注釈転写に代わり、全配列から局在を決める特徴を直接学ぶ。
- Limitations: 編者の注意: 真核タンパク質の分類で、全生物種への成績ではない。attentionが示す領域を輸送機構の因果的証明とみなさず、実験注釈の偏りも考慮する。

### Paper: Fully Automated Detection and Quantification of Macular Fluid in OCT Using Deep Learning
- Source: PubMed
- Canonical ID: pmid:29224926
- Publication date: 2017-12-08
- URL: https://pubmed.ncbi.nlm.nih.gov/29224926/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: OCTの網膜内・網膜下液を自動検出・定量し、疾患と撮像機器をまたいで評価した。
- Objective: 眼科で重要な液体の種類・位置・量を、専門家に近い一貫性で測定する。
- Methods: AMD・DME・網膜静脈閉塞各400件、2機器各600件の計1,200OCTボリュームを使用。盲検評価者2人の手動合意を基準に深層モデルを比較した。
- Data and results: 網膜内嚢胞状液の平均AUC0.94、適合率0.91、再現率0.84。網膜下液は0.92、0.61、0.81。自動・手動定量の相関はそれぞれ0.90、0.96だった。
- Novelty: 単なる液体の有無から、液体種別の局在・体積評価を複数疾患・機器へ広げた。
- Limitations: DMEの網膜下液例は少なく、他疾患より性能が低かった。編者の注意: 高いAUCと相関でも、適合率や体積の絶対誤差まで良好とは限らない。

### Paper: Diagnostic Assessment of Deep Learning Algorithms for Detection of Lymph Node Metastases in Women With Breast Cancer
- Source: PubMed
- Canonical ID: pmid:29234806
- Publication date: 2017-12-12
- URL: https://pubmed.ncbi.nlm.nih.gov/29234806/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: CAMELYON16は乳癌リンパ節転移の検出を、時間制限の条件を分けて病理医と比較した。
- Objective: 全スライド病理画像の転移検出で、深層モデルが診断業務をどこまで支援できるか調べる。
- Methods: オランダ2施設の学習270スライド、独立テスト129スライドを使用。11病理医の2時間の模擬診断と、1病理医の時間無制限判定に対して競技モデルを比較した。
- Data and results: モデルAUCは0.556–0.994。最良モデルの0.994は時間制限あり病理医の平均0.810を上回り、病変検出では時間無制限の専門医に匹敵した。
- Novelty: モデル対人の比較で、全スライド分類・病変検出・読影時間という異なる条件を明示した。
- Limitations: 著者は実臨床での有用性検証が必要とする。競技と診断模擬環境の結果であり、時間無制限の専門医を一律に上回るという結論ではない。

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

### Paper: Using Clinical Notes and Natural Language Processing for Automated HIV Risk Assessment
- Source: PubMed
- Canonical ID: pmid:29084046
- Publication date: 2018-02-01
- URL: https://pubmed.ncbi.nlm.nih.gov/29084046/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: HIV診断前の記録にある行動・社会情報をNLPで加え、検査対象のリスク識別を改善した。
- Objective: 構造化項目にない情報を診療ノートから取り出し、対象を絞るHIVスクリーニングに活用する。
- Methods: 単施設で診断前に受診したHIV陽性181人と傾向スコアで選んだ陰性543人を比較。構造化データのみ、トピック追加、臨床キーワード追加の3モデルを作った。
- Data and results: F値は構造化のみ0.59、トピック追加0.63、キーワード追加0.74。後者は性行動・薬物関連の記録と既存のリスク情報を利用した。
- Novelty: 文章に偏在する社会・行動情報を取り込み、構造化EHRだけのリスク評価を補った。
- Limitations: 編者の注意: 診断前でも記録に検査への疑いやHIVの言及が含まれ得る。症例対照評価のF値は一般集団での検査効率や公平性の保証ではない。

### Paper: CLAMP - a toolkit for efficiently building customized clinical natural language processing pipelines
- Source: PubMed
- Canonical ID: pmid:29186491
- Publication date: 2018-03-01
- URL: https://pubmed.ncbi.nlm.nih.gov/29186491/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: CLAMPはGUIと臨床NLP部品を提供し、用途に合わせた抽出処理の構築を支援する。
- Objective: 専門的なNLP技能が限られる利用者でも、既存システムを個別課題へ調整しやすくする。
- Methods: 名前付き実体認識・概念コード化などの既定部品とGUIを統合。既定処理を評価し、喫煙状態・検査値の2用途でカスタマイズを実演した。
- Data and results: 既定パイプラインで良好な認識・コード化性能、2用途で効率的な構築を報告。要旨に精度値、作業時間、対象文書数は記載されない。
- Novelty: 単一の完成済み抽出器ではなく、GUIを介して部品を組み替える臨床NLP開発環境を提供した。
- Limitations: 編者の注意: 研究利用での公開は、任意の施設で調整不要な精度や臨床運用を保証しない。カスタマイズの効率と出力の品質は用途ごとに確認が必要。

### Paper: AF Classification from a Short Single Lead ECG Recording: the PhysioNet/Computing in Cardiology Challenge 2017
- Source: PubMed
- Canonical ID: pmid:29862307
- Publication date: 2018-04-05
- URL: https://pubmed.ncbi.nlm.nih.gov/29862307/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: PhysioNet/CinC 2017は短い単誘導ECGの心房細動分類を、隠れたテストで比較した。
- Objective: 患者が記録する短いECGから、心房細動・正常・その他のリズム・雑音を区別する技術を測る。
- Methods: 9–61秒の12,186記録を公開学習8,528と非公開テスト3,658へ分割。医師のラベル不一致を有力モデルで抽出し、競技中に再確認した。
- Data and results: 75独立チームが参加し、4チームが平均F1 0.83で同点優勝。上位11法は2%以内。LASSOで選んだ45法の統合はF1 0.87だった。
- Novelty: 雑音を含む短い患者記録と隠し評価を提供し、専門家ラベルの不確実性も競技設計に取り込んだ。
- Limitations: 編者の注意: 単独参加法と多数モデルの統合は計算費用が違う。競技の平均F1から臨床集団の陽性的中率や長時間モニタリング性能は分からない。

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

### Paper: Automated Diagnosis of Plus Disease in Retinopathy of Prematurity Using Deep Convolutional Neural Networks
- Source: PubMed
- Canonical ID: pmid:29801159
- Publication date: 2018-05-02
- URL: https://pubmed.ncbi.nlm.nih.gov/29801159/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 未熟児網膜症のplus diseaseを眼底写真から判定し、専門医との一致を比較した。
- Objective: 主観的な血管拡張・蛇行の判定を支援し、plus diseaseの診断のばらつきを減らす。
- Methods: 8大学施設の5,511写真に専門医合意と臨床診断から参照ラベルを設定。5分割交差検証と独立100画像で評価し、経験豊かな8専門医と比較した。
- Data and results: 独立テストでplusの感度93%、特異度94%。pre-plus以上は感度100%、特異度94%。3クラスの重み付きκは0.92で、8専門医中6人を上回った。
- Novelty: 主観差の大きい疾患所見を合意基準で学習し、二値検出と重症度分類を併せて評価した。
- Limitations: 編者の注意: 独立テストは100画像と小さく、治療判断全体や視力予後の改善は未検証。参照も医師の合意に基づき、全病期の診断能力を示すものではない。
- Publication date note: PMC掲載原著のオンライン公開日2018-05-02を採用。巻号の2018年7月と区別。出典: https://pmc.ncbi.nlm.nih.gov/articles/6136045/

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

### Paper: Identifying Suicide Ideation and Suicidal Attempts in a Psychiatric Clinical Research Database using Natural Language Processing
- Source: PubMed
- Canonical ID: pmid:29743531
- Publication date: 2018-05-09
- URL: https://pubmed.ncbi.nlm.nih.gov/29743531/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 精神科データベースの自由記載から、自殺念慮と企図の言及を別々のNLP手法で抽出した。
- Objective: 小規模調査や回想の制約を補い、既存診療記録から大規模な研究用情報を得る。
- Methods: 念慮はルールベース、企図は機械学習とルールのハイブリッドで分類。症状コードや既知の予測因子を必須とせず、精神科記録内の言及を評価した。
- Data and results: 両分類器で良好な抽出性能を報告するが、要旨に対象数、F1、感度・特異度の具体値はない。要求に応じて分類条件を修正できるとする。
- Novelty: 念慮と企図を区別し、記録習慣や研究目的に合わせて調整可能な抽出器を提供した。
- Limitations: 編者の注意: 記録中の言及を見つける研究で、将来の企図・死亡を予測する研究ではない。他施設への適応には臨床記録の知識が必要と著者も条件付けている。

### Paper: A Long Short-Term Memory deep learning network for the prediction of epileptic seizures using EEG signals
- Source: PubMed
- Canonical ID: pmid:29807250
- Publication date: 2018-05-17
- URL: https://pubmed.ncbi.nlm.nih.gov/29807250/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 長時間EEGの事前特徴をLSTMで扱い、発作前状態の定義を変えた予測性能を比較した。
- Objective: 系列の依存を学習し、てんかん発作の予測で誤警報を減らす。
- Methods: 時間・周波数、チャネル間相関、グラフ特徴を入力する2層LSTMを選択。CHB-MITで15分から2時間まで4種類のpreictal窓を評価した。
- Data and results: 185発作すべてを予測したと報告し、偽警報は窓長に応じて毎時0.11–0.02。既報の従来法・CNNより改善した。
- Novelty: 手作業の多様なEEG特徴を時系列モデルへ統合し、発作前ラベルの時間定義による違いも検討した。
- Limitations: 編者の注意: 発作前窓の長さは実際の警報先行時間と同じではない。全発作の検出は評価データ内の結果であり、患者独立性・連続運用条件は本文での追加確認が必要。

### Paper: Deep Learning Techniques for Automatic MRI Cardiac Multi-Structures Segmentation and Diagnosis: Is the Problem Solved?
- Source: PubMed
- Canonical ID: pmid:29994302
- Publication date: 2018-05-17
- URL: https://pubmed.ncbi.nlm.nih.gov/29994302/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: ACDCは心臓MRIの分割と診断を共通データで比較し、自動臨床指標の精度と失敗例を示した。
- Objective: 心筋・左右心室の分割と病態分類で、深層学習が専門家の解析にどこまで近づいたか測る。
- Methods: 複数機器の150件の心臓MRIに、2専門医の参照測定と分類を付与。MICCAI 2017の参加法を分割9グループ、分類4グループについて評価した。
- Data and results: 最良手法では臨床指標の自動抽出と専門家の相関が平均0.97、自動診断accuracyは0.96。失敗する状況も同定し、データと詳細結果を公開した。
- Novelty: 画素分割だけでなく、測定値と疾患分類まで含めた再利用可能な心臓MRI評価基盤を提供した。
- Limitations: 編者の注意: 相関0.97はDiceや絶対的な測定一致度ではない。最良モデルの競技成績だけで、心臓MRI解析全体が解決したとは判断できない。

### Paper: Clinically applicable deep learning for diagnosis and referral in retinal disease
- Source: PubMed
- Canonical ID: pmid:30104768
- Publication date: 2018-08-13
- URL: https://pubmed.ncbi.nlm.nih.gov/30104768/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 3次元OCTを組織分割へ変換し、複数の網膜疾患の紹介判断と機器間の移植性を検討した。
- Objective: 多数の疾患が混在する眼科紹介経路で、3次元画像から専門家に匹敵する紹介勧告を行う。
- Methods: 主要眼科病院の14,884スキャンで深層モデルを学習。中間の組織分割を機器に依存しない表現として使い、異なる装置の分割でも判断を評価した。
- Data and results: 視力を脅かす複数疾患の紹介勧告で専門家に匹敵または上回り、別機器の分割でも精度を維持。要旨に具体的な正解率や対象患者数はない。
- Novelty: 画像から直接判断するだけでなく、組織表現を介して機器差に対応する臨床経路を設計した。
- Limitations: 編者の注意: 機器間の移植結果と、任意の施設・疾患での汎化は異なる。紹介勧告の精度は、導入後の視力転帰改善を直接示さない。

### Paper: A comparison of word embeddings for the biomedical natural language processing
- Source: PubMed
- Canonical ID: pmid:30217670
- Publication date: 2018-09-12
- URL: https://pubmed.ncbi.nlm.nih.gov/30217670/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 医学用語をよく表す埋め込みが、すべての下流NLP課題で最良とは限らないことを示した。
- Objective: 臨床文書、医学論文、Wikipedia、ニュースのどの学習資源が医学NLPへ有用か比較する。
- Methods: Mayo EHR、PMC論文、GloVe、Google Newsの埋め込みを、類似語の手動確認、4つの意味類似度データ、情報抽出・検索・関係抽出の共有課題で評価した。
- Data and results: EHR埋め込みは専門家の類似度判断に近く、臨床抽出F1は最良0.900。一方、検索はどの埋め込みでも改善せず、関係抽出はGoogle Newsが最良F1 0.790だった。
- Novelty: 語の意味を測る内的評価と実用課題の外的評価を分け、医学コーパスの利点が課題依存であると示した。
- Limitations: 編者の注意: コーパスと埋め込みの学習条件が異なる比較で、領域適合だけの因果効果ではない。静的単語表現の結果を後年の文脈モデルへ一律に適用できない。

### Paper: Arrhythmia detection using deep convolutional neural network with long duration ECG signals
- Source: PubMed
- Canonical ID: pmid:30245122
- Publication date: 2018-09-15
- URL: https://pubmed.ncbi.nlm.nih.gov/30245122/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 単一拍の抽出に依存せず、10秒ECGを1次元CNNで17クラスへ分類した。
- Objective: 従来の特徴抽出・選択を一体化し、短時間で不整脈区間を分類する。
- Methods: MIT-BIHの45人から1,000個のMLII誘導10秒区間を使用。手作業特徴を用いないend-to-endの1D-CNNを設計した。
- Data and results: 17クラスの全体accuracy91.33%、1標本の分類0.015秒。QRS単位の解析より分類回数を平均約13分の1に減らす構成だった。
- Novelty: 拍ごとの分割・特徴選択から、複数拍を含む一定長の信号を直接学ぶ処理へ進めた。
- Limitations: 編者の注意: 45人という少人数の区間データであり、患者独立の性能は要旨から不明。分類時間は処理環境に依存し、クラウドや携帯端末での実運用を保証しない。

### Paper: Classification and mutation prediction from non-small cell lung cancer histopathology images using deep learning
- Source: PubMed
- Canonical ID: pmid:30224757
- Publication date: 2018-09-17
- URL: https://pubmed.ncbi.nlm.nih.gov/30224757/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 肺癌の病理画像から組織型を分類し、一部の遺伝子変異まで予測する可能性を示した。
- Objective: 腺癌・扁平上皮癌・正常組織の識別と、腺癌の変異情報の画像からの推定を調べる。
- Methods: TCGAの全スライド画像でInception v3を学習。凍結・パラフィン包埋・生検の独立データで組織型を検証し、頻度の高い10変異も学習した。
- Data and results: 組織型分類の平均AUCは0.97。STK11、EGFR、FAT1、SETBP1、KRAS、TP53の6遺伝子で、保留集団の変異予測AUCは0.733–0.856だった。
- Novelty: 病理画像の形態情報を、組織型だけでなく分子変異の推定へ接続した。
- Limitations: 編者の注意: 10遺伝子すべてで成功したわけではなく、画像推定は遺伝子検査の代替を確立しない。他癌種へ適用できるという提案と検証済み範囲を区別する。

### Paper: Deep neural network improves fracture detection by clinicians
- Source: PubMed
- Canonical ID: pmid:30348771
- Publication date: 2018-10-22
- URL: https://pubmed.ncbi.nlm.nih.gov/30348771/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 骨折検出AIの予測を提示すると、救急臨床家の手関節X線読影が改善した対照実験。
- Objective: 整形外科専門家の知識を学んだモデルが、一般臨床家の骨折検出を支援できるか調べる。
- Methods: 専門整形外科医18人が注釈した135,409X線で検出・局在モデルを学習。救急臨床家が支援あり・なしで手関節画像を読む比較実験を行った。
- Data and results: 平均感度80.8%→91.5%、特異度87.5%→93.9%。誤読率の相対減少は47.0%（95%CI 37.4–53.9%）だった。
- Novelty: AI単独の専門医比較を超え、専門外の臨床家へ情報を提示したときの改善を直接測定した。
- Limitations: 編者の注意: 47%は誤読率の相対減少で、精度の47ポイント増加ではない。手関節の読影実験から、全身骨折や実際の治療・回復への利益は確定しない。

### Paper: Robust EEG-based cross-site and cross-protocol classification of states of consciousness
- Source: PubMed
- Canonical ID: pmid:30285102
- Publication date: 2018-11-01
- URL: https://pubmed.ncbi.nlm.nih.gov/30285102/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 意識障害のEEG分類を、施設・測定設定・ノイズが変わる条件で検証した。
- Objective: 意識状態に関連するEEG指標が、実務で起こる測定差にも耐えるか調べる。
- Methods: 意識障害327記録と健常66人を2施設で収集。複数特徴の決定木アンサンブルを用い、電極・epoch数、別コホート、ノイズやラベル反転を変えて評価した。
- Data and results: 未見データAUCは約0.77、設定変更平均0.750±0.014。Paris内の移植0.73、Paris→Liège0.78。複数特徴が単一特徴を上回り、20%までの無作為ラベル反転でも移植性能は安定した。
- Novelty: 同一設定の分類精度から、実際の施設間・プロトコル間の頑健性を主要な検証対象へ移した。
- Limitations: 編者の注意: 無作為ラベル反転への耐性は、系統的な診断バイアスへの耐性と異なる。EEGの判別は意識の有無を誤りなく確定する検査ではない。

### Paper: Deep learning for chest radiograph diagnosis: A retrospective comparison of the CheXNeXt algorithm to practicing radiologists
- Source: PubMed
- Canonical ID: pmid:30457988
- Publication date: 2018-11-20
- URL: https://pubmed.ncbi.nlm.nih.gov/30457988/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: CheXNeXtは胸部X線14病変を分類し、放射線科医に匹敵する項目と劣る項目を分けて示した。
- Objective: 胸部X線異常の同時検出を、実務経験のある読影医と同じ画像群で比較する。
- Methods: ChestX-ray8でCNNを学習し、保留420画像を9人の読影医と比較。胸部専門医3人の多数決を参照とし、病変別AUCを評価した。
- Data and results: 11病変では医師相当だが3病変で劣った。心拡大・肺気腫・食道裂孔ヘルニアのモデルAUCは0.831・0.704・0.851、医師は0.888・0.911・0.985。無気肺ではモデルが有意に高かった。
- Novelty: 多数病変を一括で分類し、平均的な『専門医水準』に埋もれる病変別の性能差を示した。
- Limitations: 著者は単施設評価、病歴と過去画像を双方が使えない条件を限界とする。臨床的な有用性には前向き評価が必要で、全病変で医師を上回ったわけではない。

### Paper: Deep-learning-assisted diagnosis for knee magnetic resonance imaging: Development and retrospective validation of MRNet
- Source: PubMed
- Canonical ID: pmid:30481176
- Publication date: 2018-11-27
- URL: https://pubmed.ncbi.nlm.nih.gov/30481176/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: MRNetは膝MRIの異常・靱帯・半月板損傷を分類し、施設移植と医師支援を別々に評価した。
- Objective: MRI系列を迅速に分類し、単独モデルの精度と専門家へ予測を提示した効果を調べる。
- Methods: Stanfordの1,370検査でCNNを学習し、3系列の出力を回帰で統合。内部120検査とクロアチアの外部183検査を評価し、9臨床家の支援あり・なしも比較した。
- Data and results: 内部AUCは異常0.937、ACL断裂0.965、半月板断裂0.847。外部ACLでは調整なし0.824、外部データで再学習すると0.911。支援で臨床家のACL特異度が改善した。
- Novelty: 系列単位の画像表現を検査単位へ統合し、外部移植と人との協働を含めて評価した。
- Limitations: 著者は前向きの臨床有用性検証を求める。外部データは撮像系列も異なり、移植と再学習の成績を混同しない。医師が上回る感度・特異度の項目もあった。

### Paper: PROBAST: A Tool to Assess the Risk of Bias and Applicability of Prediction Model Studies
- Source: PubMed
- Canonical ID: pmid:30596875
- Publication date: 2019-01-01
- URL: https://pubmed.ncbi.nlm.nih.gov/30596875/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: PROBASTは予測モデル研究のバイアスと、対象集団への適用可能性を構造的に評価する道具。
- Objective: 診断・予後モデルの性能推定が研究上の問題で歪んでいないか、透明に判断する。
- Methods: 既存の評価道具・報告指針を検討し、38専門家のDelphi手続きと試行で改良。参加者、予測因子、転帰、解析の4領域に整理した。
- Data and results: 計20のsignaling questionを備え、開発・検証・更新研究のバイアスと適用可能性を評価する枠組みを提供した。
- Novelty: 報告内容の有無だけでなく、設計・実施・解析が性能を系統的に歪めるかを判断対象にした。
- Limitations: 編者の注意: チェック結果をモデルの精度値へ換算する道具ではない。評価には研究内容と専門判断が必要で、報告不足と実際のバイアスは区別する。

### Paper: PROBAST: A Tool to Assess Risk of Bias and Applicability of Prediction Model Studies: Explanation and Elaboration
- Source: PubMed
- Canonical ID: pmid:30596876
- Publication date: 2019-01-01
- URL: https://pubmed.ncbi.nlm.nih.gov/30596876/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: PROBASTの解説は、4領域20質問の根拠と予測研究への適用例を詳しく示す。
- Objective: 競合する予測モデルをレビューする際に、バイアスと利用先への適合性を一貫して評価できるようにする。
- Methods: 専門家の合意で作られたPROBASTについて、各領域・質問を含める理由と判断方法を、異なる医学領域の既刊例で説明した。
- Data and results: 参加者・予測因子・転帰・解析の20質問に対する実用的解釈を提供。新モデルの患者データやAUCを報告する研究ではない。
- Novelty: ツール本体を、難しい評価判断に使える根拠・事例付きの実務的説明へ展開した。
- Limitations: 編者の注意: 合意ベースの評価法の解説であり、低バイアス判定が臨床利益を保証するわけではない。利用先の患者・時期・施設への適用可能性は別に評価する。

### Paper: Cardiologist-level arrhythmia detection and classification in ambulatory electrocardiograms using a deep neural network
- Source: PubMed
- Canonical ID: pmid:30617320
- Publication date: 2019-01-07
- URL: https://pubmed.ncbi.nlm.nih.gov/30617320/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 単誘導の携帯心電図から12種類のリズムを分類し、循環器医と同じテストで比較した。
- Objective: 多数の不整脈をend-to-endで識別し、専門家による確認作業を支援する。
- Methods: 53,549人の91,232単誘導ECGで深層モデルを開発。独立テストを循環器医委員会が合意判定し、平均AUC・F1と同じ特異度での感度を比較した。
- Data and results: 平均AUC0.97、F1はモデル0.837対医師平均0.780。医師平均の特異度に固定すると、全リズムクラスでモデルの感度が高かった。
- Novelty: 単一の不整脈検出にとどまらず、携帯単誘導ECGの広い診断群を同じモデルで評価した。
- Limitations: 著者は臨床環境での確認を条件とする。編者の注意: 特定の携帯機器の単誘導記録で、12誘導や別機器、導入後の誤診減少を直接実証したわけではない。

### Paper: CheXpert: A Large Chest Radiograph Dataset with Uncertainty Labels and Expert Comparison
- Source: arXiv
- Canonical ID: arxiv:1901.07031
- Publication date: 2019-01-21
- URL: https://arxiv.org/abs/1901.07031
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: CheXpertは胸部画像の自動ラベルに『不確か』を残し、病変ごとの学習上の扱いを比較した。
- Objective: レポート由来のラベルの曖昧さを扱い、再現可能な胸部X線の評価基盤を作る。
- Methods: 65,240人224,316画像に14所見の自動ラベルを付与。200検査の医師注釈で不確実ラベルの処理を検討し、500検査の5専門医合意を基準に別の3医師と比較した。
- Data and results: 適切な不確実性の扱いは病変ごとに異なった。5病変の比較のうち心拡大・浮腫・胸水では、モデルのROC・PR曲線が3医師すべての動作点を上回った。
- Novelty: 文章の曖昧な表現を単純な陰性へ潰さず、大規模学習データと専門医評価を接続した。
- Limitations: 編者の注意: レポート抽出ラベルと専門医合意ラベルは同質ではない。3病変での曲線比較を全14所見の臨床的優越性や患者転帰の改善へ拡張しない。

### Paper: Real-time automatic detection system increases colonoscopic polyp and adenoma detection rates: a prospective randomised controlled study
- Source: PubMed
- Canonical ID: pmid:30814121
- Publication date: 2019-02-27
- URL: https://pubmed.ncbi.nlm.nih.gov/30814121/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 実時間のポリープ検出支援を加えると腺腫発見率が上がるか、診療中に無作為比較した。
- Objective: 画像単体の検出率を超え、深層学習支援が内視鏡医のポリープ・腺腫発見を改善するか測る。
- Methods: 連続患者1,058人を通常内視鏡536人と支援あり522人へ前向き無作為化。検出時に視覚通知・音声警報を出し、腺腫発見率を主要転帰とした非盲検試験。
- Data and results: 腺腫発見率は支援あり29.1%、通常20.3%。主に微小腺腫の検出増加と、過形成性ポリープの増加を報告した。
- Novelty: 医療AIの後ろ向き性能評価から、人と組み合わせた実時間支援の無作為試験へ進んだ。
- Limitations: 著者は費用便益の追加検討を求める。低い基礎腺腫発見率の集団かつ非盲検で、癌死亡の減少や微小病変を多く切除する長期利益は未確定。

### Paper: Stand-Alone Artificial Intelligence for Breast Cancer Detection in Mammography: Comparison With 101 Radiologists
- Source: PubMed
- Canonical ID: pmid:30834436
- Publication date: 2019-03-05
- URL: https://pubmed.ncbi.nlm.nih.gov/30834436/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: マンモグラフィのAI単独読影を、多国の後ろ向きデータで101人の放射線科医と比較した。
- Objective: 乳癌検出でAIが平均的な読影医に対し、事前に決めた許容差の範囲で非劣性か評価する。
- Methods: 7か国・4機器メーカーに由来する9読影研究の2,652検査（悪性653）と28,296判定を統合。非劣性マージン0.05でAUCを比較した。
- Data and results: AIのAUC0.840、医師平均0.814、差の95%CIは−0.003–0.055で非劣性を示した。AIは医師の61.4%より高いAUCだった。
- Novelty: 少数の読影医に限らず、多施設・多国の多数の医師を同じ後ろ向き比較へ取り込んだ。
- Limitations: 著者は実際の検診場面での性能・影響の検証を求める。非劣性は優越性とは異なり、AI単独の読影試験から併用支援の効果は分からない。
- Publication date note: 出版社PDFのFirst published online March 5, 2019を採用。巻号の2019年9月と区別。出典: https://academic.oup.com/jnci/article-pdf/111/9/916/31963401/djy222.pdf

### Paper: CE-Net: Context Encoder Network for 2D Medical Image Segmentation
- Source: PubMed
- Canonical ID: pmid:30843824
- Publication date: 2019-03-07
- URL: https://pubmed.ncbi.nlm.nih.gov/30843824/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: CE-Netは多尺度の文脈を取り入れ、2次元医用画像の分割で空間情報の損失に対処する。
- Objective: 連続するpoolingやstride付き畳み込みで失われる位置情報を補い、高位の文脈も捉える。
- Methods: 事前学習ResNetの特徴抽出器、dense atrous convolutionとresidual multi-kernel poolingによる文脈抽出器、復号器を組み合わせた。
- Data and results: 視神経乳頭、血管、肺、細胞輪郭、網膜OCT層の分割で元のU-Netや比較法を上回ると報告。要旨にデータ数・課題別スコアはない。
- Novelty: encoder–decoder型の分割器へ、拡張畳み込みと複数受容野のpoolingを組み合わせた文脈処理を加えた。
- Limitations: 編者の注意: 2次元の複数課題の結果であり、3次元処理や別施設への性能を保証しない。計算費用と改善幅の比較には本文の実験条件が必要。

### Paper: Development and Validation of a Deep-Learning Model to Screen for Hyperkalemia From the Electrocardiogram
- Source: PubMed
- Canonical ID: pmid:30942845
- Publication date: 2019-04-03
- URL: https://pubmed.ncbi.nlm.nih.gov/30942845/
- read_level: full_text
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 少数誘導のECGから高カリウム血症を検出し、腎疾患患者の複数拠点で検証した。
- Objective: 採血前の非侵襲スクリーニングを想定し、心電図に表れる高カリウム血症の情報を利用する。
- Methods: 449,380人の約158万ECGでCNNを学習。CKDステージ3以上の61,965例を3拠点で評価し、4時間以内の採血を参照。本文の高カリウム血症定義は5.5mEq/L以上。
- Data and results: I・II誘導のAUCはMinnesota0.883、Florida0.860、Arizona0.853。高感度閾値の感度は88.9–91.3%、特異度54.7–63.2%だった。
- Novelty: ECGからリズム以外の血液生化学異常を推定し、少数誘導での検出を複数拠点で検証した。
- Limitations: 要旨の閾値『5.5以下』は本文Methodsの『以上』と矛盾するため本文を採用。編者の注意: 偽陽性が少なくなく、採血の代替や前向き臨床利益は未実証。
- Publication date note: 出版社のPublished Online April 3, 2019を採用。巻号の2019年5月と区別。出典: https://jamanetwork.com/journals/jamacardiology/fullarticle/2729582

本文の照合箇所: [MethodsのValidation Study・Hyperkalemia、電子公開日](https://jamanetwork.com/journals/jamacardiology/fullarticle/2729582)。

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

### Paper: An artificial intelligence-enabled ECG algorithm for the identification of patients with atrial fibrillation during sinus rhythm: a retrospective analysis of outcome prediction
- Source: PubMed
- Canonical ID: pmid:31378392
- Publication date: 2019-08-01
- URL: https://pubmed.ncbi.nlm.nih.gov/31378392/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 洞調律中の短い12誘導ECGから、心房細動を持つ患者を識別する研究。
- Objective: 長時間のモニタリングを全員に行わず、追加検査の候補となる心房細動患者を見つける。
- Methods: 成人180,922人の洞調律ECG649,931件を使い、心房細動・粗動記録の有無をラベル化。CNNを7:1:2の学習・検証・テストで評価した。
- Data and results: 単一ECGのAUC0.87、感度79.0%、特異度79.5%、F1 39.2%。期間内の複数ECGを使うとAUC0.90、F1 45.4%へ改善した。
- Novelty: 異常リズムが記録された瞬間だけでなく、正常リズムの信号に残る患者の特徴を利用した。
- Limitations: 編者の注意: テスト陽性群には洞調律ECGより前に心房細動が確認された患者が含まれ、純粋な将来新規発症予測ではない。AUROCの高さと低いF1を併記して読む。

### Paper: MultiResUNet : Rethinking the U-Net architecture for multimodal biomedical image segmentation
- Source: PubMed
- Canonical ID: pmid:31536901
- Publication date: 2019-09-04
- URL: https://pubmed.ncbi.nlm.nih.gov/31536901/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: MultiResUNetはU-Netの改変を、容易な画像と難しい医用画像で比較した分割モデル。
- Objective: U-Netが難しい画像で残す不足を補い、異なる医用画像データで性能を改善する。
- Methods: U-Netの構造を改変したMultiResUNetを提案し、固有の難しさを持つ5データセットで古典的U-Netと定量・定性比較した。要旨に各構成部品の詳細はない。
- Data and results: 5データの相対改善は10.15%、5.07%、2.63%、1.41%、0.62%。理想的画像での改善は小さく、難しい画像で大きいと報告した。
- Novelty: 共通のencoder–decoderを維持しつつ、難例の扱いを改善するU-Net拡張の一例を示した。
- Limitations: 編者の注意: 改善率を絶対ポイントと読み替えない。要旨に指標名・データ別対応がなく、全課題で同じ幅の改善やU-Netの一般的な置換を主張できない。

### Paper: Unified rational protein engineering with sequence-based deep representation learning
- Source: PubMed
- Canonical ID: pmid:31636460
- Publication date: 2019-10-21
- URL: https://pubmed.ncbi.nlm.nih.gov/31636460/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: UniRepは未ラベルのタンパク質配列から汎用表現を学び、機能・安定性の予測へ使った。
- Objective: 配列に含まれる構造・進化・生物物理情報を、タンパク質工学で再利用可能な表現へまとめる。
- Methods: 未ラベルのアミノ酸系列に深層学習を適用し、得た表現上に単純な予測器を構築。天然・新規設計の安定性と多様な変異体の定量的機能を評価した。
- Data and results: 未経験の配列空間でも比較法に匹敵する予測を示し、1つの工学課題で2桁の効率改善を報告。要旨に対象数や各課題の絶対スコアはない。
- Novelty: 課題ごとの専用特徴から、ラベルなし配列で学ぶ共通表現を多数の工学課題へ転用した。
- Limitations: 編者の注意: 100倍相当の改善は特定課題の効率に関する結果で、全タンパク質の精度や実験数削減の保証ではない。機能確認には実験が残る。

### Paper: Dissecting racial bias in an algorithm used to manage the health of populations
- Source: PubMed
- Canonical ID: pmid:31649194
- Publication date: 2019-10-25
- URL: https://pubmed.ncbi.nlm.nih.gov/31649194/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 医療支援対象を選ぶ商用予測器で、医療費を健康の代理にしたことが人種格差を生んだ。
- Objective: 広く使われる集団健康管理アルゴリズムで、同じリスク値が同じ医療ニーズを表すか検証する。
- Methods: 同じスコアの黒人・白人患者で病状を比較し、予測対象の費用と実際の疾患負担の違い、医療アクセスの不均衡を分析した。
- Data and results: 同スコアでも黒人患者は重症だった。格差を補正すると追加支援を受ける黒人患者の割合は17.7%から46.5%に増えると推定した。
- Novelty: モデルの精度の問題に限らず、便利な代理目的変数の選択そのものが不公平を作る機序を示した。
- Limitations: 編者の注意: 46.5%は是正後の推定で、介入試験の実測転帰ではない。医療費を使う特定用途の分析から、あらゆるモデルで同じ格差量を予測できない。

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

### Paper: Improved protein structure prediction using predicted interresidue orientations
- Source: PubMed
- Canonical ID: pmid:31896580
- Publication date: 2020-01-02
- URL: https://pubmed.ncbi.nlm.nih.gov/31896580/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: trRosettaにつながる手法は、残基間距離に向きの情報を加えて構造推定を改善した。
- Objective: 共進化から得る残基対の幾何学情報を増やし、より速く正確な構造最適化を行う。
- Methods: 深い残差モデルで距離と相対配向を予測し、Rosettaの制約付きエネルギー最小化で構造化。CASP13とCAMEO由来のセットで比較した。
- Data and results: 比較した既報の構造予測法を上回った。天然タンパク質のみで学習したモデルが新規設計に高い確率を与え、折り畳みを決める残基の評価にも使えた。要旨に絶対スコアはない。
- Novelty: 単なる接触・距離だけでなく、残基の配向を学習制約へ組み込み、予測と設計の評価へ接続した。
- Limitations: 編者の注意: 計算上の構造・確率の評価は、新規タンパク質の機能や安定性の実験的保証ではない。既報との優越性は当時の比較対象とベンチマークに限る。

### Paper: Artificial intelligence for diagnosis and grading of prostate cancer in biopsies: a population-based, diagnostic study
- Source: PubMed
- Canonical ID: pmid:31926806
- Publication date: 2020-01-08
- URL: https://pubmed.ncbi.nlm.nih.gov/31926806/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 前立腺生検の癌検出、癌の長さ、Gleason分類を独立標本と外部標本で検証した。
- Objective: 病理医不足と分類のばらつきに対応する、臨床的に許容できる生検評価器を作る。
- Methods: STHLM3の976人6,682スライドなどで学習。独立246人1,631生検、外部73人330生検で評価し、87生検の分類を23人の専門医とも比較した。
- Data and results: 癌検出AUCは内部0.997、外部0.986。癌長の相関は0.96、0.87。Gleason分類の平均ペアκは0.62で、専門医の0.60–0.73の範囲内だった。
- Novelty: 癌の有無だけでなく、量と悪性度分類を一連の病理支援として外部検証した。
- Limitations: 編者の注意: 分類の一致度は専門医間の幅の中にあり、すべての専門医への優越性を示さない。業務負荷や過剰治療・過小治療への実際の影響は追加検証が必要。

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

### Paper: Improved protein structure prediction using potentials from deep learning
- Source: PubMed
- Canonical ID: pmid:31942072
- Publication date: 2020-01-15
- URL: https://pubmed.ncbi.nlm.nih.gov/31942072/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 初期AlphaFoldは残基間距離からポテンシャルを作り、勾配法で構造を求めた。
- Objective: 接触の有無より豊かな距離情報を用い、複雑な標本探索なしにタンパク質構造を改善する。
- Methods: 深層モデルで残基対の距離を予測して平均力ポテンシャルへ変換し、勾配降下で最適化。盲検のCASP13で比較した。
- Data and results: free modellingの43ドメイン中24でTM-score≥0.7の高精度構造を得た。接触情報と探索を使う次点手法は14/43だった。
- Novelty: 二値の残基接触から距離分布へ進み、学習した幾何学的制約を直接構造最適化へ使った。
- Limitations: 編者の注意: CASP13の特定ドメイン群の結果であり、後年のAlphaFold2と同じ構造や精度ではない。高いTM-scoreも機能・動態の完全な再現を示さない。

### Paper: A 12-lead electrocardiogram database for arrhythmia research covering more than 10,000 patients
- Source: PubMed
- Canonical ID: pmid:32051412
- Publication date: 2020-02-12
- URL: https://pubmed.ncbi.nlm.nih.gov/32051412/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: Chapman–Shaoxingの12誘導ECGデータを公開し、多数の不整脈・状態の研究を支えた。
- Objective: 高品質なECGと専門家ラベルを共有し、検出器の設計・比較・微調整を可能にする。
- Methods: 10,646人の10秒・12誘導信号を500Hzで収集し、11の一般的なリズムと追加67状態を専門家がラベル付けした。
- Data and results: 患者別の信号とリズム・病態ラベルを備える研究資源を提供。要旨は特定モデルの精度を報告する論文ではない。
- Novelty: 多誘導かつ1万人超の公開臨床データを、複数のリズム・心血管状態の学習に利用可能にした。
- Limitations: 編者の注意: 10秒記録であり、長時間モニタリングデータではない。施設・収集条件・ラベルの不均衡を考慮し、患者をまたいだ分割で評価する必要がある。

### Paper: Assessing and Mitigating Bias in Medical Artificial Intelligence: The Effects of Race and Ethnicity on a Deep Learning Model for ECG Analysis
- Source: PubMed
- Canonical ID: pmid:32064914
- Publication date: 2020-02-16
- URL: https://pubmed.ncbi.nlm.nih.gov/32064914/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 低左室駆出率を検出するECGモデルについて、人種・民族群ごとの識別性能を調べた。
- Objective: 均質な集団で作られたモデルが他集団で劣るか、波形の集団差が性能へ影響するか検証する。
- Methods: ECGと心エコーのある97,829人を後ろ向き解析。非ヒスパニック白人96.2%の開発群44,959人で作ったCNNを、別の52,870人でLVEF≤35%の検出に評価した。
- Data and results: 検証AUCは非ヒスパニック白人0.931、アジア0.961、黒人0.937、ヒスパニック0.937、米先住民等0.938。人種を推定する別モデルも波形から集団情報を識別できた。
- Novelty: 波形に集団情報が存在することと、疾患分類で集団間格差が生じることを分けて調べた。
- Limitations: 編者の注意: 少数群は数百人で、AUCが近いことだけでは校正・誤警報・アクセスの公平性を証明しない。この検出課題の結果を他の医療AIへ一般化できない。

### Paper: A Deep Learning Approach to Antibiotic Discovery
- Source: PubMed
- Canonical ID: pmid:32084340
- Publication date: 2020-02-20
- URL: https://pubmed.ncbi.nlm.nih.gov/32084340/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 抗菌活性を予測する深層モデルからhalicinなどの候補を見つけ、実験へつなげた。
- Objective: 既知抗菌薬と構造の異なる活性分子を、大規模な化合物空間から探索する。
- Methods: 抗菌活性を学習したモデルで複数ライブラリを探索。Drug Repurposing Hubのhalicinをin vitro・マウス感染で検証し、ZINC15の1億700万超の分子もスクリーニングした。
- Data and results: halicinは広い菌群で殺菌活性を示し、マウスのC. difficileと汎耐性A. baumannii感染を治療。ZINC15から選んだ23予測候補の実験で8抗菌化合物を得た。
- Novelty: 既知薬に近い構造の探索だけでなく、予測モデルによる候補選別と生物学的検証を結び付けた。
- Limitations: 編者の注意: 選択した23候補の結果を全ライブラリの的中率と扱わない。試験管・マウスでの活性であり、ヒトでの薬効・安全性や臨床使用を確立しない。

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
- Objective: 多数の疾患を同時に予測する電子カルテAIでは、患者の診断系列を固定長の集計特徴へ押し込むと、診療の順序、年齢、受診時点の情報が失われやすい。Transformerを患者系列に適用することで、将来の複数疾病を一つの共通表現から予測できるかを調べた。
- Methods: 約160万人のEHRを利用し、診断コードを時系列として埋め込み、受診時点、年齢、位置などを患者系列のTransformer BEHRTで表現した。自己教師ありの事前学習表現を複数の将来診断課題へ転用し、従来の深層EHRモデル等と比較。単一の疾病の分類だけでなく301疾病を同時に扱い、注意・表現の検討も行った。
- Data and results: 約160万人の記録で学習・評価し、301疾病の将来発生に関する課題で従来表現より平均適合率（average precision）が8.0〜13.2%向上したと報告。ただし要旨に疾患ごとの絶対値や改善がポイントか相対値かの全内訳はなく、数値をAUROCや患者一人の正答率へ読み替えない。
- Novelty: EHRの時系列を言語モデルのトークン列になぞらえ、事前学習した患者表現を多数の予測課題へ再利用した。患者の状態履歴を逐次的に表現する価値と、特定の疾患だけの手作業特徴を減らす可能性を示す。
- Limitations: 予測が良くなることと、治療を変えたら発症が防げるという因果関係は異なる。病院間のコーディング慣行、時期・患者の違い、モデルの校正や意思決定効用は個別に検証が必要。

### Paper: Efficacy of Real-Time Computer-Aided Detection of Colorectal Neoplasia in a Randomized Trial
- Source: PubMed
- Canonical ID: pmid:32371116
- Publication date: 2020-05-01
- URL: https://pubmed.ncbi.nlm.nih.gov/32371116/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: イタリア3施設の無作為試験で、AI内視鏡支援が腺腫発見率を高めた。
- Objective: 実時間CADe支援が腫瘍性病変の発見を増やし、検査時間や不要切除へ影響するか調べる。
- Methods: 2019年の685人を支援あり・なしへ1:1に無作為化。GI-Geniusが疑わしい病変を表示し、6分以上の抜去時間を要求。組織診を参照し腺腫発見率を主要転帰とした。
- Data and results: 腺腫発見率は54.8%対40.4%、1検査あたり腺腫は1.07対0.71。抜去時間417対435秒、非腫瘍性病変切除26.0%対28.7%には有意差がなかった。
- Novelty: 複数施設で人とAIを組み合わせ、検出増加だけでなく時間と不要切除も評価した。
- Limitations: 編者の注意: この試験の主転帰は病変発見で、癌罹患・死亡の減少ではない。絶対率から単純計算した比を原著の調整済み効果量と混同しない。

### Paper: Prediction of mortality from 12-lead electrocardiogram voltage data using a deep neural network
- Source: PubMed
- Canonical ID: pmid:32393799
- Publication date: 2020-05-11
- URL: https://pubmed.ncbi.nlm.nih.gov/32393799/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 12誘導ECGの電圧系列から、医師が正常とした記録も含めて1年死亡リスクを予測した。
- Objective: 通常の波形判読に加え、深層学習が将来の全死亡に関する予後情報を抽出できるか調べる。
- Methods: 地域医療システムの34年分、253,397人の1,169,662ECGで学習。別の168,914人で評価し、正常判定45,285人と循環器医の盲検レビューも調べた。
- Data and results: 1年全死亡のAUC0.88、正常判定群でも0.85。予測高低群の25年追跡でハザード比9.5だった。医師には一部の識別特徴が明瞭でなかった。
- Novelty: 既知のECG診断ラベルを再現するだけでなく、波形から将来転帰の追加情報を学習した。
- Limitations: 編者の注意: 全死亡の関連予測であり、心疾患による死亡や介入可能な原因を特定しない。単一医療システムでの評価と、導入による生存改善は別である。

### Paper: Pan-cancer image-based detection of clinically actionable genetic alterations
- Source: PubMed
- Canonical ID: pmid:33763651
- Publication date: 2020-07-27
- URL: https://pubmed.ncbi.nlm.nih.gov/33763651/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 通常のH&E病理画像から、複数癌種の遺伝的変化や分子指標を推定する統合手順を示した。
- Objective: 日常の組織標本に現れる形態から、治療選択に関わる分子情報を推定できるか調べる。
- Methods: 開発・最適化・検証・公開を含む深層学習手順を、複数固形癌の5,000人超に適用。変異、分子亜型、遺伝子発現署名、病理バイオマーカーを扱った。
- Data and results: 複数の分子変化を予測し、他集団への汎化と空間的な推定を報告。モバイル機器への実装可能性も示すが、要旨に各標的のAUCはない。
- Novelty: 単一癌種・単一変異の研究を、通常染色から多数の分子標的を扱う共通ワークフローへ広げた。
- Limitations: 編者の注意: モバイル実装の可能性は、現場検査としての承認や治療選択の利益を意味しない。分子検査の代替可否には標的別性能と外部検証が必要。

### Paper: Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension
- Source: PubMed
- Canonical ID: pmid:32908283
- Publication date: 2020-09-09
- URL: https://pubmed.ncbi.nlm.nih.gov/32908283/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: CONSORT-AIはAIを含む無作為試験の結果報告に、14の追加項目を定めた。
- Objective: AI介入が患者転帰へ与える影響を、透明で批判的に評価できる試験報告を促す。
- Methods: 文献・専門家相談で候補を作り、103人の2段階Delphi、31人の合意会議、34人の試行で精緻化。SPIRIT-AIと並行開発した。
- Data and results: CONSORT 2010に加える14項目を採択。利用者の技能、導入環境、入出力の扱い、人とAIの相互作用、誤り事例の解析などを明記する。
- Novelty: アルゴリズムの性能だけでは報告できない、AIを含む介入と人・現場の条件を試験報告へ組み込んだ。
- Limitations: 編者の注意: 報告指針であり、個別AIの臨床効果を示す試験ではない。遵守していても研究設計や対象集団への適合性は独立に評価する必要がある。

### Paper: Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension
- Source: PubMed
- Canonical ID: pmid:32908284
- Publication date: 2020-09-09
- URL: https://pubmed.ncbi.nlm.nih.gov/32908284/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: SPIRIT-AIはAI介入の臨床試験計画書へ、15の追加報告項目を定めた。
- Objective: 試験開始前にAIの仕様と利用条件を明確にし、計画の評価可能性を高める。
- Methods: 文献と専門家相談、103人の2段階Delphi、31人の合意会議、34人の試行を通じて作成。CONSORT-AIと並行して検討した。
- Data and results: SPIRIT 2013に追加する15項目を採択。使用技能、組込み環境、入力・出力、人とAIの相互作用、誤り事例の解析計画などを扱う。
- Novelty: 実施後の報告だけでなく、計画段階でAI介入の再現性と評価条件を明示する共通枠組みを作った。
- Limitations: 編者の注意: 計画書の報告指針で、手順の遵守や介入の成功を保証しない。結果報告用CONSORT-AIとは用途を区別する。

### Paper: External validation of prognostic models: what, why, how, when and where?
- Source: PubMed
- Canonical ID: pmid:33564405
- Publication date: 2020-11-24
- URL: https://pubmed.ncbi.nlm.nih.gov/33564405/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 予後モデルの外部検証を、目的・対象選択・統計解析・現場への解釈に分けて解説した。
- Objective: 予後モデルが開発集団で良い精度を示しても、別の患者・施設・時期へ移ったときに予測確率が妥当かは分からない。外部検証をどの患者集団で、いつ、どの目的で行うべきかを方法論として明らかにする。
- Methods: 外部検証のための患者の選び方、開発対象との違い、予測因子と転帰の定義、識別・校正の評価、必要に応じた再校正やモデル更新を体系的に解説した方法論レビュー。新たな臨床コホートを用いる単一モデルの比較実験ではなく、既存の検証研究から設計と結果解釈の実務を説明する。
- Data and results: 既存モデルの出力を独立データに適用し、識別力が残っているか、確率が系統的にずれるかを検査することの重要性を整理。新しい患者数やAUC改善幅を直接報告した研究ではない。外部検証で成績が下がっても、患者構成や転帰頻度の差による影響を分離する必要がある。
- Novelty: 単純な『外部データで精度を測った』という有無の区別から、どんな分布差に耐えられるのかを意識した評価設計へ議論を深めた。医療予測の研究で時期外・施設外の校正を確認する根拠になる。
- Limitations: 実用的な方法論的指針であり、特定モデルの一般化や臨床介入効果を証明するものではない。目的と対象集団に合わせた外部検証と意思決定閾値の評価は個別に必要。

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

### Paper: Deep Neural Networks Can Predict New-Onset Atrial Fibrillation From the 12-Lead ECG and Help Identify Those at Risk of Atrial Fibrillation-Related Stroke
- Source: PubMed
- Canonical ID: pmid:33588584
- Publication date: 2021-02-16
- URL: https://pubmed.ncbi.nlm.nih.gov/33588584/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 心房細動歴のない患者の12誘導ECGから、1年以内の新規心房細動を予測した。
- Objective: 未診断の心房細動と関連脳卒中を減らすため、追加スクリーニング候補を事前に絞る。
- Methods: 43万人・160万ECGで学習し、1年新規発症を評価。2010年以前で学習、2010–2014年でテストする運用模擬と脳卒中レジストリへの照合も行った。
- Data and results: AUROC0.85、AUPRC0.22。運用模擬の感度69%、特異度81%、新規1例に必要な検査数9。3年以内の心房細動関連脳卒中患者の62%を高リスクに分類した。
- Novelty: 現在の不整脈判定を超え、将来発症と関連脳卒中を結び付けて時間分割で評価した。
- Limitations: 編者の注意: 運用は後ろ向きの模擬で、実介入による脳卒中減少は示していない。AUROCとAUPRCを併記し、高リスクラベルが確定診断ではないことを区別する。

### Paper: Multi-domain clinical natural language processing with MedCAT: The Medical Concept Annotation Toolkit
- Source: PubMed
- Canonical ID: pmid:34127232
- Publication date: 2021-05-01
- URL: https://pubmed.ncbi.nlm.nih.gov/34127232/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: MedCATは医学概念の自己教師あり抽出と人の注釈を組み合わせ、施設間での転用を調べた。
- Objective: UMLSやSNOMED-CTの概念を自由記載から抽出し、個別施設の用途に調整できるようにする。
- Methods: 概念抽出アルゴリズム、注釈画面、CogStack連携を提供。ロンドン3病院の約1,700万記録・88億語で自己教師あり学習し、約6,000の臨床家注釈で微調整した。
- Data and results: 公開データのUMLS抽出F1は0.448–0.738、比較法0.429–0.650。臨床施設・データ・概念間の転用ではF1>0.94と報告した。
- Novelty: 大きな医学語彙の抽出と、現場の人が継続的に修正する運用環境を組み合わせた。
- Limitations: 編者の注意: 公開データと実臨床データのF1は評価範囲が異なり直接比較しない。高い転用成績から任意施設での調整不要や未検証言語への性能を推論できない。

### Paper: Deep Learning for ECG Analysis: Benchmarks and Insights from PTB-XL
- Source: PubMed
- Canonical ID: pmid:32903191
- Publication date: 2021-05-11
- URL: https://pubmed.ncbi.nlm.nih.gov/32903191/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: PTB-XLでECGモデルを共通比較し、精度に加え潜在的な下位集団差や不確実性を検討した。
- Objective: 適切な公開データと評価手順の不足を補い、自動ECG解析を比較可能にする。
- Methods: 12誘導ECGの診断記述、年齢、性別など複数課題で深層時系列分類器を比較。ICBEB2018で整合性、転移学習、hidden stratification、不確実性、解釈も調べた。
- Data and results: ResNet・Inception系CNNが全課題で強く、別のICBEB2018でも一貫した傾向。要旨にモデル別スコアや対象数はない。
- Novelty: 平均的な正解率の順位だけでなく、臨床的に重要な部分集団や信頼度へ評価を広げた。
- Limitations: 編者の注意: 公開データの基準比較であり、導入後の診療成績を示さない。平均性能が良好でも、特定の異常や集団での誤差を個別に確認する必要がある。

### Paper: Med7: A transferable clinical natural language processing model for electronic health records
- Source: PubMed
- Canonical ID: pmid:34412834
- Publication date: 2021-05-18
- URL: https://pubmed.ncbi.nlm.nih.gov/34412834/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: Med7は薬剤に関する7種の項目を抽出し、米国ICUから英国精神科への転用を検証した。
- Objective: 少数の正解注釈で臨床情報を構造化し、別領域への転移学習の条件を調べる。
- Methods: MIMIC-IIIの200万記録で次語予測を事前学習し、薬剤名、経路、頻度、用量、強度、剤形、期間のNERへ微調整。英国CRISへ直接適用し、少量追加学習も評価した。
- Data and results: 元領域のmicro-F1は0.957。CRISへの直接移植では0.762へ低下し、少量のCRISで微調整すると0.944へ回復した。
- Novelty: 自己教師あり表現の有用性に加え、似た抽出課題でも医療領域が変わると追加調整が重要と示した。
- Limitations: 編者の注意: 領域適応後の高精度を調整不要の汎化と混同しない。薬剤の言及抽出は実際の服用状態や処方の安全性評価とは異なる。

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

### Paper: Minimum sample size for external validation of a clinical prediction model with a binary outcome
- Source: PubMed
- Canonical ID: pmid:34031906
- Publication date: 2021-05-24
- URL: https://pubmed.ncbi.nlm.nih.gov/34031906/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 外部検証の標本数を、一律のイベント数ではなく性能指標の推定精度から設計する方法。
- Objective: 小標本で不確実な検証が多い問題を補い、校正・識別・臨床効用を十分な精度で推定する。
- Methods: 目標の標準誤差、イベント率、予測値の分散・校正、意思決定閾値から、観測/期待比、校正傾き、C統計量、net benefitの必要人数を計算する。
- Data and results: 人工心臓弁不全の例（イベント率0.018）では校正・識別に9,835人177イベント、8%閾値のnet benefitに6,443人116イベントを要した。前者は校正傾きが必要数を決めた。
- Novelty: 『100イベント』等の目安から、検証で知りたい性質と許容する不確かさに応じた設計へ進めた。
- Limitations: 編者の注意: 必要数は想定イベント率、線形予測子分布、校正などの事前仮定に依存する。例の人数をすべての予測器・部分集団に適用しない。

### Paper: External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients
- Source: PubMed
- Canonical ID: pmid:34152373
- Publication date: 2021-06-21
- URL: https://pubmed.ncbi.nlm.nih.gov/34152373/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 広く導入されたEpic敗血症モデルの外部評価で、低い識別力と大きな警報負担を報告した。
- Objective: 非公開の予測器が、新しい病院で通常診療に加える価値を持つか検証する。
- Methods: Michigan Medicineの27,697人・38,455入院を後ろ向き解析。15分ごとのモデル値を敗血症基準・抗菌薬投与と照合し、識別、校正、警報負担を測った。
- Data and results: 敗血症2,552入院、入院単位AUROC0.63。閾値6以上で全入院の18%に警報を出しながら敗血症の67%を拾えず、適時抗菌薬がない敗血症183例を同定した。
- Novelty: 導入実績を性能の証明とせず、独立病院で既存診療への追加価値と警報負担を監査した。
- Limitations: 編者の注意: 1大学施設・後ろ向き・当時のモデル版の結果で、後年の更新版全般の評価ではない。閾値や敗血症定義で値は変わり、実導入の効果試験とも区別する。
- Publication date note: 出版社のPublished Online June 21, 2021を採用。巻号の2021年8月と区別。出典: https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307

### Paper: Highly accurate protein structure prediction with AlphaFold
- Source: PubMed
- Canonical ID: pmid:34265844
- Publication date: 2021-07-15
- URL: https://pubmed.ncbi.nlm.nih.gov/34265844/
- read_level: full_text
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: AlphaFold2は進化情報と幾何学的な構造を統合し、CASP14で原子精度に近い予測を示した。
- Objective: アミノ酸配列が分かっても3次元の原子配置を予測するのは難しく、物理シミュレーションだけでは探索空間が膨大になる。既知の類似タンパク質が少ない場合も含め、配列・進化情報から構造の座標まで直接予測できるかを問う。
- Methods: AlphaFold2は多重配列アラインメントの進化的な関係と残基対の情報をEvoformerで相互更新し、構造モジュールで3次元座標を構築する。予測した構造をrecyclingで繰り返し改良。CASP14で正解構造を伏せた盲検評価を実施し、後発のPDB構造とも照合した。従来の距離予測＋探索という二段階構成とは異なる。
- Data and results: CASP14の87ドメインで、骨格のr.m.s.d._95中央値は0.96Å（次点2.8Å）、全原子では1.5Å（次点3.5Å）と報告。残基ごとに推定信頼度を提供することで、全配列で同じ確実性があるかのような表示を避ける設計になっている。
- Novelty: 進化・残基対・3D座標を一体で学習・推論し、原子レベルへ近い構造予測を多数の未知標的で実証した。創薬で候補の構造仮説を得る能力を大きく進めたが、構造を知ることと動的な相互作用や薬効を予測することは別である。
- Limitations: MSAが浅い例、異種鎖の接触に依存する立体構造、複合体や動的構造で不確実性が残る。単一の構造予測は折り畳みの過程・溶液中の構造集合・生理機能を直接実証しない。

本文の照合箇所: [Fig.1・Accuracy、Evoformer、End-to-end structure prediction、MSA depth and cross-chain contacts](https://pmc.ncbi.nlm.nih.gov/articles/PMC8371605/)。

### Paper: Highly accurate protein structure prediction for the human proteome
- Source: PubMed
- Canonical ID: pmid:34293799
- Publication date: 2021-07-22
- URL: https://pubmed.ncbi.nlm.nih.gov/34293799/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: AlphaFoldをヒトのほぼ全タンパク質へ適用し、構造と領域別の信頼度を公開した。
- Objective: 実験構造で覆われていないヒト配列へ、研究に使える構造仮説を大規模に提供する。
- Methods: AlphaFoldでヒトプロテオームを予測し、信頼度の指標で多ドメイン構造や無秩序の可能性のある領域を解釈。生物学的仮説の事例も示した。
- Data and results: ヒトタンパク質の98.5%を対象とし、全残基の58%に信頼できる予測、36%に非常に高い信頼度の予測を提供。既存実験構造の全残基カバー率は17%だった。
- Novelty: 構造予測法の競技成績から、プロテオーム全体に配布可能な研究資源へ展開した。
- Limitations: 編者の注意: 98.5%はタンパク質数の対象範囲で、全残基が高精度という意味ではない。予測の信頼度と実験的な確証、疾患変異や創薬への有効性は区別する。

### Paper: ECG-Based Deep Learning and Clinical Risk Factors to Predict Atrial Fibrillation
- Source: PubMed
- Canonical ID: pmid:34743566
- Publication date: 2021-11-08
- URL: https://pubmed.ncbi.nlm.nih.gov/34743566/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: ECGによる心房細動リスクと臨床リスクスコアが、外部集団でも相補的か検証した。
- Objective: ECGのAI解析が、従来の臨床危険因子を超える汎化可能な予測情報を持つか調べる。
- Methods: 45,770人で5年リスクのCNNを学習。ECG-AI、CHARGE-AF、両者統合のCoxモデルを内部とBWH・UK Biobankで評価。追跡が短いUKは2年リスクへ再校正した。
- Data and results: 内部/BWH/UKのAUCは臨床スコア0.802/0.752/0.732、ECG-AI0.823/0.747/0.705、統合0.838/0.777/0.746。単独では概ね同等、統合が最良だった。
- Novelty: AI単独の高いスコアではなく、既存リスク評価への追加価値を複数の外部集団で検証した。
- Limitations: 編者の注意: UKは予測期間と再校正条件が他群と異なる。P波のsaliencyは生物学的機序の証明ではなく、スクリーニング導入後の利益は別途必要。

### Paper: SignalP 6.0 predicts all five types of signal peptides using protein language models
- Source: PubMed
- Canonical ID: pmid:34980915
- Publication date: 2022-01-03
- URL: https://pubmed.ncbi.nlm.nih.gov/34980915/
- read_level: full_text
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: SignalP 6.0はタンパク質言語表現から、5種類のシグナルペプチドと切断位置を推定する。
- Objective: 既存法が扱えなかった希少な種類も含め、分泌・輸送のシグナルを配列から識別する。
- Methods: BERT型表現とCRFを接続し、領域・種類を同時予測。相同配列を同じ分割に置く3分割nested交差検証で評価した。
- Data and results: 5種類を同時検出。特にSec/SPIII（113例）とTat/SPII（36例）で改善し、学習配列との同一性60%未満でも旧版を上回った。
- Novelty: 大量の未ラベル配列で学ぶ表現を、少数例のシグナルと構造化された領域予測へ転用した。
- Limitations: 一部の専用予測器が得意課題で上回る。著者は他の公開サービスの比較で相同性を揃えられないバイアスも指摘し、全条件での優越性は主張しない。

本文の照合箇所: [Fig.1–2、Methodsのdata partitioning・Evaluation and benchmarking](https://pmc.ncbi.nlm.nih.gov/articles/PMC9287161/)。

### Paper: Harnessing protein folding neural networks for peptide-protein docking
- Source: PubMed
- Canonical ID: pmid:35013344
- Publication date: 2022-01-10
- URL: https://pubmed.ncbi.nlm.nih.gov/35013344/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 単量体用に作られたAlphaFold2を、ペプチドとタンパク質のドッキングへ応用した。
- Objective: 結合に伴う受容体の変形も含め、ペプチド複合体を迅速にモデル化する。
- Methods: ペプチド側の多重配列アラインメントを要求しない簡単なAlphaFold2実装を評価。記憶と学習の役割を検討し、PIPER-FlexPepDockと具体例を比較した。
- Data and results: 迅速で正確な複合体モデルと、結合に誘導される受容体変形への対応を報告。要旨に成功率や構造誤差の値はない。
- Novelty: 単体の折り畳み予測器が、相互作用構造のモデリングにも使えることを示した。
- Limitations: 編者の注意: 要求しないのはペプチド側のMSAで、全入力で進化情報が不要という主張ではない。結合構造の予測は親和性・薬効の保証でもない。

### Paper: ProteinBERT: a universal deep-learning model of protein sequence and function
- Source: PubMed
- Canonical ID: pmid:35020807
- Publication date: 2022-04-12
- URL: https://pubmed.ncbi.nlm.nih.gov/35020807/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: ProteinBERTは局所・全体表現と機能注釈の事前学習を備えた、効率重視のタンパク質モデル。
- Objective: 文章向けモデルの転用を超え、長い配列と少量ラベルに適した共通予測基盤を作る。
- Methods: 配列言語モデルの学習とGene Ontology注釈予測を併用し、残基ごとの局所表現と全体表現を統合。構造、翻訳後修飾、生物物理特性のベンチマークで評価した。
- Data and results: 比較モデルより小さく高速な構成で、複数課題の最良法に近い性能、一部では上回る性能を報告。要旨にサイズ・速度・精度の具体値はない。
- Novelty: 機能の全体ラベルと配列の局所情報を同じ事前学習へ組み込み、用途の異なる出力を扱う。
- Limitations: 編者の注意: GO注釈を使うため、すべての事前学習がラベル不要という意味ではない。効率の主張は比較条件に依存し、全課題で最大精度を狙う設計ではない。

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

### Paper: Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI
- Source: PubMed
- Canonical ID: pmid:35585198
- Publication date: 2022-05-18
- URL: https://pubmed.ncbi.nlm.nih.gov/35585198/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: DECIDE-AIは小規模な初期臨床評価で、AI性能・安全性・人の要因を報告する指針。
- Objective: AI医療支援の研究では、開発時の診断成績と大規模なランダム化試験の間に、少人数の現場試験による適合性・安全性検証が存在する。この初期段階で何を報告すれば評価者が研究の妥当性を判断できるかを標準化する。
- Methods: 患者・医師・規制関係者など20の利害関係者群を含めて専門家を募集し、2回のmodified Delphiを実施（参加者123人、138人）。オンラインでの合意会議と定性的な検討には各16人が参加し、AIシステム、人間との相互作用、臨床的な安全性などの報告項目を合意形成によって整理した。
- Data and results: AI特有17項目（28下位項目）と一般10項目を含むDECIDE-AI報告ガイドラインを策定。研究段階・用途に応じて必要な情報を欠落なく伝える標準であり、チェック項目を守った製品のAUCや患者転帰が向上することを計測した介入結果ではない。
- Novelty: モデル単体のテストと大規模臨床試験の間にある、実際の現場で人間がAIをどう使うかという初期実装の報告単位を定義した。システム改修の過程や使用者の行動も評価対象へ含める必要を示す。
- Limitations: 専門家合意による報告指針であり、個別システムの有効性・安全性認定の代わりにはならない。項目の充足率をそのまま製品の性能点数として使うことは不適切。

### Paper: Robust deep learning-based protein sequence design using ProteinMPNN
- Source: PubMed
- Canonical ID: pmid:36108050
- Publication date: 2022-09-15
- URL: https://pubmed.ncbi.nlm.nih.gov/36108050/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: ProteinMPNNは与えた骨格に適合する配列を設計し、複数の構造・機能実験で検証した。
- Objective: 望むタンパク質の骨格構造が得られても、その骨格に安定して折り畳まれるアミノ酸配列を探す逆設計は難しい。Rosettaなど物理的なエネルギー評価に依存する方法に対し、深層学習で配列を効率よく提案できるかを検証した。
- Methods: タンパク質骨格の局所幾何学をグラフとして入力し、複数の残基と鎖の関係をメッセージパッシングするProteinMPNNで配列を生成した。既知の天然構造を与えて天然配列が回復される率をRosettaと比較したうえ、単量体・環状集合体・四面体粒子・結合体などについて提案配列を合成し、X線、cryo-EM、機能測定で検証した。
- Data and results: 天然骨格から元配列を復元する率はProteinMPNN 52.4%、Rosetta 32.9%。さらに物理設計で成功しなかった複数の構造・機能実験で提案配列による改善を報告。ただし配列回復率52.4%は新しいタンパク質の合成成功率や機能獲得率ではない。
- Novelty: 構造予測（配列→骨格）とは逆向きの『骨格→配列』を深層学習で現実的な設計工程へ接続した。生成した候補のスコアだけでなく実験的な構造・機能の再現で成功を確認するという、制約付き生成の重要な評価設計を示す。
- Limitations: 目標骨格が既に用意されていることを前提とし、骨格自体をゼロから考案する研究と区別すべき。天然配列への類似性と、目的とする結合・安定性・機能の実現は別の結果である。

### Paper: Large language models generate functional protein sequences across diverse families
- Source: PubMed
- Canonical ID: pmid:36702895
- Publication date: 2023-01-26
- URL: https://pubmed.ncbi.nlm.nih.gov/36702895/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: ProGenは特性タグ付きの配列生成を行い、天然配列と離れた人工酵素の活性を検証した。
- Objective: 多様なタンパク質ファミリーで、機能を制御した新しい配列を生成する。
- Methods: 19,000超のファミリー、2億8,000万配列で言語モデルを学習し、特性タグを付加。整備したファミリー配列で微調整し、5種のリゾチーム群などを検証した。
- Data and results: 人工リゾチームで天然に近い触媒効率を示し、天然配列との同一性は最低31.4%。chorismate mutaseとmalate dehydrogenaseへの適応も示した。
- Novelty: 文章の条件付き生成の考え方を、実験で機能する酵素配列の条件付き設計へ広げた。
- Limitations: 著者は十分な相同配列のあるファミリーでの微調整と条件付ける。編者の注意: 一部生成物の活性は全候補の成功率や未知の機能の自由設計を保証しない。

### Paper: Evolutionary-scale prediction of atomic-level protein structure with a language model
- Source: PubMed
- Canonical ID: pmid:36927031
- Publication date: 2023-03-16
- URL: https://pubmed.ncbi.nlm.nih.gov/36927031/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: ESMFoldはタンパク質言語モデルを構造予測へ使い、メタゲノム規模の構造カタログを作成した。
- Objective: 多重配列の進化情報に依存する予測より高速に、一次配列から原子レベルの構造を推定する。
- Methods: 最大150億パラメータへ拡大した配列言語モデルの表現を構造推定に利用し、大規模なメタゲノム配列へ適用した。
- Data and results: 高解像度予測の1桁の高速化を報告。6億1,700万超の配列の構造を予測し、うち2億2,500万超が高信頼度のESM Metagenomic Atlasを構築した。
- Novelty: 大きな配列モデルに現れる構造情報を利用し、配列検索を伴う従来の処理から高速な直接推定へ広げた。
- Limitations: 編者の注意: 高信頼度の計算予測は実験による構造決定ではない。全予測が同じ精度ではなく、速度比較の計算条件と信頼度の低い領域も確認する必要がある。

### Paper: Fine-tuning large neural language models for biomedical natural language processing
- Source: PubMed
- Canonical ID: pmid:37123444
- Publication date: 2023-04-14
- URL: https://pubmed.ncbi.nlm.nih.gov/37123444/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 医学NLPでの微調整の不安定さを調べ、モデルや課題ごとに異なる有効な対策を示した。
- Objective: 少数ラベルの医学課題で、大きい事前学習モデルを安定して調整する方法を得る。
- Methods: 事前学習条件の影響と、下位層の凍結、層別の学習率減衰、上位層の再初期化などを体系的に比較した。
- Data and results: BERT-BASEは下位層凍結、BERT-LARGE・ELECTRAは層別減衰が有効。少数例のBIOSSES類似度では上位層再初期化が最良。要旨にスコアや試行間分散の数値はない。
- Novelty: 単一の微調整手順を推奨せず、事前学習・モデル規模・下流課題の組合せに応じた安定化を検証した。
- Limitations: 編者の注意: 特定モデル群と課題の実験であり、すべてのモデルへ同じ調整則を適用できない。最良スコアだけでなく乱数や少数ラベル選択による変動の確認が必要。

### Paper: ChatDoctor: A Medical Chat Model Fine-Tuned on a Large Language Model Meta-AI (LLaMA) Using Medical Domain Knowledge
- Source: PubMed
- Canonical ID: pmid:37492832
- Publication date: 2023-06-24
- URL: https://pubmed.ncbi.nlm.nih.gov/37492832/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: ChatDoctorは患者・医師対話の微調整と情報検索を組み合わせた医療対話モデル。
- Objective: 一般LLMの医療知識不足に対し、患者相談の理解と情報に基づく応答を改善する。
- Methods: オンライン相談由来の10万対話を清掃・匿名化してLLaMAを微調整。Wikipediaなどのオンライン情報と整備したオフライン医学データへの自律検索を組み込んだ。
- Data and results: 実対話による微調整と検索で患者理解・応答精度の改善を報告するが、要旨に評価例数、比較スコア、統計的な改善幅はない。
- Novelty: 公開基盤モデルの専門対話調整に、更新可能な外部知識の参照を加えた初期の医療LLM例。
- Limitations: 編者の注意: 原著の改善という結論を、臨床試験による助言の安全性証明へ拡張しない。収集対話の質、検索情報の信頼性、匿名化の残余リスクは別々の課題である。

### Paper: De novo design of protein structure and function with RFdiffusion
- Source: PubMed
- Canonical ID: pmid:37433327
- Publication date: 2023-07-11
- URL: https://pubmed.ncbi.nlm.nih.gov/37433327/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: RFdiffusionは構造のノイズ除去を学び、指定条件からタンパク質骨格を生成・実験検証した。
- Objective: 結合体、対称構造、活性部位の足場など、多様なタンパク質設計を共通の方法で扱う。
- Methods: RoseTTAFoldを構造のノイズ除去課題で微調整。無条件・トポロジー制約・結合・対称性・機能モチーフの設計を行い、数百の設計物の構造と機能を評価した。
- Data and results: 対称集合体、金属結合タンパク質、標的結合体の実験検証を報告。インフルエンザHAと結合体の複合体cryo-EM構造は設計モデルに極めて近かった。
- Novelty: 既存配列の構造予測器を、条件を満たす新規骨格を作る拡散生成器へ転用した。
- Limitations: 編者の注意: 検証成功した設計の存在は全生成物の成功率や任意標的の解決を保証しない。機能の確認と治療薬としての安全性・薬効の検証は別段階である。

### Paper: A foundation model for generalizable disease detection from retinal images
- Source: PubMed
- Canonical ID: pmid:37704728
- Publication date: 2023-09-13
- URL: https://pubmed.ncbi.nlm.nih.gov/37704728/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: RETFoundは大量の未ラベル網膜画像から学び、眼疾患と全身疾患の予測へ適応する基盤モデル。
- Objective: 課題ごとの専門家ラベル付けを減らし、複数の臨床応用へ転用できる網膜画像表現を得る。
- Methods: 160万枚の未ラベル画像で自己教師あり学習し、その後ラベル付き課題へ適応。眼疾患の診断・予後と、心不全・心筋梗塞などの新規発症予測を比較した。
- Data and results: 少ないラベルで複数の比較モデルを一貫して上回ったと報告。要旨には課題別の絶対性能、ラベル削減量や外部検証の具体数はない。
- Novelty: 網膜画像の単一タスク学習を、多数の眼・全身状態へ展開する自己教師あり事前学習へ拡張した。
- Limitations: 編者の注意: 網膜からの全身疾患予測は疾患の確定診断や因果的機序の証明ではない。対象集団や撮影条件が変わる場合の校正・転帰への利益も必要。

### Paper: Developing prompts from large language model for extracting clinical information from pathology and ultrasound reports in breast cancer
- Source: PubMed
- Canonical ID: pmid:37793630
- Publication date: 2023-09-21
- URL: https://pubmed.ncbi.nlm.nih.gov/37793630/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 乳癌の病理・超音波報告からLLMで項目を抽出し、精度と準備作業の費用を評価した。
- Objective: 臨床研究用データの手作業収集を、プロンプトによる抽出・形式統一で効率化できるか調べる。
- Methods: 2020–2022年に放射線治療を受けた2,931人の報告で、抽出12・形式統一12プロンプトを開発。無作為340人を完全手作業の情報と比較した。
- Data and results: 全体accuracy87.7%、脈管侵襲98.2%。プロンプト開発3.5時間、処理15分、API65.8米ドル、推定人件費込み95.4米ドル。時間・費用の比較の一部は推計だった。
- Novelty: モデルの点数だけでなく、研究者が抽出器を準備・実行する費用を含めて評価した。
- Limitations: 編者の注意: 単一研究条件の費用を現在価格や別文書へ一般化しない。全体精度と項目別精度は異なり、誤抽出の人手確認を省けるという証拠ではない。

### Paper: A study of generative large language model for medical research and healthcare
- Source: PubMed
- Canonical ID: pmid:37973919
- Publication date: 2023-11-16
- URL: https://pubmed.ncbi.nlm.nih.gov/37973919/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: GatorTronGPTは大規模臨床文書を含めて学習し、医学NLPと合成文章の有用性を調べた。
- Objective: 一般用途LLMに依存する評価から、臨床文書で学習した生成モデルの能力を検討する。
- Methods: 約200万人・126部門由来の臨床820億語と一般英語1,950億語を使い、最大200億パラメータのGPT-3型を学習。200億語の合成文をNLP学習にも使用した。
- Data and results: 合成文で学習したNLPモデルが実臨床文で学習した比較モデルを上回った。医師評価では可読性6.57対6.93、臨床関連性7.00対6.97で有意差なし（9段階）。
- Novelty: 臨床生成モデルを文章生成だけでなく、下流NLP用の合成コーパス供給源として検証した。
- Limitations: 編者の注意: 非有意差は同等性の証明ではなく、人らしい文章も医学的正確性や患者安全性を保証しない。合成文についても個人情報の漏洩評価が別途必要。

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

### Paper: An Empirical Evaluation of Prompting Strategies for Large Language Models in Zero-Shot Clinical Natural Language Processing: Algorithm Development and Validation Study
- Source: PubMed
- Canonical ID: pmid:38587879
- Publication date: 2024-04-08
- URL: https://pubmed.ncbi.nlm.nih.gov/38587879/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 臨床NLPの5課題でプロンプト形式を比較し、課題に合わせた指示の重要性を検証した。
- Objective: 専用の学習例が少ない条件で、どの指示方法が臨床情報抽出を改善するか調べる。
- Methods: 単純指示、穴埋め、CoT、anticipatory、heuristic、ensembleをGPT-3.5・Gemini・LLaMA-2で比較。語義曖昧性、医学根拠、共参照、薬剤状態・属性の課題でzero/few-shotを評価した。
- Data and results: GPT-3.5のheuristic指示で語義判別accuracy0.96、医学根拠抽出0.94。few-shotは複雑な課題を改善し、実験ではGPT-3.5が他の2モデルを上回った。
- Novelty: モデルの比較だけでなく、医学課題ごとの指示設計と複数指示の統合を体系的に比較した。
- Limitations: 編者の注意: 特定バージョン・課題・指示の組合せに関する結果で、以後のモデルの順位を示さない。zero-shotはプロンプト開発の調整まで不要という意味ではない。

### Paper: Use of a Large Language Model to Assess Clinical Acuity of Adults in the Emergency Department
- Source: PubMed
- Canonical ID: pmid:38713466
- Publication date: 2024-05-07
- URL: https://pubmed.ncbi.nlm.nih.gov/38713466/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 救急記録の2症例を比較して重症な方を選ぶ課題で、GPT-4の判定を評価した。
- Objective: 来院時の臨床記述から、必要とする医療の緊急度を相対的に識別できるか調べる。
- Methods: 単施設の成人救急受診から、異なるESI重症度を持つ10,000組を各組合せで均等抽出。匿名化文章を提示し、500組では医師レビューとも比較した横断研究。
- Data and results: GPT-4は8,940/10,000組で重症な患者を正しく選択し、accuracy0.89。旧モデル0.84。500組ではLLM0.88、医師0.86だった。
- Novelty: 試験問題から実際の救急記述へ評価を移し、相対的重症度という推論能力を測定した。
- Limitations: 編者の注意: ESIの異なる2人を均等に組み合わせる課題であり、1人の絶対的なトリアージ区分や現場の患者分布での成績ではない。実運用の安全性には追加検証が必要。
- Publication date note: PMC掲載原著のPublished May 7, 2024を採用。PubMedの月初表記2024-05-01と区別。出典: https://pmc.ncbi.nlm.nih.gov/articles/PMC11077390/

### Paper: A foundation model for clinical-grade computational pathology and rare cancers detection
- Source: PubMed
- Canonical ID: pmid:39039250
- Publication date: 2024-07-22
- URL: https://pubmed.ncbi.nlm.nih.gov/39039250/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: Virchowは病理基盤表現を使い、一般的な癌と希少癌の横断的検出を検討した。
- Objective: 多様な病理画像のパターンを学び、少ないラベルでも希少癌などの課題へ適応する。
- Methods: 病理基盤モデルの表現で汎癌検出器を作り、バイオマーカー予測と細胞同定も評価。稼働中の組織別モデルと学習データ量を変えて比較した。
- Data and results: 一般的な9癌種と希少7癌種を合わせた検体単位AUCは0.95。より少ない学習データで組織別モデルと同程度、一部の希少変種で高い性能を報告した。
- Novelty: 大規模病理表現の価値を、希少癌の少数ラベル適応と汎癌検出で示した。
- Limitations: 編者の注意: 要旨に事前学習の規模・施設別成績はなく補わない。全体AUC0.95をすべての癌種の精度と読み替えず、稼働モデルとの比較を本モデルの導入実証と混同しない。

### Paper: A pathology foundation model for cancer diagnosis and prognosis prediction
- Source: PubMed
- Canonical ID: pmid:39232164
- Publication date: 2024-09-04
- URL: https://pubmed.ncbi.nlm.nih.gov/39232164/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: CHIEFはパッチと全スライドの事前学習を組み合わせ、多施設の癌病理課題へ転用した。
- Objective: 課題・集団・標本作成条件ごとに専用モデルを作る負担と、分布変化での性能低下を減らす。
- Methods: 19解剖部位60,530全スライド、44TBの画像で、タイルの教師なし学習と全体の弱教師あり学習を併用。24病院・コホートの32独立セット19,491画像で検証した。
- Data and results: 癌細胞検出、原発推定、分子情報、予後の課題で転用を示し、比較法への改善は最大36.1%と報告。要旨に全課題の絶対値はない。
- Novelty: 局所形態と全体パターンの相補的な事前学習を、大規模な国際外部検証と結び付けた。
- Limitations: 編者の注意: 最大改善を全課題の平均や絶対ポイントと解釈しない。外部画像の予測評価は、診療での利益や未経験施設すべてでの性能保証とは異なる。

### Paper: Large Language Model Influence on Diagnostic Reasoning: A Randomized Clinical Trial
- Source: PubMed
- Canonical ID: pmid:39466245
- Publication date: 2024-10-28
- URL: https://pubmed.ncbi.nlm.nih.gov/39466245/
- read_level: full_text
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 診断推論の模擬症例試験で、GPT-4を利用できても医師の成績は有意に改善しなかった。
- Objective: LLM単独の試験成績が、医師の診断支援として実際に改善へつながるか検証する。
- Methods: 医師50人を通常資料のみとChatGPT Plus（GPT-4）併用へ無作為化。60分で最大6症例を解き、盲検専門家が鑑別・根拠・次の検査を採点した。
- Data and results: 推論スコア中央値76%対74%、調整差2ポイント（95%CI −4–8、p=0.60）。時間短縮も非有意。探索的なLLM単独の比較では通常資料群より16ポイント高かった。
- Novelty: LLMの単独解答と、人が自由に利用する支援場面を分けて無作為評価した。
- Limitations: 著者は単一LLM、6症例、プロンプト技法の明示的訓練なし、使用法を統一しない設計を限界とする。実患者の治療転帰や、あらゆる協働方法の無効性を示す試験ではない。
- Publication date note: 出版社とPMCのPublished October 28, 2024を採用。PubMedの月初表記2024-10-01とは不一致のため出版社を優先。出典: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395

本文の照合箇所: [Methodsのモデル・症例・評価、DiscussionのLimitations、刊行日](https://pmc.ncbi.nlm.nih.gov/articles/PMC11519755/)。

### Paper: External validation is necessary in prediction research: a clinical example
- Source: PubMed
- Canonical ID: pmid:14505766
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/14505766/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 小児感染症の予測器で、bootstrap補正後も外部性能を過大評価し得る例を示した。
- Objective: 内部検証だけで将来患者への一般化を判断することの限界を実例で示す。
- Methods: 原因不明の発熱小児376人で重い細菌感染の9因子モデルを作り、bootstrap内部検証。その後、別の179人で外部検証した。
- Data and results: AUCは開発データで0.83、bootstrap補正で0.76、外部では0.57。外部AUCの95%CIは0.47–0.67だった。
- Novelty: 内部の楽観性補正と、新しい状況への移植性の検証が同じではないと臨床例で示した。
- Limitations: 著者は比較的小さなデータでの例とする。編者の注意: 1モデルの事例であり、bootstrapが常に無用という結論ではなく、外部の分布変化は別に確認すべき問題である。
- Publication date note: 判明した巻号年月: 2003 Sep。PubMedは刊行年月のみ。今回の出版社資料の照合でも日単位の公開日を確認できなかった。便宜的な月初日や索引登録日は採用しない。出典: https://pubmed.ncbi.nlm.nih.gov/14505766/ ; https://doi.org/10.1016/s0895-4356(03)00207-5

### Paper: The interaction of domain knowledge and linguistic structure in natural language processing: interpreting hypernymic propositions in biomedical text
- Source: PubMed
- Canonical ID: pmid:14759819
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/14759819/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: UMLSの階層知識と浅い構文解析を使い、医学文章の上位・下位概念関係を解釈した。
- Objective: 自由記載で『特定概念は一般概念の一種』と述べる命題を機械で扱う。
- Methods: 不完全指定の構文解析に、Semantic Networkの意味グループによる整合確認とMetathesaurusの階層による方向判定を組み合わせた。
- Data and results: Chemicals and Drugs意味グループに基づく予備評価で適合率83%。要旨に標本数や再現率はなく、誤り分析と改善案を報告する。
- Novelty: 言語的な構造だけでも辞書照合だけでもなく、医学概念の互換性と階層を統合して意味命題を解釈した。
- Limitations: 編者の注意: 化学物質・薬剤の予備評価であり、臨床全域の関係抽出性能ではない。適合率のみから抽出漏れを判断できず、情報検索などの応用は提案段階。
- Publication date note: 判明した巻号年月: 2003 Dec。PubMedは刊行年月のみ。今回の出版社資料の照合でも日単位の公開日を確認できなかった。便宜的な月初日や索引登録日は採用しない。出典: https://pubmed.ncbi.nlm.nih.gov/14759819/ ; https://doi.org/10.1016/j.jbi.2003.11.003

### Paper: Substantial effective sample sizes were required for external validation studies of predictive logistic regression models
- Source: PubMed
- Canonical ID: pmid:15845334
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/15845334/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: 外部検証で性能悪化を検出するには、総人数より十分なイベント数が必要と示した。
- Objective: どの程度の検証標本なら、予測の過大評価や識別力の低下を検出できるか算定する。
- Methods: 転移性精巣癌治療後の残存病変を予測する回帰を例に、検出力80%、有意水準5%の計算とMonte Carloシミュレーションを行った。
- Data and results: 予測oddsが平均1.5倍過大な場合の検出に111イベント、C統計量0.83→0.73の低下には81–106イベントを要した。最低100イベント・100非イベントを目安とした。
- Novelty: 外部検証の標本数を、検出したいモデルの不適合とイベント数から考える枠組みを示した。
- Limitations: 著者も仮説次第でさらに大きな標本が必要とする。編者の注意: 100/100は当時の具体的な設定の目安で、すべての校正・部分集団評価に十分な万能基準ではない。
- Publication date note: 判明した巻号年月: 2005 May。PubMedは刊行年月のみ。今回の出版社資料の照合でも日単位の公開日を確認できなかった。便宜的な月初日や索引登録日は採用しない。出典: https://pubmed.ncbi.nlm.nih.gov/15845334/ ; https://doi.org/10.1016/j.jclinepi.2004.06.017

### Paper: Spatio-spectral filters for improving the classification of single trial EEG
- Source: PubMed
- Canonical ID: pmid:16189967
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/16189967/
- read_level: abstract
- Tags: 基礎文献, 医療・生体信号・創薬AI
- Summary: CSPへ時間遅延埋め込みを加え、電極ごとの周波数特性も学ぶEEG分類を提案した。
- Objective: 雑音・非定常性・アーチファクトで低下するBCIの単試行分類を改善する。
- Methods: common spatial patternを状態空間へ拡張し、time delay embeddingで空間・周波数フィルタを個別調整。想像運動のEEGで元のCSPと比較した。
- Data and results: 試行あたりのbitsで測る情報伝達率が改善し、より頑健な分類を報告。要旨に被験者数、分類精度、改善量はない。
- Novelty: 空間フィルタだけでなく、時間遅延を介して周波数選択もデータから調整する方向を示した。
- Limitations: 編者の注意: 想像運動の特定EEG実験での検証であり、全BCI課題の性能を示さない。個別調整の必要量と新規被験者への汎化は別途確認が必要。
- Publication date note: 判明した巻号年月: 2005 Sep。PubMedは刊行年月のみ。今回の出版社資料の照合でも日単位の公開日を確認できなかった。便宜的な月初日や索引登録日は採用しない。出典: https://pubmed.ncbi.nlm.nih.gov/16189967/ ; https://doi.org/10.1109/tbme.2005.851521

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
- Publication date note: 判明した巻号年月: 2019 Apr。PubMedは刊行年月のみ。今回の出版社資料の照合でも日単位の公開日を確認できなかった。出版社本文の取得はアクセス制限で不可。便宜的な月初日や索引登録日は採用しない。出典: https://pubmed.ncbi.nlm.nih.gov/29489489/ ; https://doi.org/10.1097/sla.0000000000002706

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
- Publication date note: 判明した巻号年月: 2018 Nov。PubMedは刊行年月のみ。今回の出版社資料の照合でも日単位の公開日を確認できなかった。便宜的な月初日や索引登録日は採用しない。出典: https://pubmed.ncbi.nlm.nih.gov/30385537/ ; https://doi.org/10.4037/ajcc2018525

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
- Publication date note: 判明した巻号年月: 2017 Aug。PubMedは刊行年月のみ。今回の出版社資料の照合でも日単位の公開日を確認できなかった。ACMページは取得制限があり、会期を公開日へ流用しない。便宜的な月初日や索引登録日は採用しない。出典: https://pubmed.ncbi.nlm.nih.gov/33717639/ ; https://doi.org/10.1145/3097983.3098126

<!-- PAPER_IDS -->
pmid:7702231
pmid:12091676
pmid:15187068
pmid:15188874
pmid:15845847
pmid:16359928
pmid:18031824
pmid:20713314
pmid:21810266
pmid:21862746
pmid:22400967
pmid:22397946
pmid:22934236
pmid:23496923
pmid:23567779
pmid:23842533
pmid:25179855
pmid:25441703
pmid:25560730
pmid:25569120
pmid:25925131
arxiv:1505.04597
pmid:26187250
pmid:26392543
arxiv:1512.03385
pmid:26863654
pmid:26679719
pmid:26955021
pmid:27185194
pmid:27212078
arxiv:1606.04797
arxiv:1606.06650
pmid:27521897
pmid:27558503
arxiv:1608.06993
pmid:27701631
pmid:27898976
pmid:27900952
pmid:28056090
pmid:28096249
pmid:28117445
pmid:27784047
pmid:28287963
pmid:28678710
pmid:28782865
pmid:28419261
pmid:28974302
pmid:29629118
pmid:29036616
pmid:29224926
pmid:29234806
pmid:29500022
pmid:29382633
pmid:29084046
pmid:29186491
pmid:29862307
pmid:29709069
pmid:29801159
pmid:31304302
pmid:29743531
pmid:29807250
pmid:29994302
pmid:30104768
pmid:30217670
pmid:30245122
pmid:30224757
pmid:30348771
pmid:30285102
pmid:30457988
pmid:30481176
pmid:30596875
pmid:30596876
pmid:30617320
arxiv:1901.07031
pmid:30814121
pmid:30834436
pmid:30843824
pmid:30942845
pmid:31209213
pmid:31367026
pmid:31378392
pmid:31536901
pmid:31636460
pmid:31649194
pmid:31694707
pmid:31584655
pmid:31896580
pmid:31926806
pmid:31932807
pmid:31942072
pmid:32051412
pmid:32064914
pmid:32084340
pmid:33328078
pmid:32346050
pmid:32371116
pmid:32393799
pmid:33763651
pmid:32908283
pmid:32908284
pmid:33564405
pmid:33288961
pmid:33588584
pmid:34127232
pmid:32903191
pmid:34412834
pmid:34017034
pmid:34031906
pmid:34152373
pmid:34265844
pmid:34293799
pmid:34743566
pmid:34980915
pmid:35013344
pmid:35020807
pmid:35589549
pmid:35585198
pmid:36108050
pmid:36702895
pmid:36927031
pmid:37123444
pmid:37492832
pmid:37433327
pmid:37704728
pmid:37793630
pmid:37973919
pmid:38207039
pmid:38587879
pmid:38713466
pmid:39039250
pmid:39232164
pmid:39466245
pmid:14505766
pmid:14759819
pmid:15845334
pmid:16189967
pmid:29489489
pmid:30385537
pmid:33717639
<!-- /PAPER_IDS -->
