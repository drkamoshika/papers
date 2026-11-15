# 基礎文献 — 表形式・時系列・因果推論

> schema_version: 1
> report_date: 2026-11-15

## ダイジェスト

選定119件中、以下は原著照合・編集確認を終えた119件。選定リストだけの論文を完成済み件数には含めない。原著要旨までの記述と本文確認を区別し、Limitationsの「編者の注意」は著者の自己申告と区別する。

研究の流れと2026年論文との接続は [文献集の案内](README.md) を参照。

## 完全版レポート

### Paper: Causal Discovery from Changes
- Source: arXiv
- Canonical ID: arxiv:1301.2312
- Publication date: 2013-01-10
- URL: https://arxiv.org/abs/1301.2312
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 局所的な生成機構の自発的変化を利用し、等価な因果構造の範囲を狭める方法。
- Objective: 単一の静的分布では区別しにくい構造を、変化する分布の列から推定する。
- Methods: 局所変化が生む分布系列に対する構造の等価クラスを解析し、そのグラフ表現を出すアルゴリズムを設計。人工データで変化検出と構造回復の誤りを調べた。
- Data and results: 等価クラスの特徴付けとシミュレーション結果を提供。要旨にデータ規模、回復率、検出誤差の数値はない。
- Novelty: 非定常性を単に障害とせず、局所的な機構変化を因果方向の情報源として利用した。
- Limitations: 編者の注意: 局所的に変わるという仮定と変化点検出の正しさに依存する。等価クラスの出力は一意な真のDAGの同定とは限らない。

### Paper: Distributionally Robust Logistic Regression
- Source: arXiv
- Canonical ID: arxiv:1509.09259
- Publication date: 2015-09-30
- URL: https://arxiv.org/abs/1509.09259
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Wasserstein球内の最悪loglossを最小化し、通常・正則化ロジスティック回帰を包含するDRO。
- Objective: 経験分布の近傍にある未知の真分布へ、過度に楽観的でない分類器を学ぶ。
- Methods: 学習標本の一様経験分布の周囲にWasserstein球を構成。最悪期待損失を計算可能な形へ変換し、誤分類確率の上下界も2つの線形計画で求める。
- Data and results: 適切な半径の下で分布外保証と扱いやすい定式化を示し、人工・実データで検証。要旨に精度や区間幅の具体値はない。
- Novelty: 分布の距離による不確かさと正則化を結び、推定・評価に共通する頑健な枠組みを示した。
- Limitations: 編者の注意: 真分布を高確率で含む保証は半径の適切な選択に依存する。球の外の変化を保証せず、頑健性と保守的な予測の交換関係がある。

### Paper: Estimation and Inference of Heterogeneous Treatment Effects using Random Forests
- Source: arXiv
- Canonical ID: arxiv:1510.04342
- Publication date: 2015-10-14
- URL: https://arxiv.org/abs/1510.04342
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: causal forestはランダムフォレストを異質な処置効果へ拡張し、推定と信頼区間の理論を示す。
- Objective: 個別化医療などで、平均だけでなく共変量による効果の違いを柔軟に推定する。
- Methods: 非交絡性を置くpotential outcomesの下で因果森を構成。点ごとの一致性、中心化した漸近Gaussian分布、分散と区間推定を解析した。
- Data and results: 理論条件下の推論を示し、実験では特に無関係な共変量がある場合に近傍matchingより強い結果を報告。要旨に効果誤差や人数の数値はない。
- Novelty: 森を柔軟な予測器として使うだけでなく、異質効果に対する統計的な推論保証を整えた。
- Limitations: 編者の注意: 非交絡性・重なり・森の構成などの仮定が必要。条件付き平均効果の推定を、個人の観測できない両方の転帰の確定予測と解釈しない。

### Paper: Private Causal Inference
- Source: arXiv
- Canonical ID: arxiv:1512.05469
- Publication date: 2015-12-17
- URL: https://arxiv.org/abs/1512.05469
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Private Causal Inferenceは加法ノイズモデルによる因果方向推定へ、差分プライバシーを組み込む。
- Objective: 医療などの機密性の高い個人データを保護しながら、因果関係を推定する。
- Methods: additive noise modelの複数の変種に対し、利用者の差分プライバシーを満たす枠組みを構築し、実験で実装可能性を調べた。
- Data and results: 複数のANMにDP保証を与え、実用的で実装しやすいと報告。要旨にプライバシー予算、データ規模、方向判定精度の値はない。
- Novelty: 予測や統計量に限られていた個人情報保護を、因果方向の学習へ展開した。
- Limitations: 編者の注意: DP保証は因果推定の正しさを保証しない。方向の識別にはANMの仮定、保護には予算・隣接関係・実装条件が必要である。

### Paper: XGBoost: A Scalable Tree Boosting System
- Source: arXiv
- Canonical ID: arxiv:1603.02754
- Publication date: 2016-03-09
- URL: https://arxiv.org/abs/1603.02754
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: XGBoostは木のブースティングを、疎なデータと大規模計算に適した実装へ統合した。
- Objective: 高精度な木モデルを、限られた計算資源でも大きなデータへ拡張する。
- Methods: 疎性を考慮した学習、近似木学習用のweighted quantile sketch、キャッシュアクセス、圧縮、データ分割を組み合わせた。
- Data and results: 既存システムより少ない資源で数十億例を超える規模に拡張したと報告。要旨に課題別精度、実行時間、比較の具体倍率はない。
- Novelty: 予測アルゴリズムとメモリ・分散処理の設計を一体化し、表形式予測の強い実用基準を作った。
- Limitations: 編者の注意: スケーラビリティと予測精度は別の指標である。要旨の資源優位を任意のハードウェア・データへ一般化せず、調整予算も揃えて比較する。

### Paper: Learning Representations for Counterfactual Inference
- Source: arXiv
- Canonical ID: arxiv:1605.03661
- Publication date: 2016-05-12
- URL: https://arxiv.org/abs/1605.03661
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 反事実推論をdomain adaptationとして捉え、処置群間で利用できる表現を学ぶ枠組み。
- Objective: 観測データから、同じ人が別の処置を受けた場合の結果を推定する。
- Methods: 領域適応と深層表現学習を統合した因果推論法を提案し、理論的根拠と先行する観測研究向け手法との実験比較を行った。
- Data and results: 比較した最良の先行法を有意に上回ったと報告。要旨にデータ名、反事実誤差の具体値や識別仮定の詳細はない。
- Novelty: 処置選択による群間分布差を、転移・領域適応の問題として表現学習へ接続した。
- Limitations: 編者の注意: 実観測では個人の反事実を同時に確認できない。表現を揃えることだけで未測定交絡や重なり不足を解消したとは言えず、評価データの作り方が重要。

### Paper: Unsupervised Feature Extraction by Time-Contrastive Learning and Nonlinear ICA
- Source: arXiv
- Canonical ID: arxiv:1605.06336
- Publication date: 2016-05-20
- URL: https://arxiv.org/abs/1605.06336
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TCLは時間区間を識別する表現を学び、非定常性を利用して非線形ICAの識別を可能にする。
- Objective: 一般には一意に決まらない非線形の独立成分を、ラベルなし系列から復元する。
- Methods: 時間窓を最適に判別する深層表現を学習し、linear ICAと組み合わせる。時間的に変化するsourceを持つ非線形ICAとして理論解析した。
- Data and results: モデル仮定の下で、sourceごとの点変換まで非線形ICAを一意に推定できると証明。要旨に実験スコアはない。
- Novelty: 非定常性を扱いにくさではなく識別のための追加情報にし、教師なし表現へ構成的な理論を与えた。
- Limitations: 編者の注意: 非定常な生成機構などの条件付き結果で、任意データの一意分解ではない。sourceごとの変換の曖昧さが残り、因果構造の完全同定とも異なる。

### Paper: Recurrent Neural Networks for Multivariate Time Series with Missing Values
- Source: arXiv
- Canonical ID: arxiv:1606.01865
- Publication date: 2016-06-06
- URL: https://arxiv.org/abs/1606.01865
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: GRU-Dは値だけでなく欠損マスクと観測間隔を使い、欠け方自体が持つ予測情報を学ぶ。
- Objective: 臨床などで予測対象と関連するinformative missingnessを、単なる穴埋めで捨てず利用する。
- Methods: GRUへ観測のmaskと時間間隔の2表現を組み込み、長期依存と欠損パターンを統合。MIMIC-III、PhysioNet、人工系列の分類で評価した。
- Data and results: 実臨床と人工データの時系列分類で最良水準を報告。要旨に患者数、AUC、補完誤差の数値はない。
- Novelty: 補完後の値だけを入力する手法から、測定されなかった事実と経過時間も表現するモデルへ進めた。
- Limitations: 編者の注意: 欠損は測定方針を反映するため、施設や運用が変わると有益な相関が崩れ得る。分類性能の改善と、真の欠損値の正確な復元は異なる。

### Paper: Ancestral Causal Inference
- Source: arXiv
- Canonical ID: arxiv:1606.07035
- Publication date: 2016-06-22
- URL: https://arxiv.org/abs/1606.07035
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Ancestral Causal Inferenceは粗い祖先関係を扱い、独立性検定に基づく因果探索を効率化する。
- Objective: 有限データで曖昧な独立性検定が多いとき、信頼できる因果予測と計算可能性を得る。
- Methods: より粗い因果情報表現で探索空間を減らし、予測のconfidenceを採点。観測・介入データと背景知識を組み合わせ、健全性・漸近一致性を証明した。
- Data and results: 人工データで既存法を上回り、数桁の高速化を報告。難しいタンパク質データへの適用も示すが、要旨に精度値・対象数はない。
- Novelty: 辺の細部をすべて列挙するより粗い表現と、利用可能な複数種の因果証拠を統合した。
- Limitations: 編者の注意: 理論保証には検定や生成過程の仮定を要する。有限標本のconfidenceと因果の確実性は同じでなく、背景知識が誤る場合の影響も残る。

### Paper: Double/Debiased Machine Learning for Treatment and Structural Parameters
- Source: arXiv
- Canonical ID: arxiv:1608.00060
- Publication date: 2016-07-30
- URL: https://arxiv.org/abs/1608.00060
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: DMLは補助予測の正則化バイアスを抑え、低次元の効果・構造パラメータの推論を行う。
- Objective: 予測精度の高い機械学習を、そのまま因果パラメータへ代入すると推定が歪む問題に対処する。
- Methods: Neyman直交スコアで補助推定誤差への感度を抑え、cross-fittingで過学習を分離。部分線形モデル、ATE・ATTE、操作変数の推定などへ適用する。
- Data and results: 必要な正則条件下でroot-N一致性・漸近正規性と信頼区間の妥当性を導く。確認した改訂版では3つの実証例も扱う。
- Novelty: 予測器の性能と対象効果の推論を分け、広い機械学習法を補助推定へ使う共通手順を示した。
- Limitations: ATEの因果解釈には非交絡性と傾向スコアの重なり等を要する。著者は非交絡性なしでは関連効果にとどまると明記。直交化も未測定交絡や弱い識別を解決しない。

本文の照合箇所: [v7（2024-11-03）の表題、Introduction、Section 5.1とAssumption 5.1・脚注10。公開日は初回提出2016年を保持](https://arxiv.org/pdf/1608.00060v7)。

### Paper: Generalized Random Forests
- Source: arXiv
- Canonical ID: arxiv:1610.01271
- Publication date: 2016-10-05
- URL: https://arxiv.org/abs/1610.01271
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Generalized Random Forestsは局所モーメント条件で定まる量を、森の適応的な重みで推定する。
- Objective: 平均予測を超え、分位点や異質な効果などを非パラメトリックに推定・推論する。
- Methods: 対象量の異質性に合わせて森を成長させ、近い標本の重みを得る。一致性・漸近正規性と分散推定を導き、分位点、平均偏効果、操作変数による処置効果へ適用した。
- Data and results: 仮定下で信頼区間を構成できる大標本理論と、R/C++の実装を提供。要旨に実験データの人数や誤差の具体値はない。
- Novelty: 回帰森を、局所方程式で識別される多様な統計量の共通推定器へ一般化した。
- Limitations: 編者の注意: 信頼区間の妥当性は理論条件を要し、有限標本で自動保証されない。IVによる因果効果には操作変数の有効性など、森では解決できない識別仮定も必要。

### Paper: Entropic Causal Inference
- Source: arXiv
- Canonical ID: arxiv:1611.04035
- Publication date: 2016-11-12
- URL: https://arxiv.org/abs/1611.04035
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Entropic Causal Inferenceは外生ノイズの単純さを仮定し、離散変数の因果方向を選ぶ。
- Objective: 加法や数値の大小関係を要求せず、順序・カテゴリデータの方向を推定する。
- Methods: 一般の関数モデルで外生変数の単純さをRényi entropyで測る。最小entropy couplingとの等価性と計算困難性を示し、Shannon entropy向け貪欲法を提案した。
- Data and results: 仮定下で真方向の低H0は逆方向の高H0を伴うと証明。n=2で貪欲法の局所最適性を示し、実データでANMの最良水準に近い性能だった。
- Novelty: 関数形を狭める代わりに、外生変数の情報量へ非対称性の仮定を置いた。
- Limitations: 編者の注意: 真方向のノイズが単純という仮定が根幹で、観測分布だけから無仮定で方向が決まるわけではない。局所最適性と大域最適性も異なる。

### Paper: Counterfactual Prediction with Deep Instrumental Variables Networks
- Source: arXiv
- Canonical ID: arxiv:1612.09596
- Publication date: 2016-12-30
- URL: https://arxiv.org/abs/1612.09596
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Deep IVは操作変数による因果推定を、処置分布と結果の2つの深層予測課題へ分解する。
- Objective: 柔軟な機械学習を使いながら、単純な観測相関でない効果の推定を行う。
- Methods: 第1段で処置の条件付き分布を推定し、第2段の結果モデルの損失にその分布上の積分を入れる。SGD、標本外検証、dropoutと分割による推論も設計した。
- Data and results: 既存MLを大きく作り変えずに使うIV枠組みと、Bayes・頻度論の推論手順を提示。要旨に実証効果量や予測誤差はない。
- Novelty: 操作変数の構造を保ちながら、2段階推定を非線形なニューラル予測へ一般化した。
- Limitations: 編者の注意: 操作変数の関連性・外生性・排除制約などが必要で、ネットワークが有効なIVを自動生成するわけではない。予測精度だけで識別の強さは分からない。

### Paper: Double/Debiased/Neyman Machine Learning of Treatment Effects
- Source: arXiv
- Canonical ID: arxiv:1701.08687
- Publication date: 2017-01-30
- URL: https://arxiv.org/abs/1701.08687
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: DMLの短い解説として、観測データのATE・ATTEへ直交スコアとcross-fittingを適用する。
- Objective: 高次元の補助モデルを機械学習しても、平均処置効果の推論を妥当に行う方法を示す。
- Methods: 一般的なdouble/debiased MLの枠組みを、平均処置効果と処置群平均効果へ具体化。Neyman直交スコアと標本の分割・交差利用で補助推定の影響を抑える。
- Data and results: 観測研究のATE・ATTEに使う方法を例示するノート。要旨に実証データの人数、効果量、検証スコアはない。
- Novelty: 一般DML理論を、処置効果推定で使える具体的な応用として整理した。
- Limitations: 編者の注意: 機械学習の予測誤差を抑えても未測定交絡は自動解消しない。包括的なDML論文とは別の短い応用解説で、独立の臨床効果証拠ではない。

### Paper: Causal Discovery Using Proxy Variables
- Source: arXiv
- Canonical ID: arxiv:1702.07306
- Publication date: 2017-02-23
- URL: https://arxiv.org/abs/1702.07306
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 静的な2対象からproxy確率変数を作り、その因果方向を推定する枠組み。
- Objective: 写真と加工版など、通常の反復観測を持たない対象間の方向関係を調べる。
- Methods: 静的なx・yから確率変数A・Bを構成し、観測因果探索を適用。写真加工、動画フレームの時間順序、人が因果関係を付けた1万の単語対で検証した。
- Data and results: 単語対の因果関係の75%を発見したと報告し、画像やフレーム順序にも実例を示した。要旨に課題別の詳細指標はない。
- Novelty: 固定した対象の知識をproxy変数へ写し、確率分布を前提とする探索法に接続した。
- Limitations: 編者の注意: ここでのproxyは未観測交絡の代理測定とは用途が異なる。proxy間の方向が元対象の因果を表すかは構成仮定と人のラベルに依存する。

### Paper: DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks
- Source: arXiv
- Canonical ID: arxiv:1704.04110
- Publication date: 2017-04-13
- URL: https://arxiv.org/abs/1704.04110
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: DeepARは関連する多数の系列を共同学習し、将来値の分布を出す自己回帰RNN予測法。
- Objective: 需要などの予測で、点予測だけでなく不確実性を含む将来分布を得る。
- Methods: 多くの関連時系列上で自己回帰のrecurrent networkを学習し、各系列の履歴から確率予測を生成。複数の実世界予測データで比較した。
- Data and results: 最良の既存法に対し約15%の精度改善を報告。要旨にデータ数、誤差指標の絶対値や区間校正の結果はない。
- Novelty: 系列ごとに個別モデルを作る方法から、関連系列間で情報を共有する確率的なglobalモデルへ進めた。
- Limitations: 編者の注意: 関連系列を共有学習する設定であり、未知の任意分野へのzero-shot基盤モデルではない。分布を出すことと予測区間が正しく校正されることは別である。

### Paper: Causal Effect Inference with Deep Latent-Variable Models
- Source: arXiv
- Canonical ID: arxiv:1705.08821
- Publication date: 2017-05-24
- URL: https://arxiv.org/abs/1705.08821
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: CEVAEは交絡因子の不完全な代理測定から、潜在変数と個別処置効果を同時に学ぶ。
- Objective: 全交絡因子を直接観測できない状況で、ノイズのあるproxy情報を因果推論に利用する。
- Methods: proxyを含む因果構造に沿ったVAEを作り、未知の交絡を表す潜在空間と処置・結果の関係を同時推定。個別効果の既存ベンチマークで比較した。
- Data and results: 比較法より頑健で、従来の個別効果ベンチマークでは最良水準に匹敵と報告。要旨に標本数や効果推定誤差はない。
- Novelty: 未測定交絡を単に無視せず、代理観測を使う潜在生成モデルとして表現した。
- Limitations: 編者の注意: 潜在変数を置くだけで因果効果が識別されるわけではない。proxyの情報量、因果構造・分布の仮定に依存し、任意の未測定交絡を解消する保証はない。

### Paper: CatBoost: unbiased boosting with categorical features
- Source: arXiv
- Canonical ID: arxiv:1706.09516
- Publication date: 2017-06-28
- URL: https://arxiv.org/abs/1706.09516
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: CatBoostはordered boostingとカテゴリ処理で、目的変数の漏洩による予測のずれを抑える。
- Objective: 既存のブースティングで生じるtarget leakageの一形態を分析し、精度を改善する。
- Methods: 順列に基づくordered boostingと新しいカテゴリ特徴処理を組み合わせ、prediction shiftを理論的に分析。複数データで既存実装と比較した。
- Data and results: 提案手順が問題を効果的に抑え、多様なデータで公開boosting実装より良好な品質を報告。要旨にデータ数や改善値はない。
- Novelty: モデルの表現力だけでなく、学習時の目的情報の使い方が作る分布のずれへ対処した。
- Limitations: 編者の注意: 題名のunbiasedは対象とする予測シフトの文脈であり、一般的な因果推定の無偏性ではない。データ漏洩全般や、どんな前処理でも安全である保証でもない。

### Paper: DAGs with NO TEARS: Continuous Optimization for Structure Learning
- Source: arXiv
- Canonical ID: arxiv:1803.01422
- Publication date: 2018-03-04
- URL: https://arxiv.org/abs/1803.01422
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: NOTEARSはDAGの非巡回性を滑らかな等式で表し、構造学習を連続最適化へ変換する。
- Objective: 超指数的なグラフ空間の組合せ探索を避け、汎用の数値最適化で構造を学ぶ。
- Methods: 行列指数を使うh(W)=tr(exp(W∘W))−d=0が非巡回性と同値と示し、拡張Lagrangianで解く。最後に小さな重みを閾値処理する。
- Data and results: 厳密で微分可能な非巡回条件を証明し、比較法より良好な構造推定を報告。数値解は大域最適解ではなく停留点として求める。
- Novelty: 非巡回制約を局所的なグラフ操作から、全重みを同時更新できる滑らかな等式へ置き換えた。
- Limitations: 著者は非凸性、滑らかなスコアの必要性、行列指数のO(d³)費用を指摘。編者の注意: 最適化上の非巡回性は、観測データからの因果方向の識別保証とは異なる。

本文の照合箇所: [Theorem 1、Section 4、Discussionの非凸性・計算量](https://proceedings.neurips.cc/paper_files/paper/2018/file/e347c51419ffb23ca3fd5050202f9c3d-Paper.pdf)。

### Paper: BRITS: Bidirectional Recurrent Imputation for Time Series
- Source: arXiv
- Canonical ID: arxiv:1805.10572
- Publication date: 2018-05-27
- URL: https://arxiv.org/abs/1805.10572
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: BRITSは補完値を双方向RNNの計算グラフ内の変数として扱い、下流課題と同時に更新する。
- Objective: 相関する多変量系列の欠損を、線形な動態や単純な平滑化へ限定せず推定する。
- Methods: 前後の再帰から遅延勾配と整合性制約を与え、欠損値もbackpropagationで更新。分類・回帰を同じグラフで共同学習する。
- Data and results: 空気質、医療、人活動の位置情報という3実データで、補完と分類・回帰の双方で比較法を上回った。要旨に具体的な誤差値はない。
- Novelty: 一度補った値を定数にせず、前後の観測と下流の教師信号から修正できるようにした。
- Limitations: 編者の注意: 双方向の補完は後の観測を使える設定で、未来を使えない実時間予測と同一条件ではない。特定の線形仮定を不要にしても、任意の欠損機構での正しさは保証しない。

本文の照合箇所: [Introductionの技術的貢献、Sections 3–4.1の欠損値・遅延勾配の定義。欠けた要旨文を原著で確認](https://arxiv.org/pdf/1805.10572v1)。

### Paper: Wasserstein Distributionally Robust Kalman Filtering
- Source: arXiv
- Canonical ID: arxiv:1809.08830
- Publication date: 2018-09-24
- URL: https://arxiv.org/abs/1809.08830
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 正規分布だけを含むWasserstein集合で最悪推定誤差を抑え、頑健なKalman filterを構成する。
- Objective: 状態推定で仮定した分布がずれるモデルリスクへ対処する。
- Methods: 非凸なWasserstein曖昧集合上の平均二乗誤差推定を、凸計画へ等価変換。推定器と最悪分布のNash均衡を示し、準閉形式の方向探索を持つFrank–Wolfe法を導入した。
- Data and results: 扱いやすい凸定式化と、これを基礎にした分布頑健Kalman filterを提示。要旨に追跡誤差や速度の具体値はない。
- Novelty: 分布のずれを最悪条件で扱う推定問題を、逐次状態推定へ組み込んだ。
- Limitations: 編者の注意: 曖昧集合は正規分布へ限定され、任意の非Gaussian外れ値への保証ではない。集合の半径やモデル化した不確かさの選択に依存する。

### Paper: Synthesizing Tabular Data using Generative Adversarial Networks
- Source: arXiv
- Canonical ID: arxiv:1811.11264
- Publication date: 2018-11-27
- URL: https://arxiv.org/abs/1811.11264
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TGANは離散・連続列を同時生成するGANを、医療・教育などの表データへ適用した。
- Objective: 実データの列間関係を保つ、完全に合成された表を生成する。
- Methods: 表分布をGANで暗黙に学び、離散と連続の変数を併せてサンプル。3データセットで従来の統計的生成モデルと比較した。
- Data and results: 列間の相関保持と大きなデータへの拡張で統計的比較法を上回ったと報告。要旨に忠実度・下流効用・速度の具体値はない。
- Novelty: 画像用の敵対的生成を、混合型の表の分布・列間依存の学習へ展開した。
- Limitations: 編者の注意: このTGANと後続のCTGANは別論文・別手法。合成であること自体は個人情報の非漏洩を保証せず、3データでの相関評価だけでは全統計量の保存を示せない。

### Paper: Causal Discovery with a Mixture of DAGs
- Source: arXiv
- Canonical ID: arxiv:1901.09475
- Publication date: 2019-01-28
- URL: https://arxiv.org/abs/1901.09475
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 時間・集団で異なるDAGの混合から、因果関係を要約するグラフを推定する枠組み。
- Objective: 固定DAGでは扱いにくいフィードバックや、時間・集団で変わる過程を表現する。
- Methods: 各時点は非巡回でも時間でDAGが変わるモデルを使い、縦断データへCausal Inference over Mixturesを適用。循環を複数時点のDAGへ分けて考える。
- Data and results: 実・人工データで従来法より良い成績を報告。確認したv2は理論・CIM・評価指標を改良した版で、要旨に性能の具体値はない。
- Novelty: 単一の安定したグラフを仮定せず、複数機構の混合として因果過程を扱った。
- Limitations: 要旨の『directed cyclic graphs (DAGs)』は本文の非巡回定義に従って整理。編者の注意: 出力は混合関係の要約で、全時点の完全な機構を一意に回復する意味ではない。

本文の照合箇所: [v2（2020-09-05）のIntroduction・Fig.1、DAG混合の定義と改訂内容](https://arxiv.org/pdf/1901.09475v2)。

### Paper: DAG-GNN: DAG Structure Learning with Graph Neural Networks
- Source: arXiv
- Canonical ID: arxiv:1904.10098
- Publication date: 2019-04-22
- URL: https://arxiv.org/abs/1904.10098
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: DAG-GNNは連続的な非巡回制約とグラフVAEを組み合わせ、非線形の構造学習を行う。
- Objective: NOTEARSの線形SEMと二乗損失を超え、離散・ベクトル変数も扱う。
- Methods: graph neural networkでパラメータ化するVAEへ、非巡回性を表す構造制約の変種を導入。非線形人工データと離散変数の基準で評価した。
- Data and results: 非線形生成データでより正確なグラフを得て、離散基準では大域最適に近い結果を報告。要旨に辺誤差や対象ノード数はない。
- Novelty: 微分可能なDAG制約を、より柔軟な深層生成モデルへ組み込み、変数型の範囲も広げた。
- Limitations: 編者の注意: よい観測適合や非巡回性だけでは真の因果方向を識別できない。非凸最適化、潜在交絡、生成モデルの仮定に関する条件を分けて確認する。

### Paper: N-BEATS: Neural basis expansion analysis for interpretable time series forecasting
- Source: arXiv
- Canonical ID: arxiv:1905.10437
- Publication date: 2019-05-24
- URL: https://arxiv.org/abs/1905.10437
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: N-BEATSは深い全結合層と前後の残差構造で、単変量の点予測を行う。
- Objective: 領域別の複雑な専用部品に頼らず、幅広い系列を同じ構造で高精度に予測する。
- Methods: backward・forward residual linkを持つ深いブロックを積層。汎用構成と解釈可能な構成をM3、M4、TOURISMで比較した。
- Data and results: 対象競技データで両構成が最良水準。要旨は統計基準比11%、当時のM4優勝法比3%の精度改善を報告し、解釈構成でも大きな性能低下を避けた。
- Novelty: 時系列固有の部品なしの基本構成でも強い予測を得られ、必要に応じて解釈可能な出力を加える設計を示した。
- Limitations: 編者の注意: 単変量・点予測の対象で、多変量依存や確率校正を実証する結果ではない。改善率は原著の比較条件に限り、絶対ポイントに変換しない。

### Paper: Adapting Neural Networks for the Estimation of Treatment Effects
- Source: arXiv
- Canonical ID: arxiv:1906.02120
- Publication date: 2019-06-05
- URL: https://arxiv.org/abs/1906.02120
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Dragonnetは傾向スコアを意識した構造とtargeted regularizationで処置効果の推定を改善する。
- Objective: 補助的な予測モデルの精度だけでなく、最終的な効果推定の質へニューラル学習を合わせる。
- Methods: 結果予測と処置確率のモデル設計を適応し、傾向スコアの調整上の十分性を使う構造を導入。推論上よい性質を持つ方向へtargeted regularizationで学習を誘導した。
- Data and results: 因果推論の基準データで比較法を上回ったと報告。要旨にデータ名や効果推定誤差、標本数はない。
- Novelty: 一般的な予測器を後で推定式へ入れるだけでなく、効果推定の統計的目的を補助モデルの学習へ反映した。
- Limitations: 編者の注意: 漸近的によい性質へ誘導することは、有限データでの無偏性や識別保証ではない。交絡調整と処置の重なりの仮定が別途必要。

### Paper: Causal Discovery with Reinforcement Learning
- Source: arXiv
- Canonical ID: arxiv:1906.04477
- Publication date: 2019-06-11
- URL: https://arxiv.org/abs/1906.04477
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 強化学習を探索手段として使い、観測データに合う高スコアのDAGを探す。
- Objective: 局所ヒューリスティックに依存する構造探索の実用性能を改善する。
- Methods: encoder–decoderが隣接行列を生成し、事前定義スコアと2つの非巡回ペナルティで報酬化。学習中に出た最良報酬のグラフを最終出力する。
- Data and results: 人工・実データで探索能力の改善と柔軟なスコア利用を示した。要旨にグラフ数や構造誤差・実行時間の絶対値はない。
- Novelty: 新環境で使う方策を得る通常のRLと異なり、候補グラフの組合せ探索を目的にRLを利用した。
- Limitations: 編者の注意: 高いスコアのグラフが真の因果構造とは限らず、スコアと識別仮定に依存する。非巡回ペナルティや探索の計算量も含めた評価が必要。

### Paper: Distributionally Robust Counterfactual Risk Minimization
- Source: arXiv
- Canonical ID: arxiv:1906.06211
- Publication date: 2019-06-14
- URL: https://arxiv.org/abs/1906.06211
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: DROの視点で反事実リスク最小化を統一し、KL divergenceによる頑健な目的を導く。
- Objective: ログから意思決定を評価・改善する際の、不確かなリスク推定を原理的に扱う。
- Methods: CRMの標本分散penaltyを一般DROの一例として整理し、距離・divergenceで不確かさを表現。KLを使う新しい目的関数を4基準データで比較した。
- Data and results: 既存最良法を上回り、別の不確かさ尺度が有用なことを示した。要旨に各データ名、リスクや改善率はない。
- Novelty: 既存の反事実評価のpenaltyを分布の頑健化として捉え、異なる不確かさ設計を比較可能にした。
- Limitations: 編者の注意: DROはログの支持不足や誤った処置確率を自動解消しない。反事実的な政策リスク評価を、個人の因果効果の無仮定推定と混同しない。

### Paper: Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting
- Source: arXiv
- Canonical ID: arxiv:1907.00235
- Publication date: 2019-06-29
- URL: https://arxiv.org/abs/1907.00235
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: LogSparse Transformerは局所文脈を畳み込みで補い、長い系列のattentionのメモリ負担を減らす。
- Objective: 通常Transformerの局所性の弱さと、系列長の2乗に増えるメモリを改善する。
- Methods: causal convolutionでquery・keyを生成し、LogSparseな接続で長期関係を扱う。人工・実世界の予測データで比較した。
- Data and results: O(L(log L)²)のメモリ費用を示し、限られたメモリ下で細粒度・長期依存の系列を良好に予測。要旨に誤差・実測速度の値はない。
- Novelty: 各時点独立のattention入力へ局所文脈を加え、疎な長期接続と組み合わせた。
- Limitations: 編者の注意: 漸近的なメモリ量は実測の実行速度と同じではない。疎な接続が拾いにくい依存や、非周期的な変化の性能は別に確認が必要。

### Paper: Modeling Tabular data using Conditional GAN
- Source: arXiv
- Canonical ID: arxiv:1907.00503
- Publication date: 2019-07-01
- URL: https://arxiv.org/abs/1907.00503
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: CTGANは多峰な連続変数と不均衡なカテゴリを扱う、条件付きの表生成モデル。
- Objective: 混合型の表に特有の分布を保つ合成データを生成する。
- Methods: mode-specific normalization、条件付き生成、training-by-samplingを組み合わせ、7人工・8実データでBayesネットワークやGANを比較した。正式版の名称CTGANを使用する。
- Data and results: Table 1では8実データ中、CLBNに対して7、PrivBNに対して8データで優位。尤度適合と合成データの学習効用を使う共通基盤も公開した。
- Novelty: 画像用GANの単純転用を超え、列ごとの多峰性と希少カテゴリへの学習偏りへ対処した。
- Limitations: 編者の注意: 下流学習で有用な合成表でも、全ての依存関係や個人の秘密を保護する保証はない。比較で勝つデータ数と改善幅は異なる。

本文の照合箇所: [Introduction・Table 1、正式版のモデル名と設計の要点](https://proceedings.neurips.cc/paper_files/paper/2019/file/254ed7d2de3b23ab10936522dd547b78-Paper.pdf)。

### Paper: Invariant Risk Minimization
- Source: arXiv
- Canonical ID: arxiv:1907.02893
- Publication date: 2019-07-05
- URL: https://arxiv.org/abs/1907.02893
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: IRMは複数の訓練環境で同じ最適分類器を持つ表現を学び、分布外予測を狙う。
- Objective: 環境に固有の相関に頼らず、複数の分布で安定した予測関係を得る。
- Methods: 表現上の最適分類器が全訓練分布で一致するようリスク最小化を構成。理論と実験で不変性、因果構造、OOD汎化の関係を検討した。
- Data and results: 不変性を学ぶ枠組みと、その条件下での分布外汎化の根拠を示した。要旨に課題数や具体的精度はない。
- Novelty: 単一分布の平均誤差最小化から、環境間で予測則が共通であるという学習目標へ進めた。
- Limitations: 編者の注意: 観測した環境間の不変性が任意の未知環境へ続くとは限らない。理想の目的と実用的な近似を区別し、後続の失敗例・比較研究と併読する。

### Paper: Variational Autoencoders and Nonlinear ICA: A Unifying Framework
- Source: arXiv
- Canonical ID: arxiv:1907.04809
- Publication date: 2019-07-10
- URL: https://arxiv.org/abs/1907.04809
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 補助観測に条件付けた潜在事前分布で、VAEと非線形ICAの識別理論を統合する。
- Objective: 観測分布へよく合うだけでなく、真の潜在変数とのjointも推定できる条件を得る。
- Methods: 追加の観測変数に条件付けてfactorizeする潜在事前分布を仮定。ノイズ・低次元潜在・離散観測も含め、非線形ICAを最尤学習の枠組みへ広げた。
- Data and results: 広い深層潜在モデルで、単純な変換までjointを識別できる理論を示した。識別可能なflowも特殊例となるが、要旨に数値実験結果はない。
- Novelty: 無条件のVAEでは解消しない非識別性を、観測された補助情報と条件付き潜在独立性で扱った。
- Limitations: 編者の注意: 任意のVAEで自動的にdisentanglementを保証する結果ではない。補助変数・分布族・識別の条件と、残る変換の曖昧さがある。

### Paper: Distributionally Robust Optimization: A Review
- Source: arXiv
- Canonical ID: arxiv:1908.05659
- Publication date: 2019-08-13
- URL: https://arxiv.org/abs/1908.05659
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: DROの主要概念を、頑健最適化・リスク回避・機会制約・正則化との関係から整理したレビュー。
- Objective: operations researchと統計学習の双方で発展した分布頑健最適化の関係を見通す。
- Methods: DROの主要な概念と研究貢献を文献横断で概説し、関連する最適化・統計学習の枠組みとのつながりを説明する。
- Data and results: 分布に関する不確かさを扱うDROの概念地図を提供。要旨に新しいデータセットや統合性能値はなく、文献レビューである。
- Novelty: 個別の不確かさモデルを並べるだけでなく、リスク・制約・正則化の見方を統合して整理した。
- Limitations: 編者の注意: 同じデータで全手法を比較した実証研究ではない。対象文献の範囲と以後の研究を区別し、個別保証は各手法の仮定まで確認する必要がある。

### Paper: TabNet: Attentive Interpretable Tabular Learning
- Source: arXiv
- Canonical ID: arxiv:1908.07442
- Publication date: 2019-08-20
- URL: https://arxiv.org/abs/1908.07442
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TabNetは判断ステップごとに特徴を選ぶattentionで、表形式予測と特徴寄与を扱う。
- Objective: 重要な変数へ学習能力を集中し、精度と解釈可能性を両立する。
- Methods: 逐次的なattentionで各判断の入力特徴を選び、局所・全体の特徴寄与を示す。未ラベルが豊富な場合の自己教師あり表現学習も評価した。
- Data and results: 性能が飽和していない複数表データで比較ニューラル法・木の変種を上回り、自己教師あり学習も改善したと報告。要旨にデータ数と絶対スコアはない。
- Novelty: 表データ専用の段階的な特徴選択と、未ラベルデータからの学習を一つの構造へ統合した。
- Limitations: 編者の注意: 選定ベンチマークの結果をすべての木モデルへの優越性としない。attentionによる特徴寄与は、変数の因果効果を示す説明ではない。

### Paper: Distributionally Robust Language Modeling
- Source: arXiv
- Canonical ID: arxiv:1909.02060
- Publication date: 2019-09-04
- URL: https://arxiv.org/abs/1909.02060
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: topic CVaRは話題の最悪混合を考えるDROで、未知の話題分布への言語モデルの頑健性を狙う。
- Objective: 訓練に無関係な文章を加えると、対象分布の性能が下がるMLEの問題を減らす。
- Methods: 訓練と十分に重なる話題混合のうち、最悪の損失を小さくする分布頑健目的を導出。Yelpレビューとニュースの混合学習を評価した。
- Data and results: レビューだけのテストで、MLEよりperplexityを5.5低減した。これは5.5ポイントのperplexity差で、5.5%という表記ではない。
- Novelty: 平均的な訓練話題の損失だけでなく、未知の話題配分に対する最悪条件を学習へ組み込んだ。
- Limitations: 編者の注意: 想定する話題混合と訓練の重なりの範囲内を扱い、完全に新しい意味・言語への保証ではない。perplexity改善と下流の意思決定の利益は異なる。

### Paper: InceptionTime: Finding AlexNet for Time Series Classification
- Source: arXiv
- Canonical ID: arxiv:1909.04939
- Publication date: 2019-09-11
- URL: https://arxiv.org/abs/1909.04939
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: InceptionTimeはInception型CNNの集合で、高精度な系列分類を大きいデータへ拡張する。
- Objective: 高精度だが計算の重いHIVE-COTEに近い分類を、実務で使える学習時間で得る。
- Methods: Inception-v4に着想を得た深いCNNをアンサンブルし、精度と訓練のスケーラビリティを比較した。
- Data and results: HIVE-COTEに匹敵するaccuracyを報告。1,500系列を1時間、800万系列を13時間で学習し、比較法では難しい規模を扱った。
- Novelty: 系列分類の精度と大規模化を両立する、畳み込み系の強い公開基準を示した。
- Limitations: 編者の注意: 時間は当時の測定環境・並列化条件に依存し、accuracyの一致を全データの同点と解釈しない。分類以外の用途や分布変化は別評価が必要。

### Paper: Neural Oblivious Decision Ensembles for Deep Learning on Tabular Data
- Source: arXiv
- Canonical ID: arxiv:1909.06312
- Publication date: 2019-09-13
- URL: https://arxiv.org/abs/1909.06312
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: NODEはoblivious decision treeのアンサンブルを、多層で勾配学習できる構造へ拡張した。
- Objective: 表データで強い木の性質と、深層学習のend-to-end最適化・階層表現を組み合わせる。
- Methods: Neural Oblivious Decision Ensemblesを設計し、多数の表データで主要GBDT実装と比較。PyTorch実装を公開した。
- Data and results: 多くの比較課題で競合法を上回ったと報告。要旨にデータ数、平均改善量、探索・計算予算は記載されない。
- Novelty: 木とニューラルモデルを別々に使う代わりに、木のアンサンブルを深い微分可能なモデルへ一般化した。
- Limitations: 編者の注意: 『多くの課題』はすべての表への優越性ではない。調整の費用、特徴の型、学習データ量を揃えた比較が必要である。

### Paper: ROCKET: Exceptionally fast and accurate time series classification using random convolutional kernels
- Source: arXiv
- Canonical ID: arxiv:1910.13051
- Publication date: 2019-10-29
- URL: https://arxiv.org/abs/1910.13051
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: ROCKETはランダム畳み込みの特徴と単純な線形分類器で、高速な系列分類を行う。
- Objective: 強い分類法が小データでも長い訓練を要する問題を、低費用の変換で改善する。
- Methods: ランダムなconvolutional kernelで系列を特徴化し、その変換上で線形分類器を学習。形状だけ・周波数だけの専用特徴に限定しない構成を評価した。
- Data and results: 既存最良水準のaccuracyを、計算費用の小さな一部で得たと報告。要旨にデータ数、精度、速度倍率はない。
- Novelty: 畳み込みフィルタを深く訓練する代わりに、豊富なランダム変換と軽い分類器を組み合わせた。
- Limitations: 編者の注意: 元論文は分類であり、予測や確率推定の基準ではない。低い計算費用でも特徴変換・保存の費用は残り、後続MiniRocket等とは区別する。

### Paper: Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting
- Source: arXiv
- Canonical ID: arxiv:1912.09363
- Publication date: 2019-12-19
- URL: https://arxiv.org/abs/1912.09363
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TFTは静的属性・既知の未来入力・過去だけの情報を区別し、多期間予測と寄与の説明を行う。
- Objective: 実務に混在する入力をまとめて扱い、短期・長期の依存と重要特徴を捉える。
- Methods: recurrent層で局所処理、解釈可能なself-attentionで長期関係を学習。特徴選択とgatingで不要部品を抑え、実データで精度と3つの説明用途を評価した。
- Data and results: 既存基準への有意な改善と実用的な解釈例を報告。要旨にデータ数・精度の絶対値はない。
- Novelty: 入力の利用可能時点と種類に合わせた処理を、多期間予測・特徴選択・時間寄与と統合した。
- Limitations: 編者の注意: 将来入力は予測時点で既知のものに限る。attentionや選択重みは因果効果ではなく、説明の見やすさと真の機構の同定を区別する。

### Paper: Causal mediation analysis with double machine learning
- Source: arXiv
- Canonical ID: arxiv:2002.12710
- Publication date: 2020-02-28
- URL: https://arxiv.org/abs/2002.12710
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: DMLを媒介分析へ拡張し、高次元交絡を調整して処置の直接・間接効果を推定する。
- Objective: 結果・処置・媒介変数の柔軟な予測器を使い、経路ごとの効果を推論する。
- Methods: 観測変数による選択仮定の下で、多重頑健な効率スコアと標本分割を利用。LASSOのシミュレーションと米国NLSYの保険・健診・健康の例で評価した。
- Data and results: 正則条件下でroot-n一致性と漸近正規性を導出。応用では保険の短期健康効果は中程度だが、通常健診で媒介されないと推定した。
- Novelty: 総効果だけでなく、媒介経路を通る効果と通らない効果へDMLの推論を展開した。
- Limitations: 編者の注意: 媒介の因果解釈には観測交絡等の強い仮定が必要。健診経路がないという推定を、全集団・長期の保険効果や健診の無効性へ一般化しない。

### Paper: Double Machine Learning based Program Evaluation under Unconfoundedness
- Source: arXiv
- Canonical ID: arxiv:2003.03191
- Publication date: 2020-03-06
- URL: https://arxiv.org/abs/2003.03191
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 非交絡性下の政策評価へDMLを整理・応用し、極端な個別効果を抑えるNDR-learnerを提案する。
- Objective: 平均・異質効果・最適割当を包括的に評価し、不安定な個別処置効果を改善する。
- Methods: スイスの積極的労働市場政策の複数プログラムへDMLを適用。DR-learnerの逆確率重みを個別に正規化するNDR-learnerを導入した。
- Data and results: 政策評価の一連の利用を示し、極端なDR効果推定に対する安定化を提案。要旨に雇用効果、誤差、極端値の減少量はない。
- Novelty: 効果推定だけでなく割当ルールまでつなぎ、逆確率重みの局所的な安定化を加えた。
- Limitations: 編者の注意: 非交絡性と処置の重なりを前提とし、正規化は未測定交絡を除かない。個別効果の安定化と、真の効果への一致・政策導入利益は別に検証する。

### Paper: Supervised Whole DAG Causal Discovery
- Source: arXiv
- Canonical ID: arxiv:2006.04697
- Publication date: 2020-06-08
- URL: https://arxiv.org/abs/2006.04697
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 既知の構造を教師にして、変数対ごとではなくDAG全体を予測する因果探索を提案した。
- Objective: 二変数の方向分類に限られた教師あり因果学習を、全体構造へ拡張する。
- Methods: 変数の並べ替えに対応するpermutation equivariantモデルを利用し、データから全DAG構造を学習。10・20・50・100ノードの人工グラフと実データで比較した。
- Data and results: 複数の従来法に対して有望な結果を報告。要旨に構造回復率、辺誤差、実データの規模はない。
- Novelty: 手設計の探索スコアだけでなく、DAG全体を出す規則を教師ありで学ぶ方向を示した。
- Limitations: 編者の注意: 教師構造と学習時の生成分布に依存する。未知の機構・グラフサイズへの移植性と因果識別は、順列対応だけでは保証されない。

### Paper: DNF-Net: A Neural Architecture for Tabular Data
- Source: arXiv
- Canonical ID: arxiv:2006.06465
- Publication date: 2020-06-11
- URL: https://arxiv.org/abs/2006.06465
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: DNF-Netは論理式に似た帰納バイアスと局所的特徴選択を持つ表向けニューラル構造。
- Objective: 通常の全結合ネットが表で弱い問題を、表に合った判断構造で改善する。
- Methods: affineなsoft-threshold項の選言標準形に対応する構造を学び、少数の特徴部分集合で局所判断。Boolean形式・局所性・特徴選択のablationを行った。
- Data and results: 広い実験で全結合ネットを有意かつ一貫して上回り、各設計要素の寄与を示した。要旨に課題数やスコアはない。
- Novelty: 単なる層増加ではなく、論理的な判断の組合せと局所性を深層モデルの設計へ組み込んだ。
- Limitations: 編者の注意: 主な結論は全結合ネットとの比較で、すべての木モデルより優れるという結果ではない。softな論理構造は、離散ルールの完全な解釈性保証とは異なる。

### Paper: Kernel Distributionally Robust Optimization
- Source: arXiv
- Canonical ID: arxiv:2006.06981
- Publication date: 2020-06-12
- URL: https://arxiv.org/abs/2006.06981
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Kernel DROはRKHSを使い、不確かな分布上の最悪最適化を関数の双対問題へ置き換える。
- Objective: 多様な曖昧集合と損失を扱える、分布頑健最適化の共通理論・計算法を得る。
- Methods: RKHSで凸な分布集合を作り、積分確率距離や有限次モーメントへ一般化。モーメント問題の双対定理を拡張し、batch凸解法と確率的関数勾配の算法を提案した。
- Data and results: universal RKHSを使う広い損失で双対化でき、従来の多項式損失や既知Lipschitz定数の制限を緩めた。要旨に実験スコアはない。
- Novelty: 分布についての探索をRKHS関数についての探索へ変換し、複数の頑健・確率最適化を統一した。
- Limitations: 編者の注意: 曖昧集合・kernel・半径の選択と計算近似に依存する。双対定理の広さは、任意の分布変化や有限データでの性能保証とは異なる。

### Paper: In Search of Lost Domain Generalization
- Source: arXiv
- Canonical ID: arxiv:2007.01434
- Publication date: 2020-07-02
- URL: https://arxiv.org/abs/2007.01434
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: DomainBedはdomain generalizationのモデル選択まで揃えると、丁寧なERMが強い基準になると示した。
- Objective: データ・構造・選択基準の不一致で難しかった、分布外汎化手法の現実的比較を行う。
- Methods: 7つの多領域データ、9基準アルゴリズム、3種類のモデル選択を共通評価基盤へ実装した。モデル選択のない手法提案は不完全と位置付けた。
- Data and results: 適切に実装された経験リスク最小化が、すべての対象データで最良水準の性能を示した。要旨に精度の絶対値はない。
- Novelty: 訓練目的だけでなく、テスト領域を見ずにどのモデルを選ぶかも手法の一部として検証した。
- Limitations: 編者の注意: 選定データと実装条件の結果で、OOD手法すべてが無効と結論しない。7/9/3は論文時点の構成で、現在のツール収録数を示すものではない。

### Paper: Double/Debiased Machine Learning for Logistic Partially Linear Model
- Source: arXiv
- Canonical ID: arxiv:2009.14461
- Publication date: 2020-09-30
- URL: https://arxiv.org/abs/2009.14461
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: ロジスティック部分線形モデルの低次元成分を、機械学習で交絡調整しながら推論する。
- Objective: logitの非線形性がある場合も、補助学習の誤差を制御してパラメトリック速度の推定を得る。
- Methods: 2つの補助関数を持つNeyman直交スコアを構築。疎な高次元モデルではモーメント校正、一般MLではfull model refittingを使い、シミュレーションとチリの政策例へ適用した。
- Data and results: 疎モデルの特定条件下でmodel double robustness、一般MLでrate double robustnessを示した。要旨に政策効果や数値性能はない。
- Novelty: 線形DMLの手順を単純転用できないlogitの補助推定を、再適合の工夫で扱った。
- Limitations: 編者の注意: 一方のモデルが正しければ常に十分という主張ではなく、疎モデルでは両方のultra-sparsity等の条件も要る。因果解釈には政策・交絡の仮定が別途必要。

### Paper: The Risks of Invariant Risk Minimization
- Source: arXiv
- Canonical ID: arxiv:2010.05761
- Publication date: 2020-10-12
- URL: https://arxiv.org/abs/2010.05761
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: IRMの分類問題を理論解析し、不変な最適予測器を回復できない条件を示した。
- Objective: 保証が乏しかったIRMと関連目標が、どの条件で成功・失敗するか明らかにする。
- Methods: 自然な生成モデルの下で線形・非線形の分類を解析。最適解が真の不変予測器へ一致する条件と、訓練・テスト分布の関係を調べた。
- Data and results: 線形で成功する場合と、より多くの失敗条件を示し、非線形でもテストが訓練に十分近くないと壊滅的に失敗する設定を構成した。
- Novelty: 経験的なOOD改善の主張に対し、目的関数の最適解でも失敗し得る理論的な限界を提示した。
- Limitations: 編者の注意: 結論は解析したモデル・目的の範囲に依存する。特定設定でERMを改善しないことと、すべての環境設計・不変学習への否定は異なる。

### Paper: Semiparametric proximal causal inference
- Source: arXiv
- Canonical ID: arxiv:2011.08411
- Publication date: 2020-11-17
- URL: https://arxiv.org/abs/2011.08411
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: proximal causal inferenceで、交絡の不完全な代理変数からATE・ATTEを推定する半パラメトリック理論。
- Objective: 観測共変量だけでは交換可能性が成り立たない場合の、因果推論の可能性を整理する。
- Methods: proxyに関する非パラメトリック識別条件、効率限界、二重頑健・局所効率的推定器を導出。シミュレーションとICU右心カテーテルの応用で例示した。
- Data and results: ATEに加え処置群平均効果にも識別・効率の結果を提示。要旨に右心カテーテルの効果量や推定誤差はない。
- Novelty: proxyを誤差のない交絡因子とみなさず、不完全性を前提に識別と効率を扱った。
- Limitations: 編者の注意: 代理変数があれば無条件で識別できるわけではない。proxyの構造と識別条件に依存し、応用例はカテーテルの臨床効果を無作為試験で確立するものではない。

### Paper: TabTransformer: Tabular Data Modeling Using Contextual Embeddings
- Source: arXiv
- Canonical ID: arxiv:2012.06678
- Publication date: 2020-12-11
- URL: https://arxiv.org/abs/2012.06678
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TabTransformerはカテゴリ特徴を文脈付き埋め込みへ変換し、予測と欠損・雑音への頑健性を改善する。
- Objective: 独立したカテゴリ埋め込みでは捉えにくい、特徴間の関係を学ぶ。
- Methods: 自己attentionでカテゴリ表現を文脈化し、教師あり・半教師ありの学習を実施。15公開データで深層法、木のアンサンブル、欠損・雑音条件と比較した。
- Data and results: 平均AUCで深層比較法を少なくとも1.0%上回り、木に匹敵。半教師あり事前学習では平均2.1%のAUC向上と報告した。
- Novelty: 文章中の単語の文脈化を、同じ行にあるカテゴリ変数の表現へ適用した。
- Limitations: 編者の注意: %は原著の表記を保持し、絶対ポイントへ変換しない。欠損・雑音の実験条件を任意の実データの欠損機構へ一般化できない。

### Paper: Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting
- Source: arXiv
- Canonical ID: arxiv:2012.07436
- Publication date: 2020-12-14
- URL: https://arxiv.org/abs/2012.07436
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: InformerはProbSparse attention、系列の蒸留、一括復号で長い将来系列を効率的に予測する。
- Objective: 長期予測で通常Transformerの二次計算量・高メモリ・逐次出力の負担を減らす。
- Methods: O(L log L)のProbSparse機構を用い、層入力を段階的に半減。復号器は1回の前向き処理で長い予測系列をまとめて出力する。
- Data and results: 4つの大規模データで比較法への有意な改善を報告。要旨に誤差値や実測速度倍率はない。
- Novelty: attentionの疎化だけでなく、入力圧縮と非逐次の出力を組み合わせて長期予測を設計した。
- Limitations: 編者の注意: 計算量の主張と全処理時間の削減は別指標。系列の蒸留で消える細部、予測期間、調整予算を揃えて後続の単純な基準とも比較する。

### Paper: MINIROCKET: A Very Fast (Almost) Deterministic Transform for Time Series Classification
- Source: arXiv
- Canonical ID: arxiv:2012.08791
- Publication date: 2020-12-16
- URL: https://arxiv.org/abs/2012.08791
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: MiniRocketはランダム畳み込み変換をほぼ決定的に再構成し、線形分類を高速化する。
- Objective: ROCKETに近い分類精度を、さらに少ない計算と高い再現性で得る。
- Methods: ROCKETの系列特徴変換を再定式化し、ほぼ決定的な出力を線形分類器へ入力。追加費用を払えば完全に決定的にもできる構成を比較した。
- Data and results: 大きいデータで最大75倍高速化し、ほぼ同じ精度を維持。原著はUCR109データの学習・評価を10分未満と報告する。
- Novelty: 深いモデルの追加訓練ではなく、強い固定変換の構成と計算を絞って精度・速度を両立した。
- Limitations: 編者の注意: 最大速度倍率と10分は当時の計算環境の結果で、任意機器での保証ではない。分類の結果を予測や異常検知の性能へ拡張しない。

### Paper: Does Invariant Risk Minimization Capture Invariance?
- Source: arXiv
- Canonical ID: arxiv:2101.01134
- Publication date: 2021-01-04
- URL: https://arxiv.org/abs/2101.01134
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 実用的なIRM近似が自然な不変性を捉えず、ERMより悪くなる例と理由を示した。
- Objective: IRMの理想的な目的と線形近似IRMv1の間にある差を検証する。
- Methods: IRMの動機に沿う単純な問題で理想形と線形版を分析。不変性の捕捉、環境間の損失の違い、標本化の影響を調べた。
- Data and results: 線形版が適切な不変性を逃す例に加え、正しい不変性を得ても損失の非不変性で劣る予測器になる場合を示した。有限標本で脆弱さが増した。
- Novelty: IRMの失敗を単なる調整不足でなく、近似目的と最適化対象のずれとして分析した。
- Limitations: 編者の注意: 特定の定式化に対する反例であり、不変性に基づく学習全体の不可能性定理ではない。理想IRMとIRMv1に対する結論を分けて読む。

### Paper: Out-of-distribution Prediction with Invariant Risk Minimization: The Limitation and An Effective Fix
- Source: arXiv
- Canonical ID: arxiv:2101.07732
- Publication date: 2021-01-16
- URL: https://arxiv.org/abs/2101.07732
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 強い共通原因による見せかけ相関でIRMが劣化する条件を調べ、条件付き分布の整合を加えた。
- Objective: 元のColored MNISTでは成功するIRMが、より強い環境依存の相関で失敗する理由を明らかにする。
- Methods: domainがラベルと偽の特徴の双方へ強く影響するΛ型相関を解析。IRMとconditional distribution matchingを組み合わせ、Colored MNIST plusの半人工実験で評価した。
- Data and results: 強いΛ型相関でのIRMの大きな劣化と、提案する組合せによる改善を示した。要旨に精度値や改善幅はない。
- Novelty: 不変性の目的だけでは残る特定の偽相関を、条件付き分布の一致で補う。
- Limitations: 編者の注意: 特定の相関構造を対象とする修正で、任意の未知領域への保証ではない。半人工の色付き数字実験から実務の全分布変化への有効性は確定しない。

### Paper: MultiRocket: Multiple pooling operators and transformations for fast and effective time series classification
- Source: arXiv
- Canonical ID: arxiv:2102.00457
- Publication date: 2021-01-31
- URL: https://arxiv.org/abs/2102.00457
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: MultiRocketは元系列と差分に複数poolingを使い、MiniRocketの特徴の多様性を増やす。
- Objective: 複雑なアンサンブルを避けつつ、固定畳み込みによる高速分類の精度を高める。
- Methods: 生系列と1階差分の両方を畳み込み変換し、出力へ4種のpoolingを適用。UCRの分類基準でMiniRocketやHIVE-COTE 2.0と比較した。
- Data and results: MiniRocketより有意に高精度で、HIVE-COTE 2.0に競争的ながら数桁速いと報告。要旨に全体精度や時間の絶対値はない。
- Novelty: 単一の集約特徴に限定せず、変換とpoolingの組合せで低費用の分類表現を強化した。
- Limitations: 編者の注意: UCR分類の比較で、任意の長さ・多変量・分布変化への性能を保証しない。速度は計算環境・データ規模に依存する。

### Paper: Automatic Double Machine Learning for Continuous Treatment Effects
- Source: arXiv
- Canonical ID: arxiv:2104.10334
- Publication date: 2021-04-21
- URL: https://arxiv.org/abs/2104.10334
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 連続処置の平均用量反応関数を、DMLとautomatic DMLの補正で推定する。
- Objective: 処置の有無だけでなく、特定の投与量・介入水準における平均結果を柔軟に推定する。
- Methods: DML・ADMLの道具を組み合わせた新しいdebiasingを導入し、安定性・バランスの理論的性質と漸近正規性を示した。シミュレーションで既存法と比較した。
- Data and results: 人工実験で良好な比較性能を報告。要旨に誤差値や標本数はなく、非パラメトリックな連続用量関数に対する結果である。
- Novelty: 二値処置の平均効果から、連続的な処置水準ごとの平均反応へ自動補正の方法を拡張した。
- Limitations: 編者の注意: 漸近正規性を二値ATEと同じroot-n速度と読み替えない。因果解釈には交絡調整と用量の支持・重なりなどの識別条件が別途必要。

### Paper: TABBIE: Pretrained Representations of Tabular Data
- Source: arXiv
- Canonical ID: arxiv:2105.02584
- Publication date: 2021-05-06
- URL: https://arxiv.org/abs/2105.02584
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TABBIEは表だけから壊れたセルを検出する事前学習で、セル・行・列の表現を得る。
- Objective: 対応する文章を必要としない、欠損セル補充などの表単独の課題に強い表現を学ぶ。
- Methods: corrupt cell detectionを自己教師あり課題とし、表の各部分構造の埋め込みを学習。表と文章を共同学習する比較法と、表に関する予測課題で評価した。
- Data and results: 複数の表予測課題で最良水準に達し、訓練計算も少なかった。表現の定性分析で意味・数値傾向を捉えたが、要旨に絶対スコアはない。
- Novelty: 文章向け目的を借りるだけでなく、表自体の破損検出から複数粒度の表現を学んだ。
- Limitations: 編者の注意: 記述表の意味理解と、任意の数値表の教師あり予測は同一課題ではない。定性的な意味の分析だけで計算・論理的一貫性の保証は得られない。

### Paper: Unsupervised Representation Learning for Time Series with Temporal Neighborhood Coding
- Source: arXiv
- Canonical ID: arxiv:2106.00750
- Publication date: 2021-06-01
- URL: https://arxiv.org/abs/2106.00750
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TNCは局所的に安定した時間近傍を使い、非定常系列の自己教師あり表現を学ぶ。
- Objective: 状態が変わる一方でラベルの少ない信号を、分類・クラスタリングに使えるようにする。
- Methods: 生成過程の局所的滑らかさから時間近傍を定義し、近傍内と外の信号分布を区別するdebiasした対照目的を用いた。複数データで既存の教師なし法と比較した。
- Data and results: クラスタリングと分類で比較法を上回ったと報告。要旨にデータ数やスコア、患者追跡の実測値はない。
- Novelty: 全系列が定常とは仮定せず、短い時間近傍に残る安定性を表現学習の教師信号にした。
- Limitations: 編者の注意: 局所滑らかさが破れる急変や、離れた時点の同じ状態の扱いに注意が要る。医療という動機と、患者の潜在状態を臨床で正しく追跡した証拠は区別する。

### Paper: SAINT: Improved Neural Networks for Tabular Data via Row Attention and Contrastive Pre-Training
- Source: arXiv
- Canonical ID: arxiv:2106.01342
- Publication date: 2021-06-02
- URL: https://arxiv.org/abs/2106.01342
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: SAINTは列と行の双方へのattentionに、ラベル不足向けの対照事前学習を組み合わせる。
- Objective: 異種特徴を持つ表データで、従来深層法や強い木モデルに匹敵する表現を得る。
- Methods: 改良した埋め込みに行・列のattentionを適用し、自己教師ありの対照学習も評価。XGBoost、CatBoost、LightGBMなどと比較した。
- Data and results: 複数ベンチマーク平均で深層比較法を改善し、木の比較法も上回ったと報告。要旨にデータ数、平均スコア、計算量の具体値はない。
- Novelty: 行内の特徴間関係だけでなく、標本間の関係と未ラベルデータの事前学習を統合した。
- Limitations: 編者の注意: 平均での優位は全データでの勝利ではない。行間attentionの評価時の入力集合、訓練・テスト分離、ラベル利用条件を確認して比較する必要がある。

### Paper: TS2Vec: Towards Universal Representation of Time Series
- Source: arXiv
- Canonical ID: arxiv:2106.10466
- Publication date: 2021-06-19
- URL: https://arxiv.org/abs/2106.10466
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TS2Vecは階層的な対照学習で時点表現を学び、部分系列から系列全体まで集約できる。
- Objective: 任意の長さ・意味粒度で使える時系列表現を、ラベルなしに獲得する。
- Methods: 拡張した文脈viewを階層的に対照し、各時点の文脈表現を学習。必要な部分の集約を分類・線形予測・教師なし異常検知へ利用した。
- Data and results: UCR125・UEA29データの分類で既存の教師なし表現を改善し、予測と異常検知でも最良水準を報告。要旨に精度の具体値はない。
- Novelty: 系列全体に固定長ベクトルを割り当てるだけでなく、時点から任意部分の表現を共有できるようにした。
- Limitations: 編者の注意: ラベルなしの表現学習と下流予測器の学習条件を区別する。データ拡張で保存する性質が課題に適するか、未来情報やテスト混入がないかも確認が必要。

### Paper: Revisiting Deep Learning Models for Tabular Data
- Source: arXiv
- Canonical ID: arxiv:2106.11959
- Publication date: 2021-06-22
- URL: https://arxiv.org/abs/2106.11959
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 表形式の深層モデルを同じ調整手順で比較し、強いResNet型基準とFT-Transformerを示した。
- Objective: モデルごとに異なるベンチマーク・実験手順で、優劣が不明だった状況を改善する。
- Methods: 主要な深層モデル群を共通の訓練・調整プロトコルで比較。単純なResNet型と表向けTransformerを評価し、最良の深層法をGBDTとも比較した。
- Data and results: ResNet型は見落とされがちな強い基準、Transformerの適応は多くの課題で他の深層法を上回った。一方、GBDTも含め普遍的な勝者はなかった。要旨に絶対スコアはない。
- Novelty: 新構造の主張だけでなく、基準モデルの強さと公平な調整手順を表形式研究の中心に置いた。
- Limitations: 編者の注意: 多数課題の実験でも、任意の表でTransformerが最良とは結論しない。データ規模・特徴型・調整費用に応じた比較が必要。

### Paper: Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting
- Source: arXiv
- Canonical ID: arxiv:2106.13008
- Publication date: 2021-06-24
- URL: https://arxiv.org/abs/2106.13008
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Autoformerは分解を内部ブロックにし、周期性に基づくAuto-Correlationで部分系列の依存を扱う。
- Objective: 長い将来の複雑なパターンを、点ごとの疎なattentionより効果的に利用する。
- Methods: 前処理だった系列分解を深層モデル内で段階的に実行。周期性から部分系列の関係を見つけ、表現を集約する機構を設計した。
- Data and results: エネルギー・交通・経済・天候・疾病の5用途を含む6基準で、38%の相対改善を報告。要旨に各課題の絶対誤差はない。
- Novelty: 局所時点間のattentionから、分解と周期に基づく部分系列単位の依存推定へ移した。
- Limitations: 編者の注意: 38%は原著の比較条件による相対改善で、全用途の保証ではない。周期の弱い系列・変化する周期・非定常な突発事象も個別評価が必要。

### Paper: Time-Series Representation Learning via Temporal and Contextual Contrasting
- Source: arXiv
- Canonical ID: arxiv:2106.14112
- Publication date: 2021-06-26
- URL: https://arxiv.org/abs/2106.14112
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TS-TCCは時間予測と文脈の対照を組み合わせ、未ラベル系列の特徴を学ぶ。
- Objective: 動的な系列から、少数ラベルと領域転移に役立つ表現を得る。
- Methods: 弱い・強い拡張で2viewを作り、cross-viewの時間予測を学習。同じ標本の文脈を近づけ、別標本を離すcontextual contrastも追加した。
- Data and results: 3実データで、特徴上の線形分類器が教師あり訓練に匹敵。少数ラベル・転移でも高い効率を報告するが、要旨に数値スコアはない。
- Novelty: 時系列の局所的な動態と、標本全体の識別性を2つの対照目的で分けて学ぶ。
- Limitations: 編者の注意: 選んだ拡張が元のラベル・意味を保持することに依存する。3データの比較から、すべての生体・産業信号への転用は保証されない。

### Paper: SCARF: Self-Supervised Contrastive Learning using Random Feature Corruption
- Source: arXiv
- Canonical ID: arxiv:2106.15147
- Publication date: 2021-06-29
- URL: https://arxiv.org/abs/2106.15147
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: SCARFは一部特徴を無作為に壊したviewで対照学習し、表の分類表現を事前学習する。
- Objective: 画像特有の拡張を使えない表でも、未ラベルデータから有用な表現を得る。
- Methods: ランダムな特徴部分集合をcorruptしてviewを形成。OpenML-CC18の69分類データで、全ラベル、ラベル雑音、少数ラベル条件と各設計要素を比較した。
- Data and results: 3条件で分類精度を改善し、autoencoderなどの代替法を上回った。既存の工夫と相補的だったが、要旨に平均改善値はない。
- Novelty: 広い表分類へ使える単純な特徴破損を、対照表現学習の共通操作として示した。
- Limitations: 編者の注意: 特徴の破損が意味的に妥当かはデータ次第である。既存ラベルを一部隠す評価と、実務での選択的ラベル欠損は同じではない。

### Paper: CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation
- Source: arXiv
- Canonical ID: arxiv:2107.03502
- Publication date: 2021-07-07
- URL: https://arxiv.org/abs/2107.03502
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: CSDIは観測済みの時系列を条件とするscore-based拡散で、欠損値の分布を補完する。
- Objective: 観測間の相関を活かし、点推定に限らず不確実性を含めた補完を行う。
- Methods: 補完向けに条件付き拡散を明示的に訓練。医療・環境データで確率補完と決定的補完を比較し、補間・確率予測にも適用した。
- Data and results: 既存の確率補完指標を40–65%、決定的な補完誤差を5–20%改善と報告。補間と確率予測でも競争的だった。
- Novelty: 無条件生成からの転用だけでなく、観測値を条件として欠損を推定する拡散過程を直接学んだ。
- Limitations: 編者の注意: 改善率は対象指標・欠損設定に依存し、全機構での不偏補完や区間校正を保証しない。反復的なサンプリングの計算費用も考慮する。

### Paper: LocalGLMnet: interpretable deep learning for tabular data
- Source: arXiv
- Canonical ID: arxiv:2107.11059
- Publication date: 2021-07-23
- URL: https://arxiv.org/abs/2107.11059
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: LocalGLMnetはGLMに似た加法分解を保ちつつ、深層表現で表の回帰を柔軟化する。
- Objective: 深層回帰の予測力を利用しながら、変数選択と寄与の説明を可能にする。
- Methods: 一般化線形モデルの構造を参考にネットワークを設計し、学習済み予測をShapley値やintegrated gradientsに通じる加法形で解釈する。
- Data and results: 変数選択と予測の分解が可能な構造を提案し、古典的モデルより柔軟な回帰を狙う。要旨には評価データや精度・説明の数値検証はない。
- Novelty: 後から説明器を加えるだけでなく、説明可能な分解をモデル構造へ組み込んだ。
- Limitations: 編者の注意: 加法分解ができても各項は因果効果ではない。GLMに似た形から古典的GLMと同じ統計的推論保証が自動で得られるわけではない。

### Paper: Efficiently Modeling Long Sequences with Structured State Spaces
- Source: arXiv
- Canonical ID: arxiv:2111.00396
- Publication date: 2021-10-31
- URL: https://arxiv.org/abs/2111.00396
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: S4は構造化した状態空間モデルを効率計算し、非常に長い系列の依存を扱う。
- Objective: 1万ステップ以上で負担が増すRNN・CNN・Transformerに代わる共通系列モデルを作る。
- Methods: 状態行列Aに低rank補正を用いて安定に対角化し、計算をCauchy kernelへ帰着。分類、生成、Long Range Arenaで評価した。
- Data and results: 逐次CIFAR-10で追加拡張・補助損失なしにaccuracy91%。長さ16kのPath-Xを解き、画像・言語生成で60倍の高速化も報告した。
- Novelty: 長期記憶の数学的性質を持つSSMを、構造化パラメータと効率的なkernel計算で実用化した。
- Limitations: 編者の注意: 課題ごとの結果と速度倍率を、全種類の推論へ一般化しない。長い依存を扱えることと、内容依存の選択的な記憶が得意なことは異なる。

### Paper: Transformers Can Do Bayesian Inference
- Source: arXiv
- Canonical ID: arxiv:2112.10510
- Publication date: 2021-12-20
- URL: https://arxiv.org/abs/2112.10510
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: PFNは事前分布から多数の課題を作り、例の集合からBayes的な予測を1回で近似する。
- Objective: 明示的な事前知識と不確実性を扱う推論を、深層モデルで高速に実行する。
- Methods: 事前から関数・学習例を繰り返し生成し、1ラベルを隠して残りの集合から確率予測するよう学習。GP、Bayes neural network、少数表分類・画像分類を評価した。
- Data and results: Gaussian processをほぼ再現し、複数設定で既存法より200倍超高速な推論を報告。扱いにくい問題でも効率的な近似を示した。
- Novelty: 課題ごとに事後推論を解く代わりに、事前からの訓練で推論手続き自体を償却し、後のTabPFNにつながった。
- Limitations: 編者の注意: 事前から課題をサンプルできることが前提で、学習外の分布の事後を厳密に出す保証ではない。推論の速度比較と事前学習を含む全費用は異なる。

### Paper: FEDformer: Frequency Enhanced Decomposed Transformer for Long-term Series Forecasting
- Source: arXiv
- Canonical ID: arxiv:2201.12740
- Publication date: 2022-01-30
- URL: https://arxiv.org/abs/2201.12740
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: FEDformerは季節・トレンド分解と周波数表現を組み合わせ、長期予測を効率化する。
- Objective: Transformerの局所的詳細に加え、系列全体の形を捉えつつ計算負担を減らす。
- Methods: 分解で全体傾向、Transformerで細部を扱い、Fourier等での疎な表現を周波数強化へ利用。6つの予測基準で評価した。
- Data and results: 系列長に線形の計算量を示し、既存最良法に対し多変量14.8%、単変量22.6%の予測誤差低下を報告。
- Novelty: 時間領域の分解と、周波数領域で少数成分を使う表現を長期予測器へ統合した。
- Limitations: 編者の注意: 相対的な誤差低下を絶対精度の増分に読み替えない。周波数疎性や分解が適する範囲と、実測の速度・メモリはデータ依存である。

### Paper: N-HiTS: Neural Hierarchical Interpolation for Time Series Forecasting
- Source: arXiv
- Canonical ID: arxiv:2201.12886
- Publication date: 2022-01-30
- URL: https://arxiv.org/abs/2201.12886
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: N-HiTSは階層補間と異なる率の標本化で、多周波数・多尺度の長期予測を組み立てる。
- Objective: 長期予測の不安定さと計算負担を減らす。
- Methods: 入力を分解しながら、異なる周波数・尺度の成分の予測を逐次合成。滑らかさの下で長い予測区間を近似する理論と、大規模系列の比較実験を行った。
- Data and results: 当時のTransformer群に対し平均でほぼ20%の精度改善、計算時間50倍の高速化を報告。要旨に課題別の絶対誤差はない。
- Novelty: すべての将来時点を同じ解像度で直接予測する代わりに、階層的な補間と成分合成を利用した。
- Limitations: 編者の注意: 理論は滑らかさを前提とし、任意の急変を高精度に近似する保証ではない。速度倍率と平均改善は対象モデル・データ・実装に依存する。

### Paper: CoST: Contrastive Learning of Disentangled Seasonal-Trend Representations for Time Series Forecasting
- Source: arXiv
- Canonical ID: arxiv:2202.01575
- Publication date: 2022-02-03
- URL: https://arxiv.org/abs/2202.01575
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: CoSTはトレンドと季節性を分けた対照表現を先に学び、単純な回帰で予測する。
- Objective: 予測器をend-to-endで作る以外の、頑健で転用しやすい時系列学習の枠組みを得る。
- Methods: 時間領域と周波数領域の対照損失を、傾向・季節性の識別表現へそれぞれ利用。表現の後に回帰を適応し、encoderや回帰器を変えて比較した。
- Data and results: 多変量基準でMSEを21.3%改善し、異なるbackbone・下流回帰でも頑健な結果を報告した。
- Novelty: 予測に重要な成分の分離を、時間・周波数の自己教師あり学習として設計した。
- Limitations: 編者の注意: 因果的な動機付けがあっても、学習した成分が真の因果機構と同一とは限らない。21.3%は比較条件での相対MSE改善である。

### Paper: Validating Causal Inference Methods
- Source: arXiv
- Canonical ID: arxiv:2202.04208
- Publication date: 2022-02-09
- URL: https://arxiv.org/abs/2202.04208
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Credenceは実データに近い合成観測研究を作り、因果推定法の相対性能を調べる。
- Objective: 単純化した手作りシミュレーションだけでなく、手元のデータに近い条件で推定法を評価する。
- Methods: 深層生成器を経験分布へ合わせ、因果効果と交絡バイアスの真値・形を指定できるようにする。広い人工実験とLalonde・Project STARの2応用で比較した。
- Data and results: 異なる推定法の相対性能を評価できることを示した。要旨に分布一致や順位予測の具体値はない。
- Novelty: 観測分布の現実性と、反事実の真値を指定できる実験環境を組み合わせた。
- Limitations: 編者の注意: 合成データで指定した反事実が現実の真実とは限らない。観測分布に似ていても因果構造は一意でなく、評価は指定した効果・交絡のシナリオに条件付く。

### Paper: SAITS: Self-Attention-based Imputation for Time Series
- Source: arXiv
- Canonical ID: arxiv:2202.08516
- Publication date: 2022-02-17
- URL: https://arxiv.org/abs/2202.08516
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: SAITSは2つの対角mask付きself-attentionを重み付きで統合し、多変量系列を補完する。
- Objective: 時間依存と特徴間相関を利用し、補完精度と学習速度を改善する。
- Methods: joint optimizationで2つのDMSAブロックを学習。attention mapと欠損情報に応じた重みで、異なる表現を動的に組み合わせた。
- Data and results: 定量・定性実験で既存の最良法を効率的に上回り、不完全系列での認識モデルも改善する可能性を示した。要旨にデータ数・数値指標はない。
- Novelty: 再帰処理とは異なり、attentionによる時間・特徴関係と欠損依存の表現統合を補完に特化した。
- Limitations: 編者の注意: 補完誤差と下流性能は別々に評価すべきで、値依存の欠損での不偏性は示さない。後の観測も使える補完と実時間予測は利用情報が異なる。

### Paper: CTAB-GAN+: Enhancing Tabular Data Synthesis
- Source: arXiv
- Canonical ID: arxiv:2204.00401
- Publication date: 2022-04-01
- URL: https://arxiv.org/abs/2204.00401
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: CTAB-GAN+は下流課題の損失とDP-SGDを組み合わせ、表生成の効用と保護を両立しようとする。
- Objective: 実表に似せるほど情報漏洩が増える問題で、明示的なプライバシー予算下の効用を改善する。
- Methods: 条件付きGANへ分類・回帰の損失、Wasserstein損失と勾配ペナルティ、混合・不均衡変数向け符号化を追加。DP-SGDで訓練し複数予算を比較した。
- Data and results: 複数データと学習課題で、異なるプライバシー予算下に少なくとも48.16%高い効用を報告。要旨に予算値・指標の絶対値はない。
- Novelty: 経験的な匿名性評価だけでなく、差分プライバシーの訓練と下流効用を明示的に組み合わせた。
- Limitations: 編者の注意: 保証は採用したDP定義・予算・実装に依存し、任意の設定で同じではない。48.16%は相対効用の主張で、絶対精度や情報漏洩ゼロを意味しない。

### Paper: Are Transformers Effective for Time Series Forecasting?
- Source: arXiv
- Canonical ID: arxiv:2205.13504
- Publication date: 2022-05-26
- URL: https://arxiv.org/abs/2205.13504
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: DLinearなど単層の線形基準が、当時の複雑な長期予測Transformerを上回る例を示した。
- Objective: Transformerの改変による進歩が、十分強い単純な基準との比較でも成り立つか検証する。
- Methods: LTSF-Linearという単層線形モデル群を導入し、9実データで先行Transformerと比較。時間関係の取り出しに各設計要素が与える影響も分析した。
- Data and results: 対象9データの比較では線形法がすべてで先行法を上回り、しばしば大差だった。要旨に各誤差の具体値はない。
- Novelty: 構造の複雑化が必要という前提を問い、時系列の強い単純基準と評価手順の再検討を促した。
- Limitations: 編者の注意: 当時の選定モデル・データ・設定の結果で、Transformer全般の不可能性を証明しない。時間順序への著者の説明と、構造ごとの実測結果を区別する。

### Paper: Hopular: Modern Hopfield Networks for Tabular Data
- Source: arXiv
- Canonical ID: arxiv:2206.00664
- Publication date: 2022-06-01
- URL: https://arxiv.org/abs/2206.00664
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Hopularは各層から元入力と保存した学習例へアクセスする、Hopfield型の表モデル。
- Objective: 小・中規模の表で、標本間と特徴間の依存を利用して木モデルに対抗する。
- Methods: 各層にcontinuous modern Hopfield networkを置き、特徴–特徴、特徴–目的、標本–標本の関係を取得。1,000例未満と約1万例のデータで比較した。
- Data and results: 小規模で木・SVM・複数深層法を上回り、中規模でもXGBoost・CatBoost・LightGBMなどを上回ると報告。要旨にデータ数や平均スコアはない。
- Novelty: 入力を一度だけ変換する深層法と異なり、各層で学習例の記憶を参照して予測を改良する。
- Limitations: 編者の注意: 学習集合へのアクセスは記憶・計算の費用を伴い、規模が大きい場合は別途評価が必要。選定ベンチマークの優位をすべての表へ一般化しない。

### Paper: MET: Masked Encoding for Tabular Data
- Source: arXiv
- Canonical ID: arxiv:2206.08564
- Publication date: 2022-06-17
- URL: https://arxiv.org/abs/2206.08564
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: METは列ごとに異なる意味を持つ表をマスク再構成で学ぶ自己教師あり表現法。
- Objective: 表向け対照学習で設計が難しい、場当たり的なview拡張への依存を減らす。
- Methods: 各座標に別の表現を使うmasked autoencodingに、通常の再構成と敵対的再構成損失を併用。5つの実表と単純な人工データで検証した。
- Data and results: 5データすべてで当時の最良水準を更新し、最大9%改善と報告。要旨に指標の絶対値はない。
- Novelty: 画像のMAEをそのまま使わず、列の意味の非互換性と再構成損失を表向けに設計した。
- Limitations: 編者の注意: 最大改善は平均改善や絶対ポイントではない。対照学習用の拡張が不要という主張で、マスキング等の学習条件やデータ準備まで不要とは意味しない。

### Paper: TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second
- Source: arXiv
- Canonical ID: arxiv:2207.01848
- Publication date: 2022-07-05
- URL: https://arxiv.org/abs/2207.01848
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 初期TabPFNは合成データで事前学習し、小さな数値表の分類を重み更新なしの入力例から解く。
- Objective: 表ごとにモデル探索を繰り返さず、少数例分類を高速に実行する。
- Methods: 単純な構造を好む構造的因果モデルの事前分布から合成課題を作り、Bayes推論を近似するPFNを学習。ラベル付き例とテスト例をTransformerへ一括入力する。
- Data and results: 学習≤1,000行、欠損なし数値≤100特徴、≤10クラスのOpenML-CC18の18課題で木を上回り、AutoML相当を最大230倍、GPUで5,700倍高速化。追加67課題でも検証した。
- Novelty: 表ごとの訓練を、合成課題上の事前学習とin-contextな予測へ置き換えた。
- Limitations: 編者の注意: 記載の規模・数値・欠損なし条件はこの初期版の評価範囲。因果モデルを事前分布に使っても、入力表の因果関係を同定することを意味しない。

### Paper: Why do tree-based models still outperform deep learning on tabular data?
- Source: arXiv
- Canonical ID: arxiv:2207.08815
- Publication date: 2022-07-18
- URL: https://arxiv.org/abs/2207.08815
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 中規模の表データで木が強い理由を、非情報特徴・軸方向・不規則な関数への適性から調べた。
- Objective: 画像や文章と異なり表データで深層学習の優位が明確でない原因を検証する。
- Methods: 45データセットで木と新旧ニューラルモデルを比較し、訓練だけでなくハイパーパラメータ探索も評価。帰納バイアスを実験で調べ、探索の生データを公開した。
- Data and results: 約1万例の中規模データでは木が依然強く、速度を考慮しなくても優位。不要特徴への頑健性、データの向きの保持、不規則関数の学習を重要な課題として挙げた。
- Novelty: 単純な順位比較から、表データ特有の性質とモデルの仮定の対応へ踏み込んだ。
- Limitations: 編者の注意: 中規模の選定データでの結果であり、巨大データや後年の事前学習モデルへの順位を保証しない。実験的説明を唯一の理論原因と解釈しない。

### Paper: Valid Inference After Causal Discovery
- Source: arXiv
- Canonical ID: arxiv:2208.05949
- Publication date: 2022-08-11
- URL: https://arxiv.org/abs/2208.05949
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 同じデータで因果構造を選んでから効果を推定する『二重使用』による信頼区間の破綻に対処する。
- Objective: 因果探索後も、効果の信頼区間が所定の被覆率を持つようにする。
- Methods: 因果探索へランダム化を入れ、ランダム化の強さに応じて区間の誤り水準を調整。構造の質と下流区間の幅の交換関係を扱う。
- Data and results: 素朴な探索後推論は過大な非被覆率となる一方、提案法は信頼できる被覆と、データ分割より正確な構造探索を実験で示した。
- Novelty: 構造学習と効果推定を個別に正しく行うだけでは足りない、選択後推論の問題を明示した。
- Limitations: 編者の注意: 保証の対象は選択したモデルに対応する量で、グラフの因果的正しさそのものではない。ランダム化による構造精度と区間幅の交換関係が残る。

本文の照合箇所: [v3（2024-08-19）のIntroduction、式1と探索ランダム化・被覆補正の説明](https://arxiv.org/pdf/2208.05949v3)。

### Paper: TabDDPM: Modelling Tabular Data with Diffusion Models
- Source: arXiv
- Canonical ID: arxiv:2209.15421
- Publication date: 2022-09-30
- URL: https://arxiv.org/abs/2209.15421
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TabDDPMは連続・カテゴリの混合表を拡散モデルで生成し、下流効用とプライバシーを比較する。
- Objective: 異なる型の列を扱い、GAN・VAEに代わる表の生成法を作る。
- Methods: 数値へGaussian拡散、カテゴリへmultinomial拡散を使い、MLPで逆過程を学ぶ。合成表の学習効用、最近傍実記録までの距離DCR、membership攻撃を評価した。
- Data and results: GAN/VAEより強い学習効用を報告。DCRではSMOTEより実記録から離れる一方、GAN/VAEより近いという、効用との交換関係があった。
- Novelty: 列の型に対応した拡散過程を統合し、単純な補間生成法も含めて効用と近接性を比較した。
- Limitations: 著者は実世界のプライバシー要件を満たすか未確定とし、DCRが機密特徴の一致を捉えないと指摘。差分プライバシーなどの形式保証を示す結果ではない。

本文の照合箇所: [Section 4、DCR・privacy attack評価、Limitations and discussion](https://proceedings.mlr.press/v202/kotelnikov23a/kotelnikov23a.pdf)。

### Paper: TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis
- Source: arXiv
- Canonical ID: arxiv:2210.02186
- Publication date: 2022-10-05
- URL: https://arxiv.org/abs/2210.02186
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TimesNetは複数周期に沿って系列を2次元化し、周期内・周期間の変動を共通に学ぶ。
- Objective: 予測だけに専用化せず、広い時系列課題に共通する複雑な時間変動を表現する。
- Methods: 多周期性を適応的に見つけ、1次元系列を複数の2次元tensorへ変換。TimesBlockのパラメータ効率のよいinception部品で2方向の変動を抽出した。
- Data and results: 短期・長期予測、欠損補完、分類、異常検知の5課題で最良水準を報告。要旨に課題別スコアや対象数はない。
- Novelty: 周期を単なる特徴として足すのではなく、2次元kernelが扱える表現の軸へ変換した。
- Limitations: 編者の注意: 各課題で強いことと、1つの重みで全課題を無調整に解くことは異なる。周期が曖昧・急変するデータの挙動と評価条件も確認が必要。

### Paper: STaSy: Score-based Tabular data Synthesis
- Source: arXiv
- Canonical ID: arxiv:2210.04018
- Publication date: 2022-10-08
- URL: https://arxiv.org/abs/2210.04018
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: STaSyはscore-based生成の学習を安定化し、表データの品質・多様性・時間を評価する。
- Objective: 複雑な表分布で、品質だけでなく多様な標本を効率よく生成する。
- Methods: denoising score matchingにself-paced learningと微調整を追加。15表データと7基準法を、下流課題評価・多様性・生成時間で比較した。
- Data and results: 課題依存の評価と多様性で既存法を上回ったと報告。要旨に具体的スコアや、時間でも一律に優れるという数値結果はない。
- Novelty: 表のscore-based生成へ、学習の進め方と調整方法を導入し、生成の複数目標を明示した。
- Limitations: 編者の注意: 品質と多様性の改善を生成時間やプライバシーの改善へ読み替えない。学習安定性の利点もデータと調整条件を伴って比較する。

### Paper: Language Models are Realistic Tabular Data Generators
- Source: arXiv
- Canonical ID: arxiv:2210.06280
- Publication date: 2022-10-12
- URL: https://arxiv.org/abs/2210.06280
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: GReaTは自己回帰言語モデルを使い、任意の特徴を条件に表の残りを生成する。
- Objective: 多様な列型を持つ表で、言語モデルの生成能力を活用する。
- Methods: 表分布を自己回帰LLMでモデル化し、特徴の任意の部分集合を条件として残りをサンプル。人工・実データの複数規模で妥当性と品質を評価した。
- Data and results: 異種特徴を持つ多数データで高い性能を報告。要旨にデータセット数、生成品質、下流効用、時間の数値はない。
- Novelty: 画像向け生成器の適応だけでなく、言語モデルによる表分布と柔軟な条件付き生成を示した。
- Limitations: 編者の注意: 特徴の型・値の整合、稀な組合せ、出力を表へ戻す処理も評価が必要。現実的な合成例が出ても個人情報の記憶や漏洩を否定できない。

### Paper: TabLLM: Few-shot Classification of Tabular Data with Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2210.10723
- Publication date: 2022-10-19
- URL: https://arxiv.org/abs/2210.10723
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TabLLMは表の行を自然言語へ直列化し、LLMの事前知識を少数例分類へ利用する。
- Objective: ラベルがごく少ない表形式課題で、一般言語モデルの知識が役立つか調べる。
- Methods: 行と課題説明を文字列化し、テンプレート、table-to-textモデル、LLMによる直列化を比較。zero-shotと、少数ラベルで微調整するfew-shotを評価した。
- Data and results: 複数課題で従来深層法を上回り、zero-shotでも非自明な性能。特に極少数例では勾配ブースティングとも競争的だったが、要旨にスコア・例数はない。
- Novelty: 表の数値構造だけでなく、列名や値の言語的意味を大規模事前知識へ接続した。
- Limitations: 編者の注意: 本研究のfew-shotは微調整を含み、常に重み更新なしではない。直列化・列名・事前知識に依存し、匿名化された特徴で同じ利点を得るとは限らない。

### Paper: A Time Series is Worth 64 Words: Long-term Forecasting with Transformers
- Source: arXiv
- Canonical ID: arxiv:2211.14730
- Publication date: 2022-11-27
- URL: https://arxiv.org/abs/2211.14730
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: PatchTSTは時系列をパッチへ分け、チャネルごとに共有Transformerで長期予測する。
- Objective: 局所パターンを残しながらattention費用を減らし、より長い履歴を利用する。
- Methods: 部分系列をtoken化し、各チャネルを単変量として埋め込み・重みを共有。教師あり予測、マスク事前学習と微調整、データ間転移を評価した。
- Data and results: 先行Transformerより高い長期予測精度と、事前学習の有効性を報告。別データへの転移でも最良水準だったが、要旨に誤差値はない。
- Novelty: 点tokenと複雑なチャネル混合を見直し、パッチ化と独立チャネル処理という単純な設計を強い基準にした。
- Limitations: 編者の注意: チャネル間の直接相互作用を省く設計なので、その必要性が高い課題は別評価が要る。転移・微調整の成績を未学習zero-shot成績と混同しない。

### Paper: One Fits All:Power General Time Series Analysis by Pretrained LM
- Source: arXiv
- Canonical ID: arxiv:2302.11939
- Publication date: 2023-02-23
- URL: https://arxiv.org/abs/2302.11939
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Frozen Pretrained Transformerは言語・画像で学んだ主要層を保ち、時系列の複数課題へ適応する。
- Objective: 時系列専用の大規模事前学習データ不足を、他モダリティのモデルの再利用で補う。
- Methods: 事前学習済みのself-attention・feed-forward層を変更せず、時系列課題へ微調整。分類、異常検知、予測等を評価し、attentionとPCAの類似性も理論・実験で検討した。
- Data and results: 主要時系列課題で競争的または最良水準の性能を報告。要旨に課題別数値、モデル規模、必要な微調整量はない。
- Novelty: 専用の時系列モデルを設計する流れに対し、他分野で学習した主要変換の再利用を共通基盤として検証した。
- Limitations: 編者の注意: 凍結するのは指定された主要層で、すべての処理が無学習とは限らない。PCAとの類似分析は、全状況で同じ計算をする証明や全用途の汎化保証ではない。

### Paper: TSMixer: An All-MLP Architecture for Time Series Forecasting
- Source: arXiv
- Canonical ID: arxiv:2303.06053
- Publication date: 2023-03-10
- URL: https://arxiv.org/abs/2303.06053
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TSMixerは時間軸と特徴軸を交互に混ぜるMLPで、系列間・補助情報を利用する予測器。
- Objective: 単変量線形モデルの強さを保ちつつ、実務の多変量相互作用を効率よく扱う。
- Methods: 時間・特徴方向のmixingを行うMLPを積層。一般的な学術データと、大規模小売のM5で専用モデルと比較した。
- Data and results: 学術基準で専用最良法に匹敵し、難しいM5では比較法を上回った。要旨にデータ数や誤差の絶対値はない。
- Novelty: attentionやrecurrent構造なしで、単純なMLPへ系列間・補助情報の利用を組み込んだ。
- Limitations: 編者の注意: 追加情報を使うモデルと使わないモデルでは入力条件が異なる。M5での優位をすべての分野の多変量予測へ一般化しない。

### Paper: Efficient Multi-stage Inference on Tabular Data
- Source: arXiv
- Canonical ID: arxiv:2303.11580
- Publication date: 2023-03-21
- URL: https://arxiv.org/abs/2303.11580
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 軽い推論をアプリ内で処理し、難しい入力だけを元モデルへ渡す多段階推論を提案した。
- Objective: 表モデルの実時間提供で、別サービス呼出しによる通信・CPU・待ち時間を減らす。
- Methods: 推論法を簡素化して製品側へ埋め込み、残りを既存モデルへ送る構成をAutoMLで最適化。公開データと毎秒数百万判断の商用基盤で評価した。
- Data and results: 半数以上の入力を軽量経路で扱える場合が多く、商用基盤でレイテンシを約1/1.3、CPUを30%、前後段の通信を約50%削減した。
- Novelty: モデル自体の圧縮だけでなく、入力に応じた経路分岐と配置の変更で全体の推論費用を減らす。
- Limitations: 編者の注意: 削減幅はネットワーク構成と入力分布に依存する。要旨に予測精度の差はなく、軽量経路の誤判定や分布変化も個別に検証が必要。

### Paper: Long-term Forecasting with TiDE: Time-series Dense Encoder
- Source: arXiv
- Canonical ID: arxiv:2304.08424
- Publication date: 2023-04-17
- URL: https://arxiv.org/abs/2304.08424
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TiDEはMLP型encoder–decoderで共変量と非線形関係を扱い、長期予測を高速化する。
- Objective: 線形モデルの単純さ・速度と、実務に必要な非線形性・外部入力への対応を両立する。
- Methods: denseな時系列encoder–decoderを提案。単純な線形類似モデルを線形動的システム上で理論解析し、一般の構成を長期予測基準で比較した。
- Data and results: 仮定下で線形類似モデルの近最適な誤差率を証明。実験では先行法に匹敵または優れ、最良の比較Transformerより5–10倍高速だった。
- Novelty: 線形の強い基準を出発点に、MLPで共変量・非線形予測へ拡張した。
- Limitations: 編者の注意: 理論保証は線形類似モデルと仮定の範囲で、非線形モデル全体への保証ではない。速度倍率も構成・計算環境を伴う比較である。

### Paper: TABLET: Learning From Instructions For Tabular Data
- Source: arXiv
- Canonical ID: arxiv:2304.13188
- Publication date: 2023-04-25
- URL: https://arxiv.org/abs/2304.13188
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TABLETは自然言語の指示が表分類を助けるか、指示どおりに判断するかを評価する。
- Objective: ラベル収集の代わりになる指示から、LLMがどの程度正しく知識を使えるか測る。
- Methods: 20表データに表現・粒度・専門性の違う指示を付与し、その論理と構造的な変更も提供。zero-shotの改善と、例を与えても指示に従うかを調べた。
- Data and results: 指示によりF1が平均でFlan-T5 11Bは44%、ChatGPTは13%向上。一方、指示を無視し、例があっても特定の事例を誤判定した。
- Novelty: 言語知識による表予測の点数だけでなく、入力指示への忠実性を検証した。
- Limitations: 編者の注意: 改善率を絶対ポイントに換算しない。20データの特定モデルでの評価で、指示を与えればルール遵守や高リスク用途の安全性が保証されるわけではない。

### Paper: Statistical Foundations of Prior-Data Fitted Networks
- Source: arXiv
- Canonical ID: arxiv:2305.11097
- Publication date: 2023-05-18
- URL: https://arxiv.org/abs/2305.11097
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: PFNを頻度論的な事前調整済み予測器として捉え、標本数増加時の分散とバイアスを解析した。
- Objective: 小さな合成課題で学んだ固定モデルが、より大きな入力表でも改善する仕組みを説明する。
- Methods: 個々の標本への感度と、テスト特徴の近傍への局所化という条件から、予測器の分散・バイアスの消失を理論的に考察した。
- Data and results: 個別標本への感度が消えれば分散は消えるが、バイアスには適切な局所化が必要。現在のTransformer構造が確保するのは前者のみとする。
- Novelty: Bayes的な動機だけでなく、PFNの統計的挙動を固定予測器の頻度論的性質として説明した。
- Limitations: 編者の注意: 任意分布での一致性やバイアス消失を保証する結論ではない。入力表が大きいだけでは局所化条件を満たさず、有限標本の精度も別に評価する。

### Paper: On the Usefulness of Synthetic Tabular Data Generation
- Source: arXiv
- Canonical ID: arxiv:2306.15636
- Publication date: 2023-06-27
- URL: https://arxiv.org/abs/2306.15636
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 合成表が機械学習を実際に改善するか、共有・拡張・均衡化・要約の4用途で検証した。
- Objective: データ交換に使えることと、学習精度を高めることを分けて有用性を評価する。
- Methods: 4種類の用途で合成表を使った機械学習性能をベンチマークし、生成の進歩が下流の改善へつながるか比較した。
- Data and results: 一部データのクラス均衡化で小さな改善を観察したが、学習用合成表の有用性を広く主張するには証拠が不足すると結論した。要旨に数値はない。
- Novelty: もっともらしい分布の生成から、具体的な使い方ごとの下流利益へ評価の問いを移した。
- Limitations: 編者の注意: 証拠不足という結論はあらゆる合成法の無効性を証明しない。保護目的の共有と精度向上目的の拡張は異なり、利用条件を分けて読む。

### Paper: TabR: Tabular Deep Learning Meets Nearest Neighbors in 2023
- Source: arXiv
- Canonical ID: arxiv:2307.14338
- Publication date: 2023-07-26
- URL: https://arxiv.org/abs/2307.14338
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TabRはfeed-forwardモデルの中で近傍の学習例とラベルを参照し、表予測を改善する。
- Objective: 強いGBDTに対して、効率的な検索拡張で深層表モデルを強化する。
- Methods: 中間に独自のkNN型部品を置き、attentionに似た機構で近傍を探して特徴・ラベルから信号を得る。数百万例までの公開基準で比較した。
- Data and results: 深層法の平均で最良、複数データで新しい最良水準、GBDTに有利な基準でもGBDTを上回ったと報告。要旨に絶対スコアはない。
- Novelty: 単純なfeed-forward予測器へ、標本ごとに必要な学習例を検索する機構を効率的に統合した。
- Limitations: 編者の注意: ラベルを参照する検索集合は学習分に限定する必要がある。近傍索引・保存・取得の費用と、稀な例や分布変化での性能も考慮する。

### Paper: ReMasker: Imputing Tabular Data with Masked Autoencoding
- Source: arXiv
- Canonical ID: arxiv:2309.13793
- Publication date: 2023-09-25
- URL: https://arxiv.org/abs/2309.13793
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: ReMaskerは観測済みの値も追加で隠して復元を学び、自然に欠けた表の値を補完する。
- Objective: 単純なmasked autoencodingを使い、欠損率が高い表でも忠実で有用な補完を得る。
- Methods: 元の欠損に加え無作為にre-maskした観測値を再構成するよう学習し、そのモデルを実欠損へ適用。複数の欠損条件で忠実度と下流効用、表現の性質を検討した。
- Data and results: 比較法に匹敵または上回り、欠損率が高いほど優位が増える傾向。欠損に不変な表現を学ぶ理論的説明も示すが、要旨に誤差値はない。
- Novelty: 自然欠損を直接正解にできない問題を、観測値の再マスクによる自己教師あり課題で扱った。
- Limitations: 編者の注意: 人工的な再マスクと実際の欠損機構は同じとは限らない。特に値に依存して欠ける場合の不偏性や、補完の不確実性を保証しない。

### Paper: Time-LLM: Time Series Forecasting by Reprogramming Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2310.01728
- Publication date: 2023-10-03
- URL: https://arxiv.org/abs/2310.01728
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Time-LLMは時系列を再符号化して凍結LLMへ渡し、その出力から予測する。
- Objective: 時系列と言語の表現差を埋め、既存LLMの系列処理能力を予測へ転用する。
- Methods: 時系列patchをtext prototypeでreprogramし、Prompt-as-Prefixで文脈を加える。LLM本体を保ち、変換後のpatchを予測値へ投影した。
- Data and results: 専用の先行予測器を上回り、few-shot・zero-shotでも良好と報告。要旨に課題数、絶対誤差、推論費用はない。
- Novelty: 時系列用の巨大モデルを一から訓練する代わりに、既存言語モデルの凍結した計算を適応層から利用した。
- Limitations: 編者の注意: 本体の凍結と、周辺のreprogram・投影の学習費用を区別する。高性能という結果だけで言語的推論が改善原因とは確定せず、同予算の基準比較が必要。

### Paper: TimeGPT-1
- Source: arXiv
- Canonical ID: arxiv:2310.03589
- Publication date: 2023-10-05
- URL: https://arxiv.org/abs/2310.03589
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TimeGPT-1は大規模時系列で学んだ専用Transformerを、未見データの即時予測へ適用する。
- Objective: データごとのモデル作成を減らし、多分野の予測を追加訓練なしに提供する。
- Methods: 履歴窓へ局所位置符号を加えるencoder–decoderと線形出力層を用い、予測誤差を学習。既存の文章LLMを転用するモデルではない。
- Data and results: 確認したv3は公開時系列由来の1,000億超のデータ点で訓練。統計・ML・深層基準に対するzero-shotの精度・効率上の利点を報告した。
- Novelty: 時系列専用の大規模共有モデルを、分野をまたぐzero-shot推論へ展開した。
- Limitations: 編者の注意: 記載は著者の評価であり、確認箇所だけでは同じ学習コーパス・重みでの独立再現性を確定できない。『最初』という優先性の主張は採用せず、現行サービスの仕様とも区別する。

本文の照合箇所: [v3（2024-05-27）のSections 5.1–5.2、既存LLMとは異なる点と学習規模](https://arxiv.org/pdf/2310.03589v3)。

### Paper: iTransformer: Inverted Transformers Are Effective for Time Series Forecasting
- Source: arXiv
- Canonical ID: arxiv:2310.06625
- Publication date: 2023-10-10
- URL: https://arxiv.org/abs/2310.06625
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: iTransformerは時点でなく変数をtokenにし、attentionで変数間関係を学ぶ。
- Objective: 異質な測定を同じ時点tokenに混ぜる問題と、長い履歴での性能・計算量の問題を見直す。
- Methods: 各変数の時間履歴を埋め込んでtoken化し、attentionを変数間、feed-forwardを変数ごとの非線形表現へ適用。基本のTransformer部品は保持した。
- Data and results: 難しい実データで最良水準、異なる変数への汎化や長い履歴の利用改善を報告。要旨にデータ数と誤差値はない。
- Novelty: attention自体を改変する代わりに、時間と変数のどちらをtokenとするかを反転した。
- Limitations: 編者の注意: 多変量token間のattention費用は変数数に依存する。任意の履歴長を扱える設計と、すべての長さ・変数集合で精度が保証されることは異なる。

### Paper: Lag-Llama: Towards Foundation Models for Probabilistic Time Series Forecasting
- Source: arXiv
- Canonical ID: arxiv:2310.08278
- Publication date: 2023-10-12
- URL: https://arxiv.org/abs/2310.08278
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Lag-Llamaは遅延値を共変量として使う、単変量の確率予測基盤モデル。
- Objective: 多分野の事前学習を、新しい系列のzero-shot・少数データ適応へ利用する。
- Methods: decoder-only Transformerへlag特徴を入力し、多様な分野の系列コーパスで事前学習。未見データで追加学習なしと少量の微調整を分けて比較した。
- Data and results: zero-shotで強い汎化を示し、少量微調整では先行深層法を上回る平均性能を報告。要旨に課題数、確率予測スコア、計算費用はない。
- Novelty: 系列の過去値の構造を利用し、単変量の予測分布を多数データで共有する設計を示した。
- Limitations: 編者の注意: 最良平均という主張には微調整条件が含まれ、zero-shotの結果とは区別する。単変量の確率出力が多変量依存や全集団の校正を保証するわけではない。

### Paper: Mixed-Type Tabular Data Synthesis with Score-based Diffusion in Latent Space
- Source: arXiv
- Canonical ID: arxiv:2310.09656
- Publication date: 2023-10-14
- URL: https://arxiv.org/abs/2310.09656
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TabSynはVAEの共通潜在空間でscore-based拡散を学び、異種列の表を生成する。
- Objective: 列の型と分布の多様性をまとめて扱い、少ない逆拡散ステップで高品質な表を得る。
- Methods: 列間関係を捉えるVAEで混合型データを共通空間へ写し、潜在分布を拡散学習向けに整える。6データ、5指標で既存法と比較した。
- Data and results: 最も競争的な基準に対し、列単独分布の推定誤差を86%、列対相関の推定誤差を67%減らしたと報告。既存拡散より少ない逆ステップを用いた。
- Novelty: 異種列へ個別の拡散を当てるだけでなく、学習した連続潜在表現で生成をまとめた。
- Limitations: 編者の注意: 86%・67%は指定指標の相対誤差減少で、全下流課題の精度改善ではない。VAEの再構成と情報保護の誤差・保証も別に確認が必要。

### Paper: A decoder-only foundation model for time-series forecasting
- Source: arXiv
- Canonical ID: arxiv:2310.10688
- Publication date: 2023-10-14
- URL: https://arxiv.org/abs/2310.10688
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TimesFMは大量の系列をpatch単位で事前学習する、decoder-only型の予測基盤モデル。
- Objective: 系列ごとの専用訓練を減らし、異なる履歴長・予測長・頻度へ即座に対応する。
- Methods: patchを残差MLPで埋め込み、causal attentionのdecoderで処理。出力patchを別MLPで復元し、可変履歴に対応するマスクで事前学習した。
- Data and results: 確認したv3の主モデルは約2億パラメータ、実・人工を合わせ約1,000億時点で学習。未見の複数分野で、専用学習モデルに近いzero-shot性能を報告した。
- Novelty: 時系列の予測を、入力patchより大きい出力patchも生成できる共有decoderへまとめた。
- Limitations: 編者の注意: 当時版はデータ固有の動的・静的共変量を持たない構成で、追加情報のある専用モデルと条件が異なる。zero-shotは事前学習や計算費用が不要という意味ではない。

本文の照合箇所: [v3（2024-02-04）のSections 1・4・7、Appendix A.3–A.4](https://arxiv.org/html/2310.10688v3)。

### Paper: Efficient Bayesian Learning Curve Extrapolation using Prior-Data Fitted Networks
- Source: arXiv
- Canonical ID: arxiv:2310.20447
- Publication date: 2023-10-31
- URL: https://arxiv.org/abs/2310.20447
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: LC-PFNは学習曲線の事前分布で訓練し、途中の成績から将来性能の分布を高速に予測する。
- Objective: 学習曲線の外挿で、不確実性を表現しつつMCMCの計算負担を減らす。
- Methods: 既存のパラメトリック事前分布から作った1,000万の打切り人工曲線でPFNを学習。4ベンチマーク・53データの約2万実曲線へ適用した。
- Data and results: MCMCより正確な事後予測近似を1万倍超速く実行。予測早期停止は45データで2–6倍の高速化を示した。
- Novelty: 表の分類に限らないPFNの用途として、Bayes的な学習曲線推論の償却を実証した。
- Limitations: 編者の注意: 事前分布から外れる曲線や後半の急変は別途評価が必要。推論単体のMCMC比較と、事前学習費用・訓練全体の高速化を混同しない。

### Paper: Scaling TabPFN: Sketching and Feature Selection for Tabular Prior-Data Fitted Networks
- Source: arXiv
- Canonical ID: arxiv:2311.10609
- Publication date: 2023-11-17
- URL: https://arxiv.org/abs/2311.10609
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 初期TabPFNの入力規模の制約に対し、学習例と特徴の要約方法を比較した。
- Objective: 事前学習済みPFNを変えず、大きい表を入力へ収めるために何を残すべきか調べる。
- Methods: ラベル付き学習標本のsketchingと特徴選択を検討し、従来の表ごとに学習するモデルとの違いを分析した。
- Data and results: 要約法による挙動と従来モデルとの相違を初期調査として報告。要旨にデータ数、最良の要約法、精度・速度の数値はない。
- Novelty: モデル重みの訓練ではなく、in-context推論に渡す学習データの要約を最適化対象にした。
- Limitations: 編者の注意: 探索的な初期版TabPFNの研究であり、汎用的な大規模化の解決を保証しない。要約による少数クラスや希少特徴の消失も確認が必要。

### Paper: Mamba: Linear-Time Sequence Modeling with Selective State Spaces
- Source: arXiv
- Canonical ID: arxiv:2312.00752
- Publication date: 2023-12-01
- URL: https://arxiv.org/abs/2312.00752
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Mambaは入力に依存して状態空間の情報保持を変え、attentionなしで長い系列を処理する。
- Objective: 従来の準二次時間モデルが苦手だった、内容に応じた選択・推論を効率的に扱う。
- Methods: SSMのパラメータを入力の関数にし、選択的に伝達・忘却。畳み込みを使えなくなる部分をハードウェア対応の並列recurrent計算で処理する。
- Data and results: 系列長への線形拡張、Transformer比5倍の推論throughput、実データで百万長までの改善を報告。Mamba-3Bは同規模Transformerを上回り、倍規模に匹敵した。
- Novelty: 固定の状態遷移を入力依存に変え、内容選択と効率的なscan計算を統合した。
- Limitations: 編者の注意: 5倍は比較した構成・計算環境の結果。百万長で改善する実験を、全タスクで百万tokenの情報を正確に再現できる保証と解釈しない。

### Paper: Benchmarking Distribution Shift in Tabular Data with TableShift
- Source: arXiv
- Canonical ID: arxiv:2312.07577
- Publication date: 2023-12-10
- URL: https://arxiv.org/abs/2312.07577
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TableShiftは実務的な15の表分類で分布変化を定義し、頑健性を共通比較する。
- Objective: 表モデルの実利用で重要な、学習分布外への性能を体系的に測る。
- Methods: 金融・教育・政策・医療・市民参加などの二値15課題にshiftを付与。表向けモデルと頑健学習・domain generalization法を比較した。
- Data and results: IDとOOD精度には線形傾向。頑健手法は差を縮めてもID精度を下げる場合があり、ラベル分布の変化と性能差が強く関連した。
- Novelty: 画像・文章に偏りがちだった分布変化の評価を、表データの実務課題とモデルへ拡張した。
- Limitations: 編者の注意: ID–OOD差が小さいだけではOOD精度が高いとは限らない。定義された15種類の課題での経験的傾向で、あらゆる変化の原因や解決策を同定しない。

### Paper: TabMT: Generating tabular data with masked transformers
- Source: arXiv
- Canonical ID: arxiv:2312.06089
- Publication date: 2023-12-11
- URL: https://arxiv.org/abs/2312.06089
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TabMTはマスクされた特徴を予測するTransformerで、異種列と欠損を持つ表を生成する。
- Objective: 小規模から大規模までの表で、欠損にも対応する共通の合成データ生成器を作る。
- Methods: 表向けのmasked Transformerと改良マスキングを用い、生成と欠損を自然に扱う設計を評価。プライバシー重視の用途でも比較した。
- Data and results: 幅広い規模で高い生成性能、良好な品質とプライバシーの交換関係を報告。要旨にデータ数、規模の上下限、評価値はない。
- Novelty: マスク予測を、表の生成と欠損列の条件付き処理に共通利用した。
- Limitations: 編者の注意: 経験的なプライバシー評価は形式的な匿名性保証とは異なる。要旨だけでは攻撃条件や計算費用が分からず、全データへの優越性は確定しない。

### Paper: Rethinking Tabular Data Understanding with Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2312.16702
- Publication date: 2023-12-27
- URL: https://arxiv.org/abs/2312.16702
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 同じ内容でも表の構造が変わるとLLMが誤る問題を調べ、構造正規化と推論経路の統合を提案した。
- Objective: 表の構造への頑健性、文章・記号による推論の差、複数経路統合の効果を評価する。
- Methods: 内容を保った構造変形で性能を測り、正規化を導入。文章的・記号的推論の誤りを比較し、混合self-consistencyで出力を統合した。
- Data and results: 構造変動で特に記号推論が低下し、文章推論がわずかに優位だが強みは課題依存。統合でWikiTableQuestionsのaccuracy73.6%を得た。
- Novelty: 表QAを1種類の推論に固定せず、表の等価な構造と相補的な推論経路を扱った。
- Limitations: 編者の注意: WikiTableQuestionsの正解率は一般的な表分類や厳密な計算能力の指標ではない。複数経路は推論費用を増やし、誤りが独立とは限らない。

### Paper: Timer: Generative Pre-trained Transformers Are Large Time Series Models
- Source: arXiv
- Canonical ID: arxiv:2402.02368
- Publication date: 2024-02-04
- URL: https://arxiv.org/abs/2402.02368
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Timerは系列を共通形式へまとめ、次token予測で予測・補完・異常検知へ適応する。
- Objective: データが少ない実務で、課題ごとの小モデルを一から学習する制約を減らす。
- Methods: 最大10億時点の系列をsingle-series sequence（S3）形式へ統一し、GPT型の生成事前学習を実施。3種類の解析を共通生成課題へ変換した。
- Data and results: 予測・補完・異常検知への適応と、少数例一般化・規模拡張の可能性を示した。要旨に各課題の具体的スコアはない。
- Novelty: 系列形式と下流課題を生成へ揃え、同じ事前学習から複数用途へ展開した。
- Limitations: 編者の注意: 下流への適応を含む結果で、すべての課題の無調整zero-shotを意味しない。現在のモデル群と比べるときも、版・学習規模・入力条件を揃える必要がある。

### Paper: Unified Training of Universal Time Series Forecasting Transformers
- Source: arXiv
- Canonical ID: arxiv:2402.02592
- Publication date: 2024-02-04
- URL: https://arxiv.org/abs/2402.02592
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Moiraiは異なる頻度・変数数・分布を持つ系列を一つのmasked encoderで学ぶ。
- Objective: 1データ1モデルを超え、多様な下流予測へ共通の大規模学習を利用する。
- Methods: 複数patch長、any-variate attention、混合分布を備える構造と統一学習を提案。9分野・270億超の観測を持つLOTSAで事前学習した。
- Data and results: 分布内・分布外で確率予測と長期予測を評価し、zero-shotでもfull-shotモデルに匹敵または優位な性能を報告。要旨に課題別の誤差値はない。
- Novelty: 単変量・単一頻度へ限定せず、異なる変数数や出力分布を共通訓練へまとめた。
- Limitations: 著者は高次元系列への対応の制限、patch長の設定がheuristicな点、データの領域・頻度の多様性不足を指摘。構造上の柔軟性を無制限の規模対応と解釈しない。

本文の照合箇所: [v1のMethodの構成・Problem Formulation、ConclusionのLimitations & Future Work](https://arxiv.org/html/2402.02592v1)。

### Paper: MOMENT: A Family of Open Time-series Foundation Models
- Source: arXiv
- Canonical ID: arxiv:2402.03885
- Publication date: 2024-02-06
- URL: https://arxiv.org/abs/2402.03885
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: MOMENTは公開系列を集め、マスク復元で学んだ表現を複数の時系列課題へ使う公開モデル群。
- Objective: 共通データ不足と多様な系列の違いを乗り越え、少ない教師情報で汎用解析を行う。
- Methods: Time-series Pileを構築し、非重複patchをマスクして軽量headで復元するTransformerを学習。予測・分類・異常検知・補完をzero-shotやlinear probing等で評価した。
- Data and results: 少量データと限定的な課題適応で有効な結果を報告。本文では課題に応じてzero-shotと数epochのlinear probingを使い分けている。
- Novelty: 単一予測課題だけでなく、公開データ・事前学習・少教師量の多課題評価をまとめて提供した。
- Limitations: 編者の注意: 全課題が無調整ではない。比較値の一部は既報の値を採用しており、全モデルの完全に同条件の再実装比較ではない点を確認して読む。

本文の照合箇所: [Sections 3.2–3.3・4、Appendix FのResults Sources](https://arxiv.org/html/2402.03885v1)。

### Paper: Systematic Assessment of Tabular Data Synthesis
- Source: arXiv
- Canonical ID: arxiv:2402.06806
- Publication date: 2024-02-09
- URL: https://arxiv.org/abs/2402.06806
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 表生成を忠実度・保護・効用の3軸で調べ、統計法と深層法の得意条件を比較した。
- Objective: 評価指標や調整条件の違いにより、生成器の優劣が食い違う問題を改善する。
- Methods: Wasserstein距離、membership disclosure、下流予測・queryの評価と統一調整をSynMeterへ実装。8種類の生成器を12データで比較した。
- Data and results: 単一の勝者はなく、TabDDPMは忠実度・効用で強いがmembershipリスクが大きかった。DPが必要な条件では統計法が深層法を上回った。
- Novelty: 新旧の生成器を、デフォルト値だけに頼らず調整と3軸の共通基準で評価した。
- Limitations: 編者の注意: v1の表と本文で一部のDP/HP分類が一致しないため、保証の有無は各手法の原著を優先する。実験上の情報漏洩評価を形式的DP保証と混同しない。

本文の照合箇所: [v1（初版題名Towards Principled Assessment...）のIntroduction・Main Findings・評価設計、Table 1とHPの本文記述](https://arxiv.org/html/2402.06806v1)。

### Paper: TuneTables: Context Optimization for Scalable Prior-Data Fitted Networks
- Source: arXiv
- Canonical ID: arxiv:2402.11137
- Publication date: 2024-02-17
- URL: https://arxiv.org/abs/2402.11137
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TuneTablesは大きい表を小さな学習済み文脈へ圧縮し、初期PFNの規模制約を緩める。
- Objective: 約1,000行を超える表にもPFNを利用し、精度とパラメータ効率を高める。
- Methods: parameter-efficientなcontext optimizationで学習データを圧縮。19アルゴリズム・98データで比較し、解釈と公平性目的による調整も検討した。
- Data and results: TabPFNの5%未満のパラメータを最適化し、平均でCatBoostを含む比較法より最良の性能を報告。要旨に平均スコアの数値はない。
- Novelty: 固定PFNへ渡す文脈をデータから学び、表ごとの小規模な適応を可能にした。
- Limitations: 編者の注意: 元の重み更新不要の推論とは異なり、文脈の最適化に学習費用を要する。公平性目的での改善は、選んだ公平性指標以外の保証ではない。

### Paper: HyperFast: Instant Classification for Tabular Data
- Source: arXiv
- Canonical ID: arxiv:2402.14335
- Publication date: 2024-02-22
- URL: https://arxiv.org/abs/2402.14335
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: HyperFastはデータセットから専用分類ネットワークを生成し、表ごとの訓練を短縮する。
- Objective: 表分類での長い学習とハイパーパラメータ探索を、メタ学習済みの生成器で減らす。
- Methods: hypernetworkをメタ訓練し、新しい表に合ったニューラルネットを1回の前向き計算で作る。OpenMLとゲノムでニューラル法、木、AutoMLを比較した。
- Data and results: 少量または微調整なしで競争的な性能と大きな速度改善を報告。要旨にデータ数・速度倍率・平均精度はない。
- Novelty: 予測器を各表で最適化する代わりに、予測器の重みをデータから生成する設計へ移した。
- Limitations: 編者の注意: 新課題での訓練不要と、メタ訓練の費用が不要であることは異なる。未経験の規模・特徴型への汎化と全体費用は個別評価が必要。

### Paper: UniTS: A Unified Multi-Task Time Series Model
- Source: arXiv
- Canonical ID: arxiv:2403.00131
- Publication date: 2024-02-29
- URL: https://arxiv.org/abs/2403.00131
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: UniTSはtask tokenizationで生成・予測の複数時系列課題を一つの枠組みへまとめる。
- Objective: 予測だけに偏らず、異なる領域と課題の要求へ共通表現を転用する。
- Methods: 改良Transformerとtask tokenを使い、異なる動態・標本化率・時間尺度で多領域事前学習。38データで4課題、few-shot・prompt適応と単独課題も比較した。
- Data and results: 予測12、分類20、異常検知18、補完16の比較モデルに対する優位を報告。単独課題でも専用法を上回ったが、要旨に絶対スコアはない。
- Novelty: 予測専用の事前学習を超え、生成・識別課題をtask tokenで共通の処理へ統合した。
- Limitations: 編者の注意: 38データでの多課題結果を任意課題への普遍性としない。prompt、few-shot、単独課題は学習・評価条件が異なるため分けて比較する。

### Paper: Chronos: Learning the Language of Time Series
- Source: arXiv
- Canonical ID: arxiv:2403.07815
- Publication date: 2024-03-12
- URL: https://arxiv.org/abs/2403.07815
- read_level: full_text
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: Chronosは数値を語彙へ量子化し、時系列自体で事前学習する確率的な予測基盤モデル。
- Objective: 異なる分野の系列を共有学習し、新しいデータでも追加学習なしの予測を得る。
- Methods: scale調整・量子化した値をT5型へ入力し、cross-entropyで学習。公開系列にGaussian processの人工系列を追加し、2,000万–7.1億パラメータを評価した。
- Data and results: 42データは訓練と重なる15、未見27に分かれる。未見群の集約確率予測でChronosモデルが2・3位となり、多くの課題専用モデルを上回った。
- Novelty: 言語モデル構造を数値のtoken生成へ利用し、異種系列を横断した確率予測へ展開した。
- Limitations: 著者は指数トレンドの難しさと短い履歴での傾向過小評価を示す。未見27課題でも厳密な全データの時間分離には注意を付記しており、42件すべてをzero-shot評価と扱わない。

本文の照合箇所: [v2のSections 5.1・5.5.2（脚注4）・5.7、15対27の評価区分](https://arxiv.org/html/2403.07815v2)。

### Paper: Structured Evaluation of Synthetic Tabular Data
- Source: arXiv
- Canonical ID: arxiv:2403.10424
- Publication date: 2024-03-15
- URL: https://arxiv.org/abs/2403.10424
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: 合成表が元表と同じ分布に従うという共通目標から、生成評価指標を構造的に整理する。
- Objective: 多数の忠実度・効用指標を、何を測り何を見落とすか一貫して解釈する。
- Methods: 単一の数学的目標を構造分解し、既存の分布・下流・モデル依存の指標を統合。指標集合の完全性、新指標群、モデル不要の基準を考察した。
- Data and results: 表の構造を明示する生成器が、特に小データで他法を上回った。要旨にデータ数や分布距離の具体値はない。
- Novelty: 指標の羅列ではなく、共通分布目標の分解として評価の網羅性を論じた。
- Limitations: 編者の注意: 観測標本の分布への適合と、真の母集団への適合は異なる。同分布の再現を目指しても個人情報保護は自動達成されず、別評価が必要。

### Paper: TabPFGen -- Tabular Data Generation with TabPFN
- Source: arXiv
- Canonical ID: arxiv:2406.05216
- Publication date: 2024-06-07
- URL: https://arxiv.org/abs/2406.05216
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TabPFGenは分類用TabPFNをエネルギー関数に利用し、表の生成・補完へ展開する。
- Objective: 表で強い識別モデルと生成モデルの構造の隔たりを減らす。
- Methods: 事前学習済みTabPFNを含むエネルギーベース生成器を設計し、追加訓練・調整なしで標本生成。データ拡張、クラス均衡化、欠損補完を評価した。
- Data and results: 標準的な生成課題で良好な結果を報告するが、要旨にデータ数、忠実度・下流精度・補完誤差の数値はない。
- Novelty: 識別用in-contextモデルを生成へ変換し、再学習なしの表生成という利用を示した。
- Limitations: 編者の注意: 追加訓練不要でもサンプリング費用は残る。合成データの効用・分布忠実度・プライバシーは別指標で、生成できることだけでは安全な匿名化を保証しない。

### Paper: TALENT: A Tabular Analytics and Learning Toolbox
- Source: arXiv
- Canonical ID: arxiv:2407.04057
- Publication date: 2024-07-04
- URL: https://arxiv.org/abs/2407.04057
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TALENTは20超の表向け深層法と前処理を共通の環境に集める比較用ツールボックス。
- Objective: 特徴の扱い・目的関数・構造の違うモデルを、使い、分析し、公平に比較しやすくする。
- Methods: 多様なencoding・正規化部品と予測モデルを統一interfaceへ実装。事例を示し、同じ環境で各法の性能を比較した。
- Data and results: 20超の深層予測法を含む公開基盤を提供。要旨にデータセット数や最良モデルのスコアはない。
- Novelty: 論文ごとに分散した実装と処理手順を、拡張可能な共通比較基盤へまとめた。
- Limitations: 編者の注意: 実装が共通でも、探索予算・早期停止・分割の違いを揃える必要がある。収録法数は公開時点の情報であり、現在のツール仕様を示す記述ではない。

### Paper: Better by Default: Strong Pre-Tuned MLPs and Boosted Trees on Tabular Data
- Source: arXiv
- Canonical ID: arxiv:2407.04491
- Publication date: 2024-07-05
- URL: https://arxiv.org/abs/2407.04491
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: RealMLPと木モデルの強い既定値を、メタ訓練と独立評価で作り、表ごとの探索負担を減らす。
- Objective: 深層法の大量調整と、実務での速い木モデルという比較条件の差を見直す。
- Methods: 118データのmeta-trainでMLPと既定値を調整し、別90データとGBDT-friendly基準で評価。1,000–500,000例を扱い、RealMLPとGBDTの組合せも検討した。
- Data and results: RealMLPは良好な時間・精度の交換関係でGBDTに競争的。改善既定値を持つ両者の組合せは、表ごとの探索なしで高性能だった。
- Novelty: 新構造だけでなく、異なる表群で事前調整した既定値を独立表で検証し、実用的な基準を強化した。
- Limitations: 編者の注意: 『探索なし』でも既定値作成のメタ調整はある。選定した中・大規模データの結果で、少数例・極端な欠損・新領域では再評価が必要。

### Paper: TabM: Advancing Tabular Deep Learning with Parameter-Efficient Ensembling
- Source: arXiv
- Canonical ID: arxiv:2410.24210
- Publication date: 2024-10-31
- URL: https://arxiv.org/abs/2410.24210
- read_level: abstract
- Tags: 基礎文献, 表形式・時系列・因果推論
- Summary: TabMはパラメータを共有する複数MLPの予測を統合し、精度と効率の両立を狙う。
- Objective: 複雑なattention・検索構造に頼らず、表向けMLPの性能を改善する。
- Methods: 大半の重みを共有する暗黙のMLP群を同時学習し、1標本あたり複数予測を生成。公開基準で精度・効率を比較し、個別予測と集合の挙動も分析した。
- Data and results: 表向け深層比較法で最良の性能と良好な効率を報告。個別の予測は弱いが集合すると強く、要旨に具体的な平均スコア・費用はない。
- Novelty: 独立した多数モデルの訓練を避け、共有パラメータによるアンサンブルを表の基準モデルへ取り入れた。
- Limitations: 編者の注意: 共有モデルの集合は独立なdeep ensembleと同じではない。深層法内の順位と木を含む全手法への優越性、予測の校正・不確実性は区別する。

<!-- PAPER_IDS -->
arxiv:1301.2312
arxiv:1509.09259
arxiv:1510.04342
arxiv:1512.05469
arxiv:1603.02754
arxiv:1605.03661
arxiv:1605.06336
arxiv:1606.01865
arxiv:1606.07035
arxiv:1608.00060
arxiv:1610.01271
arxiv:1611.04035
arxiv:1612.09596
arxiv:1701.08687
arxiv:1702.07306
arxiv:1704.04110
arxiv:1705.08821
arxiv:1706.09516
arxiv:1803.01422
arxiv:1805.10572
arxiv:1809.08830
arxiv:1811.11264
arxiv:1901.09475
arxiv:1904.10098
arxiv:1905.10437
arxiv:1906.02120
arxiv:1906.04477
arxiv:1906.06211
arxiv:1907.00235
arxiv:1907.00503
arxiv:1907.02893
arxiv:1907.04809
arxiv:1908.05659
arxiv:1908.07442
arxiv:1909.02060
arxiv:1909.04939
arxiv:1909.06312
arxiv:1910.13051
arxiv:1912.09363
arxiv:2002.12710
arxiv:2003.03191
arxiv:2006.04697
arxiv:2006.06465
arxiv:2006.06981
arxiv:2007.01434
arxiv:2009.14461
arxiv:2010.05761
arxiv:2011.08411
arxiv:2012.06678
arxiv:2012.07436
arxiv:2012.08791
arxiv:2101.01134
arxiv:2101.07732
arxiv:2102.00457
arxiv:2104.10334
arxiv:2105.02584
arxiv:2106.00750
arxiv:2106.01342
arxiv:2106.10466
arxiv:2106.11959
arxiv:2106.13008
arxiv:2106.14112
arxiv:2106.15147
arxiv:2107.03502
arxiv:2107.11059
arxiv:2111.00396
arxiv:2112.10510
arxiv:2201.12740
arxiv:2201.12886
arxiv:2202.01575
arxiv:2202.04208
arxiv:2202.08516
arxiv:2204.00401
arxiv:2205.13504
arxiv:2206.00664
arxiv:2206.08564
arxiv:2207.01848
arxiv:2207.08815
arxiv:2208.05949
arxiv:2209.15421
arxiv:2210.02186
arxiv:2210.04018
arxiv:2210.06280
arxiv:2210.10723
arxiv:2211.14730
arxiv:2302.11939
arxiv:2303.06053
arxiv:2303.11580
arxiv:2304.08424
arxiv:2304.13188
arxiv:2305.11097
arxiv:2306.15636
arxiv:2307.14338
arxiv:2309.13793
arxiv:2310.01728
arxiv:2310.03589
arxiv:2310.06625
arxiv:2310.08278
arxiv:2310.09656
arxiv:2310.10688
arxiv:2310.20447
arxiv:2311.10609
arxiv:2312.00752
arxiv:2312.07577
arxiv:2312.06089
arxiv:2312.16702
arxiv:2402.02368
arxiv:2402.02592
arxiv:2402.03885
arxiv:2402.06806
arxiv:2402.11137
arxiv:2402.14335
arxiv:2403.00131
arxiv:2403.07815
arxiv:2403.10424
arxiv:2406.05216
arxiv:2407.04057
arxiv:2407.04491
arxiv:2410.24210
<!-- /PAPER_IDS -->
