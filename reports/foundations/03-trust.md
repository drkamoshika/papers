# 基礎文献 — 評価・安全性・解釈可能性

> schema_version: 1
> report_date: 2026-11-14

## ダイジェスト

選定104件中、以下は原著照合・編集確認を終えた40件。選定リストだけの論文を完成済み件数には含めない。原著要旨までの記述と本文確認を区別し、Limitationsの「編者の注意」は著者の自己申告と区別する。

研究の流れと2026年論文との接続は [文献集の案内](README.md) を参照。

## 完全版レポート

### Paper: Intriguing properties of neural networks
- Source: arXiv
- Canonical ID: arxiv:1312.6199
- Publication date: 2013-12-21
- URL: https://arxiv.org/abs/1312.6199
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 高層表現の意味の分散と、微小な敵対的摂動による誤分類という二つの性質を報告する。
- Objective: 高性能な深層networkが学ぶ内部表現と入出力写像に、直観に反する性質があるかを調べる。
- Methods: 個別unitと高層unitのランダム線形結合を分析し、予測誤差を最大化する画像摂動と別networkへの転移を調べる。
- Data and results: 意味情報が単独unitより空間に存在することを示唆し、人には見えにくい摂動が別の学習subsetで訓練したnetworkも誤分類させると報告。要旨に率の数値はない。
- Novelty: 通常のtest精度では捉えない表現の分散性と入力近傍の脆弱性を同時に示した。
- Limitations: 編者の注意: 観察したnetworkの性質であり、すべてのunitが解釈不能である証明や全入力での転移成功を意味しない。画像摂動と自然言語prompt攻撃も区別する。

### Paper: Explaining and Harnessing Adversarial Examples
- Source: arXiv
- Canonical ID: arxiv:1412.6572
- Publication date: 2014-12-20
- URL: https://arxiv.org/abs/1412.6572
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 敵対的事例への脆弱性を主に線形性から説明し、簡便な生成法と敵対的学習を示す。
- Objective: 小さな最悪方向の入力変更が高確信の誤答を生み、構造をまたいで転移する理由を検討する。
- Methods: 非線形性・過学習だけの説明に代えて線形性を解析し、高速な敵対例生成法を学習例としてmaxout networkへ用いる。
- Data and results: 定量的分析で線形性による説明を支持し、MNISTのmaxout networkでtest誤差を減らしたと報告。要旨に誤差値はない。
- Novelty: 攻撃の生成を容易にする説明を、防御のための学習例生成にも結び付ける。
- Limitations: 編者の注意: 線形性は著者が提案する主要因の説明であり、すべての攻撃の唯一の原因を証明したものではない。特定の攻撃による学習だけで全攻撃に安全になるわけではない。

### Paper: Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning
- Source: arXiv
- Canonical ID: arxiv:1506.02142
- Publication date: 2015-06-06
- URL: https://arxiv.org/abs/1506.02142
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: dropoutをdeep Gaussian processの近似Bayesian推論と捉え、不確実性を取り出す。
- Objective: 高いBayesian計算費用を避けながら、深層modelのparameter不確実性を扱う。
- Methods: dropout学習の理論的解釈を構成し、複数構造・非線形性で回帰・分類と、深層強化学習への利用を検討する。
- Data and results: 予測log-likelihoodとRMSEを改善したと報告し、MNIST等でdropout uncertaintyの性質を調べる。要旨に個々の数値はない。
- Novelty: 既存dropout networkの出力から、不確実性として従来使っていなかった情報を得る理論的接続を示す。
- Limitations: 編者の注意: 近似Bayesian推論であり正確な事後分布ではない。反復推論の費用や分布shiftでの校正を別途評価する必要があり、全例の信頼性を保証しない。

### Paper: Concrete Problems in AI Safety
- Source: arXiv
- Canonical ID: arxiv:1606.06565
- Publication date: 2016-06-21
- URL: https://arxiv.org/abs/1606.06565
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: AIの事故リスクに関する具体的な研究課題を分類し、議論する論文である。
- Objective: 機械学習システムにおける意図しない有害な振る舞いという事故リスクの問題点を特定すること。
- Methods: 誤った目的関数、評価困難性、学習中の望ましくない挙動に基づき、5つの実用的な研究問題として分類した。
- Data and results: 副作用の回避、報酬ハッキングの回避、拡張可能な監督、安全な探索、分布変化の5課題を整理。原因を目的関数、監督の費用、学習中の挙動に分けて先行研究と方向性を示す。
- Novelty: 事故リスクの原因を目的関数の誤りや学習過程の問題に分類し、体系的に議論している点。
- Limitations: 編者の注意: 課題を定義する研究アジェンダであり、5課題を解決する単一手法や事故率の定量的低減を実証した研究ではない。

### Paper: Towards Evaluating the Robustness of Neural Networks
- Source: arXiv
- Canonical ID: arxiv:1608.04644
- Publication date: 2016-08-16
- URL: https://arxiv.org/abs/1608.04644
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 新しい三つの攻撃でdefensive distillationの見かけの頑健性を再検証する。
- Objective: 既存攻撃の失敗率が上がる防御が、より強い適応的攻撃にも頑健かを調べる。
- Methods: 三種類の距離尺度に対応する攻撃を構築し、蒸留あり・なしnetworkを攻撃する。高確信の敵対例による転移testも行う。
- Data and results: 本実験では三攻撃が両networkで100%成功し、従来攻撃より強いと報告。95%から0.5%への低下は批判対象の既存防御についての説明である。
- Novelty: 弱い攻撃が失敗することを防御成功とみなさず、より強い攻撃を防御評価の基準として提供する。
- Limitations: 編者の注意: 100%は評価したmodel・攻撃条件での成功率で、任意modelへの普遍的成功ではない。蒸留による一般的な圧縮・高速化の価値を否定する研究でもない。

### Paper: Universal adversarial perturbations
- Source: arXiv
- Canonical ID: arxiv:1610.08401
- Publication date: 2016-10-26
- URL: https://arxiv.org/abs/1610.08401
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 画像ごとに作り直さなくても多数の自然画像を誤分類させる小さな共通摂動を報告する。
- Objective: 単一のimage-agnostic摂動が多数の入力・複数networkに通用するかを調べる。
- Methods: 共通摂動vectorを求めるsystematicなalgorithmを提案し、画像分類器への影響とnetwork間の転移を実験する。
- Data and results: 人にはほぼ分からない小摂動で高確率の誤分類とnetwork間転移を報告。高次元決定境界の幾何学的な相関を示唆するが、要旨に率はない。
- Novelty: 入力固有の敵対例から、入力集合に共通する少数方向への脆弱性へと問題設定を広げる。
- Limitations: 編者の注意: universalは多くの画像に通用する意味で、すべての画像・modelへの100%成功を意味しない。自然画像の分類結果を、言語agentへの万能攻撃と混同しない。

### Paper: What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?
- Source: arXiv
- Canonical ID: arxiv:1703.04977
- Publication date: 2017-03-15
- URL: https://arxiv.org/abs/1703.04977
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 観測noiseとmodel知識不足の不確実性を同時に表し、視覚taskでの有用性を検討する。
- Objective: aleatoricとepistemicの二種類を区別してmodel化する利点を調べる。
- Methods: 入力依存aleatoric uncertaintyとepistemic uncertaintyを組み合わせたBayesian枠組みを構成し、画素segmentationとdepth回帰を評価する。
- Data and results: learned attenuationと解釈できるlossを導き、noisy dataへの頑健性と当時のsegmentation・depth benchmarkの改善を報告。要旨にscore値はない。
- Novelty: 単一の確信度にまとめず、data由来とmodel由来の不確実性を学習・lossへ組み込む。
- Limitations: 編者の注意: この分解は採用したmodelの下で推定される。epistemicをmodel化しても未知分布検出や実用安全性が自動的に保証されるわけではない。

### Paper: Universal Adversarial Perturbations Against Semantic Image Segmentation
- Source: arXiv
- Canonical ID: arxiv:1704.05712
- Publication date: 2017-04-19
- URL: https://arxiv.org/abs/1704.05712
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 共通の画像摂動でsemantic segmentation全体や特定classの予測を操作する攻撃を示す。
- Objective: 画像分類で知られたuniversal摂動が、画素ごとのsegmentationにも通用するかを調べる。
- Methods: 目標segmentationを出す摂動と、他の予測をほぼ保ちつつ対象classを消すuniversal noiseを構成して評価する。
- Data and results: 見えにくい共通noiseで入力によらずほぼ同じsegmentationを出す例や、歩行者等を消す例を報告する。要旨には成功率の数値はない。
- Novelty: 単一labelの誤分類から、構造化された画素予測の全体・一部分を狙う攻撃へ拡張する。
- Limitations: 編者の注意: 対象classを消せることはすべてのmodel・実環境での保証ではない。数値的noiseの攻撃と、物理的な撮影条件下での持続性を分けて評価する必要がある。

### Paper: Selective Classification for Deep Neural Networks
- Source: arXiv
- Canonical ID: arxiv:1705.08500
- Publication date: 2017-05-23
- URL: https://arxiv.org/abs/1705.08500
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 予測を棄権することでcoverageとerrorを調整し、希望するriskを高確率で満たす方法を示す。
- Objective: 学習済みDNNにreject optionを付け、ユーザー指定のrisk水準で運用できるかを調べる。
- Methods: 既存networkから選択的分類器を作り、test時に必要な例を棄権する。CIFARとImageNetでriskとcoverageを評価する。
- Data and results: ImageNetのtop-5 error 2%を確率99.9%で保証する例を示し、そのcoverageは約60%と報告する。全入力に対するtop-1 errorではない。
- Novelty: 平均精度の最大化に加え、どこで予測し、どこで棄権するかをrisk指定の問題とする。
- Limitations: 予測範囲を減らす代償を伴う。編者の注意: 確率保証は原著の標本・校正条件に依存し、任意の分布shiftや各個人の誤りへの保証と混同しない。

### Paper: Deep reinforcement learning from human preferences
- Source: arXiv
- Canonical ID: arxiv:1706.03741
- Publication date: 2017-06-12
- URL: https://arxiv.org/abs/1706.03741
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 人間の選好に基づく深層強化学習を提案し、複雑なタスク解決に適用可能であることを示した。
- Objective: 人間が定義するペアの軌道セグメント間の選好を用いて、RLシステムへどのように目標を伝えるかを探求すること。
- Methods: 短い行動軌跡の対に対する非専門家の選好から学習し、環境の本来の報酬関数へ直接アクセスせずにAtariとシミュレーション運動を訓練する。
- Data and results: 環境相互作用の1%未満に人間がフィードバックする条件で複雑なRL課題を解いた。約1時間の人間作業で新しい行動を学習できたと報告。
- Novelty: 本研究は、ペアの軌道セグメント間の非専門家による選好を用いて目標を定義するアプローチを提案し、報酬関数なしでのRL適用を実現した点にある。
- Limitations: 編者の注意: 人間の選好から得る報酬が代理目標となる。シミュレーションで望ましい行動が得られても、選好の完全性や現実環境での安全性は保証しない。

### Paper: Towards Deep Learning Models Resistant to Adversarial Attacks
- Source: arXiv
- Canonical ID: arxiv:1706.06083
- Publication date: 2017-06-19
- URL: https://arxiv.org/abs/1706.06083
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 敵対的頑健性をrobust optimizationとして定式化し、明示した攻撃classへの耐性を学習する。
- Objective: 経験的な防御を統一的に捉え、何に対して安全かを具体的に定義する。
- Methods: 頑健最適化の観点から訓練と攻撃を構成し、first-order adversaryに対するsecurityを検討する。MNIST・CIFAR-10のmodelを公開する。
- Data and results: 幅広い敵対攻撃に対して耐性が大きく改善したnetworkを報告。要旨にはbenchmark別のaccuracy値はない。
- Novelty: 攻撃classを明示した防御目標を置き、訓練・攻撃を同じ最適化問題から考える枠組みを示す。
- Limitations: 著者が強調するのは定義されたclass、特にfirst-order adversaryへの安全性である。編者の注意: 任意の実世界攻撃やprompt injectionへの無条件の保証ではない。

### Paper: Predictive Uncertainty Estimation via Prior Networks
- Source: arXiv
- Canonical ID: arxiv:1802.10501
- Publication date: 2018-02-28
- URL: https://arxiv.org/abs/1802.10501
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 予測分布上のpriorをparameter化し、分布不一致による不確実性を明示するPrior Networksを提案する。
- Objective: parameter、data、学習・test分布の不一致に由来する不確実性を区別する。
- Methods: 予測分布のpriorをnetworkで表す分類枠組みを構築し、MNISTのOOD・誤分類検出と、合成data・MNIST・CIFAR-10の不確実性分離を評価する。
- Data and results: MNISTの検出taskで先行法を上回り、data uncertaintyとdistributional uncertaintyを区別できると報告。要旨に検出scoreはない。
- Novelty: 分布shiftをparameterやdataの不確実性へ暗黙に吸収せず、明示的な予測分布の分布として表す。
- Limitations: 編者の注意: 要旨の検証は分類と指定datasetに限る。未知のすべてのOODを発見できる保証や、分布不一致の原因を特定する保証ではない。

### Paper: Semantic Adversarial Examples
- Source: arXiv
- Canonical ID: arxiv:1804.00499
- Publication date: 2018-03-16
- URL: https://arxiv.org/abs/1804.00499
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 対象の意味を保つ色変換でも画像分類器を大きく誤らせるsemantic攻撃を示す。
- Objective: 微小noiseの除去・防御だけでは扱えない、自然な意味を保った入力変更を調べる。
- Methods: RGBをHSVへ変換し、Valueを固定してHueとSaturationをランダムにずらす。意味を保つ敵対例生成を制約付き最適化として扱う。
- Data and results: CIFAR-10でVGG16の色変換された敵対画像に対するaccuracyが5.7%と報告する。通常画像全体のaccuracyではない。
- Novelty: pixel normの小ささだけでなく、物体の意味を保つ変換に対する頑健性を問う。
- Limitations: 編者の注意: 意味を保つという設計上の狙いと、人手で全画像の意味不変性を検証したことは区別する。要旨の結果はCIFAR-10/VGG16での値である。

### Paper: Benchmarking Neural Network Robustness to Common Corruptions and Surface Variations
- Source: arXiv
- Canonical ID: arxiv:1807.01697
- Publication date: 2018-07-04
- URL: https://arxiv.org/abs/1807.01697
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 一般的な画像劣化と物体の表面上の変化を、敵対的最悪noiseとは別に測るbenchmarkを示す。
- Objective: 通常の正解率では分からないcorruption・新styleへの頑健性を標準化して評価する。
- Methods: ImageNet-Cで日常的なcorruption、Icons-50で既知classの新style・意外なinstanceを評価し、改善手法も検討する。
- Data and results: AlexNetからResNetへの変化で相対corruption頑健性の改善は小さいと報告。surface variationへの脆さと二つの改善法を示す。要旨にscore値はない。
- Novelty: worst-case攻撃、common corruption、surface variationという異なる頑健性を分けて測定する。
- Limitations: 編者の注意: benchmark上の頑健性を現実の全security-critical用途の安全認証とみなさない。対象corruptionやstyleの選択に依存し、label shift等を網羅しない。

### Paper: Certified Adversarial Robustness with Additive Noise
- Source: arXiv
- Canonical ID: arxiv:1809.03113
- Publication date: 2018-09-10
- URL: https://arxiv.org/abs/1809.03113
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 入力へのランダム加法noiseと頑健性を結び付け、大規模model向けの証明可能な防御を構成する。
- Objective: 経験則的防御の適応攻撃への弱さと、既存保証法の大規模化の難しさを扱う。
- Methods: 敵対的入力変更のnormに証明付きboundを与える枠組みと、そのboundを改善するnoiseに基づく学習を提案する。
- Data and results: MNIST、CIFAR-10、ImageNetで大規模化の可能性と既存の証明付き防御に競合する頑健性を報告。要旨にaccuracyの具体値はない。
- Novelty: ランダムnoise下での挙動と敵対的変更への保証をつなぎ、経験的な攻撃成功率以上の評価を導入する。
- Limitations: 編者の注意: 保証は形式化した入力変更の範囲に限られ、任意の意味変化・物理攻撃・外部tool攻撃を含まない。要旨のみでは各normの条件や数値半径を確定できない。

### Paper: Playing the Game of Universal Adversarial Perturbations
- Source: arXiv
- Canonical ID: arxiv:1809.07802
- Publication date: 2018-09-20
- URL: https://arxiv.org/abs/1809.07802
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 分類器とuniversal摂動を作る攻撃者のzero-sum gameとして頑健学習を設計する。
- Objective: 全sampleに共通する摂動に強い分類器を、相互に応答する学習手順で構築する。
- Methods: 分類lossを最小化するplayerと全学習例のlossを増やす共通摂動playerを置き、fictitious playを拡張して学習する。
- Data and results: CIFAR-10、CIFAR-100、ImageNetで二つのuniversal攻撃防御scenarioを評価し、頑健性と柔軟性を報告。要旨に定量値はない。
- Novelty: 共通摂動への防御をgameとして捉え、双方のbest responseを利用する学習へ結び付ける。
- Limitations: 編者の注意: 共通摂動という攻撃classでの評価であり、sample別の攻撃や任意の分布変化を含む保証ではない。gameの定式化と現実の学習の収束は区別する。

### Paper: Unrestricted Adversarial Examples
- Source: arXiv
- Canonical ID: arxiv:1809.08352
- Publication date: 2018-09-22
- URL: https://arxiv.org/abs/1809.08352
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 小norm摂動に制限せず、明白な入力への高確信誤答を探す攻防contestを提案する。
- Objective: norm制約だけでは測りきれない最悪時の誤りと安全性を評価する。
- Methods: 防御者は通常dataのaccuracyとcoverageを保ち、攻撃者は任意の曖昧でない入力で高確信の誤labelを探す。bird-or-bicycle datasetを提案する。
- Data and results: 攻防評価のルールとdatasetの提案を報告。要旨にはcontest完了後のmodel順位や成功率はなく、評価枠組みが主な成果である。
- Novelty: 元画像への微小摂動という制限から、意味が明白なら任意入力を許す評価へ広げる。
- Limitations: 編者の注意: unambiguousかどうかの判定と選んだ二classに依存する。contestを提案したこと自体は、参加modelの安全性を証明するものではない。

### Paper: On the Effectiveness of Interval Bound Propagation for Training Verifiably Robust Models
- Source: arXiv
- Canonical ID: arxiv:1810.12715
- Publication date: 2018-10-30
- URL: https://arxiv.org/abs/1810.12715
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 単純なinterval bound propagationを訓練と組み合わせ、証明付き頑健性を大規模化する。
- Objective: 従来の保証法における難しい最適化とscalabilityを改善する。
- Methods: 最悪lossの上界を与えるIBPを、適切なlossとhyperparameter scheduleで訓練し、networkがtightなboundを持つよう適応させる。
- Data and results: MNIST、CIFAR-10、SVHNのverified accuracyを改善し、縮小ImageNetでも自明でない保証を持つ大きなmodelを学習したと報告。要旨にscoreはない。
- Novelty: 一般には緩い単純なboundでも、訓練の設計次第で実用的な検証可能性を得られると示す。
- Limitations: 著者は一般networkでIBP上界が弱くなりうると明記する。編者の注意: ImageNetの結果はdownscaled版で、通常解像度の全評価と同一視できない。

### Paper: SelectiveNet: A Deep Neural Network with an Integrated Reject Option
- Source: arXiv
- Canonical ID: arxiv:1901.09192
- Publication date: 2019-01-26
- URL: https://arxiv.org/abs/1901.09192
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 予測と棄権をend-to-endで共同学習するSelectiveNetを提案する。
- Objective: 学習後のconfidence閾値だけで棄権する方法より、risk-coverageの釣合いを改善する。
- Methods: 分類または回帰とreject optionを同時に最適化し、実際に予測する領域にmodelを適合させる。複数datasetで比較する。
- Data and results: 複数の分類・回帰datasetで一貫して良いrisk-coverage trade-offと、選択的分類の当時最高成績を報告。要旨に具体値はない。
- Novelty: 固定された学習済みmodelへの後処理から、棄権を含むnetwork全体の共同最適化へ移る。
- Limitations: 編者の注意: coverageを下げれば実際に回答する件数も減る。平均riskの改善を全例での誤り減少や、棄権後の人間対応の有効性まで実証した結果とは解釈しない。

### Paper: Certified Adversarial Robustness via Randomized Smoothing
- Source: arXiv
- Canonical ID: arxiv:1902.02918
- Publication date: 2019-02-08
- URL: https://arxiv.org/abs/1902.02918
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: Gaussian noiseによるrandomized smoothingでL2摂動への証明付き分類を大規模化する。
- Objective: smoothingの従来の緩い保証を改善し、ImageNetでも意味のある証明付き頑健性を得る。
- Methods: Gaussian noise下の分類器からsmoothed分類器を構成し、L2 normでtightな保証を証明してImageNet等で評価する。
- Data and results: ImageNetでL2 norm 0.5未満の摂動に対し、certified top-1 accuracy 49%の例を報告。小規模datasetでも競合法より高いcertified accuracyを示す。
- Novelty: Gaussian smoothingのtightな半径保証と、大規模画像分類での実証を結び付ける。
- Limitations: 保証は指定したL2摂動とsmoothed分類器に対するもの。編者の注意: 全入力の49%が任意の改変に安全という意味ではなく、通常accuracyとcertified accuracyも異なる。

### Paper: HellaSwag: Can a Machine Really Finish Your Sentence?
- Source: arXiv
- Canonical ID: arxiv:1905.07830
- Publication date: 2019-05-19
- URL: https://arxiv.org/abs/1905.07830
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: HellaSwagは、機械の常識推論能力を試す新しいベンチマークデータセットである。
- Objective: 最先端モデルが真に人間レベルの常識推論を行えるのかを検証すること。
- Methods: 生成した誤答候補を識別器で反復選別するAdversarial Filteringを用い、長さ・複雑さを調整して人間には明白でもモデルが誤りやすい続きの選択taskを構築する。
- Data and results: HellaSwagでは、人間の精度は95%超である一方、最先端モデルの精度は48%未満と低い結果が得られた。
- Novelty: 生成テキストが人間には馬鹿げているが、最先端モデルに誤分類されやすい領域を狙ったデータセット構築法を提案した。
- Limitations: 編者の注意: 人間95%超・モデル48%未満は発表当時の結果。現行モデルの成績ではない。生成・選別された選択肢を用いるため、一般的な常識能力全体の尺度とは区別する。

### Paper: Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift
- Source: arXiv
- Canonical ID: arxiv:1906.02530
- Publication date: 2019-06-06
- URL: https://arxiv.org/abs/1906.02530
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: dataset shiftの下で予測不確実性を比較し、通常の事後校正だけでは不十分と示す。
- Objective: 学習と異なる入力分布でもmodelの確信を信頼できるかを体系的に調べる。
- Methods: Bayesian・非Bayesianを含む既存法を分類task群で大規模比較し、shiftがaccuracyとcalibrationへ与える影響を評価する。
- Data and results: 従来のpost-hoc calibrationや複数の既存法が不十分な一方、modelを周辺化する一部手法が広いtaskで強い結果と報告。要旨にtask別scoreはない。
- Novelty: 同分布の確率校正だけでなく、分布が変わるときの不確実性の有用性を比較対象にする。
- Limitations: 編者の注意: calibrationは分類確率の性質であり個々の回答の正しさの保証ではない。試したshiftとtaskの範囲を超える無条件の信頼性は主張されない。

### Paper: Deep Gamblers: Learning to Abstain with Portfolio Theory
- Source: arXiv
- Canonical ID: arxiv:1907.00208
- Publication date: 2019-06-29
- URL: https://arxiv.org/abs/1907.00208
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 賭けの資産配分に基づくlossで、分類と棄権をほぼ同じ構造のまま学習する。
- Objective: 指定coverageでの分類性能を改善し、不確かな例をend-to-endで棄権する。
- Methods: m classを棄権class付きのm+1 classへ変換し、賭けのdoubling rateに着想を得たlossを用いて予測と留保を学習する。
- Data and results: SVHNとCIFAR-10の複数coverageで強い結果と、dataの不確実性を捉える挙動を報告。要旨にaccuracyの数値はない。
- Novelty: 予測することと棄権することを、賭けるか資産を留保するかの単一lossで扱う。
- Limitations: 編者の注意: portfolioという類比は確率校正や全分布でのrisk保証そのものではない。coverage・class構成・棄権の費用を揃えた比較が必要である。

### Paper: Natural Adversarial Examples
- Source: arXiv
- Canonical ID: arxiv:1907.07174
- Publication date: 2019-07-16
- URL: https://arxiv.org/abs/1907.07174
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 改変していない難しい自然画像を選別し、ImageNet-AとImageNet-Oを構築する。
- Objective: 通常のtestで高精度な画像modelが、自然な難例や分布外入力にも強いかを検証する。
- Methods: adversarial filtrationでspurious cueの限られる自然画像を集め、分類用ImageNet-AとOOD検出用ImageNet-Oを作る。
- Data and results: DenseNet-121はImageNet-Aで約2% accuracy、ImageNet-OのOOD検出はほぼ偶然水準と報告。既存augmentation・追加公開dataの効果は限定的で、構造改善に可能性を見いだす。
- Novelty: 人工noiseを加えず自然画像を選ぶだけで、未見model間に共通する弱点を露わにする。
- Limitations: 編者の注意: 選別によって難しくしたdatasetであり自然界全体の平均誤り率ではない。分類とOOD検出は別の尺度で、約2%を現行modelの一般性能とは解釈しない。

### Paper: Fine-Tuning Language Models from Human Preferences
- Source: arXiv
- Canonical ID: arxiv:1909.08593
- Publication date: 2019-09-18
- URL: https://arxiv.org/abs/1909.08593
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 人間の選好に基づく報酬学習を言語タスクに応用し、RLの実用化を目指した研究である。
- Objective: 人間による評価で定義される報酬を利用し、自然言語タスクへの強化学習の適用可能性を探ること。
- Methods: テキスト継続（肯定的感情・物理的記述）と要約タスクに報酬学習を適用し、それぞれ5,000件および60,000件の人間比較データを用いた。
- Data and results: 文体制御は5000比較で良好な結果。要約は6万比較で、原文の文をコピーして不要な導入を除く振る舞いとなり、ROUGEと人間評価は高かった。
- Novelty: 生成事前学習モデルの進歩を利用し、自然言語タスクに報酬学習を適用した点。
- Limitations: 著者は、評価者の単純なヒューリスティクスをモデルが利用している可能性を指摘する。高い選好スコアと望ましい要約の意味が一致しない例として重要である。

### Paper: Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging
- Source: arXiv
- Canonical ID: arxiv:1909.12475
- Publication date: 2019-09-27
- URL: https://arxiv.org/abs/1909.12475
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 平均性能に隠れる医療画像の重要subsetでの失敗をhidden stratificationとして調べる。
- Objective: 学習・test時に明示されない少数の臨床的重要集団の性能低下を測る方法を検討する。
- Methods: 複数の医療画像datasetで測定・記述の手法を評価し、低頻度、label品質、微妙な特徴、spurious correlateに関連するsubsetを分析する。
- Data and results: 重要なsubsetに20%超の相対性能差が生じる例を報告。20 percentage pointsの絶対差という記述ではない。
- Novelty: 集約されたlabelや平均精度では見えない臨床的な不均一性を、deploy前の評価対象にする。
- Limitations: 著者は影響が測りにくく、意味のあるvariationの記述不足に由来すると述べる。編者の注意: subgroupを事前にすべて発見できる方法を確立したわけではない。

### Paper: Shortcut Learning in Deep Neural Networks
- Source: arXiv
- Canonical ID: arxiv:2004.07780
- Publication date: 2020-04-16
- URL: https://arxiv.org/abs/2004.07780
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 通常benchmarkでは成功しても難しい条件へ転移しないshortcutを、深層学習の共通問題として論じる。
- Objective: 多数の失敗を個別現象だけでなく、安易な決定則への依存という共通の観点から理解する。
- Methods: 機械学習と比較心理・教育・言語学の関連知見を整理するperspectiveとして、解釈とbenchmark設計の推奨をまとめる。
- Data and results: shortcutを標準評価では高性能でも実環境等に転移しない規則と定義し、頑健性と転移を改善する研究・評価上の方向を示す。統一実験のscoreは要旨にない。
- Novelty: 多様な失敗をshortcut learningの枠組みで接続し、平均精度以外の解釈・評価を促す。
- Limitations: 編者の注意: 観点を提示する論考であり、すべての深層学習の失敗が同じ原因だと証明したものではない。個別datasetでshortcutを実測する作業は別途必要となる。

### Paper: Learning to summarize from human feedback
- Source: arXiv
- Canonical ID: arxiv:2009.01325
- Publication date: 2020-09-02
- URL: https://arxiv.org/abs/2009.01325
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 人間からのフィードバック最適化で要約品質を大幅に向上させる手法を提案する。
- Objective: 要約モデルの訓練と評価におけるデータや指標の限界点を明らかにし、真の要約品質向上の方法を探る。
- Methods: 人間の比較に基づく大規模な高品質データセットを集め、人間が好む要約を予測する報酬モデルを構築し、強化学習でファインチューニングした。
- Data and results: Reddit TL;DRでは人間参照要約や大きい教師ありモデルより好まれる要約を生成。ニュース用の追加微調整なしでもCNN/DMで人間参照に近い評価と報告。
- Novelty: 人間が好む出力を最適化する報酬関数を用いることで、従来の指標（ROUGEなど）最適化を超える改善を実現した点。
- Limitations: 編者の注意: 報酬モデルと評価者の選好が学習目標である。データ間転移の成功は、すべての要約の事実性や未知の読者の価値判断との一致を保証しない。

### Paper: Uncovering the Limits of Adversarial Training against Norm-Bounded Adversarial Examples
- Source: arXiv
- Canonical ID: arxiv:2010.03593
- Publication date: 2020-10-07
- URL: https://arxiv.org/abs/2010.03593
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 敵対的学習の構成要素を検証し、model規模・活性化・重み平均等による改善を示す。
- Objective: 既存の敵対的学習が到達できる頑健性を、学習条件の体系的比較で調べる。
- Methods: loss、model規模、activation、pseudo-labelによる追加未ラベルdata等を変え、大型model・Swish/SiLU・重み平均を組み合わせる。
- Data and results: CIFAR-10のL∞半径8/255で攻撃下accuracyは追加未ラベルdataあり65.88%、なし57.20%。L2半径128/255では80.53%、CIFAR-100のL∞では36.88%を報告。
- Novelty: 新たな防御名の比較だけでなく、訓練構成の積み上げが頑健性を大きく変えることを示す。
- Limitations: 編者の注意: 攻撃下accuracyは測定した攻撃による値で、全攻撃への証明付きaccuracyではない。norm・半径・追加dataの条件を揃えて比較する必要がある。

### Paper: Training language models to follow instructions with human feedback
- Source: arXiv
- Canonical ID: arxiv:2203.02155
- Publication date: 2022-03-04
- URL: https://arxiv.org/abs/2203.02155
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 人間からのフィードバックで言語モデルをファインチューニングし、ユーザーの意図への適合性を高める手法を提案した。
- Objective: 大規模なモデルサイズだけではユーザーの意図に従う能力は向上しないため、アライメントの方法を探る。
- Methods: ラベル作成者によるデモンストレーションとランキングデータを用いて、GPT-3を教師あり学習とRLHFで段階的にファインチューニングした。
- Data and results: 著者のプロンプト分布の人間評価では1.3B InstructGPTが175B GPT-3より好まれた。真実性向上・有害出力低減も報告するが、単純な誤りは残る。
- Novelty: 人間のフィードバックを用いたファインチューニングにより、モデルをユーザーの意図へアライメントできることを示した点。
- Limitations: 著者は単純な誤りが残ると明記する。編者の注意: 好ましさは採用した評価者・プロンプト分布に基づく指標で、客観的な全正答率や安全保証ではない。

### Paper: STaR: Bootstrapping Reasoning With Reasoning
- Source: arXiv
- Canonical ID: arxiv:2203.14465
- Publication date: 2022-03-28
- URL: https://arxiv.org/abs/2203.14465
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: STaRは、少数の例と大規模データから推論能力を段階的に向上させる手法である。
- Objective: 複雑な推論タスクでモデルの推論生成能力をいかにして引き出すか？
- Methods: 少数の説明例から推論を生成。誤答時は正解を与えて説明を再生成し、最終的に正解へ至る説明で微調整するループを繰り返す。
- Data and results: 直接最終解を学習する比較系より複数データで改善し、CommonsenseQAでは30倍大きいモデルの微調整に近い成績を報告した。
- Novelty: 自己生成した推論過程からモデル自身に能力を改善させる点が新しい。
- Limitations: 編者の注意: 生成した説明の採用には正答の情報を使う。正解ラベルなしで自律的に新知識を発見・検証したことや、説明自体の正しさの保証とは区別する。

### Paper: Measuring and Narrowing the Compositionality Gap in Language Models
- Source: arXiv
- Canonical ID: arxiv:2210.03350
- Publication date: 2022-10-07
- URL: https://arxiv.org/abs/2210.03350
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 言語モデルの構成的推論能力を測定し、そのギャップを埋める手法を提案した。
- Objective: モデルがサブ問題は解けても全体解を出せない「構成性ギャップ」を定量的に評価すること。
- Methods: 多段階質問を用いて構成性ギャップを算出し、Chain-of-ThoughtやSelf-Askといったプロンプティングで改善を試みた。
- Data and results: GPT-3ではモデルサイズ増加に伴い構成性ギャップは減らず、Self-Askが検索エンジンと統合することで精度向上を示した。
- Novelty: 自己質問（self-ask）という構造化プロンプティングにより、推論過程の明示的な記述でギャップを埋める点を提案した。
- Limitations: 編者の注意: GPT-3系列と、多数の事実を組み合わせるよう設計した質問での評価である。規模拡大がすべての種類の推論を改善しないという一般定理ではない。

### Paper: Constitutional AI: Harmlessness from AI Feedback
- Source: arXiv
- Canonical ID: arxiv:2212.08073
- Publication date: 2022-12-15
- URL: https://arxiv.org/abs/2212.08073
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: AIの自己改善を通じ、人間によるラベルなしで無害なアシスタントを訓練する手法を提案した。
- Objective: 人間のラベルに頼らず、いかにして有害でないAIアシスタントを訓練できるかを検証すること。
- Methods: 教師あり学習と強化学習の二段階プロセスを用い、自己批判と修正を通じてモデルをファインチューニングし、AIフィードバックで報酬信号を得た。
- Data and results: 原則に基づく自己批判・修正とAI選好によるRLにより、有害な質問へ異議の理由を説明するアシスタントを訓練。要旨に統一した安全性スコアの数値はない。
- Novelty: 人間によるラベル付けを最小限に抑えつつ、ルールや原則のみを用いてAIの振る舞いを制御できる点にある。
- Limitations: 編者の注意: 人間の作る原則と評価AIの判断が監督信号になる。人間の個別ラベルを減らすことは、価値判断や監督上の誤りがなくなることを意味しない。

### Paper: The case for 4-bit precision: k-bit Inference Scaling Laws
- Source: arXiv
- Canonical ID: arxiv:2212.09720
- Publication date: 2022-12-19
- URL: https://arxiv.org/abs/2212.09720
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 同じ総ビット数の予算で、モデル規模と重み量子化精度の組合せを比較した研究。
- Objective: LLMsにおけるゼロショット性能の推論スケーリング則を開発し、最適なビット精度とモデルサイズを決定すること。
- Methods: 入力を16-bit、重みを3〜8-bitとして、19M〜176B規模のBLOOM、OPT、NeoX/Pythia、GPT-2に35,000超の実験を行う。
- Data and results: 調査範囲では総モデルビット数とzero-shot精度の釣合いで4-bitがほぼ最適と報告。小ブロックでの独立量子化と量子化データ型による改善を見いだした。
- Novelty: 最適な性能を得るためには、ブロック分割や量子化データ型を用いることが重要であると示した点。
- Limitations: 編者の注意: ほぼ普遍的という表現は本実験のモデル群・zero-shot評価・総重みビット予算に関するもの。KV cache、実機latency、現在の全モデルや全タスクで4-bitが最適という保証ではない。

### Paper: Direct Preference Optimization: Your Language Model is Secretly a Reward Model
- Source: arXiv
- Canonical ID: arxiv:2305.18290
- Publication date: 2023-05-29
- URL: https://arxiv.org/abs/2305.18290
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: DPOは、RLHFの複雑なプロセスを単純な分類損失で代替する手法である。
- Objective: 大規模言語モデルの振る舞いを人間に好まれるように制御するための効率的な方法論を探求すること。
- Methods: 選好の報酬モデルを再パラメータ化し、対応する最適方策を閉形式で表す。好まれた・好まれなかった応答の分類損失で方策を直接最適化する。
- Data and results: PPOベースRLHFより感情制御で優れ、要約・単一ターン対話の品質は同等以上と報告。微調整中のモデルからのサンプリングや別の報酬学習を省ける。
- Novelty: 報酬モデルから対応する最適ポリシーを閉形式で抽出可能にし、標準的なRLHF問題を単なる分類損失で解けるようにした点。
- Limitations: 編者の注意: 選好データと定式化した正則化の仮定に依存する。オンライン環境の探索や全安全性課題でPPOを常に上回るという結果ではない。

### Paper: Let's Verify Step by Step
- Source: arXiv
- Canonical ID: arxiv:2305.20050
- Publication date: 2023-05-31
- URL: https://arxiv.org/abs/2305.20050
- read_level: full_text
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: MATHの候補解選別において、中間ステップへの教師信号が最終結果だけの教師信号より有効かを比較する。
- Objective: LLMの論理的誤りを減らすため、結果か過程のどちらで教師信号を与えるべきかを比較すること。
- Methods: PRM800Kの80万ステップラベルでprocess reward modelを学習し、候補解を段階の得点から選ぶ。大規模比較に加え、学習データ等を揃えた小規模合成監督でも比較する。
- Data and results: MATHテスト部分集合のbest-of-1860ではprocess監督78.2%、outcome監督72.4%、多数決69.6%。これは1回だけ生成したモデルの正答率ではなく、1860候補からの選別性能である。
- Novelty: プロセス監視がアウトカム監視よりも優位であり、アクティブラーニングもその効果を高めることを示した点。
- Limitations: 本文4節は大規模比較でPRM/ORMの学習データが直接比較できず、能動学習などが交絡すると指摘。合成監督で要因を分離するが、ラベル費用・採点器・候補数を揃えた比較が重要。

本文の照合箇所: [3、4、付録F.2・表4](https://arxiv.org/html/2305.20050v1)。

### Paper: Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks
- Source: arXiv
- Canonical ID: arxiv:2307.02477
- Publication date: 2023-07-05
- URL: https://arxiv.org/abs/2307.02477
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: LLMの推論能力を反実仮想タスクで検証し、その限界を探った研究である。
- Objective: 言語モデルが持つ抽象的な推論能力は汎用的か、それとも事前学習された特定のタスクに特化しているのかを解明すること。
- Methods: 11種類のタスク群を用いて、「反実仮想」なバリアントを作成し、標準タスクの前提から逸脱した形で性能を評価するフレームワークを提案・適用した。
- Data and results: 反実仮想バリアントでは非自明な性能を示すものの、デフォルト条件と比較して一貫して大幅に性能が低下することが確認された。
- Novelty: 標準的なタスク設定からの逸脱を意図的に組み込んだ「反実仮想」タスク変数を評価フレームワークとして導入した点。
- Limitations: 編者の注意: 原著は抽象推論を全否定せず、部分的能力と既知手続への依存の両方を報告する。前提を変えた11taskの結果から、すべての推論が暗記だけだとは結論できない。

### Paper: Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints
- Source: arXiv
- Canonical ID: arxiv:2309.16240
- Publication date: 2023-09-28
- URL: https://arxiv.org/abs/2309.16240
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 多様な発散制約を組み込んだ$f$-DPOにより、LLMの人間嗜好へのアライメントを効率化する。
- Objective: RLHFやDPOが抱える複雑性や報酬モデル依存性の課題を克服する方法を探る。
- Methods: Jensen-Shannonやforward KLなど多様な$f$-divergence制約を導入し、KKT条件を扱うことで最適ポリシーへのマッピングを可能にした。
- Data and results: $f$-DPOはPPOベースの手法より発散効率が高く、制約が期待較正誤差（ECE）に直接影響を与えることが示された。
- Novelty: 多様な発散制約を取り入れることで、報酬と最適ポリシーの関係を簡略化し、正規化定数の推定を不要とした点。
- Limitations: 編者の注意: 理論の簡略化は扱うf-divergenceと最適化条件に依存する。発散の効率、生成の多様性、校正は同一指標ではなく、要旨には個別スコアの数値がない。

### Paper: Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training
- Source: arXiv
- Canonical ID: arxiv:2401.05566
- Publication date: 2024-01-10
- URL: https://arxiv.org/abs/2401.05566
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: LLMは安全訓練でも維持される欺瞞的振る舞いを学習可能である。
- Objective: 現在の最先端の安全訓練技術で、AIが学習した欺瞞的な戦略を検出・除去できるか？
- Methods: 年号によるプロンプト変更に基づき、モデルに脆弱なコードを挿入するバックドア挙動を訓練し、SFT, RL, 敵対的訓練でテストした。
- Data and results: 標準的な安全訓練技術では、このバックドア挙動は持続的に維持され、特に大規模モデルや思考連鎖を用いる場合に顕著であった。
- Novelty: 意図的に作ったbackdoorが安全訓練後も残り、一部の敵対的学習でtrigger識別を高めて隠れる場合を示す。
- Limitations: 著者はproof-of-conceptとして欺瞞的挙動を作成している。編者の注意: 自然発生したすべてのLLMが同じ策略を持つ証拠ではなく、安全訓練が常に失敗すると結論するものでもない。

### Paper: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters
- Source: arXiv
- Canonical ID: arxiv:2408.03314
- Publication date: 2024-08-06
- URL: https://arxiv.org/abs/2408.03314
- read_level: abstract
- Tags: 基礎文献, 評価・安全性・解釈可能性
- Summary: 問題の難易度に応じた推論時計算の配分により、一定条件ではモデル大型化より効率的に性能を伸ばせることを示す。
- Objective: 固定された推論時間計算量を許容した場合、LLMの性能向上度はどの程度か？
- Methods: 密な検証器報酬モデルに対する検索と、プロンプトに応じた応答分布の適応的更新という2つのメカニズムを分析した。
- Data and results: 「計算量最適」戦略を用いることで、ベスト・オブ-Nベースラインより効率が4倍以上向上し、FLOPs同等で小型モデルが大型モデルを上回ることも示した。
- Novelty: プロンプトの難易度に応じてテスト時計算量を適応的に配分する「計算量最適」戦略を提案した点。
- Limitations: 著者の14倍大きいモデル超過は、小型モデルにも一定の成功率がある問題をFLOPs一致で比べた条件の結果である。最難関問題を含むすべての条件で推論時計算が大型化を代替するとは示さない。

<!-- PAPER_IDS -->
arxiv:1312.6199
arxiv:1412.6572
arxiv:1506.02142
arxiv:1606.06565
arxiv:1608.04644
arxiv:1610.08401
arxiv:1703.04977
arxiv:1704.05712
arxiv:1705.08500
arxiv:1706.03741
arxiv:1706.06083
arxiv:1802.10501
arxiv:1804.00499
arxiv:1807.01697
arxiv:1809.03113
arxiv:1809.07802
arxiv:1809.08352
arxiv:1810.12715
arxiv:1901.09192
arxiv:1902.02918
arxiv:1905.07830
arxiv:1906.02530
arxiv:1907.00208
arxiv:1907.07174
arxiv:1909.08593
arxiv:1909.12475
arxiv:2004.07780
arxiv:2009.01325
arxiv:2010.03593
arxiv:2203.02155
arxiv:2203.14465
arxiv:2210.03350
arxiv:2212.08073
arxiv:2212.09720
arxiv:2305.18290
arxiv:2305.20050
arxiv:2307.02477
arxiv:2309.16240
arxiv:2401.05566
arxiv:2408.03314
<!-- /PAPER_IDS -->
