# 基礎文献 — 言語モデルの学習・推論・効率化

> schema_version: 1
> report_date: 2026-11-14

## ダイジェスト

選定101件中、以下は原著照合・編集確認を終えた31件。選定リストだけの論文を完成済み件数には含めない。原著要旨までの記述と本文確認を区別し、Limitationsの「編者の注意」は著者の自己申告と区別する。

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

<!-- PAPER_IDS -->
arxiv:1301.3781
arxiv:1310.4546
arxiv:1409.0473
arxiv:1409.3215
arxiv:1508.04025
arxiv:1511.06434
arxiv:1606.08415
arxiv:1607.06450
arxiv:1706.03762
arxiv:1711.05101
arxiv:1802.05365
arxiv:1810.04805
arxiv:1906.08237
arxiv:1907.11692
arxiv:1909.11942
arxiv:1910.01108
arxiv:1910.10683
arxiv:1910.13461
arxiv:2001.08361
arxiv:2003.10555
arxiv:2004.05150
arxiv:2005.14165
arxiv:2104.08691
arxiv:2201.11903
arxiv:2203.11171
arxiv:2203.15556
arxiv:2204.02311
arxiv:2205.10625
arxiv:2210.17323
arxiv:2212.10560
arxiv:2306.02707
<!-- /PAPER_IDS -->
