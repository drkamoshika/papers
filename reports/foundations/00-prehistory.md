# 基礎文献 — さらに前の主要な出発点

> report_date: 2026-11-14

以下はarXiv/PubMed以外の出版社・主催機関の一次資料を確認した古典12件である。主編の556件とは別に数える。個別項目の形式は共通とし、存在しないarXiv IDを作らずDOIまたは出版社識別子を使う。日付は確認できた精度で扱い、月までしか分からないものに架空の日を補わない。

## 完全版レポート

### Paper: Learning representations by back-propagating errors
- Source: Publisher
- Canonical ID: doi:10.1038/323533a0
- Publication date: 1986-10-09
- URL: https://www.nature.com/articles/323533a0
- read_level: abstract
- Tags: 基礎文献, 誤差逆伝播, 表現学習
- Summary: 目標出力との差が小さくなるよう接続重みを反復的に調整し、隠れユニットに課題の特徴を獲得させる学習手順を示す。
- Objective: 入出力として直接与えない内部表現を、ニューラルネットワークが学習によって形成できるかを調べる。
- Methods: 実出力と所望出力の差を損失として、誤差逆伝播によりネットワークの重みを繰り返し更新する。
- Data and results: 原著要旨は、隠れユニットが重要な特徴を表し、課題の規則性がユニット間相互作用に表現されることを報告する。要旨に統一的なデータ規模・精度の数値はない。
- Novelty: 特徴を固定して分類器だけを学習する考え方から、目的に応じて内部特徴そのものを学ぶ表現学習を前面に出す。
- Limitations: 編者の注意: 要旨は現代の大規模モデルの収束や汎化を保証していない。本論文を誤差逆伝播の唯一の起源とみなす主張はしていない。

研究の系譜: 今日の事前学習、LoRA、選好最適化でも、目的関数がどの内部表現や重みを変更するかという共通の問題が残る。この接続は編集上の比較である。

### Paper: Long Short-Term Memory
- Source: Publisher
- Canonical ID: doi:10.1162/neco.1997.9.8.1735
- Publication date: 1997-11-15
- URL: https://ieeexplore.ieee.org/abstract/document/6795963/
- read_level: abstract
- Tags: 基礎文献, RNN, 長期依存, 記憶
- Summary: 再帰学習で誤差が減衰する問題に対し、誤差の流れを保つ内部ユニットと乗算ゲートを用いて長い時間依存を学習する。
- Objective: 離れた時点の情報を学習する際、誤差の逆流が弱まるため学習が遅くなる問題を扱う。
- Methods: constant error carouselを持つ特殊ユニットと、誤差の流れへのアクセスを調整する乗算ゲートを導入し、人工系列課題で既存の再帰学習法と比較する。
- Data and results: 人工データで1000離散時点を超える依存を橋渡しでき、複数の既存再帰学習法より成功試行が多く高速に学習したと報告する。自然な長期実務の成功率を測ったものではない。
- Novelty: 長期情報の保存経路とアクセス制御を構造として持ち、通常の再帰誤差伝播で難しかった長期依存を扱う。
- Limitations: 編者の注意: 主な検証は人工系列であり、現代のLSTMの変種やLLMのファイル記憶とは構造も評価設定も異なる。長期記憶という名称だけで同等視しない。

研究の系譜: seq2seqからTransformerへの移行を読む前に、再帰計算、勾配の伝播、長期依存という出発点を確認する。エージェントの外部記憶とは別の層の「記憶」である。

### Paper: Random Forests
- Source: Publisher
- Canonical ID: doi:10.1023/A:1010933404324
- Publication date: 未記載
- URL: https://link.springer.com/article/10.1023/A:1010933404324
- read_level: abstract
- Tags: 基礎文献, 表形式, 木, アンサンブル
- Summary: 独立に生成されるランダム性に依存した決定木を組み合わせ、個々の木の強さと相関が森林の汎化誤差にどう関わるかを調べる。
- Objective: 決定木の集合の予測性能を、構成する木の性質と関連付けて理解し、頑健なアンサンブルを構成する。
- Methods: 各木が独立同分布のランダムベクトルに依存する森林を構成。節点ごとのランダムな特徴選択を用い、汎化誤差の性質と実験成績を評価する。
- Data and results: 木の数を増やしたときの汎化誤差の極限と、個々の木の強さ・木間相関の関係を示す。実験ではAdaBoostと競争的でノイズに強いと報告。要旨に統一的な精度値はない。
- Novelty: 強い個体を作るだけでなく、個体間の相関を抑えるランダム化を性能の重要要因として明示する。
- Limitations: 編者の注意: 誤差が極限へ収束することは誤差がゼロになることではない。出版社は2001年10月までの刊行情報を示すため、日単位の公開日は未確定としている。

研究の系譜: XGBoost、FT-Transformer、TabPFN、TabRなどを読む際、深層モデルだけでなく木・アンサンブル・特徴量処理という強い比較対象を置くための出発点となる。

### Paper: A Neural Probabilistic Language Model
- Source: Publisher
- Canonical ID: jmlr:bengio03a
- Publication date: 未記載
- URL: https://jmlr.csail.mit.edu/papers/v3/bengio03a
- read_level: abstract
- Tags: 基礎文献, 言語モデル, 分散表現
- Summary: 単語の分散表現と、その表現を用いた単語系列の確率関数を同時に学習し、未観測の系列への汎化を図る。
- Objective: 語の組合せが膨大になる次元の呪いの下で、未観測の文にも妥当な確率を与える言語モデルを学ぶ。
- Methods: 各単語の連続表現と系列の確率をニューラルネットワークで同時に学習。表現空間で似た単語を持つ系列の間で統計的な情報を共有させる。
- Data and results: 二つのテキストコーパスで当時のn-gram方式より改善し、長い文脈を利用できると報告する。要旨にはコーパス別の困惑度の数値が示されない。
- Novelty: 単語の類似性を学習する表現と確率的言語予測を一体化し、観測した系列から意味的に近い未観測系列へ汎化させる。
- Limitations: 著者は数百万パラメータ規模でも実用時間内の学習が大きな課題と述べる。出版社の刊行情報は2003年2月であり、日付は推定せず未記載とした。

研究の系譜: word2vec、文脈化埋め込み、事前学習言語モデルへ進む前に、なぜ単語の連続表現と予測学習が結び付いたかを確認する。

### Paper: Term-weighting approaches in automatic text retrieval
- Source: Publisher
- Canonical ID: doi:10.1016/0306-4573(88)90021-0
- Publication date: 未記載
- URL: https://www.sciencedirect.com/science/article/pii/0306457388900210
- read_level: abstract
- Tags: 基礎文献, 情報検索, term weighting
- Summary: 単語への重み付けに基づく検索の実験的知見を整理し、複雑な表現法を比較するための基準を示す。
- Objective: 自動索引で適切な単語重みを選ぶことが検索性能にどう関わるかを整理する。
- Methods: 過去約20年の実験的知見からterm weightingを概説し、単一termによる索引のbaselineを提示する。
- Data and results: 要旨は、適切に重み付けした単一term表現が複雑な表現より良い検索結果を得るという蓄積を述べる。要旨にdataset別の性能値はない。
- Novelty: 表現の複雑さより重みの選び方を比較の中心に置き、再利用できるbaselineを整理する。
- Limitations: 編者の注意: 1988年の知見であり、現代のdense retrievalへの優越を主張する資料ではない。出版社の公開情報では年まで確認し、日付は補わない。

研究の系譜: DPRやColBERTの比較対象となる語彙検索を理解するための出発点。検索改善が表現、重み、query拡張のどこに由来するかを分けて読む。

### Paper: Okapi at TREC-3
- Source: NIST
- Canonical ID: doi:10.6028/NIST.SP.500-225.routing-city
- Publication date: 未記載
- URL: https://pages.nist.gov/trec-browser/trec3/proceedings/#okapi-at-trec-3
- read_level: abstract
- Tags: 基礎文献, 情報検索, Okapi, BM25
- Summary: Okapiのterm weighting、passage検索、query拡張と関連feedbackをTREC-3で検討した報告。
- Objective: query情報が減る条件でも検索を改善するため、重み付け・検索単位・拡張語選択を洗練する。
- Methods: term weightingの修正、検索中のpassage決定、上位文書からのad hoc query拡張、関連feedback後の語選択、対話interfaceを検討する。
- Data and results: TREC-3ではquery拡張とroutingの語選択が主な成果。重みの修正とpassage検索の効果は小さく、組合せでCONCEPTS field欠落の影響をかなり補ったと報告する。
- Novelty: 語彙検索を単一のscore式だけでなく、feedback・passage・query拡張を含む系として評価する。
- Limitations: 編者の注意: NISTの要旨で確認した範囲ではBM25の詳細式・parameter別結果を再掲できない。1994年TRECの会期は公開日と区別し、日単位の刊行日は未確定とした。

研究の系譜: RAGの検索器を評価するとき、neural化の効果とquery拡張・rerankingの効果を切り分けるために読む。

### Paper: A Formal Basis for the Heuristic Determination of Minimum Cost Paths
- Source: Publisher
- Canonical ID: doi:10.1109/TSSC.1968.300136
- Publication date: 1968-07-31
- URL: https://ieeexplore.ieee.org/abstract/document/4082128/authors
- read_level: abstract
- Tags: 基礎文献, 探索, A-star, 計画
- Summary: 問題領域のheuristicをgraph探索の理論へ取り込み、探索戦略の最適性を検討する。
- Objective: 最小費用経路を効率的に見つける探索手順の理論的基盤を与える。
- Methods: domain知識に基づくheuristicを形式的なgraph探索へ組み込み、探索戦略群の性質を解析する。
- Data and results: 要旨は探索戦略のある最適性を示すと述べる。実験datasetや成功率の数値は要旨にはない。
- Novelty: heuristicによる探索を経験則だけでなく、最適性を論じる数学的枠組みに置く。
- Limitations: 編者の注意: 要旨だけでは全定理の仮定を列挙できない。LLMが生成するheuristicや不確実なworld modelに同じ保証が成立すると主張するものではない。

研究の系譜: Tree of Thoughts、RAP、LATS等の探索を読む際、探索空間・状態評価・停止条件・計算予算を分けるための原点となる。

### Paper: Strips: A new approach to the application of theorem proving to problem solving
- Source: Publisher
- Canonical ID: doi:10.1016/0004-3702(71)90010-5
- Publication date: 未記載
- URL: https://www.sciencedirect.com/science/article/pii/0004370271900105
- read_level: abstract
- Tags: 基礎文献, 計画, world model, STRIPS
- Summary: 初期world modelを目標式が成り立つmodelへ変えるoperator列を探索する問題解決系。
- Objective: 大きな論理式集合で表した世界から、目標に至る行動系列を求める。
- Methods: 一階述語論理でworld modelを表し、resolution theorem proverでmodelへの問いに答え、means-ends analysisで探索を導く。
- Data and results: 要旨はSTRIPSの構成と問題解決方式を報告する。benchmarkの規模・成功率は要旨にはない。
- Novelty: 論理的world model、operatorによる状態変換、目標へ向かう探索を結合する。
- Limitations: 編者の注意: 記号的な状態・operatorを使う設定であり、自然言語からの正しい状態推定や確率的実環境への適用が自動的に保証されるわけではない。出版社はWinter 1971と記載する。

研究の系譜: 現在のtool agentでも、行動の前提条件・効果・観測後の状態更新をどのように表すかという計画の問題が残る。

### Paper: Learning to predict by the methods of temporal differences
- Source: Publisher
- Canonical ID: doi:10.1007/BF00115009
- Publication date: 未記載
- URL: https://link.springer.com/article/10.1007/BF00115009
- read_level: abstract
- Tags: 基礎文献, 強化学習, temporal difference
- Summary: 最終結果との誤差ではなく、時間的に隣接する予測の差から逐次的に学習する方法を整理する。
- Objective: 不完全に分かったsystemの経験から、未来を予測する学習法を理解する。
- Methods: temporal differenceを学習信号とする逐次手順を示し、特定の場合の収束・最適性と教師あり学習との関係を解析する。
- Data and results: 特殊な場合の理論保証を報告し、従来法に対するmemory・peak計算量・予測精度の利点を論じる。要旨に統一的な数値比較はない。
- Novelty: 最終的な結果を待つ学習と、予測から次の予測へ情報を伝える学習を区別する。
- Limitations: 理論保証は特定の場合に関するものと著者が明記する。編者の注意: 任意の非線形LLMや非定常agentでの収束を保証しない。刊行情報は1988年8月まで。

研究の系譜: value推定、credit assignment、actor-criticと現在のagent RLを読む前に、何を予測目標として更新するかを確認する。

### Paper: Technical Note: Q-Learning
- Source: Publisher
- Canonical ID: doi:10.1023/A:1022676722315
- Publication date: 未記載
- URL: https://doi.org/10.1023/A:1022676722315
- read_level: abstract
- Tags: 基礎文献, 強化学習, Q-learning
- Summary: Markov環境で状態ごとの行動価値を逐次改善するQ-learningの収束を証明する。
- Objective: modelを用いた動的計画に対し、経験から行動価値を学ぶ手順の理論的性質を示す。
- Methods: Watkinsの先行手順をもとに、離散的に表す行動価値と全状態・全行動の反復samplingの下で収束定理を証明する。
- Data and results: その条件下で最適行動価値へ確率1で収束すると示す。非割引の吸収Markov環境等への拡張も概説する。
- Novelty: 単純な逐次更新法の有効性を、明示した条件下の収束として裏付ける。
- Limitations: 離散的な価値表現と十分なsamplingが条件。編者の注意: 巨大な部分観測状態やニューラル近似で同じ保証をそのまま使えない。刊行情報は1992年5月まで。

研究の系譜: agentの経験再利用やRLでは、探索不足、状態表現、報酬の設計を、modelの言語能力とは別に考える。

### Paper: The central role of the propensity score in observational studies for causal effects
- Source: Publisher
- Canonical ID: doi:10.1093/biomet/70.1.41
- Publication date: 1983-04-01
- URL: https://academic.oup.com/biomet/article-abstract/70/1/41/240879?login=false
- read_level: abstract
- Tags: 基礎文献, 因果推論, propensity score
- Summary: 観測共変量を条件とする治療割当確率という単一scoreによる調整を示す。
- Objective: 多数の観測共変量を持つ観察研究で、治療群間の差をどう調整するかを扱う。
- Methods: propensity scoreを定義し、大小標本の理論、matching、subclassification、可視化への応用を示す。
- Data and results: 単一scoreで調整することで観測共変量に由来するbiasを除けるという理論を報告する。要旨に実患者での治療効果の数値はない。
- Novelty: 多次元の共変量調整を、治療割当確率に基づく一次元の調整へ結び付ける。
- Limitations: 編者の注意: 観測共変量に関する性質であり、未観測交絡の除去を保証しない。予測精度が高いscoreを作ることと因果効果の識別は同一ではない。

研究の系譜: causal forestやdouble machine learningでも、柔軟な学習器によって未観測交絡という識別上の問題が解消するわけではない。

### Paper: Regression Models and Life-Tables
- Source: Publisher
- Canonical ID: doi:10.1111/j.2517-6161.1972.tb00899.x
- Publication date: 未記載
- URL: https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1972.tb00899.x
- read_level: abstract
- Tags: 基礎文献, 医療, survival analysis, Cox model
- Summary: 打切りのある生存時間に対し、共変量の効果と未知の時間関数を分けたhazard回帰を扱う。
- Objective: 説明変数を持つ個人の打切り故障・生存時間から、回帰係数を推測する。
- Methods: hazardを共変量と未知係数の関数に、任意の未知時間関数を掛けた形に置き、条件付き尤度から係数を推定する。
- Data and results: 未知の基準hazardを残したまま回帰係数について推測する方法と一般化を提示。要旨に予測accuracyや患者規模はない。
- Novelty: 生存時間の時間依存部分を完全に指定せず、共変量との関係を推測する枠組みを与える。
- Limitations: 編者の注意: hazardのモデル構造を置く方法であり、あらゆる時間変化や交絡を解決しない。出版社情報は1972年までを採用し、会合日や月表示を日単位の正式公開日へ変換しない。

研究の系譜: 深層生存予測やEHR risk modelを読む際、打切り、hazard、時点ごとのrisk、校正という評価対象を確認する。
