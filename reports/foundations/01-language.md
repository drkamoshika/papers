# 基礎文献 — 言語モデルの学習・推論・効率化

> schema_version: 1
> report_date: 2026-11-14

## ダイジェスト

選定101件中、以下は原著照合・編集確認を終えた85件。選定リストだけの論文を完成済み件数には含めない。原著要旨までの記述と本文確認を区別し、Limitationsの「編者の注意」は著者の自己申告と区別する。

研究の流れと2026年論文との接続は [文献集の案内](README.md) を参照。

## 完全版レポート

### Paper: Efficient Estimation of Word Representations in Vector Space
- Source: arXiv
- Canonical ID: arxiv:1301.3781
- Publication date: 2013-01-16
- URL: https://arxiv.org/abs/1301.3781
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 大規模データから効率的に単語ベクトルを推定する新しいモデルを提案した。
- Objective: どのようなアーキテクチャが、計算コストを抑えつつ高品質な単語表現を学習できるか？
- Methods: 二つの新規モデルアーキテクチャを用いて、非常に大規模なデータセットから連続的な単語ベクトルを算出・比較した。
- Data and results: 提案手法は、以前の最良技術と比較して高い精度を示し、16億単語のデータセットから1日未満で学習可能であった。
- Novelty: 計算コストを大幅に削減しながら、最高水準の性能を持つ単語表現を生成するモデルを提案した点。
- Limitations: 編者の注意: 静的な単語ベクトルの類似・関係評価であり、文脈で変わる語義や文章全体の意味は直接モデル化しない。

### Paper: Distributed Representations of Words and Phrases and their Compositionality
- Source: arXiv
- Canonical ID: arxiv:1310.4546
- Publication date: 2013-10-16
- URL: https://arxiv.org/abs/1310.4546
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 単語の分散表現が持つ順序性や慣用句への対応を改善する手法を提案した。
- Objective: 単語埋め込みが持つ、単語の順序や慣用的なフレーズの意味を捉えられないという限界を克服すること。
- Methods: 頻出単語のサブサンプリングによる高速化と、階層的ソフトマックスの代替としてネガティブサンプリングを用いる手法を提案した。
- Data and results: フレーズ単位で良好なベクトル表現を学習することが可能であり、これにより「Air Canada」のような複合的な意味表現が可能になった。
- Novelty: 単語埋め込みが持つ順序性や慣用句への対応の限界を克服するため、フレーズ単位でのベクトル表現学習法を提案した点。
- Limitations: 編者の注意: フレーズ抽出と静的なベクトル表現を用いる。句を学習することと、任意の語順・構文・文脈依存意味を理解することは区別する。

### Paper: Neural Machine Translation by Jointly Learning to Align and Translate
- Source: arXiv
- Canonical ID: arxiv:1409.0473
- Publication date: 2014-09-01
- URL: https://arxiv.org/abs/1409.0473
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: アライメントと翻訳を同時に学習するニューラル機械翻訳モデルを提案した。
- Objective: 固定長ベクトルがボトルネックであるという仮説に基づき、より良い翻訳性能を目指す。
- Methods: エンコーダ・デコーダ構造に、ターゲット単語予測に必要なソース文部分を自動で検索する機構を追加した。
- Data and results: この新しいアプローチにより、英語-フランス語翻訳タスクで既存の最先端のフレーズベースシステムに匹敵する性能を達成した。
- Novelty: 固定長ベクトルを用いる代わりに、関連するソース文部分をソフトに検索可能にした点である。
- Limitations: 編者の注意: 英仏翻訳での実証が中心である。学習されたsoft alignmentの重みを、そのまま一般的な因果説明と解釈しない。

### Paper: Sequence to Sequence Learning with Neural Networks
- Source: arXiv
- Canonical ID: arxiv:1409.3215
- Publication date: 2014-09-10
- URL: https://arxiv.org/abs/1409.3215
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: LSTMを用いたエンドツーエンドな系列学習アプローチを提案し、機械翻訳タスクで高い性能を示した。
- Objective: DNNが苦手とする系列から系列へのマッピングを行う汎用的な手法を確立すること。
- Methods: 入力系列を固定次元のベクトルに写像する多層LSTMと、そのベクトルからターゲット系列をデコードする別の深層LSTMを用いるエンドツーエンドなアプローチを採用した。
- Data and results: WMT'14の英仏翻訳タスクにおいて、提案されたLSTMはBLEUスコア34.8を達成し、従来のフレーズベースSMT（33.3）を上回った。さらに、SMTが出力した仮説のリランキングにも利用可能であった。
- Novelty: 系列構造に最小限の仮定しか置かない、汎用的なエンドツーエンドな系列学習アプローチを提案した点。
- Limitations: 編者の注意: 原著の主な検証は翻訳であり、固定長の中間表現を使う。この論文単独では、後続のattention方式や現代の長期エージェントへの優位性は評価されない。

### Paper: Adam: A Method for Stochastic Optimization
- Source: arXiv
- Canonical ID: arxiv:1412.6980
- Publication date: 2014-12-22
- URL: https://arxiv.org/abs/1412.6980
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: Adamは、適応的な低次モーメント推定に基づく最適化手法である。
- Objective: 確率的目的関数の勾配ベースの最適化のための新しいアルゴリズムを提案すること。
- Methods: 勾配の低次モーメントの適応的推定を利用し、実装が容易で計算効率が高い方法を用いる。
- Data and results: 実証結果から、Adamは他の確率的最適化手法と比較して良好に機能することが示された。
- Novelty: 勾配の低次モーメントの適応的な推定を使い、データ・パラメータ規模、勾配の疎性やノイズへ対応する更新則を設計する。
- Limitations: 編者の注意: 要旨で述べる理論的なregret解析はオンライン凸最適化の枠組みに属する。大規模な非凸ニューラルネットワークで常に最適解へ収束するという保証ではない。

### Paper: Trust Region Policy Optimization
- Source: arXiv
- Canonical ID: arxiv:1502.05477
- Publication date: 2015-02-19
- URL: https://arxiv.org/abs/1502.05477
- read_level: full_text
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 理論的に単調改善する方策更新を出発点に、実用的な近似アルゴリズムTRPOを構成する。
- Objective: どのようにして理論的に正当化されたポリシー最適化の手順を実用的なアルゴリズムに近似できるか？
- Methods: 新旧方策のKLで更新幅を制約し、実装では全状態での最大KLを平均KLへ近似する。目的・制約をサンプルで推定して、大きい非線形方策を最適化する。
- Data and results: シミュレーションロボットの遊泳、ホッピング、歩行ガイト学習やAtariゲームでのプレイにおいて堅牢な性能を示した。
- Novelty: 理論的根拠に基づいた手順を近似し、実用的なTRPOアルゴリズムとして開発された点。
- Limitations: 最大KLに基づく理論と平均KL等の実用近似を区別する。本文のAtari比較は各課題1試行で、時間制約により誤差統計を得られず、試行間変動が大きいと著者が明記する。

本文の照合箇所: [4、5、8.1、8.2節・表1注記](https://arxiv.org/pdf/1502.05477)。

### Paper: Distilling the Knowledge in a Neural Network
- Source: arXiv
- Canonical ID: arxiv:1503.02531
- Publication date: 2015-03-09
- URL: https://arxiv.org/abs/1503.02531
- read_level: full_text
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 複数のモデルの知識を単一モデルに圧縮する手法を提案し、性能向上を目指す。
- Objective: アンサンブル学習の予測を計算コストを抑えつつ実現する方法を探る。
- Methods: 教師のsoftmax温度を上げたsoft target分布へ生徒を合わせ、正解ラベルがあればhard targetの交差エントロピーも組み合わせる。推論時は温度1に戻す。
- Data and results: MNISTの小型ネットでは通常学習の146誤りが蒸留で74誤り、教師は67誤り。音響実験では10モデルensembleのWER 10.7%を単一蒸留モデルでも達成し、通常単体10.9%を改善。
- Novelty: 教師の正答クラスだけでなく低確率のクラス間関係もsoft targetで渡す。温度を使った分布の移転と、専門家ensembleの構成を提示する。
- Limitations: 本文では小さすぎる生徒が教師を完全には模倣できず、温度の選択で効果が変わることを示す。主な実証はMNIST・音響等であり、教師の誤りや偏りの除去を保証しない。

本文の照合箇所: [1、2、3、4.1節・表1](https://arxiv.org/html/1503.02531v1)。

### Paper: You Only Look Once: Unified, Real-Time Object Detection
- Source: arXiv
- Canonical ID: arxiv:1506.02640
- Publication date: 2015-06-08
- URL: https://arxiv.org/abs/1506.02640
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: YOLOは物体検出を回帰問題として捉え、単一ネットワークでリアルタイムに実行する手法である。
- Objective: 従来の物体検出アプローチの課題を克服し、高速かつ高精度な統一的な検出フレームワークを提案すること。
- Methods: 物体検出をバウンディングボックスとクラス確率の回帰問題として定式化し、単一ニューラルネットワークで全画像から直接予測する。
- Data and results: ベースモデルは45 fpsでリアルタイム処理が可能であり、Fast YOLOは155 fpsを達成し、他の実時間検出器より高いmAPを示した。
- Novelty: 物体検出パイプライン全体を単一のネットワークとして最適化できるため、極めて高速な統一アーキテクチャを実現した点。
- Limitations: 著者は当時の最先端検出系より位置推定の誤りが多い一方、存在しない対象への誤検出が少ないと報告。fpsは原著のモデル・実行条件であり、現行端末での値ではない。

### Paper: Effective Approaches to Attention-based Neural Machine Translation
- Source: arXiv
- Canonical ID: arxiv:1508.04025
- Publication date: 2015-08-17
- URL: https://arxiv.org/abs/1508.04025
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: アテンション機構を用いたNMTの有効なアーキテクチャを提案する。
- Objective: アテンションベースのNMTに有用なアーキテクチャを探求すること。
- Methods: グローバルアプローチとローカルアプローチという二つのアテンション機構クラスを検証した。
- Data and results: ローカルアテンションにより、非アテンショナルシステムより5.0 BLEUポイントの向上が見られた。
- Novelty: 文全体を見るglobal attentionと一部を見るlocal attentionを比較し、注意位置の設計が翻訳品質に与える影響を検証する。
- Limitations: 編者の注意: 改善値は採用した翻訳データ・非attention比較系に対するもの。local attentionの範囲設計と長距離依存の扱いは別途検討が必要である。

### Paper: Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks
- Source: arXiv
- Canonical ID: arxiv:1511.06434
- Publication date: 2015-11-19
- URL: https://arxiv.org/abs/1511.06434
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 深層畳み込み敵対的生成ネットワーク（DCGAN）を提案し、教師なし学習におけるCNNの可能性を示した。
- Objective: 教師あり学習で成功したCNNと教師なし学習とのギャップを埋めることを目指す。
- Methods: 特定のアーキテクチャ制約を持つ深層畳み込み敵対的生成ネットワーク（DCGANs）というクラスのCNNを導入し、様々な画像データセットで訓練を行った。
- Data and results: 提案された敵対的ペアが、ジェネレータとディスクリミネータの両方において、物体部分からシーンに至る階層的な表現を学習することを示した。これらの特徴は新規タスクにも適用可能である。
- Novelty: 特定のアーキテクチャ制約を持つ深層畳み込み敵対的生成ネットワーク（DCGANs）というクラスのCNNを導入した点。
- Limitations: 編者の注意: 提案するCNN構造と画像データでの教師なし表現評価である。画像の視覚的な良さと、密度推定や生成の完全性は同一指標ではない。

### Paper: An Analysis of Deep Neural Network Models for Practical Applications
- Source: arXiv
- Canonical ID: arxiv:1605.07678
- Publication date: 2016-05-24
- URL: https://arxiv.org/abs/1605.07678
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: DNNの性能評価には、精度以外にリソース利用の考慮が重要である。
- Objective: 実用的な応用において、単なる精度だけでなくどのような指標を考慮すべきか？
- Methods: 本研究では、精度、メモリフットプリント、パラメータ数、演算回数、推論時間、消費電力といった複数の重要な指標を用いて包括的な分析を行った。
- Data and results: 評価したDNNの測定から、精度と推論時間の関係、エネルギー制約と到達可能な精度・複雑性、演算量と推論時間の関係を分析。精度以外の資源指標を設計判断に含める必要性を示す。
- Novelty: 本研究は、効率的なDNNの設計とエンジニアリングを支援する情報を提供する点にある。
- Limitations: 編者の注意: 原著の画像分類モデル・実測環境に関する経験的分析である。電力とバッチサイズ等の関係を、すべての現代LLM・ハードウェアで成り立つ法則と解釈しない。

### Paper: Concrete Problems in AI Safety
- Source: arXiv
- Canonical ID: arxiv:1606.06565
- Publication date: 2016-06-21
- URL: https://arxiv.org/abs/1606.06565
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: AIの事故リスクに関する具体的な研究課題を分類し、議論する論文である。
- Objective: 機械学習システムにおける意図しない有害な振る舞いという事故リスクの問題点を特定すること。
- Methods: 誤った目的関数、評価困難性、学習中の望ましくない挙動に基づき、5つの実用的な研究問題として分類した。
- Data and results: 副作用の回避、報酬ハッキングの回避、拡張可能な監督、安全な探索、分布変化の5課題を整理。原因を目的関数、監督の費用、学習中の挙動に分けて先行研究と方向性を示す。
- Novelty: 事故リスクの原因を目的関数の誤りや学習過程の問題に分類し、体系的に議論している点。
- Limitations: 編者の注意: 課題を定義する研究アジェンダであり、5課題を解決する単一手法や事故率の定量的低減を実証した研究ではない。

### Paper: Gaussian Error Linear Units (GELUs)
- Source: arXiv
- Canonical ID: arxiv:1606.08415
- Publication date: 2016-06-27
- URL: https://arxiv.org/abs/1606.08415
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 提案されたGELUは、標準正規分布の累積分布関数を用いた高性能な活性化関数である。
- Objective: どのような活性化関数が様々なタスクで高い性能を発揮するかを検証すること。
- Methods: GELUを提案し、$x ext{Φ}(x)$として定義した。ReLUやELUと比較するため、実証的な評価を実施した。
- Data and results: 本研究では、考慮された全てのコンピュータビジョン、自然言語処理、および音声タスクにおいて性能向上を確認した。
- Novelty: ReLUのように符号で切り替える代わりに、標準正規分布の累積確率Phi(x)で入力xを重み付けする滑らかな活性化関数を提案する。
- Limitations: 編者の注意: 比較した視覚・言語・音声タスクでの実験結果であり、全アーキテクチャで常に優れるという保証ではない。

### Paper: Layer Normalization
- Source: arXiv
- Canonical ID: arxiv:1607.06450
- Publication date: 2016-07-21
- URL: https://arxiv.org/abs/1607.06450
- read_level: full_text
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 層正規化は、バッチサイズ依存性の問題を解決しRNNへの適用を容易にする手法である。
- Objective: バッチ正規化の課題点を克服し、再帰型ニューラルネットワーク（RNN）に適用可能な正規化手法を提案すること。
- Methods: 単一事例・単一層内で平均と分散を求め、学習可能なgainとbiasを適用する。RNNでは時点ごとに統計量を計算し、batch normalization等と不変性と学習挙動を比較。
- Data and results: 本文6節では画像言語埋め込み、読解、文章表現、MNIST、筆跡などで評価。小バッチ・長系列のRNNで特に有効で、学習時と推論時に同じ計算を使う。
- Novelty: 本手法は、ミニバッチ全体ではなく単一訓練ケース内の全入力から統計量を計算する点に新規性がある。
- Limitations: 本文6.7節のCNN予備実験ではbatch normalizationが上回った。著者は空間位置ごとの統計の違いを挙げ、ConvNetでの追加研究が必要と述べる。

本文の照合箇所: [3、6.6、6.7、7節](https://arxiv.org/html/1607.06450v1)。

### Paper: Variational Lossy Autoencoder
- Source: arXiv
- Canonical ID: arxiv:1611.02731
- Publication date: 2016-11-08
- URL: https://arxiv.org/abs/1611.02731
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: VAEと自己回帰モデルを組み合わせ、グローバルな表現学習を実現する手法を提案した。
- Objective: データからタスクに適したグローバルな潜在表現をどのように学習できるかを探求すること。
- Methods: VAEにRNNやMADEなどのニューラル自己回帰モデルを組み込み、事前分布$p(z)$とデコード分布$p(x|z)$として利用する。
- Data and results: このアプローチにより、MNISTなどで最先端の結果を達成し、グローバルな潜在コードがテクスチャのような無関係な情報を破棄できることを示した。
- Novelty: VAEに自己回帰モデルを統合することで、潜在空間の学習内容を制御し、情報損失型のエンコーディングが可能になった点。
- Limitations: 編者の注意: 潜在表現が捨てる情報はアーキテクチャで誘導される。ある画像課題で不要なテクスチャが、別の臨床・科学課題でも不要とは限らない。

### Paper: Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer
- Source: arXiv
- Canonical ID: arxiv:1701.06538
- Publication date: 2017-01-23
- URL: https://arxiv.org/abs/1701.06538
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 疎なゲート機構を持つMoE層でモデル容量を大幅に向上させる手法を提案した。
- Objective: 計算量を増やさずにモデルの情報を吸収する能力を高める方法を探求すること。
- Methods: 最大数千のFFサブネットワークからなるSparsely-Gated MoE層を導入し、学習可能なゲートネットワークが各例ごとにスパースな組み合わせを決定する。
- Data and results: MoEを適用したモデルは、大規模言語モデリングや機械翻訳で最先端を上回り、計算コストを抑えた高い性能を示した。
- Novelty: 疎にゲートされたMixture-of-Experts層を用いることで、パラメータ数を大幅に増やしつつ効率的な条件付き計算を実現する点。
- Limitations: 編者の注意: GPUクラスタ上の言語モデル・翻訳での実証である。条件付き計算が常に小規模端末で速いとは示していない。

### Paper: Deep reinforcement learning from human preferences
- Source: arXiv
- Canonical ID: arxiv:1706.03741
- Publication date: 2017-06-12
- URL: https://arxiv.org/abs/1706.03741
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 人間の選好に基づく深層強化学習を提案し、複雑なタスク解決に適用可能であることを示した。
- Objective: 人間が定義するペアの軌道セグメント間の選好を用いて、RLシステムへどのように目標を伝えるかを探求すること。
- Methods: 短い行動軌跡の対に対する非専門家の選好から学習し、環境の本来の報酬関数へ直接アクセスせずにAtariとシミュレーション運動を訓練する。
- Data and results: 環境相互作用の1%未満に人間がフィードバックする条件で複雑なRL課題を解いた。約1時間の人間作業で新しい行動を学習できたと報告。
- Novelty: 本研究は、ペアの軌道セグメント間の非専門家による選好を用いて目標を定義するアプローチを提案し、報酬関数なしでのRL適用を実現した点にある。
- Limitations: 編者の注意: 人間の選好から得る報酬が代理目標となる。シミュレーションで望ましい行動が得られても、選好の完全性や現実環境での安全性は保証しない。

### Paper: Attention Is All You Need
- Source: arXiv
- Canonical ID: arxiv:1706.03762
- Publication date: 2017-06-12
- URL: https://arxiv.org/abs/1706.03762
- read_level: full_text
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: Transformerは注意機構のみに基づく新アーキテクチャであり、再帰や畳み込みを排除した。
- Objective: 既存の複雑なリカレントまたは畳み込みネットワークに代わる、効率的な系列変換モデルを提案すること。
- Methods: encoderの自己attention、decoderのmasked自己attention、encoder-decoder attentionをmulti-headで構成し、位置表現と位置ごとのfeed-forward層を組み合わせる。
- Data and results: WMT 2014英独翻訳で28.4 BLEU、英仏で41.8 BLEUを報告。英仏モデルは8 GPUで3.5日学習。翻訳以外に英語句構造解析も評価した。
- Novelty: 再帰や畳み込みに頼らず、注意機構のみを用いて高性能な系列変換モデルを構築した点。
- Limitations: 本文7節では他モダリティ、巨大な入出力への局所attention、生成の逐次性低減を今後の課題とする。原著の主な実証は翻訳であり、後年のLLM全能力を検証したものではない。

本文の照合箇所: [3.2.3、3.3、6、7節](https://arxiv.org/html/1706.03762v7)。

### Paper: Proximal Policy Optimization Algorithms
- Source: arXiv
- Canonical ID: arxiv:1707.06347
- Publication date: 2017-07-20
- URL: https://arxiv.org/abs/1707.06347
- read_level: full_text
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: PPOは、データサンプリングと代理目的関数最適化を繰り返す新しい方策勾配法である。
- Objective: 標準的な方策勾配法の課題を克服し、効率的で実装しやすい学習手法を提案すること。
- Methods: 新旧方策の行動確率比とadvantageを用いる代理目的を作り、clipした場合との小さい方を採用して大きすぎる更新の利益を抑える。同じrolloutに複数epochのminibatch更新を行う。KLペナルティ版も比較。
- Data and results: PPOは、ロボットの運動やAtariゲームなど複数のベンチマークタスクで他のオンライン方策勾配法を上回り、性能を示した。
- Novelty: TRPOの利点を持ちながら実装が容易で汎用性が高く、サンプル効率が良い新しい目的関数を提案した点。
- Limitations: 本文のclipは確率比の変化を好む誘因を抑える設計で、全状態のKLへの厳密な制約ではない。実験上の安定性を、報酬の正しさや各更新での単調改善保証と同一視しない。

本文の照合箇所: [2.2、3、4、5、6.1節](https://arxiv.org/pdf/1707.06347)。

### Paper: Searching for Activation Functions
- Source: arXiv
- Canonical ID: arxiv:1710.05941
- Publication date: 2017-10-16
- URL: https://arxiv.org/abs/1710.05941
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 活性化関数を自動探索し、比較した深いモデルでReLUより改善傾向を示すSwishを得る。
- Objective: 深層ネットワークにおける最適な活性化関数を特定することが目的である。
- Methods: 網羅的検索と強化学習を組み合わせた手法で新しい活性化関数を探索・検証した。
- Data and results: SwishはImageNetのtop-1精度でMobile NASNet-Aを0.9%、Inception-ResNet-v2を0.6%改善したと報告。
- Novelty: 自動検索技術を用いて、従来の設計に頼らない新たな活性化関数を発見した点。
- Limitations: 編者の注意: 比較した深いネットワークで改善傾向を示す結果であり、全モデルで最良の活性化関数という保証ではない。探索費用と個別実行の費用も別に考える。

### Paper: Decoupled Weight Decay Regularization
- Source: arXiv
- Canonical ID: arxiv:1711.05101
- Publication date: 2017-11-14
- URL: https://arxiv.org/abs/1711.05101
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 適応的勾配法における重み減衰の誤りを指摘し、最適化ステップから分離する手法を提案した。
- Objective: 適応勾配法では同値でないL2正則化と重み減衰を切り分け、Adamの汎化を改善する。
- Methods: 重み減衰を損失関数に関する最適化ステップから「デカップリング」する単純な修正を提案した。これにより、標準SGDおよびAdamの両方で最適な重み減衰係数の選択を学習率の設定から分離可能にした。
- Data and results: 提案手法は、(i) 標準SGDとAdamの両方で重み減衰因子の最適選択を学習率設定から分離し、(ii) Adamの汎化性能を大幅に改善させ、画像分類データセットにおいてSGD with momentumに匹敵する性能を示した。
- Novelty: 重み減衰を最適化ステップからデカップリングすることで、適応的勾配法における重み減衰の本来の定式化を回復させた点。
- Limitations: 編者の注意: 理論上の同値性の区別と、画像分類での実証を分ける。重み減衰を分離するだけで、すべてのモデル・データで最適な汎化が保証されるわけではない。

### Paper: Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm
- Source: arXiv
- Canonical ID: arxiv:1712.01815
- Publication date: 2017-12-05
- URL: https://arxiv.org/abs/1712.01815
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: AlphaZeroは、自己対戦による学習でチェスや将棋も攻略可能である。
- Objective: ゲームのルールのみから、様々な難易度のゲームで超人的な性能を達成できるか？
- Methods: ランダムなプレイから開始し、ドメイン知識なしに自己対戦を通じてアルファゼロを訓練した。
- Data and results: AlphaZeroは24時間以内にチェスや将棋などで人間を超えるレベルのプレイを達成し、世界チャンピオンプログラムに勝利した。
- Novelty: 単一のアルファゼロアルゴリズムで、複数の異なるゲーム（チェス、将棋、囲碁）に対応できる汎用性を実現した点。
- Limitations: 編者の注意: 既知のルールと明確な勝敗を持つ完全情報ゲームでの自己対戦である。24時間という学習時間も計算資源とセットで読み、未知の現実環境における同じ汎用性を仮定しない。

### Paper: Deep contextualized word representations
- Source: arXiv
- Canonical ID: arxiv:1802.05365
- Publication date: 2018-02-15
- URL: https://arxiv.org/abs/1802.05365
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 文脈を考慮した深層単語表現を提案し、NLP性能の大幅な向上を実現した。
- Objective: 単語の使用に伴う複雑な特徴と、言語的文脈による使用の変動性をモデル化する方法は何か。
- Methods: 深層双方向言語モデル（biLM）の内部状態を利用して単語ベクトルを学習させ、既存モデルへの組み込みを可能にした。
- Data and results: 質問応答やテキスト含意など6つの課題で最先端を大幅に改善し、性能向上を示した。
- Novelty: 単なる静的な埋め込みではなく、深層biLMの内部状態に基づく文脈依存型の表現を学習させた点である。
- Limitations: 編者の注意: 既存の課題モデルに事前学習biLMの特徴を追加する設定である。6課題の改善は、生成型LLMや任意の新規領域での性能を直接示すものではない。

### Paper: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- Source: arXiv
- Canonical ID: arxiv:1810.04805
- Publication date: 2018-10-11
- URL: https://arxiv.org/abs/1810.04805
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: BERTは双方向の事前学習により、多様なNLPタスクで高性能を発揮するモデルである。
- Objective: いかにして単一の追加層で様々な自然言語処理タスクに対応できるか？
- Methods: 無ラベルテキストから左右両方の文脈を同時に考慮し、深層双方向表現を事前学習させる手法を用いた。
- Data and results: GLUEスコア80.5%、MultiNLI精度86.7%など、複数のNLPタスクでSOTAの結果を達成した。
- Novelty: BERTは全層で左右両方の文脈を同時に考慮する深層双方向表現の事前学習を行う点に新規性がある。
- Limitations: 編者の注意: 事前学習表現の微調整による理解課題評価であり、自己回帰型の自由生成・ツール実行・長期計画を検証した論文ではない。

### Paper: Parameter-Efficient Transfer Learning for NLP
- Source: arXiv
- Canonical ID: arxiv:1902.00751
- Publication date: 2019-02-02
- URL: https://arxiv.org/abs/1902.00751
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: アダプターモジュールを用いたパラメータ効率的な転移学習を提案する。
- Objective: 多数のダウンストリームタスクにおいて、いかにパラメータ効率的にモデルを適応させるか。
- Methods: 元のBERTの重みを固定し、少数の学習可能なadapterをタスクごとに追加。GLUEを含む26のテキスト分類課題で、全層微調整と資源・精度を比較。
- Data and results: アダプターは全ファインチューニングの性能に近く、タスクあたりわずか3.6%のパラメータ追加で高い性能を示した。
- Novelty: 各タスクごとにモデル全体を再学習せず、少数の可訓練パラメータのみを追加する点が新しい。
- Limitations: 編者の注意: 少数パラメータによる分類課題への転移を評価している。後続LoRAと異なる追加モジュールの実行費用や自由生成への転移は別に比較する必要がある。

### Paper: XLNet: Generalized Autoregressive Pretraining for Language Understanding
- Source: arXiv
- Canonical ID: arxiv:1906.08237
- Publication date: 2019-06-19
- URL: https://arxiv.org/abs/1906.08237
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: XLNetは、双方向コンテキスト学習と自己回帰の利点を統合した事前学習モデルであり、BERTを凌駕する性能を示す。
- Objective: BERTが抱えるマスク依存性と事前学習・ファインチューニングの乖離という課題を克服する方法を探ること。
- Methods: 期待尤度を全順列で最大化することで双方向コンテキストを学習可能にし、Transformer-XLのアイデアを取り入れた自己回帰形式を採用した。
- Data and results: 比較可能な実験設定において、質問応答や自然言語推論など20のタスクでBERTを上回り、しばしば大きな差をもって性能向上を示した。
- Novelty: 全順列での期待尤度最大化により双方向コンテキスト学習と自己回帰性を両立させた点。
- Limitations: 編者の注意: 比較対象は評価した20課題・計算条件に限られる。順列による双方向学習の有効性と、任意の長さの推論の正しさは別である。

### Paper: RoBERTa: A Robustly Optimized BERT Pretraining Approach
- Source: arXiv
- Canonical ID: arxiv:1907.11692
- Publication date: 2019-07-26
- URL: https://arxiv.org/abs/1907.11692
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: BERTの事前学習が過小評価されており、ハイパーパラメータ調整の重要性が示された。
- Objective: 様々なアプローチの比較が困難な中で、どの設計選択が性能に最も影響するかを検証すること。
- Methods: BERTの事前学習を再現し、多くの主要なハイパーパラメータと訓練データサイズの影響を注意深く測定した。
- Data and results: BERTが十分に学習されていなかったことを示し、学習条件を見直したモデルでGLUE、RACE、SQuADの当時最高水準を達成した。
- Novelty: これまで見過ごされてきた設計選択の重要性を強調し、最近報告された改善点の出所に疑問を呈した点。
- Limitations: 編者の注意: 既存手法の差が学習量・データ・ハイパーパラメータに左右されることを示す再現実験である。後続の全構造改良が無効だと結論するものではない。

### Paper: Fine-Tuning Language Models from Human Preferences
- Source: arXiv
- Canonical ID: arxiv:1909.08593
- Publication date: 2019-09-18
- URL: https://arxiv.org/abs/1909.08593
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 人間の選好に基づく報酬学習を言語タスクに応用し、RLの実用化を目指した研究である。
- Objective: 人間による評価で定義される報酬を利用し、自然言語タスクへの強化学習の適用可能性を探ること。
- Methods: テキスト継続（肯定的感情・物理的記述）と要約タスクに報酬学習を適用し、それぞれ5,000件および60,000件の人間比較データを用いた。
- Data and results: 文体制御は5000比較で良好な結果。要約は6万比較で、原文の文をコピーして不要な導入を除く振る舞いとなり、ROUGEと人間評価は高かった。
- Novelty: 生成事前学習モデルの進歩を利用し、自然言語タスクに報酬学習を適用した点。
- Limitations: 著者は、評価者の単純なヒューリスティクスをモデルが利用している可能性を指摘する。高い選好スコアと望ましい要約の意味が一致しない例として重要である。

### Paper: ALBERT: A Lite BERT for Self-supervised Learning of Language Representations
- Source: arXiv
- Canonical ID: arxiv:1909.11942
- Publication date: 2019-09-26
- URL: https://arxiv.org/abs/1909.11942
- read_level: full_text
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: パラメータ削減技術により、BERTのメモリ効率と学習速度を改善したモデルを提案する。
- Objective: 大規模な事前学習モデルの計算資源制約という課題にどう対処するか。
- Methods: 語彙埋め込みを二つの小行列に分解し、層間でパラメータを共有する。さらに文順序予測SOPを用い、各要素の寄与をablationで比較する。
- Data and results: 本文ではBERT-largeに近い構成でパラメータ18分の1、学習約1.7倍高速と報告。大規模構成もGLUE、RACE、SQuADで高性能だが、共有条件・幅で速度と精度は変わる。
- Novelty: 埋め込み次元と隠れ次元の分離、層間共有、文の整合性を学ぶSOPにより、パラメータ効率と表現性能を両立させる。
- Limitations: 本文の比較表では非常に幅広い構成はBERTより遅い場合もある。パラメータ数の削減は、すべての構成で同じ速度改善を意味しない。

本文の照合箇所: [3、4.3〜4.7節](https://arxiv.org/html/1909.11942v6)。

### Paper: DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter
- Source: arXiv
- Canonical ID: arxiv:1910.01108
- Publication date: 2019-10-02
- URL: https://arxiv.org/abs/1910.01108
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: BERTの知識蒸留を利用し、サイズを削減した軽量な言語モデルDistilBERTを提案する。
- Objective: 大規模事前学習モデルをエッジデバイスや計算資源が限られた環境で運用するための課題解決を目指す。
- Methods: 知識蒸留を事前学習フェーズに利用し、言語モデリング損失、蒸留損失、コサイン距離損失を組み合わせた三重損失を導入した。
- Data and results: DistilBERTはBERTモデルのサイズを40%削減しながら、言語理解能力を97%維持し、処理速度が60%向上することを示した。
- Novelty: タスク固有モデルへの蒸留利用ではなく、事前学習フェーズでの知識蒸留を活用する点に新規性がある。
- Limitations: 編者の注意: 97%の維持率は著者の言語理解評価に関する値であり、全能力や安全性の維持率ではない。実端末での速度は実装とハードウェアにも依存する。

### Paper: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
- Source: arXiv
- Canonical ID: arxiv:1910.10683
- Publication date: 2019-10-23
- URL: https://arxiv.org/abs/1910.10683
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: テキストベースの課題を統一的なテキスト生成形式に変換する枠組みを提案した研究。
- Objective: 自然言語処理における転移学習技術の全体像を探り、比較すること。
- Methods: すべてのテキストベースの問題をテキスト生成形式に変換し、事前学習目的やアーキテクチャなどを体系的に比較した。
- Data and results: この探求と大規模なコーパスを用いることで、要約や質問応答など多くのベンチマークで最先端の結果を達成した。
- Novelty: 全てのテキスト言語問題をテキスト-to-テキスト形式に統一する単一のフレームワークを導入した点。
- Limitations: 編者の注意: 統一した入出力形式でも、課題ごとのデータ・評価指標は異なる。多くのテキスト課題の好成績を、因果推論や現実環境での行動能力へ直接外挿しない。

### Paper: BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension
- Source: arXiv
- Canonical ID: arxiv:1910.13461
- Publication date: 2019-10-29
- URL: https://arxiv.org/abs/1910.13461
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: BARTはノイズ除去オートエンコーダによる事前学習モデルであり、多様なNLPタスクに適用可能である。
- Objective: どのようなノイズ付加と再構築のプロセスが、自然言語生成や理解タスクにおいて最適な性能を発揮するかを検証すること。
- Methods: 任意のノイズ関数でテキストを破損させ、元のテキストを復元するように学習させる。ランダムシャッフルや新規のインフィリングスキームなど複数のノイズ除去アプローチを評価した。
- Data and results: GLUEおよびSQuADにおいてRoBERTaと同等の性能を示し、要約タスクでは最大6 ROUGEの向上を達成した。機械翻訳でも1.1 BLEUの改善が見られた。
- Novelty: テキスト破損と再構築というノイズ除去オートエンコーダの枠組みを用いることで、BERTやGPTなどの既存手法を包括的にカバーする汎用的な事前学習フレームワークを提供した点。
- Limitations: 編者の注意: ノイズ付加・復元の選択と課題で性能が変わる。生成のベンチマーク改善は、すべての出力の事実性や安全性を保証するものではない。

### Paper: Fast Transformer Decoding: One Write-Head is All You Need
- Source: arXiv
- Canonical ID: arxiv:1911.02150
- Publication date: 2019-11-06
- URL: https://arxiv.org/abs/1911.02150
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: マルチクエリ注意機構を提案し、推論時のメモリ帯域幅を削減した。
- Objective: Transformerの逐次推論における計算速度低下の原因と対策は何か？
- Methods: キーとバリューテンソルを全アテンションヘッドで共有するマルチクエリ注意機構を採用した。
- Data and results: この手法によりデコードが大幅に高速化し、品質劣化は軽微であることが実験的に確認された。
- Novelty: キーとバリューを共有することで、メモリ帯域幅の要求を大きく削減できる点。
- Limitations: 著者はdecodeの高速化と同時に、baselineから小さい品質低下があると報告する。編者の注意: KVの共有による効率化と、出力分布を完全に保存する手法は区別する。

### Paper: Scaling Laws for Neural Language Models
- Source: arXiv
- Canonical ID: arxiv:2001.08361
- Publication date: 2020-01-23
- URL: https://arxiv.org/abs/2001.08361
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 言語モデルの損失とモデル規模・データ量・学習計算量の間に経験的なべき乗則を見いだす。
- Objective: 言語モデルのクロスエントロピー損失に対するスケーリング則を経験的に研究すること。
- Methods: モデルサイズ、データセットサイズ、計算量を用いた訓練における損失の変化を調査した。
- Data and results: 損失はモデルサイズ、データセットサイズ、および使用された計算量のいずれかに対してべき乗則でスケールする。
- Novelty: 最適な計算効率的な訓練は、比較的少ないデータで非常に大きなモデルを訓練し、収束前に停止することを含む。
- Limitations: 編者の注意: 特定の学習領域で観測した経験則である。後続のChinchillaと最適配分の結論が異なるため、式を学習範囲・データ条件から切り離して使わない。

### Paper: ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators
- Source: arXiv
- Canonical ID: arxiv:2003.10555
- Publication date: 2020-03-23
- URL: https://arxiv.org/abs/2003.10555
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: ELECTRAは、トークン生成ではなく識別器として事前学習を行う効率的な手法を提案した。
- Objective: BERTのようなMLMの計算コストの問題点を克服する新しい事前学習タスクは何か？
- Methods: 入力の一部を代替トークンに置き換え、各トークンが置換されたか否かを予測する二値分類器を訓練する。
- Data and results: 同じモデルサイズ、データ量、計算量でBERTより優れた文脈表現を獲得し、特に小規模モデルでの性能向上が顕著である。
- Novelty: 生成タスクではなく、入力のどのトークンが置換されたかを識別する判別的タスクを採用した点。
- Limitations: 編者の注意: 置換を検出する表現事前学習である。計算効率や理解ベンチマークの比較を、自由生成・対話の品質比較と混同しない。

### Paper: Longformer: The Long-Document Transformer
- Source: arXiv
- Canonical ID: arxiv:2004.05150
- Publication date: 2020-04-10
- URL: https://arxiv.org/abs/2004.05150
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: Longformerは、自己注意機構の計算量を線形に抑え、長文処理を可能にしたTransformerモデルである。
- Objective: Transformerベースのモデルが抱える、シーケンス長に対する二次関数的な計算量の問題を解決すること。
- Methods: ローカルウィンドウアテンションとタスク特化型のグローバルアテンションを組み合わせた新しい注意機構を採用し、標準の自己注意機構の置き換えとして機能させる。
- Data and results: 文字レベル言語モデリングでtext8およびenwik8においてSOTAを達成したほか、RoBERTaを上回りWikiHopやTriviaQAでSOTAを記録した。
- Novelty: ローカルウィンドウアテンションとタスク特化型グローバルアテンションの組み合わせにより、計算量を線形にスケールさせた点。
- Limitations: 編者の注意: 疎な局所・大域attentionの配置が必要である。長文を入力できることは、文中の全情報を正確に利用できることを保証しない。

### Paper: Language Models are Few-Shot Learners
- Source: arXiv
- Canonical ID: arxiv:2005.14165
- Publication date: 2020-05-28
- URL: https://arxiv.org/abs/2005.14165
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 大規模言語モデルは、ファインチューニングなしで少数の例から高い性能を発揮する。
- Objective: 現在のNLPシステムが苦手とする、数例や指示からの新しいタスク遂行能力を検証すること。
- Methods: GPT-3（1750億パラメータ）を用いて、翻訳やQAなど様々なタスクに対し、勾配更新やファインチューニングなしでテキスト対話のみで適用した。
- Data and results: GPT-3は、翻訳や質問応答を含む多くのNLPデータセットで高い性能を示し、人間が書いた記事と区別困難なサンプル生成も可能であった。
- Novelty: モデルのスケールアップにより、タスク固有のファインチューニングなしでの少ショット学習能力が大幅に向上した点。
- Limitations: 著者はfew-shotでも苦戦するデータセット、およびWebコーパス学習に伴う方法論上の問題を報告する。ニュース生成を人間が見分けにくいことの社会的影響も論じる。

### Paper: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding
- Source: arXiv
- Canonical ID: arxiv:2006.16668
- Publication date: 2020-06-30
- URL: https://arxiv.org/abs/2006.16668
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: GShardは、条件付き計算と自動シャーディングで巨大モデルのスケーリングを可能にする。
- Objective: 大規模なニューラルネットワークの訓練における計算コストや実装効率性の課題を解決すること。
- Methods: 軽量なアノテーションAPIとXLAコンパイラ拡張を利用し、並列計算パターンを表現する。
- Data and results: GShardにより6000億パラメータ超のモデルが2048 TPU v3で4日間にわたり訓練され、翻訳品質が向上した。
- Novelty: 自動シャーディングを用いて、既存コード変更を最小限に抑えつつ巨大モデルのスケーリングを実現した点。
- Limitations: 編者の注意: 2048 TPU v3を使う多言語翻訳系でのスケール実証である。小さなハードウェアや異なる通信構成で同じ効率を得られるとは限らない。

### Paper: Learning to summarize from human feedback
- Source: arXiv
- Canonical ID: arxiv:2009.01325
- Publication date: 2020-09-02
- URL: https://arxiv.org/abs/2009.01325
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 人間からのフィードバック最適化で要約品質を大幅に向上させる手法を提案する。
- Objective: 要約モデルの訓練と評価におけるデータや指標の限界点を明らかにし、真の要約品質向上の方法を探る。
- Methods: 人間の比較に基づく大規模な高品質データセットを集め、人間が好む要約を予測する報酬モデルを構築し、強化学習でファインチューニングした。
- Data and results: Reddit TL;DRでは人間参照要約や大きい教師ありモデルより好まれる要約を生成。ニュース用の追加微調整なしでもCNN/DMで人間参照に近い評価と報告。
- Novelty: 人間が好む出力を最適化する報酬関数を用いることで、従来の指標（ROUGEなど）最適化を超える改善を実現した点。
- Limitations: 編者の注意: 報酬モデルと評価者の選好が学習目標である。データ間転移の成功は、すべての要約の事実性や未知の読者の価値判断との一致を保証しない。

### Paper: Prefix-Tuning: Optimizing Continuous Prompts for Generation
- Source: arXiv
- Canonical ID: arxiv:2101.00190
- Publication date: 2021-01-01
- URL: https://arxiv.org/abs/2101.00190
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 本研究は、大規模言語モデルのファインチューニングに代わる軽量な手法としてプレフィックスチューニングを提案した。
- Objective: 自然言語生成タスクにおいて、全パラメータ更新なしで高い性能を発揮する効率的な学習方法を探求すること。
- Methods: GPT-2とBARTを用いて、言語モデルのパラメータを固定しつつ、小さな連続的なタスク固有ベクトル（プレフィックス）のみを最適化する手法を適用した。
- Data and results: 学習パラメータ0.1%で、GPT-2の表から文章生成とBARTの要約において全データ時に全層微調整に近い性能。低データ時や未学習トピックへの外挿でも優位と報告。
- Novelty: 言語モデルのパラメータを固定し、タスク固有の小さな連続ベクトル（プレフィックス）のみを最適化するアプローチを提案した点。
- Limitations: 編者の注意: 検証は表から文章生成と要約であり、prefixを最適化する学習は必要。勾配更新なしのin-context learningとは資源・データ利用条件が異なる。

### Paper: Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
- Source: arXiv
- Canonical ID: arxiv:2101.03961
- Publication date: 2021-01-11
- URL: https://arxiv.org/abs/2101.03961
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: Switch Transformerは、MoEの複雑性やコストを改善し、大規模モデルの実用化を目指した。
- Objective: MoEの課題である複雑性、通信コスト、訓練不安定性をどのように解決するか。
- Methods: T5-BaseとT5-Largeを基に改良モデルを設計し、ルーティングアルゴリズムを単純化した。
- Data and results: 提案手法により、計算リソースを維持したまま事前学習速度が最大7倍向上し、1兆パラメータ級のモデルも訓練可能となった。
- Novelty: MoEの複雑性を軽減するシンプルなルーターと効率的なスパース性設計を導入した点。
- Limitations: 編者の注意: 疎な活動による計算効率と、全パラメータの保存や分散通信の費用は別である。最大7倍の高速化は固定した計算資源・比較構成での値。

### Paper: The Power of Scale for Parameter-Efficient Prompt Tuning
- Source: arXiv
- Canonical ID: arxiv:2104.08691
- Publication date: 2021-04-18
- URL: https://arxiv.org/abs/2104.08691
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: プロンプトチューニングは、凍結モデルにソフトプロンプトを学習させる手法であり、大規模化に伴い性能が向上し、フルファインチューニングに匹敵する。
- Objective: GPT-3のような離散テキストプロンプトと比較して、ソフトプロンプトによる条件付けがどの程度効果的かを探ること。
- Methods: T5モデルを用いて、アブレーション実験によりモデルサイズとプロンプトチューニングの性能関係を検証した。また、他の類似手法との比較も行った。
- Data and results: モデルが数十億パラメータを超えるにつれて、プロンプトチューニングはスケールに伴い競争力を増し、モデル全体をファインチューニングした場合の強力な性能に匹敵することが示された。
- Novelty: 凍結モデルに対してソフトプロンプトで条件付けを行うことで、大規模モデルの共有・利用コストの問題を緩和できる点を示した。
- Limitations: 編者の注意: 全層微調整との差が縮むという結果はT5の規模実験に基づく。小さいモデルや別の事前学習方式でも同じ関係が成り立つとは示さない。

### Paper: LoRA: Low-Rank Adaptation of Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2106.09685
- Publication date: 2021-06-17
- URL: https://arxiv.org/abs/2106.09685
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: LoRAは、大規模言語モデルのファインチューニングを効率化する手法である。
- Objective: 巨大なLLMのタスク適応において、全パラメータ更新が非現実的となる課題を解決すること。
- Methods: 事前学習済みモデルの重みを固定し、Transformer層に低ランク分解行列を注入して訓練可能なパラメータ数を削減した。
- Data and results: GPT-3 175BのAdamによる全層微調整比で、学習パラメータを1万分の1、GPUメモリ要件を約3分の1にできたと報告。RoBERTa、DeBERTa、GPT-2/3の評価で全層微調整に同等以上。
- Novelty: 追加の推論遅延なしに、少ない学習パラメータで高いモデル品質を達成できる点が新規である。
- Limitations: 編者の注意: 更新を低ランクに制約する方式であり、必要ランクと対象層は課題に依存する。要旨の資源削減率はGPT-3 175Bの特定比較に関する値。

### Paper: Towards a Unified View of Parameter-Efficient Transfer Learning
- Source: arXiv
- Canonical ID: arxiv:2110.04366
- Publication date: 2021-10-08
- URL: https://arxiv.org/abs/2110.04366
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: PEファインチューニングを統一的に捉え、設計要素間の関連性を明らかにした。
- Objective: パラメータ効率的な転移学習の成功要因と手法間の繋がりを解明すること。
- Methods: 各PEFT法を、特定の隠れ状態に加える変更の関数・適用位置などの設計次元で統一。翻訳、要約、言語理解、分類で設計の寄与を比較する。
- Data and results: 統一的フレームワークにより、既存手法の重要な設計選択肢を特定し、より少ないパラメータで同等の性能を達成する新手法を提案した。
- Novelty: 各手法を特定の隠れ状態の修正として捉え、その計算関数や適用位置といった設計次元で関連付けた点。
- Limitations: 編者の注意: 統一はモデル内表現の変更として扱える手法の設計枠組みである。比較した4課題領域以外の性能や全パラメータ効率化法への完全な網羅を保証しない。

### Paper: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2201.11903
- Publication date: 2022-01-28
- URL: https://arxiv.org/abs/2201.11903
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 思考の連鎖（CoT）プロンプティングは、LLMの複雑な推論能力を大幅に向上させることが示された。
- Objective: 中間的な推論ステップを生成する「思考の連鎖」が、大規模言語モデルの複雑な推論能力をどのように改善するかを探ること。
- Methods: 数点のCoTデモンストレーションをプロンプティングとして提供する単純な方法（CoTプロンプティング）を用いる。算術、常識的、記号的推論タスクで実験を行った。
- Data and results: CoTプロンプティングは、算術、常識的、記号的推論タスク全般で性能を向上させ、540BパラメータモデルがGSM8KベンチマークでSOTA精度を達成した。
- Novelty: Few-shotのCoTデモンストレーションをプロンプトとして提供する「chain of thought prompting」という単純な手法で推論能力を引き出す点。
- Limitations: 編者の注意: 効果はモデル規模と例示・課題に依存する。生成された説明がモデルの実際の意思決定原因であるか、正しい推論を保証するかは検証対象と異なる。

### Paper: Training language models to follow instructions with human feedback
- Source: arXiv
- Canonical ID: arxiv:2203.02155
- Publication date: 2022-03-04
- URL: https://arxiv.org/abs/2203.02155
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 人間からのフィードバックで言語モデルをファインチューニングし、ユーザーの意図への適合性を高める手法を提案した。
- Objective: 大規模なモデルサイズだけではユーザーの意図に従う能力は向上しないため、アライメントの方法を探る。
- Methods: ラベル作成者によるデモンストレーションとランキングデータを用いて、GPT-3を教師あり学習とRLHFで段階的にファインチューニングした。
- Data and results: 著者のプロンプト分布の人間評価では1.3B InstructGPTが175B GPT-3より好まれた。真実性向上・有害出力低減も報告するが、単純な誤りは残る。
- Novelty: 人間のフィードバックを用いたファインチューニングにより、モデルをユーザーの意図へアライメントできることを示した点。
- Limitations: 著者は単純な誤りが残ると明記する。編者の注意: 好ましさは採用した評価者・プロンプト分布に基づく指標で、客観的な全正答率や安全保証ではない。

### Paper: Self-Consistency Improves Chain of Thought Reasoning in Language Models
- Source: arXiv
- Canonical ID: arxiv:2203.11171
- Publication date: 2022-03-21
- URL: https://arxiv.org/abs/2203.11171
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 自己一貫性（self-consistency）という新しいデコーディング戦略を提案し、思考連鎖プロンプティングの性能向上を目指した。
- Objective: 複雑な推論タスクにおいて、単なる貪欲なデコーディングに代わる効果的な推論パス選択方法を確立すること。
- Methods: 従来の貪欲なデコーディングの代わりに、多様な推論パスをサンプリングし、それらのパスから最も一貫性のある答えを選択する自己一貫性を適用した。
- Data and results: GSM8Kで+17.9%、SVAMPで+11.0%、AQuAで+12.2%など、複数のベンチマークで顕著な性能向上を示した。
- Novelty: 思考連鎖プロンプティングにおける貪欲なデコーディングを、多様なパスから最も一貫性のある答えを選択する自己一貫性に置き換えた点。
- Limitations: 編者の注意: 複数の推論を生成するため単発生成より計算を要する。同じ誤答へ多数の経路が収束する場合、多数決だけでは正しさを保証できない。

### Paper: STaR: Bootstrapping Reasoning With Reasoning
- Source: arXiv
- Canonical ID: arxiv:2203.14465
- Publication date: 2022-03-28
- URL: https://arxiv.org/abs/2203.14465
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: STaRは、少数の例と大規模データから推論能力を段階的に向上させる手法である。
- Objective: 複雑な推論タスクでモデルの推論生成能力をいかにして引き出すか？
- Methods: 少数の説明例から推論を生成。誤答時は正解を与えて説明を再生成し、最終的に正解へ至る説明で微調整するループを繰り返す。
- Data and results: 直接最終解を学習する比較系より複数データで改善し、CommonsenseQAでは30倍大きいモデルの微調整に近い成績を報告した。
- Novelty: 自己生成した推論過程からモデル自身に能力を改善させる点が新しい。
- Limitations: 編者の注意: 生成した説明の採用には正答の情報を使う。正解ラベルなしで自律的に新知識を発見・検証したことや、説明自体の正しさの保証とは区別する。

### Paper: Training Compute-Optimal Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2203.15556
- Publication date: 2022-03-29
- URL: https://arxiv.org/abs/2203.15556
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 計算効率的なLLMの訓練において、モデルサイズとトークン数を等しくスケールすべきである。
- Objective: 与えられた計算予算の下で最適なモデルサイズとトークン数を見出すこと。
- Methods: 70Mから16Bを超えるパラメータを持つ400以上のモデルを50億〜5000億トークンで訓練した。
- Data and results: 同じ学習計算量のGopherに対し、70BのChinchillaを4倍のデータで学習し幅広い評価で上回った。MMLU平均精度67.5%と報告。
- Novelty: 計算効率的な訓練では、モデルサイズと訓練トークン数を等しくスケールすることが重要であるという仮説を提示した。
- Limitations: 編者の注意: 学習計算を固定した最適化であり、配布後の総推論量やデータ調達費用まで含む最適設計とは一致するとは限らない。

### Paper: PaLM: Scaling Language Modeling with Pathways
- Source: arXiv
- Canonical ID: arxiv:2204.02311
- Publication date: 2022-04-05
- URL: https://arxiv.org/abs/2204.02311
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 540BパラメータのPaLMを開発し、Pathwaysを用いて訓練。大規模化による継続的な性能向上を示した。
- Objective: Few-shot learningにおけるスケールが与える影響を理解すること。
- Methods: 5400億パラメータの密結合型Transformer言語モデル（PaLM）を構築し、新しいMLシステムであるPathwaysを用いて6144 TPU v4チップで訓練した。
- Data and results: PaLM 540Bは、多数のベンチマークで最先端の結果を達成し、特に多段階推論タスクやBIG-benchで人間平均を超える性能を示した。
- Novelty: Pathwaysという新しいMLシステムを利用することで、複数のTPU Podにわたる非常に効率的な訓練を実現した点。
- Limitations: 編者の注意: 540Bモデルと大規模TPU環境での評価であり、小規模予算への直接適用は示さない。BIG-benchの人間平均超過は全実務タスクの人間超越を意味しない。

### Paper: Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning
- Source: arXiv
- Canonical ID: arxiv:2205.05638
- Publication date: 2022-05-11
- URL: https://arxiv.org/abs/2205.05638
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: PEFTはICLより精度が高く、計算コストも大幅に低いことが示された。
- Objective: Few-shot ICLとPEFTを比較し、どちらが優れているかを検証すること。
- Methods: few-shot ICLとPEFTの精度・計算費用を比較。活性化を学習ベクトルで拡縮するIA3と、T0に基づくT-Fewを提案し、未知課題をRAFTで評価する。
- Data and results: PEFTがICLより高精度かつ低コストと報告。T-FewはRAFTで従来の最良手法より6%絶対改善し、同ベンチマークの人間基準を上回った。
- Novelty: 活性化を学習済みベクトルでスケーリングする新しいPEFT法(IA)$^3$を提案した点。
- Limitations: 編者の注意: 指示学習済みT0、few-shot条件、RAFTという評価設定に依存する。人間基準超過を一般的な人間超越や全課題でのPEFT優位と解釈しない。

### Paper: Least-to-Most Prompting Enables Complex Reasoning in Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2205.10625
- Publication date: 2022-05-21
- URL: https://arxiv.org/abs/2205.10625
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 提案手法は、複雑な問題を段階的に分解し順次解く「least-to-most prompting」であり、難易度の高い問題への汎化能力を向上させる。
- Objective: プロンプト例で示された以上の難しさを持つ問題に対するLLMの推論能力の限界を超える方法を探ること。
- Methods: 複雑な問題を一連のより単純なサブ問題に分解し、それらを順番に解く「least-to-most prompting」という新しいプロンプティング戦略を提案した。
- Data and results: GPT-3 code-davinci-002モデルでleast-to-most promptingを用いると、SCANベンチマークにおいて14個の例示のみで99%以上の精度を達成し、chain-of-thoughtでは16%に留まった。
- Novelty: 複雑な問題をより単純なサブ問題群に分解し、その解を順次利用することで、プロンプト例を超える難問への汎化を実現した点。
- Limitations: 編者の注意: 分解できる課題と適切な例示に依存する。SCANでの高成績から、任意の現実課題を正しく分解できる能力までは導けない。

### Paper: Large Language Models are Zero-Shot Reasoners
- Source: arXiv
- Canonical ID: arxiv:2205.11916
- Publication date: 2022-05-24
- URL: https://arxiv.org/abs/2205.11916
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: LLMは「Let's think step by step」追加のみで高度な推論が可能である。
- Objective: LLMがFew-shot学習に依存せず、ゼロショットでの複雑な多段階推論能力を持つか検証する。
- Methods: 各ベンチマークタスクに対し、「Let's think step by step」を前置した単一プロンプト（Zero-shot-CoT）を用いて評価した。
- Data and results: text-davinci-002でMultiArithが17.7%から78.7%、GSM8Kが10.4%から40.7%へ向上。PaLM 540Bでも同程度の改善を報告した。
- Novelty: Few-shot例なしで「Let's think step by step」を追加するだけで、LLMの基本的なゼロショット推論能力を抽出できる点。
- Limitations: 編者の注意: 効果は比較したモデルと算術・記号・論理ベンチマークに基づく。同じ短い指示が将来の全モデルや実務の難問でも同じ改善を生むとは限らない。

### Paper: FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness
- Source: arXiv
- Canonical ID: arxiv:2205.14135
- Publication date: 2022-05-27
- URL: https://arxiv.org/abs/2205.14135
- read_level: full_text
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: IO効率を考慮した正確なアテンション機構FlashAttentionを提案し、Transformerの高速化を実現した。
- Objective: 正確なattentionを維持しながら、GPU階層メモリ間の読み書きを減らして実時間・メモリ利用を改善する。
- Methods: Q/K/Vをブロックに分けてSRAMへ読み込み、softmaxを統計量で逐次集約する。逆伝播では巨大な中間行列をHBMへ保存せず、必要な値を再計算する。
- Data and results: BERT-large長512では学習全体の実時間15%改善、GPT-2長1Kでは3倍高速化と報告。モデルや系列長が異なる値を一律の高速化率として扱わない。
- Novelty: 計算量だけでなくGPUメモリ間のI/Oアクセスを考慮したアプローチが本研究の新規性である。
- Limitations: 編者の注意: exact版とblock-sparse近似版を区別する。主な改良はI/Oであり、attentionの算術計算量すべてを系列長に対して線形にしたという主張ではない。

本文の照合箇所: [2.2、3.1、付録B.1〜B.3節](https://arxiv.org/html/2205.14135v2)。

### Paper: Formal Algorithms for Transformers
- Source: arXiv
- Canonical ID: arxiv:2207.09238
- Publication date: 2022-07-19
- URL: https://arxiv.org/abs/2207.09238
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: トランスフォーマーの構造とアルゴリズムを数学的に解説する包括的な資料である。
- Objective: 読者がトランスフォーマーの基本概念、学習方法、応用分野を理解するための指針を提供すること。
- Methods: 基本的な機械学習用語に精通していることを前提とし、MLPなどの既知のニューラルネットワーク構造と比較しながら説明を進める。
- Data and results: トランスフォーマーがどのようなものか、どのように訓練され、主要な構成要素や著名なモデル群について概説されている。
- Novelty: 貢献はTransformerの構造・学習・主要モデルを自己完結した数学的アルゴリズムとして整理することにあり、新しい最高性能モデルの提案ではない。
- Limitations: 著者はアーキテクチャとアルゴリズムの概説であり、実験結果を扱う資料ではないと明記する。基本的なML用語やMLPの理解を前提とする。

### Paper: ReAct: Synergizing Reasoning and Acting in Language Models
- Source: arXiv
- Canonical ID: arxiv:2210.03629
- Publication date: 2022-10-06
- URL: https://arxiv.org/abs/2210.03629
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: ReActは、推論と行動を交互に組み合わせることでLLMの能力を高める手法である。
- Objective: LLMにおける推論と行動の統合的な利用可能性を探求すること。
- Methods: ReActでは、思考過程（reasoning traces）とタスク固有のアクションをインターリーブさせ、外部情報源との連携を行う。
- Data and results: Wikipedia APIを使うHotpotQA・FEVERで幻覚や誤り伝播を減らしたと報告。ALFWorldとWebShopでは1〜2例の提示で、比較した模倣・RL手法より成功率が34%・10%絶対改善。
- Novelty: 推論トレースが行動計画の追跡と例外処理を助け、外部アクションが情報収集を可能にする点。
- Limitations: 編者の注意: 取得する外部情報と実行環境に依存する。選定課題での幻覚低減は、全出力の事実性や悪意あるツール入力への安全性を保証しない。

### Paper: Measuring and Narrowing the Compositionality Gap in Language Models
- Source: arXiv
- Canonical ID: arxiv:2210.03350
- Publication date: 2022-10-07
- URL: https://arxiv.org/abs/2210.03350
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 言語モデルの構成的推論能力を測定し、そのギャップを埋める手法を提案した。
- Objective: モデルがサブ問題は解けても全体解を出せない「構成性ギャップ」を定量的に評価すること。
- Methods: 多段階質問を用いて構成性ギャップを算出し、Chain-of-ThoughtやSelf-Askといったプロンプティングで改善を試みた。
- Data and results: GPT-3ではモデルサイズ増加に伴い構成性ギャップは減らず、Self-Askが検索エンジンと統合することで精度向上を示した。
- Novelty: 自己質問（self-ask）という構造化プロンプティングにより、推論過程の明示的な記述でギャップを埋める点を提案した。
- Limitations: 編者の注意: GPT-3系列と、多数の事実を組み合わせるよう設計した質問での評価である。規模拡大がすべての種類の推論を改善しないという一般定理ではない。

### Paper: Scaling Instruction-Finetuned Language Models
- Source: arXiv
- Canonical ID: arxiv:2210.11416
- Publication date: 2022-10-20
- URL: https://arxiv.org/abs/2210.11416
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 指示データでのファインチューニングは、モデル性能と汎化能力を大幅に向上させる手法である。
- Objective: タスク数、モデルサイズ、CoTデータによる指示チューニングの拡張が性能に与える影響を探る。
- Methods: PaLM, T5, U-PaLMなど多様なクラスで、タスク数のスケーリング、モデルサイズのスケーリング、CoTデータでのファインチューニングを試みた。
- Data and results: Flan-PaLM 540Bは1.8Kタスクでチューニングされ、PALM 540Bより平均+9.4%の性能向上を示した。
- Novelty: 指示タスク数・モデル規模・CoT微調整を系統的に変え、複数のモデル系列とzero/few-shot評価に共通する指示学習の効果を調べる。
- Limitations: 編者の注意: 評価した指示タスク・モデル系列での一般化であり、未知の実務や外部ツールを伴う長期計画の成功を直接検証したものではない。

### Paper: GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers
- Source: arXiv
- Canonical ID: arxiv:2210.17323
- Publication date: 2022-10-31
- URL: https://arxiv.org/abs/2210.17323
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: GPTQは、大規模言語モデルの重みを高精度に量子化する手法であり、特に1750億パラメータ級のモデルを単一GPUで実行可能にする。
- Objective: 巨大なGPTモデルの高い計算量とストレージコストという課題に対し、どのような新しい軽量化技術が適用できるか？
- Methods: 近似された2次情報に基づいたワンショット重み量子化手法であるGPTQを提案した。これにより、1750億パラメータのGPTモデルを約4 GPU時間で3〜4ビットに量子化する。
- Data and results: 本手法により、1750億パラメータのモデルのビット幅を3〜4ビットまで削減しつつ、非圧縮ベースラインと比較して無視できる精度の低下に留まる。これにより、単一GPUでの生成推論が可能となり、FP16比で高性能GPUでは約3.25倍、A6000では4.5倍の高速化を達成した。
- Novelty: 近似された2次情報に基づいたワンショット重み量子化手法GPTQを提案し、これによって大規模モデルの量子化精度と効率性を大幅に向上させた点。
- Limitations: 編者の注意: 速度向上はA100/A6000と比較精度に依存する。要旨から未知タスク全般での精度保持や量子化後の安全性は確認できない。

### Paper: PAL: Program-aided Language Models
- Source: arXiv
- Canonical ID: arxiv:2211.10435
- Publication date: 2022-11-18
- URL: https://arxiv.org/abs/2211.10435
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: PALはLLMに問題分解をさせ、解法実行をPythonインタープリタで行う手法である。
- Objective: LLMの推論過程における論理的・算術的な誤りをどう克服するか？
- Methods: 自然言語の問題からプログラムを生成し、その実行ステップをPythonインタープリタで処理する。
- Data and results: 数学・記号・アルゴリズムの13課題で、大きい言語モデルによる推論より正確だったと報告。Codexを使うPALはGSM8KでPaLM-540BのCoTより15%絶対改善。
- Novelty: LLMによる問題分解とシンボリックインタープリタの実行結果を組み合わせる点。
- Limitations: 編者の注意: インタープリタは生成されたコードを正確に実行するが、問題の読み違いや誤ったコード生成まで防ぐものではない。ツール実行の費用と信頼境界も別に評価する。

### Paper: Fast Inference from Transformers via Speculative Decoding
- Source: arXiv
- Canonical ID: arxiv:2211.17192
- Publication date: 2022-11-30
- URL: https://arxiv.org/abs/2211.17192
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 推論速度を向上させるため、並列計算を利用したスペキュラティブデコーディング法を提案する。
- Objective: 自己回帰モデルのトークン生成における遅延の問題を解決する方法を探る。
- Methods: 軽量な近似モデルの候補列を大型モデルで並列に評価し、元の大型モデルの出力分布を変えないサンプリングにより複数トークンの生成を進める。
- Data and results: T5-XXLで実証し、標準実装と比較して2倍から3倍の加速を達成した。
- Novelty: 既存モデルの再学習やアーキテクチャ変更なしに、並列実行により高速推論を実現する点。
- Limitations: 編者の注意: 正確さの主張は出力分布の保存に関するもの。高速化率は候補モデル、受理される候補、並列計算とメモリの条件に依存し、全ワークロードで2〜3倍を保証しない。

### Paper: Constitutional AI: Harmlessness from AI Feedback
- Source: arXiv
- Canonical ID: arxiv:2212.08073
- Publication date: 2022-12-15
- URL: https://arxiv.org/abs/2212.08073
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: AIの自己改善を通じ、人間によるラベルなしで無害なアシスタントを訓練する手法を提案した。
- Objective: 人間のラベルに頼らず、いかにして有害でないAIアシスタントを訓練できるかを検証すること。
- Methods: 教師あり学習と強化学習の二段階プロセスを用い、自己批判と修正を通じてモデルをファインチューニングし、AIフィードバックで報酬信号を得た。
- Data and results: 原則に基づく自己批判・修正とAI選好によるRLにより、有害な質問へ異議の理由を説明するアシスタントを訓練。要旨に統一した安全性スコアの数値はない。
- Novelty: 人間によるラベル付けを最小限に抑えつつ、ルールや原則のみを用いてAIの振る舞いを制御できる点にある。
- Limitations: 編者の注意: 人間の作る原則と評価AIの判断が監督信号になる。人間の個別ラベルを減らすことは、価値判断や監督上の誤りがなくなることを意味しない。

### Paper: Self-Instruct: Aligning Language Models with Self-Generated Instructions
- Source: arXiv
- Canonical ID: arxiv:2212.10560
- Publication date: 2022-12-20
- URL: https://arxiv.org/abs/2212.10560
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: Self-Instructは、モデル自身の生成を利用して指示データを作成し、大規模言語モデルの指示追従能力を向上させるフレームワークである。
- Objective: 人間が作成した指示データへの過度な依存から脱却し、汎用性の高い指示追従能力を持つ事前学習済みLLMを構築する方法論を提案すること。
- Methods: まず、既存のLLMを用いて指示（instruction）、入力（input）、出力（output）サンプルを自動生成するパイプラインを構築した。次に、これらのデータから無効または類似度の高いものをフィルタリングし、元のモデルのファインチューニングに利用した。
- Data and results: GPT-3でSuper-NaturalInstructionsの性能が元モデルより33%絶対改善と報告。専門家作成の新規指示に対する人間評価でも既存公開指示データを上回り、InstructGPT-001との差は5%だった。
- Novelty: 本手法は、アノテーションがほとんど不要な方法（almost annotation-free method）で事前学習済みLLMの指示へのアライメントを可能にし、既存の公開データセットを超える性能向上を実現した点にある。
- Limitations: 編者の注意: モデル自身が作るデータに依存する。評価された指示分布を超える汎化や、合成データ中の誤り・偏りの長期蓄積は要旨から確認できない。

### Paper: LLaMA: Open and Efficient Foundation Language Models
- Source: arXiv
- Canonical ID: arxiv:2302.13971
- Publication date: 2023-02-27
- URL: https://arxiv.org/abs/2302.13971
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: LLaMAは、公開データのみで高性能な基盤モデルを構築可能であることを示す。
- Objective: 公開データセットのみを用いて最先端の言語モデルを訓練できるか？
- Methods: 7B〜65Bの言語モデルを、公開データだけから得た数兆トークンで事前学習し、既存のより大きなモデルとベンチマークで比較する。
- Data and results: LLaMA-13BがGPT-3 175Bを多くの評価で上回り、LLaMA-65BはChinchilla-70BやPaLM-540Bと競争的だったと報告。
- Novelty: 独自のプロプライエタリなデータセットに頼らず、公開データのみで高性能モデルの訓練が可能であることを示した点。
- Limitations: 編者の注意: 公開学習データの利用と、全データの品質・権利・汚染問題の解決は同一ではない。評価成績は採用した課題と比較条件に依存する。

### Paper: Reflexion: Language Agents with Verbal Reinforcement Learning
- Source: arXiv
- Canonical ID: arxiv:2303.11366
- Publication date: 2023-03-20
- URL: https://arxiv.org/abs/2303.11366
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: Reflexionは、言語エージェントを重み更新なしに言語的フィードバックで強化するフレームワークである。
- Objective: 従来の強化学習の課題を克服し、効率的に試行錯誤から学習する方法を探る。
- Methods: エージェントがタスクのフィードバック信号について口頭で反省し、これをエピソード記憶バッファに保持して次の試行に利用する。
- Data and results: HumanEvalコーディングベンチマークで91%のpass@1精度を達成し、GPT-4（80%）を上回った。
- Novelty: 重み更新ではなく、言語的なフィードバックを通じてエージェントを強化するというアプローチを採用した点。
- Limitations: 編者の注意: 反省を次の試行へ渡す構成であるため、モデルだけでなく試行回数、利用できる評価器、記憶の有無を揃えて比較する必要がある。誤った反省の蓄積も別の課題となる。

### Paper: Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2305.10601
- Publication date: 2023-05-17
- URL: https://arxiv.org/abs/2305.10601
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: ToTは、LLMの推論を思考の木構造で拡張し、計画的な問題解決を可能にするフレームワークである。
- Objective: 初期決定が重要なタスクや探索が必要な課題において、LLMの限界を超える方法を探ること。
- Methods: 文としての中間思考を節点にし、複数候補を生成・自己評価して探索する。先読みや後戻りを用い、Game of 24、創作文、Mini Crosswordsで評価する。
- Data and results: Game of 24では、CoTプロンプティングで4%だった成功率が、本手法により74%に大幅に向上したことが示された。
- Novelty: ToTは、単なる逐次的な思考連鎖を超え、複数の推論パスを探索し、グローバルな選択を行うことを可能にした点にある。
- Limitations: 編者の注意: 3種類の探索課題での実証であり、候補生成と自己評価に複数モデル呼び出しを要する。74%はGame of 24の設定で、一般的な問題解決率ではない。

### Paper: Goat: Fine-tuned LLaMA Outperforms GPT-4 on Arithmetic Tasks
- Source: arXiv
- Canonical ID: arxiv:2305.14201
- Publication date: 2023-05-23
- URL: https://arxiv.org/abs/2305.14201
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: ファインチューニングしたLLaMAモデル「Goat」が算術タスクでGPT-4を上回る性能を示した。
- Objective: 本研究の目的は、算術タスクにおいて既存の大規模言語モデルを超える性能を持つ新しいモデルを提案することである。
- Methods: LLaMAを合成算術データで微調整。学習可能性によって課題を分け、複雑な乗除算を基本算術に分解する。Goat-7BはLoRAにより24GB VRAM GPUで学習可能と報告。
- Data and results: Goat-7BはゼロショットでPaLM-540BのFew-shotと同等以上の精度を達成し、大規模な加減算でほぼ完璧な精度を示した。
- Novelty: 本研究は、学習困難なタスクを基本原理に基づき複数の学習可能なタスクに分解するアプローチを提案した点にある。
- Limitations: 編者の注意: 算術課題に特化した比較であり、論文タイトルのGPT-4超過を一般的な知能全体の優位性と解釈しない。数値のtokenizationと問題分解の条件に依存する。

### Paper: QLoRA: Efficient Finetuning of Quantized LLMs
- Source: arXiv
- Canonical ID: arxiv:2305.14314
- Publication date: 2023-05-23
- URL: https://arxiv.org/abs/2305.14314
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: QLoRAは、メモリ効率を保ちつつ大規模LLMのファインチューニングを可能にする手法である。
- Objective: いかにしてメモリ使用量を削減しつつ、高性能なLLMのファインチューニングを実現するか？
- Methods: 4-bitで凍結した事前学習モデルを通してLoRAへ勾配を伝える。NF4、量子化定数の二重量子化、paged optimizerを組み合わせ、1000超の微調整モデルで比較する。
- Data and results: 65Bモデルを単一48GB GPUで微調整可能と報告。GuanacoはVicuna評価でChatGPTのスコア水準の99.3%に達したが、これは全能力が99.3%という意味ではない。
- Novelty: 4-bit NormalFloat (NF4)や二重量子化など複数の革新により、メモリ消費を抑えつつ性能維持を実現した点。
- Limitations: 著者は当時のチャット評価ベンチマークの信頼性に問題を見いだし、GuanacoがChatGPTに失敗する事例も分析する。高い評価スコアを一般的な同等性と解釈しない。

### Paper: Direct Preference Optimization: Your Language Model is Secretly a Reward Model
- Source: arXiv
- Canonical ID: arxiv:2305.18290
- Publication date: 2023-05-29
- URL: https://arxiv.org/abs/2305.18290
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
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
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: MATHの候補解選別において、中間ステップへの教師信号が最終結果だけの教師信号より有効かを比較する。
- Objective: LLMの論理的誤りを減らすため、結果か過程のどちらで教師信号を与えるべきかを比較すること。
- Methods: PRM800Kの80万ステップラベルでprocess reward modelを学習し、候補解を段階の得点から選ぶ。大規模比較に加え、学習データ等を揃えた小規模合成監督でも比較する。
- Data and results: MATHテスト部分集合のbest-of-1860ではprocess監督78.2%、outcome監督72.4%、多数決69.6%。これは1回だけ生成したモデルの正答率ではなく、1860候補からの選別性能である。
- Novelty: プロセス監視がアウトカム監視よりも優位であり、アクティブラーニングもその効果を高めることを示した点。
- Limitations: 本文4節は大規模比較でPRM/ORMの学習データが直接比較できず、能動学習などが交絡すると指摘。合成監督で要因を分離するが、ラベル費用・採点器・候補数を揃えた比較が重要。

本文の照合箇所: [3、4、付録F.2・表4](https://arxiv.org/html/2305.20050v1)。

### Paper: AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration
- Source: arXiv
- Canonical ID: arxiv:2306.00978
- Publication date: 2023-06-01
- URL: https://arxiv.org/abs/2306.00978
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: AWQは、LLMの量子化誤差を低減する活性化認識型の重み量子化手法である。
- Objective: LLMのオンデバイス展開におけるモデルサイズとリソース制約という課題を解決する方法を探る。
- Methods: 活性化分布を参照し、重要な重みチャネルを特定した後、等価変換を用いてスケーリングすることでAWQを適用する。
- Data and results: 言語・コード・数学や多モダリティで量子化を評価。併設のTinyChatはkernel fusion等も用い、デスクトップ・モバイルGPUでHugging Face FP16実装より3倍超高速と報告。
- Novelty: 本手法は、バックプロパゲーションや再構築に依存せず、活性化統計からスケールを決定できる点が新規である。
- Limitations: 編者の注意: 重要な1%を保護するという表現は混合精度を残す設計ではなく、チャネルのスケーリングを使う。TinyChatの速度は量子化だけでなく実装・プラットフォームの効果も含む。

### Paper: Orca: Progressive Learning from Complex Explanation Traces of GPT-4
- Source: arXiv
- Canonical ID: arxiv:2306.02707
- Publication date: 2023-06-05
- URL: https://arxiv.org/abs/2306.02707
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: Orcaは、GPT-4の複雑な説明トレースから学習し、モデルが推論プロセスを模倣する能力を高めた13Bパラメータモデルである。
- Objective: 大規模言語モデル（LFM）の出力を利用した小規模モデルの性能向上における課題と、その解決策を探ること。
- Methods: Orcaは、GPT-4からの説明トレースや段階的な思考過程など、リッチな信号を利用して学習する。この進歩的な学習を促進するため、大規模で多様な模倣データを用いてサンプリングと選択を行った。
- Data and results: Orcaは、Big-Bench Hard (BBH)などの複雑なゼロショット推論ベンチマークにおいて、Vicuna-13Bより100%以上、AGIEvalでは42%高い性能を示した。また、CoTなしのSAT, LSAT, GRE, GMATでもChatGPTに匹敵する性能を示した。
- Novelty: 本研究は、単なる出力の模倣ではなく、GPT-4のような高度なAIモデルが生成するステップバイステップの説明から学習することで、推論プロセスを模倣する点にある。
- Limitations: 編者の注意: 教師の説明と模倣データの選択に依存する。記述された試験の相対改善を、あらゆる推論能力や正答保証の獲得と解釈しない。

### Paper: Llama 2: Open Foundation and Fine-Tuned Chat Models
- Source: arXiv
- Canonical ID: arxiv:2307.09288
- Publication date: 2023-07-18
- URL: https://arxiv.org/abs/2307.09288
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: Llama 2は、オープンな基盤モデルとチャット用にファインチューニングされたLLM群を開発・公開した。
- Objective: どのような大規模言語モデルが、オープンソースでありながら高性能で利用可能か？
- Methods: 70億から700億パラメータの範囲で事前学習済みおよびファインチューニングされたLLMを提供し、チャット用途に最適化したLlama 2-Chatを開発した。
- Data and results: テストしたほとんどのベンチマークにおいて、オープンソースのチャットモデルを上回り、有用性と安全性においても閉鎖型モデルの代替となり得る。
- Novelty: ファインチューニングと安全性の改善アプローチを詳細に記述し、コミュニティによる発展を可能にした点。
- Limitations: 編者の注意: 有用性と安全性は採用した人間評価とベンチマークに基づく。閉鎖モデルの全利用場面を代替できることや、未知の攻撃への安全性を保証しない。

### Paper: Graph of Thoughts: Solving Elaborate Problems with Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2308.09687
- Publication date: 2023-08-18
- URL: https://arxiv.org/abs/2308.09687
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: GoTはLLMの思考を任意グラフとしてモデル化し、複雑な問題解決能力を向上させるフレームワークである。
- Objective: LLMの推論能力を、既存の手法を超える形でどのように進展させられるかを探る。
- Methods: LLMが生成する情報を頂点、依存関係を辺とする任意グラフで表し、思考の結合、ネットワーク全体からの抽出、フィードバックによる改良を行う。
- Data and results: GoTはToTよりソートの質を62%向上させつつ、コストを31%以上削減できることを示した。
- Novelty: 本手法はLLMの思考を任意グラフで表現し、ネットワーク全体から本質的な出力を抽出可能にした点にある。
- Limitations: 編者の注意: 62%の品質向上と31%超の費用減は比較したソート課題の例である。グラフ表現の有効性は、脳の機構を再現したことを意味しない。

### Paper: Efficient Memory Management for Large Language Model Serving with PagedAttention
- Source: arXiv
- Canonical ID: arxiv:2309.06180
- Publication date: 2023-09-12
- URL: https://arxiv.org/abs/2309.06180
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: PagedAttentionとvLLMにより、KVキャッシュのメモリ効率を大幅に改善した。
- Objective: 大規模言語モデルのサービングにおけるKVキャッシュのメモリ管理問題を解決すること。
- Methods: 仮想メモリやページング技術に着想を得たPagedAttentionアルゴリズムを提案し、これを用いたvLLMシステムを構築した。
- Data and results: vLLMは、既存手法比でスループットが2-4倍向上し、レイテンシは同等に保たれた。
- Novelty: 仮想メモリのページング技術を応用し、KVキャッシュの断片化と重複を削減する点。
- Limitations: 編者の注意: 2〜4倍は同程度のlatency条件でのスループット比較である。単一要求の応答時間や外部ツールを含むエージェント全体の所要時間が同率で短くなることを意味しない。

### Paper: Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints
- Source: arXiv
- Canonical ID: arxiv:2309.16240
- Publication date: 2023-09-28
- URL: https://arxiv.org/abs/2309.16240
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 多様な発散制約を組み込んだ$f$-DPOにより、LLMの人間嗜好へのアライメントを効率化する。
- Objective: RLHFやDPOが抱える複雑性や報酬モデル依存性の課題を克服する方法を探る。
- Methods: Jensen-Shannonやforward KLなど多様な$f$-divergence制約を導入し、KKT条件を扱うことで最適ポリシーへのマッピングを可能にした。
- Data and results: $f$-DPOはPPOベースの手法より発散効率が高く、制約が期待較正誤差（ECE）に直接影響を与えることが示された。
- Novelty: 多様な発散制約を取り入れることで、報酬と最適ポリシーの関係を簡略化し、正規化定数の推定を不要とした点。
- Limitations: 編者の注意: 理論の簡略化は扱うf-divergenceと最適化条件に依存する。発散の効率、生成の多様性、校正は同一指標ではなく、要旨には個別スコアの数値がない。

### Paper: Mistral 7B
- Source: arXiv
- Canonical ID: arxiv:2310.06825
- Publication date: 2023-10-10
- URL: https://arxiv.org/abs/2310.06825
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: Mistral 7Bは、優れた性能と効率性を備えた7BパラメータのLLMである。
- Objective: 本モデルが既存の大規模言語モデルと比較してどのような性能向上を達成したか？
- Methods: グループ化クエリ注意機構（GQA）とスライディングウィンドウアテンション（SWA）を採用し、推論速度と長文処理能力を両立させた。
- Data and results: Mistral 7Bは、評価された全ベンチマークでLlama 2 13Bを上回り、推論、数学、コード生成ではLlama 1 34Bも凌駕した。
- Novelty: GQAとSWAの組み合わせにより、高速な推論と任意の長さのシーケンスへの対応を実現している点。
- Limitations: 編者の注意: SWAによる計算制限と、どの長さでも内容を正しく利用できる能力は区別する。性能優位は評価したモデル版・ベンチマークに対するもの。

### Paper: Mixtral of Experts
- Source: arXiv
- Canonical ID: arxiv:2401.04088
- Publication date: 2024-01-08
- URL: https://arxiv.org/abs/2401.04088
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: Mixtral 8x7Bは、スパースなMoE構造を持つ大規模言語モデルである。
- Objective: この新しいSMoEモデルが既存の最先端モデルと比較してどのような性能を示すか？
- Methods: 各層を8つのエキスパートから構成し、トークンごとにルーターが2つのエキスパートを選択して処理する。
- Data and results: 32K文脈で学習し、評価全体でLlama 2 70BやGPT-3.5に同等以上と報告。総47Bパラメータへアクセスできるがトークンごとに活動するのは13Bで、数学・コード・多言語ではLlama 2 70Bを上回った。
- Novelty: 各層で2つのエキスパートのみを使用しながらも、トークンごとに異なるエキスパートを利用可能にした点。
- Limitations: 編者の注意: 活動パラメータ13Bと全重み47Bの保存・配信コストを混同しない。比較結果は当時のモデル版とベンチマーク条件に依存する。

### Paper: KTO: Model Alignment as Prospect Theoretic Optimization
- Source: arXiv
- Canonical ID: arxiv:2402.01306
- Publication date: 2024-02-02
- URL: https://arxiv.org/abs/2402.01306
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: LLMアライメントの目的関数をプロスペクト理論に基づき最適化するKTO法を提案した。
- Objective: 人間のフィードバックに基づくLLMのアライメントにおいて、どのような損失関数が最も適切か？
- Methods: カネマン・トヴェルスキーのモデルを用い、選好の対数尤度最大化ではなく生成物の効用を直接最大化するHALOを設計し適用した。
- Data and results: KTOは1Bから30Bスケールで、バイナリ信号のみ学習しても既存の選好ベース手法と同等以上の性能を示した。
- Novelty: 従来の目的関数が対数尤度最大化であったのに対し、本研究では生成物の効用を直接最大化する損失関数を提案した点である。
- Limitations: 著者はすべての状況で優れる単一のHALOはなく、適切な帰納バイアスによって最良の損失が変わると指摘する。望ましいか否かの二値信号も、その判断者と分布に依存する。

### Paper: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models
- Source: arXiv
- Canonical ID: arxiv:2402.03300
- Publication date: 2024-02-05
- URL: https://arxiv.org/abs/2402.03300
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: DeepSeekMath 7Bは、数学的推論能力を向上させたオープンLLMである。
- Objective: 言語モデルの複雑な構造を持つ数学的推論という課題にどう対処するか。
- Methods: DeepSeek-Coder-Base-v1.5 7Bを120Bの数学関連トークンで継続事前学習し、GRPOを導入した。
- Data and results: 外部ツールや投票なしのMATH精度51.7%を報告。64サンプルのself-consistencyを用いると60.9%で、単発と複数試行の計算条件は異なる。
- Novelty: データ選択パイプラインと、メモリ効率を最適化したGroup Relative Policy Optimization (GRPO)の導入が特徴的である。
- Limitations: 編者の注意: 主な証拠は数学データ選別とMATH評価であり、GRPOの利点を全てのエージェント環境へ直接外挿しない。複数候補の投票は追加推論費用を要する。

### Paper: Smaug: Fixing Failure Modes of Preference Optimisation with DPO-Positive
- Source: arXiv
- Canonical ID: arxiv:2402.13228
- Publication date: 2024-02-20
- URL: https://arxiv.org/abs/2402.13228
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: DPOの失敗モードを修正するDPOPを提案し、性能向上を実現した。
- Objective: 標準DPO損失が持つ、好ましい例の尤度低下という問題点を特定すること。
- Methods: 標準DPOでは相対的な選好確率が上がっても望ましい応答そのものの尤度が下がることを理論・実験で示す。編集距離の小さい対で顕著な失敗を抑えるDPO-Positiveを設計。
- Data and results: DPOPは様々なデータセットやタスクでDPOを上回り、MT-Benchのような独立ベンチマークでも優位性を示した。
- Novelty: 標準DPOの失敗モードを回避するDPOPを提案し、よりロバストなファインチューニング手法を提供した点。
- Limitations: 編者の注意: 失敗の抑制と評価改善は調べたデータ・モデルに関する結果である。Smaugの当時のleaderboard成績は、現在の順位や全能力の保証を意味しない。

### Paper: Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone
- Source: arXiv
- Canonical ID: arxiv:2404.14219
- Publication date: 2024-04-22
- URL: https://arxiv.org/abs/2404.14219
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 38億パラメータのphi-3-miniは、小型ながら高性能なLLMであり、様々なタスクで高い能力を示す。
- Objective: スマートフォンでの展開を可能にしつつ、MixtralやGPT-3.5に匹敵する性能を持つモデルを開発すること。
- Methods: 訓練データセットはフィルタリングされたウェブデータと合成データから構成され、ロバスト性、安全性、チャット形式へのアライメントが追加で行われた。
- Data and results: phi-3-miniはMMLUで69%、MT-benchで8.38を達成し、小型モデルながら高い性能を示した。
- Novelty: 厳しく選別したWebデータと合成データを使い、端末に載る3.8Bモデルで強い言語評価を目指す。後続改訂ではPhi-3.5系列も追加報告されている。
- Limitations: 編者の注意: 要旨は後の改訂内容も含み、公開日はv1の初回投稿日である。学術・内部評価での同等性を、全利用条件での大規模モデル代替やスマートフォン上の全性能と解釈しない。

### Paper: WPO: Enhancing RLHF with Weighted Preference Optimization
- Source: arXiv
- Canonical ID: arxiv:2406.11827
- Publication date: 2024-06-17
- URL: https://arxiv.org/abs/2406.11827
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: WPOは、オフポリシーデータでRLHFの分布ギャップを是正する手法である。
- Objective: オフポリシーでの好み最適化が抱える分布ギャップの問題をどう解決するか？
- Methods: 現在のポリシーに基づき、好みのペアを重み付け再調整し、オンポリシー学習をシミュレーションする。
- Data and results: Alpaca Eval 2でDPOを最大5.6%上回ると報告。Gemma-2-9b-itを基にしたモデルのGPT-4-turboへのlength-controlled勝率は76.7%。
- Novelty: オフポリシーデータに重み付けを行うことで、分布ギャップを是正しつつ最適化を強化する点。
- Limitations: 編者の注意: 勝率は特定の評価器・対戦相手・長さ補正条件の値である。再重み付けによる分布補正の効果を、すべての人間の選好との一致と解釈しない。

### Paper: The Llama 3 Herd of Models
- Source: arXiv
- Canonical ID: arxiv:2407.21783
- Publication date: 2024-07-31
- URL: https://arxiv.org/abs/2407.21783
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: Llama 3は、多言語性やコーディングをネイティブにサポートする大規模モデル群である。
- Objective: Llama 3が様々なタスクにおいて既存の最先端モデルと同等の性能を発揮するかどうかを検証すること。
- Methods: 最大405Bのdense Transformerと最大128K文脈を持つモデル群を評価。事前・事後学習モデルと安全性モデルを公開し、画像・動画・音声の構成的統合も実験する。
- Data and results: Llama 3は、多数のタスクにおいてGPT-4のような主要言語モデルに匹敵する品質を提供することが判明した。
- Novelty: 本研究では、多言語性、コーディング、推論、ツール使用をネイティブにサポートする新しい大規模モデル群「Llama 3」を発表した点である。
- Limitations: 原著執筆時点では画像・動画・音声を統合したモデルは開発中で、広く公開されていない。要旨の記述は当時の公開状態であり、現在の提供状況の確認とは別である。

### Paper: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters
- Source: arXiv
- Canonical ID: arxiv:2408.03314
- Publication date: 2024-08-06
- URL: https://arxiv.org/abs/2408.03314
- read_level: abstract
- Tags: 基礎文献, 言語モデルの学習・推論・効率化
- Summary: 問題の難易度に応じた推論時計算の配分により、一定条件ではモデル大型化より効率的に性能を伸ばせることを示す。
- Objective: 固定された推論時間計算量を許容した場合、LLMの性能向上度はどの程度か？
- Methods: 密な検証器報酬モデルに対する検索と、プロンプトに応じた応答分布の適応的更新という2つのメカニズムを分析した。
- Data and results: 「計算量最適」戦略を用いることで、ベスト・オブ-Nベースラインより効率が4倍以上向上し、FLOPs同等で小型モデルが大型モデルを上回ることも示した。
- Novelty: プロンプトの難易度に応じてテスト時計算量を適応的に配分する「計算量最適」戦略を提案した点。
- Limitations: 著者の14倍大きいモデル超過は、小型モデルにも一定の成功率がある問題をFLOPs一致で比べた条件の結果である。最難関問題を含むすべての条件で推論時計算が大型化を代替するとは示さない。

<!-- PAPER_IDS -->
arxiv:1301.3781
arxiv:1310.4546
arxiv:1409.0473
arxiv:1409.3215
arxiv:1412.6980
arxiv:1502.05477
arxiv:1503.02531
arxiv:1506.02640
arxiv:1508.04025
arxiv:1511.06434
arxiv:1605.07678
arxiv:1606.06565
arxiv:1606.08415
arxiv:1607.06450
arxiv:1611.02731
arxiv:1701.06538
arxiv:1706.03741
arxiv:1706.03762
arxiv:1707.06347
arxiv:1710.05941
arxiv:1711.05101
arxiv:1712.01815
arxiv:1802.05365
arxiv:1810.04805
arxiv:1902.00751
arxiv:1906.08237
arxiv:1907.11692
arxiv:1909.08593
arxiv:1909.11942
arxiv:1910.01108
arxiv:1910.10683
arxiv:1910.13461
arxiv:1911.02150
arxiv:2001.08361
arxiv:2003.10555
arxiv:2004.05150
arxiv:2005.14165
arxiv:2006.16668
arxiv:2009.01325
arxiv:2101.00190
arxiv:2101.03961
arxiv:2104.08691
arxiv:2106.09685
arxiv:2110.04366
arxiv:2201.11903
arxiv:2203.02155
arxiv:2203.11171
arxiv:2203.14465
arxiv:2203.15556
arxiv:2204.02311
arxiv:2205.05638
arxiv:2205.10625
arxiv:2205.11916
arxiv:2205.14135
arxiv:2207.09238
arxiv:2210.03629
arxiv:2210.03350
arxiv:2210.11416
arxiv:2210.17323
arxiv:2211.10435
arxiv:2211.17192
arxiv:2212.08073
arxiv:2212.10560
arxiv:2302.13971
arxiv:2303.11366
arxiv:2305.10601
arxiv:2305.14201
arxiv:2305.14314
arxiv:2305.18290
arxiv:2305.20050
arxiv:2306.00978
arxiv:2306.02707
arxiv:2307.09288
arxiv:2308.09687
arxiv:2309.06180
arxiv:2309.16240
arxiv:2310.06825
arxiv:2401.04088
arxiv:2402.01306
arxiv:2402.03300
arxiv:2402.13228
arxiv:2404.14219
arxiv:2406.11827
arxiv:2407.21783
arxiv:2408.03314
<!-- /PAPER_IDS -->
