# 基礎文献 — 表形式・時系列・因果推論

> schema_version: 1
> report_date: 2026-11-14

## ダイジェスト

選定119件中、以下は原著照合・編集確認を終えた30件。選定リストだけの論文を完成済み件数には含めない。原著要旨までの記述と本文確認を区別し、Limitationsの「編者の注意」は著者の自己申告と区別する。

研究の流れと2026年論文との接続は [文献集の案内](README.md) を参照。

## 完全版レポート

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
arxiv:1603.02754
arxiv:1811.11264
arxiv:1907.00503
arxiv:1908.07442
arxiv:1909.06312
arxiv:2006.06465
arxiv:2012.06678
arxiv:2105.02584
arxiv:2106.01342
arxiv:2106.11959
arxiv:2204.00401
arxiv:2206.00664
arxiv:2207.01848
arxiv:2207.08815
arxiv:2209.15421
arxiv:2210.04018
arxiv:2210.06280
arxiv:2210.10723
arxiv:2304.13188
arxiv:2305.11097
arxiv:2309.13793
arxiv:2310.20447
arxiv:2311.10609
arxiv:2312.07577
arxiv:2312.06089
arxiv:2402.11137
arxiv:2402.14335
arxiv:2406.05216
arxiv:2407.04057
arxiv:2410.24210
<!-- /PAPER_IDS -->
