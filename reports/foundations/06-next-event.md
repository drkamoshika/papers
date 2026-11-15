# 基礎文献 — 次イベント予測・点過程

> schema_version: 1
> report_date: 2026-11-15

## ダイジェスト

選定100件中、一次資料へ照合した20件を掲載する。要旨確認と本文の関連箇所確認を区別し、要旨にない数値は補わない。「編者の注意」は著者の自己申告した限界と区別する。

研究の流れ・読み順・比較軸は[総覧](README.md)を参照。

## 完全版レポート

### Paper: Decoupled Learning for Factorial Marked Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:1801.06805
- Publication date: 2018-01-21
- URL: https://arxiv.org/abs/1801.06805
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 一つの事象に複数のマークを付けるfactorial marked TPPを効率的に学ぶ。
- Objective: マークを組み合わせたときに増える相互影響の推定負荷を減らす。
- Methods: ADMM・FISTAによる解法とlogistic回帰への再定式化を用い、疎なgroup正則化を加える。
- Data and results: 実データで分離・再定式化した学習の効率を検証。要旨にはデータ名や速度の絶対値がない。
- Novelty: 事象の複数属性を保ちながら、学習問題を分離する。
- Limitations: 編者の注意: 疎な関係の選択は正則化とマーク定義に依存し、解釈をそのまま因果機構としない。

### Paper: Intensity-Free Learning of Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:1909.12127
- Publication date: 2019-09-26
- URL: https://arxiv.org/abs/1909.12127
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Intensity-Free TPPは強度ではなく、事象間時間の条件付き分布を直接学ぶ。
- Objective: 柔軟性、尤度計算、標本化の間の制約を減らす。
- Methods: normalizing flowと、標本化・モーメント計算を閉形式で行える混合分布を設計する。
- Data and results: 標準予測課題で高い性能を報告し、列の埋め込みと欠損補完への応用も示す。
- Novelty: 強度関数中心の設計から待ち時間分布中心の設計へ移る。
- Limitations: 編者の注意: 強度を明示しないことは履歴の影響がないことを意味せず、混合成分数などの選択も残る。

### Paper: Fast and Flexible Temporal Point Processes with Triangular Maps
- Source: arXiv
- Canonical ID: arxiv:2006.12631
- Publication date: 2020-06-22
- URL: https://arxiv.org/abs/2006.12631
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: TriTPPは三角写像で事象列を表し、標本化と尤度計算を並列化する。
- Objective: RNN型TPPの逐次計算による速度制限を解消する。
- Methods: normalizing flowを利用する非再帰型モデルを構成し、連続時間の離散状態系の変分推論にも使う。
- Data and results: 人工・実データでRNN型の柔軟性を保ち、標本化を桁違いに高速化したと報告。
- Novelty: 時間順の写像構造を利用し、履歴RNNを使わずに点過程を構成する。
- Limitations: 編者の注意: 標本化の高速化と学習全体・すべての推論の高速化は区別し、計算環境をそろえて比較する。

### Paper: Neural Spatio-Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2011.04583
- Publication date: 2020-11-09
- URL: https://arxiv.org/abs/2011.04583
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Neural ODEと連続正規化フローで、連続時間・空間の事象分布を学ぶ。
- Objective: 複雑な位置分布と時刻分布を履歴に応じて同時に表す。
- Methods: Jump型とAttentive型の連続時間normalizing flowを神経微分方程式と組み合わせる。
- Data and results: 地震、疫学、都市の移動、神経科学のデータでモデルを検証。要旨には個別の件数や誤差がない。
- Novelty: 時空間の密度変換と履歴依存を連続時間モデルに統合する。
- Limitations: 編者の注意: 空間密度の適合と次時刻の校正は異なり、ODE計算の負荷も比較条件になる。

### Paper: Long Horizon Forecasting With Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2101.02815
- Publication date: 2021-01-08
- URL: https://arxiv.org/abs/2101.02815
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: DualTPPは個々の発生時刻と時間窓内の件数を併用して長期予測する。
- Objective: 遠い将来で起こる逐次予測の劣化を減らす。
- Methods: 強度を直接使わないTPPと集約件数モデルを、制約付き二次最適化による共同推論で結ぶ。
- Data and results: 複数の実データで長期予測を改善し、真の列とのWasserstein距離がおよそ一桁小さくなる結果を報告。
- Novelty: 事象ごとの微視的予測を、窓ごとの巨視的な件数で拘束する。
- Limitations: 編者の注意: 距離の改善は評価した長期設定の結果で、次時刻の誤差すべてが一桁減るという主張ではない。

### Paper: Neural Temporal Point Processes: A Review
- Source: arXiv
- Canonical ID: arxiv:2104.03528
- Publication date: 2021-04-08
- URL: https://arxiv.org/abs/2104.03528
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 神経TPPの設計原理と応用を整理したレビュー。
- Objective: 増えたモデルを、共通の設計上の選択肢から理解できるようにする。
- Methods: モデルの定義方法、主要な設計判断、応用領域と未解決課題を文献に沿って整理する。
- Data and results: 新しい予測器の実験成績ではなく、モデル構成と研究課題の総覧を提供する。
- Novelty: 個別アーキテクチャより一般原則に重点を置く入門の接続点。
- Limitations: レビューのため独自モデルの優位性を示す研究ではない。編者の注意: 2021年以降のLLM・拡散モデルは別途補う。

### Paper: Semi-supervised Learning for Marked Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2107.07729
- Publication date: 2021-07-16
- URL: https://arxiv.org/abs/2107.07729
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: SSL-MTPPは種別ラベルのない事象列も利用する半教師あり学習。
- Objective: 時刻は分かるが事象カテゴリが不足する状況で種別予測を改善する。
- Methods: RNNのencoder-decoderで時間系列を表現し、ラベル付き・ラベルなしのデータを併用する。
- Data and results: Retweetデータを複数の評価手順で検証し、通常の教師あり学習より改善したと報告。
- Novelty: 種別予測への監督の不足を点過程の学習設定に取り込む。
- Limitations: 編者の注意: 要旨の実証範囲はRetweetであり、異分野や異なる欠測機構への一般化は未確認。

### Paper: An Empirical Study: Extensive Deep Temporal Point Process
- Source: arXiv
- Canonical ID: arxiv:2110.09823
- Publication date: 2021-10-19
- URL: https://arxiv.org/abs/2110.09823
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 深層TPPを部品へ分解し、構成の違いをそろえた比較を行う。
- Objective: 履歴符号化、強度、事象間関係、最適化の寄与を整理する。
- Methods: 部品を組み替え同じ学習法で評価し、変分推論による離散Grangerグラフ学習も導入する。
- Data and results: 潜在関係の推定を加えた方式が、事象間関係の把握と適合・予測を改善したと報告。
- Novelty: モデル名ごとの比較から、設計要素と関係構造の比較へ進める。
- Limitations: 編者の注意: Granger関係は履歴を条件とする予測的依存であり、隠れた交絡を除いた介入因果ではない。

### Paper: Counterfactual Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2111.07603
- Publication date: 2021-11-15
- URL: https://arxiv.org/abs/2111.07603
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 観測した点過程について、強度を変えた場合の反実仮想の事象列を生成する。
- Objective: 予測用モデルを、介入を比較するための反実仮想シミュレーションへ拡張する。
- Methods: Gumbel-Max構造因果モデルに基づくthinningと重ね合わせを使い、代替強度下の列を標本化する。
- Data and results: 人工データと実際の疫学データを使うシミュレーションで、対象を絞った介入への示唆を検討する。
- Novelty: 反実仮想の単調性条件を満たす点過程の間引き機構を構成する。
- Limitations: 編者の注意: 反実仮想の同定は構造モデルと単調性の仮定に依存し、観測データだけで介入効果が確定するわけではない。

### Paper: Variational Neural Temporal Point Process
- Source: arXiv
- Canonical ID: arxiv:2202.10585
- Publication date: 2022-02-17
- URL: https://arxiv.org/abs/2202.10585
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: VNTPPは潜在変数の分布を使い、次の事象種別と時刻を予測する。
- Objective: 特定種別への過適合を抑え、変化する事象間関係に対応する。
- Methods: 推論網と生成網を変分学習し、潜在分布から条件付き強度を計算する。
- Data and results: 人工・実データで種別表現の一般化と既存の深層・統計モデルに対する予測改善を報告。要旨には絶対スコアがない。
- Novelty: 決定論的な履歴表現に潜在状態の確率分布を組み込む。
- Limitations: 編者の注意: 潜在分布の導入だけで分布変化への保証や校正が成立するわけではない。

### Paper: ProActive: Self-Attentive Temporal Point Process Flows for Activity Sequences
- Source: arXiv
- Canonical ID: arxiv:2206.05291
- Publication date: 2022-06-10
- URL: https://arxiv.org/abs/2206.05291
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: ProActiveは次行動、活動の目標、行動列の生成を共通の点過程で扱う。
- Objective: 個人ごとに所要時間が異なる活動を連続時間でモデル化する。
- Methods: self-attentionと時間normalizing flowを組み合わせ、margin制約で少ない行動から目標を推定する。
- Data and results: 活動認識3データ由来の列で行動・目標予測を改善し、端から端の行動列生成も示す。
- Novelty: 次の一手だけでなく、目標の早期推定と列全体の生成を統合する。
- Limitations: 編者の注意: 認識済み行動の列を使う評価は、未処理の映像から行動を検出する課題とは異なる。

### Paper: Exploring Generative Neural Temporal Point Process
- Source: arXiv
- Canonical ID: arxiv:2208.01874
- Publication date: 2022-08-03
- URL: https://arxiv.org/abs/2208.01874
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: GNTPPは事象時刻の予測を複数の深層生成モデルで比較する枠組み。
- Objective: 尤度の適合度と生成した時刻の精度の隔たりを調べる。
- Methods: 生成デコーダを共通の枠組みに載せ、種別関係と時間差でattentionを再重み付けする。
- Data and results: 複数の生成デコーダの予測改善と、改良attentionの寄与を実験で報告。要旨には課題別の改善幅がない。
- Novelty: 生成手法と履歴符号化を共通の比較単位として扱う。
- Limitations: 編者の注意: 尤度、時刻誤差、事象列全体の分布忠実度は別々に評価する必要がある。

### Paper: HyperHawkes: Hypernetwork based Neural Temporal Point Process
- Source: arXiv
- Canonical ID: arxiv:2210.00213
- Publication date: 2022-10-01
- URL: https://arxiv.org/abs/2210.00213
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: HyperHawkesは未見の事象列への転移と継続学習を扱う。
- Objective: 少ない監督で新しい列を予測し、過去の列に関する忘却を減らす。
- Methods: hypernetworkで点過程のパラメータを生成し、zero-shotと継続学習の構成を作る。
- Data and results: 実データ2種類で未見列の将来時刻予測と過去の列の保持を評価し、有効性を報告。
- Novelty: 列ごとの点過程をパラメータ生成の側から適応させる。
- Limitations: 編者の注意: 未見の列への転移は、未知の事象語彙や任意の分野への転移を意味しない。

### Paper: Meta Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2301.12023
- Publication date: 2023-01-27
- URL: https://arxiv.org/abs/2301.12023
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Meta TPPは各事象列を別の課題として学ぶメタ学習型の点過程。
- Objective: 全列を一括学習するだけでは取り込みにくい列ごとの差を利用する。
- Methods: neural processとして定式化し、context集合と局所履歴のmatchingで特徴を学ぶ。
- Data and results: 公開ベンチマーク上で既存TPPと比較し、提案方式の可能性を示す。要旨では課題別スコアを確認できない。
- Novelty: 点過程を文脈条件付きの課題間学習として捉える。
- Limitations: 編者の注意: contextの選び方、利用可能な履歴量、列間の類似性が転移性能を左右する。

### Paper: Prompt-augmented Temporal Point Process for Streaming Event Sequence
- Source: arXiv
- Canonical ID: arxiv:2310.04993
- Publication date: 2023-10-08
- URL: https://arxiv.org/abs/2310.04993
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: PromptTPPは流入し続ける事象列を、検索型promptの集合で継続学習する。
- Objective: 過去データを保存せずに分布変化へ適応し、忘却を減らす。
- Methods: 連続時間のprompt poolを基盤TPPと共同最適化し、過去の例や課題属性をbufferに残さない。
- Data and results: 実際の利用者行動3データで、提案した逐次学習設定における既存法への優位を報告。
- Novelty: promptの選択と履歴モデルの更新を連続時間の流れへ適用する。
- Limitations: 編者の注意: ここでのpromptは学習パラメータであり、自然言語指示やLLM利用を意味しない。

### Paper: Add and Thin: Diffusion for Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2311.01139
- Publication date: 2023-11-02
- URL: https://arxiv.org/abs/2311.01139
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: ADD-THINは事象の追加と間引きを用い、列全体を拡散モデルで生成する。
- Objective: 自己回帰的な一歩予測を繰り返す際の長期誤差の蓄積を抑える。
- Methods: 離散的な事象数と連続的な時刻を扱える確率的な拡散・雑音除去過程を導く。
- Data and results: 人工・実データで密度推定は既存の高性能TPPと同等、将来列の予測は大きく改善したと報告。
- Novelty: 事象列の可変長構造を保つ追加・間引きの生成機構。
- Limitations: 編者の注意: 密度推定と長期予測で結論が異なるため、単一の総合的な勝敗へまとめない。

### Paper: Explainable History Distillation by Marked Temporal Point Process
- Source: arXiv
- Canonical ID: arxiv:2311.07797
- Publication date: 2023-11-13
- URL: https://arxiv.org/abs/2311.07797
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 将来の分布を左右する少数の過去事象を抽出し、予測の説明に用いる。
- Objective: 除去すると観測された将来の予測が悪化する最小限の履歴を見つける。
- Methods: history distillationを0–1整数計画として書き換え、解を直接推定するモデルを学習する。
- Data and results: RetweetとStackOverflowで既存の履歴抽出法を上回ると報告。抽出事象を将来の説明として提示する。
- Novelty: 事前に指定した変更を比較する代わりに、説明用の履歴自体を探す。
- Limitations: 編者の注意: モデル内での除去による予測変化は、実世界でその事象を防いだ場合の因果効果と同一ではない。

### Paper: Cumulative Hazard Function Based Efficient Multivariate Temporal Point Process Learning
- Source: arXiv
- Canonical ID: arxiv:2404.13663
- Publication date: 2024-04-21
- URL: https://arxiv.org/abs/2404.13663
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 累積ハザードの数学的制約を満たしながら、多変量TPPを少ないパラメータで学ぶ。
- Objective: 強度積分の近似誤差と、事象種別数によるモデルの大型化を抑える。
- Methods: 積分された強度を神経網で直接表し、累積ハザードとしての制約を守る構成を用いる。
- Data and results: 6データで適合度・予測を評価し、比較対象より少ないパラメータとメモリで高い性能を報告。
- Novelty: 累積ハザードの妥当性と多変量モデルの効率を同時に扱う。
- Limitations: 編者の注意: 尤度を正確に計算できることと、将来の分布や不確実性が正しく校正されることは別である。

### Paper: Neuro-Symbolic Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2406.03914
- Publication date: 2024-06-06
- URL: https://arxiv.org/abs/2406.03914
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 時間論理規則を点過程の中で学び、不規則な事象を説明する。
- Objective: 少数の説明規則を効率的に発見する。
- Methods: 述語を固定埋め込み、規則を学習埋め込みとし、尤度損失と逐次被覆法で規則を追加・再調整する。
- Data and results: 人工・実データで精度と効率を評価し、既存法に対する特に計算効率の改善を報告。
- Novelty: 連続的な規則表現と逐次的な規則集合構築を統合する。
- Limitations: 編者の注意: 規則の解釈可能性と因果的な正しさは別であり、述語の設計にも結果が依存する。

### Paper: Decoupled Marked Temporal Point Process using Neural Ordinary Differential Equations
- Source: arXiv
- Canonical ID: arxiv:2406.06149
- Publication date: 2024-06-10
- URL: https://arxiv.org/abs/2406.06149
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Decoupled MTPPは、各事象から続く影響を別々の連続時間状態として表す。
- Objective: 個々の事象が将来の全体動態にどう寄与するかを捉える。
- Methods: 影響の時間発展をNeural ODEで学び、密度と生存確率など複数の推論へ利用する。
- Data and results: 実データで既存法と比較し、影響分離の意義とモデルの挙動を分析。要旨には絶対値がない。
- Novelty: 列全体の一つの状態だけでなく、事象ごとの影響の進化を学ぶ。
- Limitations: 編者の注意: 分離した影響成分を、交絡を除いた実世界の因果効果と読み替えない。

<!-- PAPER_IDS -->
arxiv:2202.10585
arxiv:2208.01874
arxiv:2210.00213
arxiv:2111.07603
arxiv:2301.12023
arxiv:2311.07797
arxiv:2110.09823
arxiv:2011.04583
arxiv:2104.03528
arxiv:2406.03914
arxiv:2310.04993
arxiv:2404.13663
arxiv:2406.06149
arxiv:2206.05291
arxiv:2101.02815
arxiv:2311.01139
arxiv:1909.12127
arxiv:2107.07729
arxiv:1801.06805
arxiv:2006.12631
<!-- /PAPER_IDS -->
