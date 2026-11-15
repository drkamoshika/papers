# 基礎文献 — 神経科学とAI

> schema_version: 1
> report_date: 2026-11-15

## ダイジェスト

選定106件中、一次資料へ照合した50件を掲載する。要旨確認と本文の関連箇所確認を区別し、要旨にない数値は補わない。「編者の注意」は著者の自己申告した限界と区別する。

研究の流れ・読み順・比較軸は[総覧](README.md)を参照。

## 完全版レポート

### Paper: Functional connectivity in the resting brain: a network analysis of the default mode hypothesis
- Source: PubMed
- Canonical ID: pmid:12506194
- Publication date: 2002-12-27
- URL: https://pubmed.ncbi.nlm.nih.gov/12506194/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 安静時の相関からdefault mode networkのまとまりを検証する。
- Objective: 安静・視覚処理・認知課題で、default系がどう変わるかを調べる。
- Methods: 作業記憶で活動が下がるPCC・vACCをseedとし、安静と視覚課題の結合、前頭領域との相関を分析する。
- Data and results: PCCとdefault系の強い結合、安静と視覚課題で似た地図、外側前頭領域との逆相関を報告。
- Novelty: default系を単なる活動減少の領域群でなく、結合したnetworkとして検証する。
- Limitations: 編者の注意: 相関・逆相関は情報の向きや直接抑制を証明せず、処理手順の影響も考慮する必要がある。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/12506194/

### Paper: Resting-state functional connectivity reflects structural connectivity in the default mode network
- Source: PubMed
- Canonical ID: pmid:18403396
- Publication date: 2008-04-09
- URL: https://pubmed.ncbi.nlm.nih.gov/18403396/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: default modeの機能結合を、拡散画像の構造経路と対応付ける。
- Objective: 安静時のBOLD相関が、単なる非神経artifactでないかを調べる。
- Methods: 安静時fMRIをseedにDTI tractographyを行い、内側前頭・側頭・後部帯状/脳梁膨大後領域の経路を探す。
- Data and results: MTL–retrosplenial cortexとMPFC–PCCの構造的な経路を報告し、二つのmodalitiesの対応を示す。
- Novelty: 機能的なdefault系へ、非侵襲の構造情報を併せて検証する。
- Limitations: 編者の注意: 対応する経路があることは、すべての機能相関が直接接続に由来する証明ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/18403396/

### Paper: Predicting human resting-state functional connectivity from structural connectivity
- Source: PubMed
- Canonical ID: pmid:19188601
- Publication date: 2009-02-02
- URL: https://pubmed.ncbi.nlm.nih.gov/19188601/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 人間の構造的配線から、安静時機能結合の特徴を力学モデルで予測する。
- Objective: 変動する機能networkが解剖構造にどれだけ拘束されるかを調べる。
- Methods: 同じ人のfMRIと拡散tractographyを測り、構造結合を巨視的な皮質動態モデルの結合に使う。
- Data and results: 直接構造結合のない領域にも強い機能結合があり、間接経路と距離が一部を説明。走査・モデル間の変動も認める。
- Novelty: 構造・機能・計算モデルを同じ対象で対応付ける。
- Limitations: 機能結合から直接配線を逆推定することは難しいと著者が指摘。間接経路と時間変動を無視できない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/19188601/

### Paper: Cortical hubs revealed by intrinsic functional connectivity: mapping, assessment of stability, and relation to Alzheimer's disease
- Source: PubMed
- Canonical ID: pmid:19211893
- Publication date: 2009-02-11
- URL: https://pubmed.ncbi.nlm.nih.gov/19211893/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 機能結合のhubを人間の皮質で同定し、状態間の安定性を調べる。
- Objective: network統合の中心と、病理の分布との関係を検討する。
- Methods: 独立fMRI2群各24人、別群12人で検証し、127人の合意hub地図をamyloid PETと比較する。
- Data and results: 連合皮質にhubを見いだし、課題間で位置が安定。AD10人・対照29人の比較ではhub位置に高いamyloidを認める。
- Novelty: hubの位置・再現性・病理との対応を複数datasetで結ぶ。
- Limitations: 編者の注意: hubと病理の空間的対応は、hub活動が疾患を起こすという因果実証ではない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/19211893/

### Paper: Gaussian-process factor analysis for low-dimensional single-trial analysis of neural population activity
- Source: PubMed
- Canonical ID: pmid:19357332
- Publication date: 2009-04-08
- URL: https://pubmed.ncbi.nlm.nih.gov/19357332/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: GPFAは時間平滑化と次元削減を一つの確率モデルで行う。
- Objective: 単一trialの多neuron発火から、滑らかな潜在軌跡を推定する。
- Methods: Gaussian processとfactor analysisを統合し、他neuronからの発火予測で二段階手法と比較する。
- Data and results: macaque運動前野・運動皮質の61neuronで予測を改善。既知のsimulationでは最良の二段階法より数十%良い結果を報告。
- Novelty: 時間の滑らかさと発火の変動を、低次元推定の内部で同時に扱う。
- Limitations: 編者の注意: simulationの改善率を生体データでの真の潜在状態復元率としない。平滑性や潜在次元にも仮定がある。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/19357332/

### Paper: Modular and hierarchically modular organization of brain networks
- Source: PubMed
- Canonical ID: pmid:21151783
- Publication date: 2010-12-08
- URL: https://pubmed.ncbi.nlm.nih.gov/21151783/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: moduleの中にさらにmoduleを持つ、脳networkの階層構造を整理する。
- Objective: 専門化・統合・頑健性を支える複数scaleの組織を理解する。
- Methods: 階層modularityの数学と、人間の構造・機能画像から得られた研究をreviewする。
- Data and results: module内の高密度結合、比較的長距離のmodule間結合、頑健性・適応性などの含意を論じる。
- Novelty: 単一scaleの分割を超えた、階層的なnetwork構造の見取り図。
- Limitations: レビューであり頑健性の一般的な因果実証ではない。編者の注意: 階層の検出は解像度・比較基準に左右される。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/21151783/

### Paper: The human connectome: a complex network
- Source: PubMed
- Canonical ID: pmid:21251014
- Publication date: 2011-01-04
- URL: https://pubmed.ncbi.nlm.nih.gov/21251014/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: human connectomeを複雑networkとして捉え、構造が機能動態を拘束する関係を整理する。
- Objective: 大規模な配線地図から、統合と専門化の組織原理を理解する。
- Methods: 非侵襲画像による構造network研究をreviewし、cluster・module・経路長・効率を検討する。
- Data and results: 高いcluster・modularityと短い経路などの非ランダム構造を整理し、構造と機能の関係は複雑で非線形と述べる。
- Novelty: connectomeの地図をgraph理論と機能的な解釈へつなぐ。
- Limitations: レビューのため独自の全脳再構築や介入実験ではない。構造・機能に共通の指標があっても両者は同一ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/21251014/

### Paper: The organization of the human cerebral cortex estimated by intrinsic functional connectivity
- Source: PubMed
- Canonical ID: pmid:21653723
- Publication date: 2011-06-08
- URL: https://pubmed.ncbi.nlm.nih.gov/21653723/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 安静時の機能結合から、人間の皮質を大規模networkへ区分する。
- Objective: 感覚運動の局所系と、連合皮質の分散系の構成を明らかにする。
- Methods: 1,000人のsurface位置合わせ済みfMRIをcluster化し、networkの再現性と境界を調べる。
- Data and results: 感覚運動では地形的な隣接構造、連合皮質では急な境界と並列に入り組む分散networkを報告。
- Novelty: 大標本の機能結合による、皮質networkの共通の区分を提供する。
- Limitations: 編者の注意: 機能的な相関からの区分は、細胞・シナプス単位の解剖学的配線ではなく、個体差も残る。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/21653723/

### Paper: The influence of head motion on intrinsic functional connectivity MRI
- Source: PubMed
- Canonical ID: pmid:21810475
- Publication date: 2011-07-23
- URL: https://pubmed.ncbi.nlm.nih.gov/21810475/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 頭の動きが、人間の安静時機能結合へ系統的な偏りを生むことを調べる。
- Objective: 年齢群・患者群・個体差の比較で、動きを神経の差と誤認しないようにする。
- Methods: 健康若年者1,000人の安静時2走査で、変位・微小運動・回転と複数network指標を対応付ける。
- Data and results: 動きでdefault・前頭頭頂の遠距離結合が下がり、局所結合などが上がる。小さい群間の動き差でも神経差に似た地図が生じる。
- Novelty: 機能networkの個体差・集団差の解釈に、motionの具体的な影響を示す。
- Limitations: 変動の大部分がmotionによるとは報告していない。編者の注意: 相関のすべてをartifactとするのも不適切。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/21810475/

### Paper: Rich-club organization of the human connectome
- Source: PubMed
- Canonical ID: pmid:22049421
- Publication date: 2011-11-02
- URL: https://pubmed.ncbi.nlm.nih.gov/22049421/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 人間の脳hub同士が、密につながるrich clubを形成するか検証する。
- Objective: 高い次数の中心領域の間に、次数だけでは説明できない接続があるかを調べる。
- Methods: 21人の拡散tensor画像から全脳構造networkを作り、hub間の密度を次数に基づく期待と比較する。
- Data and results: 両半球の12hub領域で強い相互結合を見いだし、次数だけからの予想以上に密なrich clubを報告。
- Novelty: hubの存在だけでなく、hub間を結ぶ高次のcore構造を示す。
- Limitations: 編者の注意: MRI由来の巨視的networkであり、hub間の密結合が情報統合を生むという機能的因果は別途検証する。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/22049421/

### Paper: Neural dynamics as sampling: a model for stochastic computation in recurrent networks of spiking neurons
- Source: PubMed
- Canonical ID: pmid:22096452
- Publication date: 2011-11-03
- URL: https://pubmed.ncbi.nlm.nih.gov/22096452/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: spiking網の確率的発火を、ある条件下でMCMC samplingとして実装する。
- Objective: 抽象的な確率推論と、具体的なspike動態を結び付ける。
- Methods: 通常のGibbsとは異なる非可逆Markov chainを構成し、離散・連続時間の理論解析を行う。
- Data and results: 提案網の活動が与えられた分布をsamplingすることを、条件付きで厳密に示す。
- Novelty: 発火の時間構造に合う確率推論の実装を導く。
- Limitations: 条件を満たす提案モデルの結果。編者の注意: 脳の試行間変動すべてがBayes samplingであるという観測的証明ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/22096452/

### Paper: Neural population dynamics during reaching
- Source: PubMed
- Canonical ID: pmid:22722855
- Publication date: 2012-07-05
- URL: https://pubmed.ncbi.nlm.nih.gov/22722855/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: reaching中の運動皮質の集団活動に、短いが強い振動構造を見いだす。
- Objective: 個々のneuronが何の運動量を表すかという見方から、集団の力学を調べる。
- Methods: 到達運動時のpopulation応答を解析し、準備状態と振動の振幅・位相の関係を見る。
- Data and results: 非周期的な到達行動でも振動があり、準備状態からその位相・振幅が自然に決まると報告。
- Novelty: 複雑な単一neuron応答を、比較的単純な集団力学から解釈する。
- Limitations: 編者の注意: 集団軌跡の構造は重要だが、単一の力学モデルがすべての運動皮質機能を説明する実証ではない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/22722855/

### Paper: A visual motion detection circuit suggested by Drosophila connectomics
- Source: PubMed
- Canonical ID: pmid:23925240
- Publication date: 2013-08-08
- URL: https://pubmed.ncbi.nlm.nih.gov/23925240/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: ハエ視覚系の局所connectomeから、動きの方向検出の候補回路を導く。
- Objective: 長く不明だった局所運動計算の細胞・結合構造を特定する。
- Methods: 半自動EM再構築と光学像の細胞型matchingを使い、medullaの反復moduleを調べる。
- Data and results: 379 neuronと8,637化学シナプスを復元。方向選択性と整合する運動感受性neuronへの結合を見いだす。
- Novelty: 細胞型を伴う局所の密な配線図から、具体的な計算回路を提案する。
- Limitations: 著者は将来の機能実験の標的として位置付ける。編者の注意: 接続との整合性は、回路の機能を直接操作で確定したこととは異なる。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/23925240/

### Paper: Performance-optimized hierarchical models predict neural responses in higher visual cortex
- Source: PubMed
- Canonical ID: pmid:24812127
- Publication date: 2014-05-08
- URL: https://pubmed.ncbi.nlm.nih.gov/24812127/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 視覚課題で最適化した階層網が、高次視覚皮質の応答を予測する。
- Objective: 課題性能の最適化が、生体の神経処理モデルを作る原理になるか調べる。
- Methods: 生物的に適した階層モデル群で物体認識性能とIT応答予測を比べ、高性能網を神経記録と対応付ける。
- Data and results: 神経データへ直接適合させなくても最上層がIT、途中層がV4応答をよく予測し、課題性能との強い関係を報告。
- Novelty: 目的を解くための最適化と、脳応答を説明する表現の出現をつなぐ。
- Limitations: 編者の注意: 応答予測の一致は、脳が同じarchitectureや学習ruleを使う証明ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/24812127/

### Paper: Neural dynamics for landmark orientation and angular path integration
- Source: PubMed
- Canonical ID: pmid:25971509
- Publication date: 2015-05-14
- URL: https://pubmed.ncbi.nlm.nih.gov/25971509/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: ハエの方向表象が、視覚landmarkと自己運動を統合することを示す。
- Objective: 方向を保つnavigation回路の動態を、行動と同時に調べる。
- Methods: 頭部固定で球上を歩くハエにVRを提示し、ellipsoid bodyの二光子calcium画像を測る。
- Data and results: 明所ではlandmark、暗所では自己運動を追い、両手掛かりがなくても方向表象を保持。ring attractorを示唆する。
- Novelty: 環状の解剖と持続活動を、方向積分の計算へ結ぶ。
- Limitations: ring attractorは観察に整合する示唆。編者の注意: 頭部固定・VRの結果を、自然下の全navigation能力へ直接拡張しない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/25971509/

### Paper: Modular Brain Networks
- Source: PubMed
- Canonical ID: pmid:26393868
- Publication date: 2015-09-21
- URL: https://pubmed.ncbi.nlm.nih.gov/26393868/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 脳networkのcommunity検出法と、moduleの構造・機能的意味を整理する。
- Objective: 密な部分networkを、専門的な機能の構成要素として理解する。
- Methods: community検出の複数方式の長短をreviewし、構造・機能地図での主要な観察をまとめる。
- Data and results: 進化、配線量、専門化、複雑な動態におけるmoduleの役割を検討する。新予測器の精度比較ではない。
- Novelty: moduleの存在と検出法の選択を、network neuroscienceの中心問題として整理する。
- Limitations: 検出法ごとに長短がある。編者の注意: 分割のscale・最適化・null modelによって得られるmoduleが変わる。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/26393868/

### Paper: Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity
- Source: PubMed
- Canonical ID: pmid:26457551
- Publication date: 2015-10-12
- URL: https://pubmed.ncbi.nlm.nih.gov/26457551/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 機能結合のpatternが、個人を識別するfingerprintとなることを示す。
- Objective: 集団平均に隠れる脳networkの個体差の信頼性と行動との関係を検証する。
- Methods: Human Connectome Projectで走査session・安静/課題をまたぐ本人識別と流動性知能の予測を行う。
- Data and results: 条件をまたいだ識別が可能で、前頭頭頂networkが特に識別的かつ認知行動予測に関連した。
- Novelty: 機能networkを個人ごとの予測・同定の資源として使う。
- Limitations: 編者の注意: 本人識別が可能でも、知能の個人予測が高精度・因果的に説明可能であることを意味しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/26457551/

### Paper: Demixed principal component analysis of neural population data
- Source: PubMed
- Canonical ID: pmid:27067378
- Publication date: 2016-04-12
- URL: https://pubmed.ncbi.nlm.nih.gov/27067378/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: dPCAは混合した集団活動を、課題変数に対応する少数の成分へ分ける。
- Objective: 単一neuronのmixed selectivityで見えにくい表象を可視化する。
- Methods: 分散を捉える次元削減に、刺激・判断・報酬などへの依存の分離を組み合わせる。
- Data and results: 種・脳領域・課題の異なる4データを再解析し、課題依存のpopulation応答を簡潔に示す。
- Novelty: 無監督の分散圧縮だけでなく、実験の因子に沿って低次元表現を分離する。
- Limitations: 編者の注意: demixingには課題ラベルを使うため、成分の分離を独立した生理的回路の発見と同一視しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/27067378/

### Paper: Small-World Brain Networks Revisited
- Source: PubMed
- Canonical ID: pmid:27655008
- Publication date: 2016-09-21
- URL: https://pubmed.ncbi.nlm.nih.gov/27655008/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: small-worldを、binary graphだけでなく重み付きの脳配線で再検討する。
- Objective: 高解像度tracingに合うtopologyの解釈へ更新する。
- Methods: 基礎理論と過去10年の進展をreviewし、macaque・mouseの新しいtracing結果を検討する。
- Data and results: 強い辺・弱い辺を保持する重み付きnetworkの重要性を強調し、weighted small-worldnessの課題を示す。
- Novelty: つながる/つながらないだけの地図から、結合強度を含む組織の評価へ進む。
- Limitations: 編者の注意: binary化や重みの処理で結論が変わるため、small-world指標の値だけで種・測定法を横断比較しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/27655008/

### Paper: Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning
- Source: PubMed
- Canonical ID: pmid:27814352
- Publication date: 2016-11-04
- URL: https://pubmed.ncbi.nlm.nih.gov/27814352/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 運動皮質の回転動態を、表象tuningと力学系の両方から検証する。
- Objective: 回転patternだけで力学系を支持してよいかを確かめる。
- Methods: 遅延付き速度tuningのsimulation、共分散を保つ置換検定、RNN、生体活動を比較する。
- Data and results: 単純な表象モデルも回転を作るが条件構造への依存が異なる。生体・力学モデルはその依存を保ち、RNNは両性質を再現する。
- Novelty: 回転の見た目でなく、条件と共分散を保つ検定でモデルを区別する。
- Limitations: 著者は少数neuron・少数条件の解釈に注意を促す。表象と力学を完全な二者択一とせず、検定の構造を確認する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/27814352/

### Paper: Benchmarking of participant-level confound regression strategies for the control of motion artifact in studies of functional connectivity
- Source: PubMed
- Canonical ID: pmid:28302591
- Publication date: 2017-03-14
- URL: https://pubmed.ncbi.nlm.nih.gov/28302591/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: motion artifactを減らす14種類の回帰・除去法を比較する。
- Objective: 脳networkの結果を歪める動きを、目的に応じて処理できるようにする。
- Methods: 若年者393人でmotion残差、距離依存、network識別、自由度損失の4軸を評価する。
- Data and results: global signal回帰はmotionとの関係を減らすが距離依存を残す。censoringは両方を減らす一方、自由度を消費する。
- Novelty: 単一の残差指標でなく、処理のtrade-offを複数の軸で明示する。
- Limitations: 著者は目的別の方法選択を推奨。編者の注意: 一つの処理がすべての研究・集団で最適という結論ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/28302591/

### Paper: The complete connectome of a learning and memory centre in an insect brain
- Source: PubMed
- Canonical ID: pmid:28796202
- Publication date: 2017-08-09
- URL: https://pubmed.ncbi.nlm.nih.gov/28796202/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 幼虫ハエのキノコ体を完全再構築し、連合学習の回路を調べる。
- Objective: 刺激と正負の強化を結ぶ高次記憶回路の構造を明らかにする。
- Methods: シナプス地図でKenyon細胞の入力と再帰結合を解析し、刺激弁別の出力neuronモデルを比較する。
- Data and results: 大半の入力組合せはランダム、一部は定型的。modulatory neuronとの相互結合など、新しい標準回路を見いだす。
- Novelty: ランダムな混合表現と再帰的・modulatoryな回路を、完全地図上で同時に示す。
- Limitations: 幼虫の特定の記憶中枢が対象。編者の注意: モデルでの刺激弁別と、個体の学習行動の再現は区別する。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/28796202/

### Paper: Large-Scale Gradients in Human Cortical Organization
- Source: PubMed
- Canonical ID: pmid:29203085
- Publication date: 2017-12-01
- URL: https://pubmed.ncbi.nlm.nih.gov/29203085/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 感覚運動からtransmodal領域へ続く、皮質の主要gradientを整理する。
- Objective: 領域の並びと構造制約から、機能の連続的な範囲を理解する。
- Methods: 複数の皮質特徴に現れる優勢なgradientを解説し、内在的な座標系を提案する。
- Data and results: 感覚運動–transmodalという組織軸を、皮質機能の分布を読む座標として位置付ける。
- Novelty: 境界で分かれた領域だけでなく、連続軸による皮質の記述を強調する。
- Limitations: 解説・統合の論文で独自の汎用予測精度を示すものではない。gradientが単一の神経計算機構を意味するとは限らない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/29203085/

### Paper: Distinct contributions of functional and deep neural network features to representational similarity of scenes in human brain and behavior
- Source: PubMed
- Canonical ID: pmid:29513219
- Publication date: 2018-03-07
- URL: https://pubmed.ncbi.nlm.nih.gov/29513219/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: sceneの行動上の意味とDNN特徴が、脳・行動の類似性へどう寄与するかを分ける。
- Objective: 視覚と意味の相関による説明の混同を減らす。
- Methods: 刺激の事前選択で三つの特徴model間の相関を下げ、行動と脳応答の説明分散を分割する。
- Data and results: 行動には可能な行為と高次DNN特徴が独自に寄与。scene選択皮質では中・高次DNN特徴が独自に説明し、object labelは寄与しなかった。
- Novelty: 表現類似性の一致を、相関した複数の特徴へ分けて検証する。
- Limitations: scene選択皮質は行動に関連する情報の一部のみを表すと著者が指摘。使う特徴modelの範囲内の結論でもある。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/29513219/

### Paper: A Task-Optimized Neural Network Replicates Human Auditory Behavior, Predicts Brain Responses, and Reveals a Cortical Processing Hierarchy
- Source: PubMed
- Canonical ID: pmid:29681533
- Publication date: 2018-04-19
- URL: https://pubmed.ncbi.nlm.nih.gov/29681533/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 音声・音楽認識を解く網から、人間の聴覚行動と皮質応答を予測する。
- Objective: 自然音を扱う聴覚系の定量モデルを作る。
- Methods: 階層網を音声・音楽の課題で最適化し、行動の誤りとfMRI応答を比較する。
- Data and results: 高性能網は人並みの課題性能と似た誤りを示し、従来filterより皮質応答を予測。中間・後段層が一次・非一次領域へ対応した。
- Novelty: 課題駆動モデルから、聴覚処理の分岐と階層の候補を導く。
- Limitations: 編者の注意: 生体の配線を直接復元した網ではなく、選ぶ課題や刺激の範囲で階層対応の解釈が変わる。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/29681533/

### Paper: Unsupervised Discovery of Demixed, Low-Dimensional Neural Dynamics across Multiple Timescales through Tensor Component Analysis
- Source: PubMed
- Canonical ID: pmid:29887338
- Publication date: 2018-06-07
- URL: https://pubmed.ncbi.nlm.nih.gov/29887338/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: TCAはneuron・trial内時間・trial間変化を分け、学習に伴う集団動態を抽出する。
- Objective: millisecondsの活動と数日にわたる変化を同じ表現で捉える。
- Methods: 神経データのtensorをneuron因子、時間因子、trial因子の三つの低次元成分へ分解する。
- Data and results: 人工網、rodent前頭皮質のmaze、macaqueのBMI学習のデータで、速い動態と遅い学習変化を分析する。
- Novelty: 短時間の回路活動と長期学習を、連結した三因子で分離する。
- Limitations: 編者の注意: 分解成分は数学的に抽出した表現で、細胞assemblyや認知状態との対応は追加の解釈・検証を要する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/29887338/

### Paper: Inferring single-trial neural population dynamics using sequential auto-encoders
- Source: PubMed
- Canonical ID: pmid:30224673
- Publication date: 2018-09-17
- URL: https://pubmed.ncbi.nlm.nih.gov/30224673/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: LFADSは単一trialのspikeから、潜在的な神経力学を深層学習で推定する。
- Objective: 試行平均では失われる動態を、部分的で雑音のある記録から復元する。
- Methods: sequential autoencoderによるlatent factor analysis via dynamical systemsを用いる。
- Data and results: macaque・人間の運動皮質で行動予測、精密な発火率、選択と相関する摂動を推定し、月をまたぐ非重複sessionも統合する。
- Novelty: 単一trialの発火を、生成的な潜在力学モデルとして推定する。
- Limitations: 編者の注意: 推定状態はモデル依存であり、観測されなかったneuronや摂動の真の生理量を直接測ったものではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/30224673/

### Paper: Cortical population activity within a preserved neural manifold underlies multiple motor behaviors
- Source: PubMed
- Canonical ID: pmid:30315158
- Publication date: 2018-10-12
- URL: https://pubmed.ncbi.nlm.nih.gov/30315158/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 複数の運動課題で、運動皮質の共通するneural modeが保持されることを示す。
- Objective: 多様な筋活動を、一つの集団表現がどう柔軟に生成するかを調べる。
- Methods: 手首・reach-to-grasp課題間で、神経共分散の主要modeとその活動を比較する。
- Data and results: 筋・単一unitのpatternは異なってもmodeは大部分保持。共通の時間特徴と筋出力への写像に対応するmode群を報告。
- Novelty: 行動間で変わる単一細胞活動と、保たれる集団manifoldを分ける。
- Limitations: 編者の注意: 調べた技能課題での保存であり、未学習のすべての行動を同じ固定manifoldで表せる保証ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/30315158/

### Paper: A Neural Population Mechanism for Rapid Learning
- Source: PubMed
- Canonical ID: pmid:30344047
- Publication date: 2018-10-18
- URL: https://pubmed.ncbi.nlm.nih.gov/30344047/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 速い運動適応を、回路の接続変更ではなく集団の活動部分空間で説明する。
- Objective: 一度の誤りでも起こる急な行動変化の神経機構を探る。
- Methods: 到達運動の摂動適応中に数百neuronのPMd–M1関係をモデル化し、output-null/potent部分空間を分ける。
- Data and results: PMdのoutput-null準備活動は適応とともに変化し、M1へ送るoutput-potent写像は保持されると報告。
- Novelty: 固定的な下流写像のもとで準備状態を変え、速く出力を調整する機構を示す。
- Limitations: 編者の注意: 接続変化なしで説明できる候補を示すが、あらゆる学習で可塑性が不要という結論ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/30344047/

### Paper: Towards the neural population doctrine
- Source: PubMed
- Canonical ID: pmid:30877963
- Publication date: 2019-03-13
- URL: https://pubmed.ncbi.nlm.nih.gov/30877963/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 神経計算の単位としてpopulationを重視する研究の進展を整理する。
- Objective: 同時大規模記録が、単一neuronだけでは分からない何を明らかにしたかを示す。
- Methods: 相関変動、decoding、神経動態、人工neural networkの4領域をreviewする。
- Data and results: populationの共同解析による知見を統合し、集団が多くの領域の計算単位となる見方を提示する。
- Novelty: 装置のreviewより、それによって可能になった科学的理解に焦点を当てる。
- Limitations: 編者の注意: populationの重視は単一細胞の役割を否定するものではなく、全領域に同じ計算単位を仮定しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/30877963/

### Paper: Bayesian Computation through Cortical Latent Dynamics
- Source: PubMed
- Canonical ID: pmid:31320220
- Publication date: 2019-07-15
- URL: https://pubmed.ncbi.nlm.nih.gov/31320220/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 時間長を再現する課題で、事前分布が皮質の潜在表現を歪める仕組みを調べる。
- Objective: 再帰的なneuron集団がBayes統合をどう実装するかを探る。
- Methods: monkeyの時間間隔再現課題の前頭活動と、同じ課題を解くRNNを分析する。
- Data and results: 事前統計による表現の変形が感覚から運動への写像へ反映され、RNNでは低次元の曲がったmanifoldが支えていた。
- Novelty: Bayes的行動と、潜在力学の幾何学的な変形を対応付ける。
- Limitations: 編者の注意: RNNで調べた因果候補と、生体で同じ回路機構を直接操作して証明することは区別する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/31320220/

### Paper: Single-trial neural dynamics are dominated by richly varied movements
- Source: PubMed
- Canonical ID: pmid:31551604
- Publication date: 2019-09-24
- URL: https://pubmed.ncbi.nlm.nih.gov/31551604/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 課題中の神経活動に、指示されていない多様な運動が大きく寄与することを示す。
- Objective: 課題変数だけで活動を説明する際の見落としを調べる。
- Methods: video・sensorで運動を測り、widefield・二光子画像とNeuropixels記録を対応付ける。
- Data and results: 皮質全体の活動は運動に強く支配され、似たtrial平均のneuronでも異なる認知・運動の組合せを反映していた。
- Novelty: 単なるnoiseとされる試行間変動を、観測可能な行動で説明する。
- Limitations: 編者の注意: 認知活動が存在しないという結果ではない。課題と同期した微小運動を測ることが解釈の条件になる。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/31551604/

### Paper: BrainSpace: a toolbox for the analysis of macroscale gradients in neuroimaging and connectomics datasets
- Source: PubMed
- Canonical ID: pmid:32139786
- Publication date: 2020-03-05
- URL: https://pubmed.ncbi.nlm.nih.gov/32139786/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: BrainSpaceは、皮質gradientの抽出・位置合わせ・可視化を行うtoolbox。
- Objective: 離散的な領域を超えた、脳の連続的な組織軸を比較できるようにする。
- Methods: Python/Matlabでmanifold解析とalignmentを実装し、空間自己相関を考慮するnull modelで関連を検証する。
- Data and results: 機能・微細構造のgradientを異なる空間scaleで検証し、手順の利用可能性と一貫性を示す。
- Novelty: gradient解析と、空間的に妥当な関連検定を共通の道具へまとめる。
- Limitations: 編者の注意: 近い領域同士は似るため独立標本とみなす単純検定は不適切。道具の利用だけで生物学的な因果は確定しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32139786/

### Paper: Computation Through Neural Population Dynamics
- Source: PubMed
- Canonical ID: pmid:32640928
- Publication date: 2020-07-08
- URL: https://pubmed.ncbi.nlm.nih.gov/32640928/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 集団の動態がどのように計算を実装し、行動を駆動するかを整理するレビュー。
- Objective: neuronの活動patternから、実行される計算へ説明を進める。
- Methods: 力学系の数学と解析道具を導入し、運動・timing・意思決定・作業記憶の研究を検討する。
- Data and results: 集団動態を用いた成功例と今後の課題を提示。新しい一つの予測器の精度を示す論文ではない。
- Novelty: 計算を静的表象だけでなく、population状態の時間発展として捉える。
- Limitations: 編者の注意: 低次元の軌跡が見えることと、その軌跡が計算の因果的な実装であることは別途検証が必要。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32640928/

### Paper: A connectome and analysis of the adult Drosophila central brain
- Source: PubMed
- Canonical ID: pmid:32880371
- Publication date: 2020-09-07
- URL: https://pubmed.ncbi.nlm.nih.gov/32880371/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 成虫ハエのcentral brainの大部分を、化学シナプス単位で再構築したhemibrain資源。
- Objective: 行動を支える回路の具体的な構成を、広い脳領域で調べられるようにする。
- Methods: 標本作製からEM撮像・位置合わせ・分割・シナプス検出・校正までを改善し、細胞型と区画を注釈する。
- Data and results: central brainの多くの回路を公開し、結合強度、motif、区画化の電気的影響などを分析する。
- Novelty: 密な回路地図と、遺伝学的reagentにつなぐ公開資源を統合する。
- Limitations: 脳全体を含む地図ではない。編者の注意: 化学シナプスの構造から、活動や行動の動態まで直接確定はできない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32880371/

### Paper: Training deep neural density estimators to identify mechanistic models of neural dynamics
- Source: PubMed
- Canonical ID: pmid:32940606
- Publication date: 2020-09-17
- URL: https://pubmed.ncbi.nlm.nih.gov/32940606/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: simulationで訓練した深層密度推定器で、神経の機構モデルの事後分布を求める。
- Objective: 複雑で確率的なデータに合うパラメータの範囲を効率的に調べる。
- Methods: 生データまたは特徴からBayes推論を行い、受容野・ion channel・Hodgkin–Huxleyなどで検証する。
- Data and results: 新データを迅速に解析し、甲殻類のrhythm回路の構成空間から補償機構の仮説を得る。
- Novelty: 一つの最良パラメータだけでなく、観測と両立する機構の範囲を推定する。
- Limitations: 編者の注意: 推論結果はsimulationモデル・事前分布・選んだ特徴に依存し、真の生物機構が候補に含まれるかは別問題。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32940606/

### Paper: Topographic organization of the human subcortex unveiled with functional connectivity gradients
- Source: PubMed
- Canonical ID: pmid:32989295
- Publication date: 2020-09-28
- URL: https://pubmed.ncbi.nlm.nih.gov/32989295/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 皮質下の機能結合gradientから、複数scaleのatlasを作る。
- Objective: 皮質中心の地図で抜けやすい皮質下の構造を、全脳解析へ含める。
- Methods: fMRIの結合gradientを4scaleで分割し、超高磁場・課題fMRIで検証。個人差に合わせたatlasも作る。
- Data and results: 最細scaleで新しい両側性27領域を示し、海馬・扁桃体の細分、課題による変化と再現する脳–行動関係を報告。
- Novelty: 皮質下と皮質networkを結び、個人差にも対応する機能atlas。
- Limitations: 編者の注意: fMRI由来の境界はシナプス単位の細胞構築ではなく、scaleや状態による変化を伴う。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32989295/

### Paper: The connectome of the adult Drosophila mushroom body provides insights into function
- Source: PubMed
- Canonical ID: pmid:33315010
- Publication date: 2020-12-14
- URL: https://pubmed.ncbi.nlm.nih.gov/33315010/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 成虫ハエのキノコ体の配線から、感覚・記憶・出力の関係を解析する。
- Objective: 学習中枢が受ける情報と、行動・他領域へ渡す経路を把握する。
- Methods: 密なconnectomeで視覚入力、MB出力、dopamine系の調節とfeedbackを調べる。
- Data and results: 豊富な視覚入力、下行neuronへの直接結合、感覚modalitiesから出力への構造や中央複合体との連結を報告。
- Novelty: 記憶中枢を孤立した入力出力層としてでなく、全脳のfeedback回路へ位置付ける。
- Limitations: 著者は今後の理論・実験の基盤とする。編者の注意: 解剖から推定した情報の流れを実測の時間動態と同一視しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/33315010/

### Paper: Information flow, cell types and stereotypy in a full olfactory connectome
- Source: PubMed
- Canonical ID: pmid:34032214
- Publication date: 2021-05-25
- URL: https://pubmed.ncbi.nlm.nih.gov/34032214/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: ハエ嗅覚系の完全な経路と、個体内・個体間の型の安定性を解析する。
- Objective: 嗅覚入力から高次回路・下行出力までの情報の流れを整理する。
- Methods: hemibrainで一〜三次neuronを解析し、別datasetとの比較で2脳3半球の形態・接続を照合する。
- Data and results: 嗅覚葉の側性や下流の収束を発見。形態の類似と接続の関係、個体内と個体間の類似した変動を報告。
- Novelty: 情報flowの層構造を抽出する手法と、脳間の定型性の定量比較を示す。
- Limitations: 編者の注意: 脳間比較の標本は2脳3半球で、集団全体の個体差や性差の範囲を網羅するものではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/34032214/

### Paper: A connectome of the Drosophila central complex reveals network motifs suitable for flexible navigation and context-dependent action selection
- Source: PubMed
- Canonical ID: pmid:34696823
- Publication date: 2021-10-26
- URL: https://pubmed.ncbi.nlm.nih.gov/34696823/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: ハエ中央複合体の完全connectomeから、柔軟なnavigationの候補計算を読む。
- Objective: 頭方向の保持、vector navigation、内部状態に応じた行動選択の構造を特定する。
- Methods: EMで全neuronとシナプスを復元し、感覚・運動経路と再帰的motifを分析する。
- Data and results: 新しい細胞型と経路、attractor型の方向保持や感覚運動情報の統合に適するmotifを報告。
- Novelty: 全回路の配線を、navigationの力学系・計算モデルを拘束するblueprintへ変える。
- Limitations: 編者の注意: motifが計算に適することは、全条件で同じ力学が働くという実証ではなく、機能記録・操作が補完になる。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/34696823/

### Paper: Neural population geometry: An approach for understanding biological and artificial neural networks
- Source: PubMed
- Canonical ID: pmid:34801787
- Publication date: 2021-11-19
- URL: https://pubmed.ncbi.nlm.nih.gov/34801787/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 生物と人工網の表現を、population geometryで理解するレビュー。
- Objective: 高次元表現が情報を埋め込み、課題を解く原理を共通言語で記述する。
- Methods: 表現のuntangling、分類容量、disentanglement、認知地図、運動・認知の動態を幾何学的に整理する。
- Data and results: modalities・領域・architecture・時間scaleをまたぐ幾何学的な説明例を統合する。
- Novelty: 単一neuronと行動の間を、集団表現の形と変化でつなぐ。
- Limitations: 編者の注意: 幾何学的な類似は同じ生物学的実装の証明ではなく、選ぶ距離・次元・課題によって見え方が変わる。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/34801787/

### Paper: FlyWire: online community for whole-brain connectomics
- Source: PubMed
- Canonical ID: pmid:34949809
- Publication date: 2021-12-23
- URL: https://pubmed.ncbi.nlm.nih.gov/34949809/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: FlyWireは全脳の自動再構築を、多人数で校正するオンライン基盤。
- Objective: 膨大な人手校正を分散し、回路データの共有を進める。
- Methods: 空間分割したsupervoxel graphをbrowser上で共同編集し、変更履歴をprogramで利用可能にする。
- Data and results: 機械感覚neuronの再構築・解析で仕組みを実証。校正精度推定や参加の仕組みも利用目的として挙げる。
- Novelty: 画像処理の自動化と、校正の共同作業・公開をつなぐ社会的計算基盤。
- Limitations: 編者の注意: 校正を可能にする資源の論文であり、これ自体が2024年の完成全脳地図の論文ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/34949809/

### Paper: The connectome of an insect brain
- Source: PubMed
- Canonical ID: pmid:36893230
- Publication date: 2023-03-10
- URL: https://pubmed.ncbi.nlm.nih.gov/36893230/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 幼虫ハエ全脳のconnectomeを作り、再帰・感覚統合・学習回路の構造を調べる。
- Objective: 行動・価値計算・行動選択を支える全体architectureを明らかにする。
- Methods: シナプス単位の地図から細胞型、hub、前向き・feedback、半球間・神経索との経路を解析する。
- Data and results: 3,016 neuronと548,000シナプスを復元。学習中枢の入出力で特に強い再帰構造と、多感覚・半球間統合を報告。
- Novelty: 局所でなく全脳を対象に、多層shortcutや入れ子の再帰loopを記述する。
- Limitations: 幼虫の脳であり成虫の約14万neuron地図とは別。AI構造との類似は、同じ学習則・能力の実証ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/36893230/

### Paper: Connectome-constrained networks predict neural activity across the fly visual system
- Source: PubMed
- Canonical ID: pmid:39261740
- Publication date: 2024-09-11
- URL: https://pubmed.ncbi.nlm.nih.gov/39261740/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 配線で制約したハエ視覚モデルを課題学習し、細胞ごとの活動を予測する。
- Objective: 接続以外の生物学的詳細が未知でも、計算から活動を推定できるか検証する。
- Methods: 運動経路64細胞型の結合を固定し、単一neuron・synapseの未知パラメータを深層学習で最適化する。
- Data and results: 視覚運動課題を学んだ予測が、26研究の活動測定と整合。疎な接続のとき成功しやすいことも示す。
- Novelty: connectomeと課題最適化を使い、実験可能な細胞別の機構仮説を生成する。
- Limitations: 配線だけから無学習で全活動を復元した研究ではない。生理パラメータは課題で最適化され、疎性にも依存する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/39261740/

### Paper: Neuronal wiring diagram of an adult brain
- Source: PubMed
- Canonical ID: pmid:39358518
- Publication date: 2024-10-02
- URL: https://pubmed.ncbi.nlm.nih.gov/39358518/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 成虫雌ハエの全脳を、約14万neuronと約5千万化学シナプスで記述する地図。
- Objective: 局所の回路にとどまらず、全脳の入力から出力までを追えるようにする。
- Methods: EM再構築に細胞型・nerve・発生系列・神経伝達物質予測を加え、領域間投射と経路を解析する。
- Data and results: 139,255 neuron、約5×10の7乗シナプスを公開。光受容から下行motor経路をたどり、候補の感覚運動機構を示す。
- Novelty: 複雑な行動を持つ成虫の全脳で、細胞単位の配線を検索・解析可能にする。
- Limitations: 編者の注意: 1個体の雌の構造資源であり、配線図の完成は感情・意識や全行動の説明の完成ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/39358518/

### Paper: Whole-brain annotation and multi-connectome cell typing of Drosophila
- Source: PubMed
- Canonical ID: pmid:39358521
- Publication date: 2024-10-02
- URL: https://pubmed.ncbi.nlm.nih.gov/39358521/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: FlyWire全脳に細胞型・発生系列の体系的注釈を付け、別個体の地図と比較する。
- Objective: 脳間で再同定できる細胞型を定義し、比較connectomicsを可能にする。
- Methods: 形態と接続を跨ぐ定量比較から細胞型を定義し、FlyWireとhemibrainを共同解析する。
- Data and results: 8,453型を注釈。既提案3,643型、新規4,581型を報告し、hemibrainの提案型の約3分の1は確実な再同定が困難だった。
- Novelty: 脳内だけの類似性でなく、脳間の対応による細胞型の定義を検証する。
- Limitations: すべての旧細胞型が安定に対応するわけではない。編者の注意: 注釈総数と既存・新規内訳は原著の分類に従い、単純な和を再定義しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/39358521/

### Paper: Neuronal parts list and wiring diagram for a visual system
- Source: PubMed
- Canonical ID: pmid:39358525
- Publication date: 2024-10-02
- URL: https://pubmed.ncbi.nlm.nih.gov/39358525/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 成虫ハエ視葉の細胞型一覧と、型の間の接続規則を整理する。
- Objective: 視覚系の計算を理解するための部品と配線をそろえる。
- Methods: 全connectomeの高次元特徴の距離と識別特徴を用い、細胞型の一貫性と領域間接続を分析する。
- Data and results: 一部の既存familyは型数が倍以上となり、新しいSm familyや領域横断の型を発見。運動・物体・色覚の候補機能を提案する。
- Novelty: 密な細胞地図を、細胞型単位の簡潔な回路図へ縮約する。
- Limitations: 編者の注意: 型の分離は接続特徴に基づき、すべての型の機能が生理実験で確定したわけではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/39358525/

### Paper: Network statistics of the whole-brain connectome of Drosophila
- Source: PubMed
- Canonical ID: pmid:39358527
- Publication date: 2024-10-02
- URL: https://pubmed.ncbi.nlm.nih.gov/39358527/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 成虫ハエ全脳のmotif・hub・領域間構造をnetwork解析する。
- Objective: 配線の統計的な構成が、情報の統合・伝達をどう支えるかを調べる。
- Methods: 2・3節点motifの頻度と強さを、伝達物質・細胞型に対応付け、78領域のsubnetworkも比較する。
- Data and results: 約30%のneuronが関わるrich-club構造を報告し、統合役・broadcast役の候補集合を同定する。
- Novelty: 全脳のシナプス構造で、局所motifと広域hubを同じ資源から解析する。
- Limitations: 編者の注意: rich-clubの節点群の役割は構造からの候補であり、実際の情報伝達や行動への因果寄与は別途検証する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/39358527/

### Paper: The human connectome: A structural description of the human brain
- Source: PubMed
- Canonical ID: pmid:16201007
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/16201007/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 人間のconnectomeを収集・保存・共有する研究戦略を提案した概念的基礎論文。
- Objective: ほぼ未知だった人間の解剖学的接続行列を、共同研究の目標に据える。
- Methods: 他の哺乳類の資源と人間の不足を整理し、接続地図を作る研究戦略と影響を論じる。
- Data and results: 新たな完成脳地図や予測実験ではなく、human connectome研究を進める構想を提示する。
- Novelty: connectomeを神経科学の基盤情報として明確に定義・提案する。
- Limitations: 2005年時点の計画論文であり、現在の全細胞単位の人間全脳地図の完成を報告したものではない。
- Publication date note: PubMedに日単位の電子公開日・冊子刊行日の記録なし。巻号の刊行年月: 2005 Sep。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/16201007/

### Paper: Small-world brain networks
- Source: PubMed
- Canonical ID: pmid:17079517
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/17079517/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: small-world構造を使い、脳の局所専門化と広域統合を説明するレビュー。
- Objective: 少ない長距離配線で効率と複雑な動態を支える可能性を整理する。
- Methods: graph理論を導入し、macaque・catのtracingと人間のEEG/MEG・fMRI研究へ適用を紹介する。
- Data and results: 高い局所clusterと短い全体経路を持つnetworkの、費用・頑健性・行動への含意を議論する。
- Novelty: 脳networkの情報処理を、配線費用を含む共通のtopologyで比較する。
- Limitations: 編者の注意: small-worldという名称だけでは機構を特定せず、節点の定義・閾値・比較するnull modelに指標が依存する。
- Publication date note: PubMedに日単位の電子公開日・冊子刊行日の記録なし。巻号の刊行年月: 2006 Dec。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/17079517/

<!-- PAPER_IDS -->
pmid:32880371
pmid:39358518
pmid:23925240
pmid:39358521
pmid:28796202
pmid:33315010
pmid:34696823
pmid:36893230
pmid:34949809
pmid:34032214
pmid:39358527
pmid:39358525
pmid:39261740
pmid:21653723
pmid:12506194
pmid:19188601
pmid:19211893
pmid:26457551
pmid:16201007
pmid:21810475
pmid:22049421
pmid:18403396
pmid:28302591
pmid:21251014
pmid:17079517
pmid:26393868
pmid:29203085
pmid:32989295
pmid:21151783
pmid:27655008
pmid:32139786
pmid:22722855
pmid:31551604
pmid:32640928
pmid:30224673
pmid:25971509
pmid:27067378
pmid:19357332
pmid:30315158
pmid:30877963
pmid:29887338
pmid:34801787
pmid:31320220
pmid:32940606
pmid:30344047
pmid:22096452
pmid:27814352
pmid:24812127
pmid:29681533
pmid:29513219
<!-- /PAPER_IDS -->
