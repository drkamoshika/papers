# 基礎文献 — 次イベント予測・点過程

> schema_version: 1
> report_date: 2026-11-15

## ダイジェスト

選定100件中、一次資料へ照合した100件を掲載する。要旨確認と本文の関連箇所確認を区別し、要旨にない数値は補わない。「編者の注意」は著者の自己申告した限界と区別する。

研究の流れ・読み順・比較軸は[総覧](README.md)を参照。

## 完全版レポート

### Paper: Calibration diagnostics for point process models via the probability integral transform
- Source: arXiv
- Canonical ID: arxiv:1305.3409
- Publication date: 2013-05-15
- URL: https://arxiv.org/abs/1305.3409
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: PITを使い、点過程の予測分布が校正されているかを診断する。
- Objective: 強度や相互作用構造に潜む不整合を検出する。
- Methods: PoissonではPITを明示計算し、一般の過程ではモデルからの標本を使って評価する。
- Data and results: 多次元の点過程にも適用できる校正診断を提案。要旨には特定の予測モデルの精度競争はない。
- Novelty: 確率積分変換を、点patternのモデル検証へ適用する。
- Limitations: 編者の注意: 校正の診断はモデル間の識別力や業務上の効用と同一ではなく、十分な標本が必要。

### Paper: Sparse and low-rank multivariate Hawkes processes
- Source: arXiv
- Canonical ID: arxiv:1501.00725
- Publication date: 2015-01-04
- URL: https://arxiv.org/abs/1501.00725
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Hawkes相互作用に疎性と低rankを課し、時刻列から潜在ネットワークを推定する。
- Objective: 少ない接続と共通構造を利用して高次元推定を安定させる。
- Methods: 最小二乗損失にL1・trace normを加え、観測可能な分散を使うmatrix martingaleの集中不等式から係数を調整する。
- Data and results: 理論解析と数値実験で、データ依存の正則化による改善を示す。要旨に実データの規模はない。
- Novelty: 疎性・低rankの両方を誘導する正則化を理論的に調整する。
- Limitations: 編者の注意: 推定構造は正則化仮定に依存する。時刻の依存から解剖学的接続や介入因果を直接確定しない。

### Paper: Learning Granger Causality for Hawkes Processes
- Source: arXiv
- Canonical ID: arxiv:1602.04511
- Publication date: 2016-02-14
- URL: https://arxiv.org/abs/1602.04511
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Hawkesの影響カーネルの疎性からGrangerグラフを学ぶ。
- Objective: どの種別の過去が別種別の発生を予測するかを抽出する。
- Methods: 基底関数で影響を表し、最大尤度にsparse-group-lassoを加える。基底の適応選択も検討する。
- Data and results: 人工・実データでGrangerグラフと発火を促す時間パターンを同時推定できると報告。
- Novelty: カーネル係数のgroup疎性とGranger関係を結び付ける。
- Limitations: 編者の注意: Granger因果の解釈にはモデル化と観測範囲の仮定が必要で、隠れた交絡を除いた介入効果ではない。

### Paper: Uncovering Causality from Multivariate Hawkes Integrated Cumulants
- Source: arXiv
- Canonical ID: arxiv:1607.06333
- Publication date: 2016-07-21
- URL: https://arxiv.org/abs/1607.06333
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 積分された高次cumulantから、Hawkesの影響の総量を推定する。
- Objective: カーネル形状を決めたり推定したりせず、節点間の関係を捉える。
- Methods: 三次までの積分cumulantを利用するmoment matchingで、積分カーネル行列を求める。
- Data and results: 数値実験で形状への頑健性を示し、MemeTrackerでも有望な結果を報告。
- Novelty: 時間的な影響の形ではなく、総量を非母数的に同定する。
- Limitations: 編者の注意: 積分量は遅れの詳細を捨てる。論文の因果という表現はHawkesモデル内の関係として読む。

### Paper: The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process
- Source: arXiv
- Canonical ID: arxiv:1612.09328
- Publication date: 2016-12-29
- URL: https://arxiv.org/abs/1612.09328
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Neural Hawkesは連続時間LSTMで励起と抑制を伴う事象列を表す。
- Objective: 過去の事象が将来の確率を複雑に上げ下げする依存を学ぶ。
- Methods: 連続時間で進む隠れ状態から、複数種別の条件付き強度を生成する。
- Data and results: 実・人工データで尤度と予測精度を評価し、欠測がある設定でも競争力を示す。
- Novelty: 線形加算の励起に限らず、履歴の神経状態による自己変調を導入する。
- Limitations: 編者の注意: 欠測条件での実験は任意の欠測機構への頑健性を保証せず、隠れ状態の成分は直接の機構説明ではない。

### Paper: Learning Hawkes Processes from Short Doubly-Censored Event Sequences
- Source: arXiv
- Canonical ID: arxiv:1702.07013
- Publication date: 2017-02-22
- URL: https://arxiv.org/abs/1702.07013
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 短く、始端・終端とも観測が切れた事象列からHawkesを学ぶ。
- Objective: 観測窓の外の履歴と続きが欠けることによる推定劣化を減らす。
- Methods: 候補列から前後の事象をsamplingし、接続して長い訓練列を合成する。尤度に基づき妥当性を議論する。
- Data and results: 人工・実データで、時不変・時変のHawkesの両方における学習改善を報告。
- Novelty: 打切りを単なる短い系列として扱わず、前後の補助列で補う。
- Limitations: 編者の注意: 接続された履歴は合成であり、元の未観測の事象を実測・確定したものではない。

### Paper: Wasserstein Learning of Deep Generative Point Process Models
- Source: arXiv
- Canonical ID: arxiv:1705.08051
- Publication date: 2017-05-23
- URL: https://arxiv.org/abs/1705.08051
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Wasserstein距離を使い、強度や尤度を明示しない生成点過程を学ぶ。
- Objective: 固定的な強度形や多峰性のある列分布の尤度学習の制約を減らす。
- Methods: 元となる確率過程を目標過程へ変換し、列分布間のWasserstein距離を利用して訓練する。
- Data and results: 複数の人工・実データで通常の点過程モデルに対する利点を示す。要旨には個別の数値がない。
- Novelty: 待ち時間の密度だけでなく、列全体の分布距離を学習目的へ持ち込む。
- Limitations: 編者の注意: 尤度を使わない方式は、尤度値を主指標とする方式との比較で目的関数の差を明示する必要がある。

### Paper: Modeling The Intensity Function Of Point Process Via Recurrent Neural Networks
- Source: arXiv
- Canonical ID: arxiv:1705.08982
- Publication date: 2017-05-24
- URL: https://arxiv.org/abs/1705.08982
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 背景の変化と過去事象の影響を、二つのRNNで表す点過程。
- Objective: 固定間隔の背景と非同期の履歴をそれぞれの時間構造で学ぶ。
- Methods: 背景用RNNは時間index、履歴用RNNは事象indexへ合わせ、種類・時刻予測まで一括学習する。
- Data and results: 北米に本拠を置く銀行の1,000台超のATMログで予防保全へ適用。要旨に予測成績の値はない。
- Novelty: 二種類の時間軸を分けて強度の背景と履歴成分へ対応させる。
- Limitations: 編者の注意: 予防保全への適用を、保全介入の費用削減や故障減少の実証へ読み替えない。

### Paper: Outcome-Oriented Predictive Process Monitoring: Review and Benchmark
- Source: arXiv
- Canonical ID: arxiv:1707.06766
- Publication date: 2017-07-21
- URL: https://arxiv.org/abs/1707.06766
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 業務caseの最終結果を途中履歴から予測する手法のレビューと比較。
- Objective: 異なるデータ・基準法による従来研究の比較困難を減らす。
- Methods: 体系的レビューと分類を行い、実ログ9種類に基づく24課題で11手法を比較する。
- Data and results: 共通benchmarkによる実験的比較と、各方式の適用性を整理する。要旨に一つの勝者の数値はない。
- Novelty: 結果予測を共通条件で整理する評価資源を提供する。
- Limitations: 次活動ではなくcaseの結果分類が対象。編者の注意: 最終結果・残り時間・次事象の精度を混同しない。

### Paper: THAP: A Matlab Toolkit for Learning with Hawkes Processes
- Source: arXiv
- Canonical ID: arxiv:1708.09252
- Publication date: 2017-08-28
- URL: https://arxiv.org/abs/1708.09252
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: THAPはHawkesとその変種の学習・分析をまとめたMatlabツール。
- Objective: 古典から近年のアルゴリズムまで再利用しやすくする。
- Methods: 複数の学習アルゴリズムと分析機能を共通のtoolkitとして実装・公開する。
- Data and results: 研究・教育用の実装資源を提供。要旨は新しい一つの予測器の精度比較を主成果としていない。
- Novelty: Hawkes研究の推定手法を一つの利用可能な環境へ集約する。
- Limitations: 編者の注意: 2017年の対象範囲であり、後発の神経TPP・LLMや現在の実行環境への対応は別途確認が必要。

### Paper: Sequence to Sequence Learning for Event Prediction
- Source: arXiv
- Canonical ID: arxiv:1709.06033
- Publication date: 2017-09-18
- URL: https://arxiv.org/abs/1709.06033
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 先行文から次の事象の説明文を生成するseq2seqモデル。
- Objective: 文章中の次事象を、固定カテゴリの選択以外の形で予測する。
- Methods: 双方向多層RNNを用い、BLEUに加えて正解事象の言い換え注釈を使う評価を行う。
- Data and results: WikiHowとDeScript由来の2データで従来研究よりBLEUを改善したと報告。
- Novelty: 自由文の次事象生成に、表面的な語一致を補う言い換え評価を組み合わせる。
- Limitations: 著者はBLEUの事象予測指標としての解釈の難しさを指摘。実時間の発生時刻予測とは別の課題。

### Paper: Benefits from Superposed Hawkes Processes
- Source: arXiv
- Canonical ID: arxiv:1710.05115
- Publication date: 2017-10-14
- URL: https://arxiv.org/abs/1710.05115
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Hawkes過程の重ね合わせが推定に役立つ条件を調べる。
- Objective: 複数列の情報共有によって推定誤差を減らす。
- Methods: 最小二乗推定の枠組みで超過riskの上界を解析し、成立する典型的な条件を検討する。
- Data and results: 人工データで利点を確認し、推薦のcold-start問題への可能性を実データで示す。
- Novelty: 重ね合わせを単なる数学的操作から、推定精度の改善手段へつなぐ。
- Limitations: 改善は一定の条件下の上界と実験による。編者の注意: 異質な列を無条件に混ぜればよいという結果ではない。

### Paper: LSTM Networks for Data-Aware Remaining Time Prediction of Business Process Instances
- Source: arXiv
- Canonical ID: arxiv:1711.03822
- Publication date: 2017-11-10
- URL: https://arxiv.org/abs/1711.03822
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 事象に付随する属性を使い、進行中caseの完了までの時間をLSTMで予測する。
- Objective: service level agreement下で、完了の遅れを早く見通す。
- Methods: 単一事象に関連する任意の情報を取り込む深層再帰モデルを構成する。
- Data and results: 実データで提案方式を検証。要旨には課題数や平均誤差の絶対値がない。
- Novelty: 活動ラベルだけでなく、事象属性を残り時間の予測へ利用する。
- Limitations: 編者の注意: 完了時刻の予測は次事象時刻と異なる。結果を知った後に記録される属性を入力へ入れない。

### Paper: Temporal Stability in Predictive Process Monitoring
- Source: arXiv
- Canonical ID: arxiv:1712.04165
- Publication date: 2017-12-12
- URL: https://arxiv.org/abs/1712.04165
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 同じ業務caseへの予測が時間とともに揺れる程度を評価する。
- Objective: 精度だけでなく、人が行動を決める際の予測の安定性を改善する。
- Methods: 二値の結果予測について時間安定性を定義し、分類器の調整と時系列平滑化を比較する。
- Data and results: XGBoost・LSTMが高い安定性を示し、調整や平滑化でさらに改善。ただし平滑化は精度を少し下げる。
- Novelty: 逐次更新される予測の一貫性を、運用上の独立した評価軸へ加える。
- Limitations: 安定性と精度のtrade-offがある。編者の注意: 安定して間違う予測もあり、安定性だけを最適化しない。

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

### Paper: Superposition-Assisted Stochastic Optimization for Hawkes Processes
- Source: arXiv
- Canonical ID: arxiv:1802.04725
- Publication date: 2018-02-13
- URL: https://arxiv.org/abs/1802.04725
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 多主体Hawkesの重ね合わせを使い、確率的最適化を改善する。
- Objective: 共有する内因的影響を学び、特にデータの少ない主体を補う。
- Methods: 外因強度は主体別、影響関数は共有とし、多様性に基づく重ね合わせを確率的最大尤度へ導入する。
- Data and results: 条件付きのrisk上界改善を示し、人工データと逐次推薦のcold-startで検証する。
- Novelty: 重ね合わせの選び方を、学習と収束性の改善へ組み込む。
- Limitations: 内因的な影響を共有するモデルが前提。編者の注意: 異質な主体への適用では共有仮定を確かめる必要がある。

### Paper: Predictive Process Monitoring Methods: Which One Suits Me Best?
- Source: arXiv
- Canonical ID: arxiv:1804.02422
- Publication date: 2018-04-06
- URL: https://arxiv.org/abs/1804.02422
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 予測process monitoringを、利用価値から選ぶための分類枠組み。
- Objective: 手元のデータから何を予測でき、どの方法が適するかを整理する。
- Methods: 既存研究を体系的に抽出・分類・分析し、価値を基準とするframeworkへまとめる。
- Data and results: 新しい予測器の実験成績ではなく、組織が手法と用途を選ぶための見取り図を提供する。
- Novelty: 技術名の一覧を、意思決定に結び付く価値の分類へ変える。
- Limitations: レビューであり費用対効果をすべての現場で測った研究ではない。対象は2018年時点までの研究範囲。

### Paper: Survey and cross-benchmark comparison of remaining time prediction methods in business process monitoring
- Source: arXiv
- Canonical ID: arxiv:1805.02896
- Publication date: 2018-05-08
- URL: https://arxiv.org/abs/1805.02896
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 業務processの残り時間予測を体系的に整理し、共通データで比較する。
- Objective: 異なる実験条件のため不明だった各方式の相対的な長所を明らかにする。
- Methods: 文献レビューと分類を行い、異業種の実データ16種類で16手法をcross-benchmark比較する。
- Data and results: 残り時間予測の共通実験を提供。要旨には一律に優位な方式や誤差の絶対値はない。
- Novelty: 残り時間という特定の目的に焦点を当て、方式選択の比較基盤を作る。
- Limitations: 編者の注意: 残り時間の誤差と、次活動の分類精度や次の待ち時間の誤差は異なる尺度である。

### Paper: Lecture Notes: Temporal Point Processes and the Conditional Intensity Function
- Source: arXiv
- Canonical ID: arxiv:1806.00221
- Publication date: 2018-06-01
- URL: https://arxiv.org/abs/1806.00221
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 条件付き強度から時間点過程を定義する短い講義ノート。
- Objective: 時間の不規則な事象列を扱うための共通の数学を導入する。
- Methods: 強度による定義、尤度推論、simulation、residual解析を順に説明する。
- Data and results: 教育的な整理が成果であり、実データ上の新しい予測器の成績を提示する研究ではない。
- Novelty: モデルを読む際に繰り返し現れる強度・尤度・残差を一つの入口へまとめる。
- Limitations: 入門ノートのため高度な神経構造やLLMは対象外。編者の注意: 基本定義と特定モデルの実験的優位は区別する。

### Paper: Efficient Non-parametric Bayesian Hawkes Processes
- Source: arXiv
- Canonical ID: arxiv:1810.03730
- Publication date: 2018-10-08
- URL: https://arxiv.org/abs/1810.03730
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 分岐表現を使い、柔軟なHawkesカーネルと不確実性を効率的に推定する。
- Objective: 非母数Bayes推定の計算量を抑え、大きい拡散データに対応する。
- Methods: 有限の影響時間を仮定し、block GibbsとEMによるMAP推定を導く。
- Data and results: 人工データでカーネルを復元し、Twitter拡散2データで適合度改善とデータ量に線形の計算量を報告。
- Novelty: 分岐構造によるPoissonのcluster分解を計算効率へ利用する。
- Limitations: 有限supportが効率性の仮定。編者の注意: 動画ジャンル別のカーネル差は内容の寿命を反映する解釈で、独立した因果実証ではない。

### Paper: Fully Neural Network based Model for General Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:1905.09690
- Publication date: 2019-05-23
- URL: https://arxiv.org/abs/1905.09690
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 強度の積分を神経網で表し、その微分として柔軟な強度を得る。
- Objective: 固定的な時間減衰形と、尤度積分の数値近似を避ける。
- Methods: RNNの履歴に条件付けたfeedforward網で累積強度をモデル化し、自動微分で強度を計算する。
- Data and results: 人工・実データで既存法と同等以上の成績を報告。尤度を数値積分なしに計算できる点が核となる。
- Novelty: 積分しやすい強度を探す代わりに、積分量を直接パラメータ化する。
- Limitations: 編者の注意: 後続研究が累積ハザードの完全な制約を問題にしており、柔軟さと数学的な妥当性を分けて確認する。

### Paper: Self-Attentive Hawkes Processes
- Source: arXiv
- Canonical ID: arxiv:1907.07561
- Publication date: 2019-07-17
- URL: https://arxiv.org/abs/1907.07561
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: SAHPはself-attentionで事象履歴を集約し、次の種別と時刻を予測する。
- Objective: 長い履歴の依存を表現し、寄与をたどりやすくする。
- Methods: 多変量点過程の強度をattentionに基づいて構成し、過去事象の重みを表示する。
- Data and results: 実データ4種類で有効性を検証。要旨には個別の予測誤差やデータ規模はない。
- Novelty: 再帰計算の代わりに、過去の事象間のattentionを使う。
- Limitations: 編者の注意: attention重みはモデル内部の寄与であり、事象を取り除く介入の因果効果を保証しない。

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

### Paper: Learning Hawkes Processes from a Handful of Events
- Source: arXiv
- Canonical ID: arxiv:1911.00292
- Publication date: 2019-11-01
- URL: https://arxiv.org/abs/1911.00292
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 少ない事象からHawkesネットワークを学ぶため、正則化と不確実性を適応させる。
- Objective: 短い観測列での過適合と、単一の共有正則化係数の制約を減らす。
- Methods: 変分EMで拡張したhyperparameter集合を最適化し、パラメータの事後分布も学習する。
- Data and results: 人工・実データの短い観測設定で、既存法を大きく上回ると報告。
- Novelty: データ不足を、柔軟な正則化とパラメータ分布の推定で扱う。
- Limitations: 編者の注意: 少数事象からの復元は事前分布・正則化に影響され、任意の疎観測で識別可能になるわけではない。

### Paper: Deep Fourier Kernel for Self-Attentive Point Processes
- Source: arXiv
- Canonical ID: arxiv:2002.07281
- Publication date: 2020-02-17
- URL: https://arxiv.org/abs/2002.07281
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Deep Fourier Kernelは、複雑な類似性を持つattentionを点過程へ導入する。
- Objective: 通常の内積では捉えにくい非線形な時間依存を表す。
- Methods: スペクトルを神経網で表すFourierカーネルをattention scoreと条件付き強度へ組み込む。
- Data and results: 理論的性質を解析し、人工・実データで既存法に対し競争力のある成績を報告。
- Novelty: attentionの類似性尺度そのものを学習可能なスペクトルで拡張する。
- Limitations: 編者の注意: 要旨では理論の前提やカーネル設定の詳細が分からず、すべての非線形依存を復元する保証とは扱わない。

### Paper: Transformer Hawkes Process
- Source: arXiv
- Canonical ID: arxiv:2002.09291
- Publication date: 2020-02-21
- URL: https://arxiv.org/abs/2002.09291
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Transformer Hawkes Processはattentionで長い事象履歴を表現する。
- Objective: 短期・長期の依存を捉え、RNN型の点過程の予測を改善する。
- Methods: self-attentionで履歴を符号化し、事象間の関係情報を加えた複数過程の学習も検討する。
- Data and results: 複数データで尤度と事象予測を改善し、関係情報を組み込んだ構成でも改善を報告。
- Novelty: Transformerの履歴表現を連続時間の強度モデルへ導入する。
- Limitations: 編者の注意: モデル名にHawkesとあっても、古典的な線形励起カーネルの推定と同じ制約・解釈を持つとは限らない。

### Paper: Learning Multivariate Hawkes Processes at Scale
- Source: arXiv
- Canonical ID: arxiv:2002.12501
- Publication date: 2020-02-28
- URL: https://arxiv.org/abs/2002.12501
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 疎な拡散事象の構造を使い、大規模な多変量Hawkesを学ぶ。
- Objective: ネットワークの次元による尤度・勾配の計算負荷を抑える。
- Methods: 実データの疎なパターンを利用し、周囲の全次元に依存せず正確な尤度と勾配を求めるモデルを構成する。
- Data and results: 人工・実データで予測成績を保ち、疎な列では標準法より計算時間を数桁短縮したと報告。
- Novelty: 解釈可能な潜在変数・影響構造と大規模計算を両立する。
- Limitations: 編者の注意: 速度の利点は疎な事象列の構造に依存し、密な相互作用でも同じ短縮が得られるとは限らない。

### Paper: Predictive Business Process Monitoring via Generative Adversarial Nets: The Case of Next Event Prediction
- Source: arXiv
- Canonical ID: arxiv:2003.11268
- Publication date: 2020-03-25
- URL: https://arxiv.org/abs/2003.11268
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 敵対的学習を業務ログの次事象予測へ適用する。
- Objective: データ不足やモデル構成による一般化の弱さを改善する。
- Methods: 時系列向けにGANを適応し、二つの網を対抗させて次事象を学ぶ。非敵対設定との最悪精度の関係も解析する。
- Data and results: 実験では精度と予測の早さを改善し、case長による成績変動にも頑健と報告。
- Novelty: 複雑な特徴設計より、敵対的な訓練目的で次事象予測を改善する。
- Limitations: 編者の注意: 理論上の最悪精度の主張には前提があり、任意の学習・分布変化でGANが常に優位とは読まない。

### Paper: Graph Hawkes Neural Network for Forecasting on Temporal Knowledge Graphs
- Source: arXiv
- Canonical ID: arxiv:2003.13432
- Publication date: 2020-03-30
- URL: https://arxiv.org/abs/2003.13432
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Graph Hawkes Neural Networkは、多関係graphの変化を神経点過程で学ぶ。
- Objective: すべての候補linkを別の種別とすると巨大になる事象空間へ対応する。
- Methods: 神経的に自己変調するHawkesをgraphへ拡張し、将来時点の事実の発生を予測する。
- Data and results: 大規模な時間知識graphを含む多関係データで有効性を報告。要旨には規模や精度の絶対値がない。
- Novelty: 節点間の関係の組合せを扱える形で、事象の強度モデルを拡張する。
- Limitations: 編者の注意: link候補数と負例の作り方で難度が変わるため、他のTPPと同じ予測課題だと仮定しない。

### Paper: Spatio-Temporal Point Processes with Attention for Traffic Congestion Event Modeling
- Source: arXiv
- Canonical ID: arxiv:2005.08665
- Publication date: 2020-05-15
- URL: https://arxiv.org/abs/2005.08665
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 道路の方向と過去の事故情報を使い、渋滞事象の時空間依存を学ぶ。
- Objective: 既存渋滞と交通事故が後続の渋滞へ与える異なる影響を表す。
- Methods: sensor件数と警察報告を組み合わせ、attention付き点過程と道路向けtail-up空間モデルを使う。
- Data and results: 人工・実データで既存法より高い性能を報告。要旨には事故の収集期間や予測誤差の値はない。
- Novelty: 多種の観測と道路の方向構造を、事象の励起モデルへ統合する。
- Limitations: 編者の注意: 事故報告の記録時刻と実際の予測時点での利用可能時刻の差は、漏洩の確認事項になる。

### Paper: Shallow Neural Hawkes: Non-parametric kernel estimation for Hawkes processes
- Source: arXiv
- Canonical ID: arxiv:2006.02460
- Publication date: 2020-06-03
- URL: https://arxiv.org/abs/2006.02460
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Shallow Neural Hawkesは浅い神経網で励起カーネルを柔軟に推定する。
- Objective: Hawkesの解釈を保ちながら、固定形状でない時間的影響を学ぶ。
- Methods: 尤度推定の不偏推定量を導き、単一隠れ層の網と確率勾配法でカーネルを推定する。
- Data and results: 人工・実データで既存推定法と同等以上の成績を報告。要旨には速度や誤差の数値がない。
- Novelty: 非標準の励起形状を小さい神経網で学び、Hawkesの構造を維持する。
- Limitations: 編者の注意: カーネルの柔軟性が増しても、モデルの励起構造や観測条件に関する仮定は残る。

### Paper: Uncertainty Quantification for Inferring Hawkes Networks
- Source: arXiv
- Canonical ID: arxiv:2006.07506
- Publication date: 2020-06-12
- URL: https://arxiv.org/abs/2006.07506
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Hawkesネットワークの最大尤度推定に有限標本の信頼集合を与える。
- Objective: 推定された事象間関係の不確実性を定量化する。
- Methods: 連続時間martingaleの集中不等式を使い、Granger関係を表す有向グラフの推論を構成する。
- Data and results: 従来の漸近的な区間と比較し、神経接続の復元で利点を示す。要旨には区間幅の具体値がない。
- Novelty: 漸近近似だけに依存しないHawkesネットワークの不確実性評価。
- Limitations: 編者の注意: Granger関係はモデルと観測範囲に依存し、解剖学的シナプスや介入因果との同一視はできない。

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

### Paper: UNIPoint: Universally Approximating Point Processes Intensities
- Source: arXiv
- Canonical ID: arxiv:2007.14082
- Publication date: 2020-07-28
- URL: https://arxiv.org/abs/2007.14082
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: UNIPointは有効な強度関数を普遍近似できる関数族から作る。
- Objective: 神経TPPの柔軟性を理論的に説明し、単純な実装で活用する。
- Methods: 非負関数の近似と動的系・RNNを結び、事象ごとに基底関数の和のパラメータを更新する。
- Data and results: 普遍近似の証明に加え、人工・実データでHawkes変種や複雑な神経モデルへの予測上の利点を報告。
- Novelty: 強度の表現力の理論と基底関数型RNNの設計を接続する。
- Limitations: 編者の注意: 近似できることは有限標本で学べることや、最適化で正しい強度へ到達することの保証ではない。

### Paper: XNAP: Making LSTM-based Next Activity Predictions Explainable by Using LRP
- Source: arXiv
- Canonical ID: arxiv:2008.07993
- Publication date: 2020-08-18
- URL: https://arxiv.org/abs/2008.07993
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: XNAPはLSTMの次活動予測に、活動ごとの関連度を付ける。
- Objective: process analystが予測の根拠を理解できるようにする。
- Methods: layer-wise relevance propagationをLSTMへ統合し、入力活動へrelevanceを割り当てる。
- Data and results: 実際のevent log2種類で有用性を示す。要旨は介入による業務改善まで実証していない。
- Novelty: 深層の次活動予測を、履歴活動の寄与へ分解する。
- Limitations: 編者の注意: LRPはモデルの予測説明であり、関連度の高い活動を変更した場合の因果効果を直接示さない。

### Paper: An empirical investigation of different classifiers, encoding and ensemble schemes for next event prediction using business process event logs
- Source: arXiv
- Canonical ID: arxiv:2008.10748
- Publication date: 2020-08-24
- URL: https://arxiv.org/abs/2008.10748
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 業務ログの次事象予測で、分類器・履歴窓・ensembleを比較する。
- Objective: ログの性質に応じた手法と特徴量の選択を支援する。
- Methods: 異なる符号化窓とensemble構成を共通benchmarkで評価する。
- Data and results: 最適な履歴長はログごとに異なる。ensembleはSVMなどを改善するが、強い木系分類器では追加利得がなかった。
- Novelty: 次事象予測におけるensembleの効果と履歴窓の関係を調べる。
- Limitations: 万能な履歴窓やensembleは見いだしていない。編者の注意: 平均精度だけで全ログへの推奨を決めない。

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

### Paper: xERTE: Explainable Reasoning on Temporal Knowledge Graphs for Forecasting Future Links
- Source: arXiv
- Canonical ID: arxiv:2012.15537
- Publication date: 2020-12-31
- URL: https://arxiv.org/abs/2012.15537
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: xERTEは問い合わせに関連する時間部分graphをたどって将来linkを予測する。
- Objective: 埋め込みだけの予測に、人が読める根拠を与える。
- Methods: 時間・関係attentionと逆向き表現更新により、時間的な隣接節点をsamplingして部分graphを拡張する。
- Data and results: 4ベンチマークでHits@1を最大20%相対改善と報告。53人の調査で抽出根拠と人の理解の整合も検証する。
- Novelty: 時間的構造を予測と説明の両方に使う部分graph探索。
- Limitations: 編者の注意: 根拠の理解しやすさは因果的正しさと別。20%は相対改善で20ポイントではない。

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

### Paper: Temporal Knowledge Graph Forecasting with Neural ODE
- Source: arXiv
- Canonical ID: arxiv:2101.05151
- Publication date: 2021-01-13
- URL: https://arxiv.org/abs/2101.05151
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Neural ODEで時間知識graphの連続的な埋め込み変化を表す。
- Objective: 離散snapshotだけでは表しにくい、時間の連続性を利用する。
- Methods: 多関係GCNをNeural ODEへ拡張し、辺の生成・消失を扱うgraph transition層を加える。
- Data and results: 5ベンチマークで将来link予測を評価し、高い性能を報告。要旨に絶対スコアはない。
- Novelty: 連続時間の表現進化と、graphの構造変化を同時にモデル化する。
- Limitations: 編者の注意: 連続表現を使っても、観測されたtimestampの粒度や欠落した事象を自動的に解決するわけではない。

### Paper: Comparative evaluation of point process forecasts
- Source: arXiv
- Canonical ID: arxiv:2103.11884
- Publication date: 2021-03-22
- URL: https://arxiv.org/abs/2103.11884
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 点過程の予測をproper scoring ruleなどの原理に沿って比較する。
- Objective: 社会的な判断に使う確率予測を、適切な目標量に対応した尺度で測る。
- Methods: consistent scoreとproper scoreを点過程へ拡張し、既存の地震予測評価を整理する。
- Data and results: simulationとイタリアの運用地震予測で検証。Poisson対数尤度がcell期待値の比較に適することを示す。
- Novelty: 真の分布全体とcellごとの期待値など、評価対象に合うscoreを区別する。
- Limitations: 編者の注意: Poisson対数尤度が期待値比較に使えることは、真の事象列がPoisson過程であるという証明ではない。

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

### Paper: Interval-censored Hawkes processes
- Source: arXiv
- Canonical ID: arxiv:2104.07932
- Publication date: 2021-04-16
- URL: https://arxiv.org/abs/2104.07932
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 正確な時刻がなく、時間窓ごとの件数だけがあるHawkes推定を扱う。
- Objective: 通常の点過程尤度を計算できない集約観測からパラメータを求める。
- Methods: Hawkesとパラメータが対応するMean Behavior Poisson Processを作り、区間打切りPoisson尤度と近似法で推定する。
- Data and results: 人工・実データで検証し、既存のHawkes Intensity Processを提案方式の特例として位置付ける。
- Novelty: 時刻観測と件数観測の違いを明示した平均挙動モデル。
- Limitations: 編者の注意: Poisson化した平均挙動からの推定は、失われた個々の時刻を観測したことにはならず、近似条件の確認が必要。

### Paper: Temporal Knowledge Graph Reasoning Based on Evolutional Representation Learning
- Source: arXiv
- Canonical ID: arxiv:2104.10353
- Publication date: 2021-04-21
- URL: https://arxiv.org/abs/2104.10353
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: RE-GCNはgraph構造と時系列変化を再帰的に学び、将来の事実を予測する。
- Objective: 同時刻の構造依存と隣接時刻のpatternを効率的に統合する。
- Methods: 関係対応GCN、gate付き再帰更新、entityの静的属性を使うgraph制約を組み合わせる。
- Data and results: 6ベンチマークで精度・効率を改善。最大11.46%のMRR改善と最大82倍の高速化を報告。
- Novelty: entityとrelationの表現を、snapshot列全体の進化として学ぶ。
- Limitations: 編者の注意: 最大改善値と最大速度は各評価条件での値であり、全課題で同時に得られるとは限らない。

### Paper: A Differentiable Point Process with Its Application to Spiking Neural Networks
- Source: arXiv
- Canonical ID: arxiv:2106.00901
- Publication date: 2021-06-02
- URL: https://arxiv.org/abs/2106.00901
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 微分可能な点過程を作り、隠れたspiking neuronを持つ確率モデルを学ぶ。
- Objective: score-function勾配の高分散による学習の難しさを減らす。
- Methods: 点過程の実現を微分できる構成を導き、SNNの変分推論へpath-wise勾配推定を適用する。
- Data and results: 数値simulationで勾配推定の有効性を調べる。要旨は生体脳や大規模な実課題での検証を示していない。
- Novelty: 事象時刻の確率モデルと、spiking網の勾配学習を接続する。
- Limitations: 編者の注意: 数値モデルの学習可能性を示す研究であり、生物学的に同じ勾配計算が行われるという実証ではない。

### Paper: Detecting Anomalous Event Sequences with Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2106.04465
- Publication date: 2021-06-08
- URL: https://arxiv.org/abs/2106.04465
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: TPPの適合度検定を使い、通常と異なる連続時間の事象列を検出する。
- Objective: 既存の検定統計量では見逃す異常列を捉える。
- Methods: 事象列の異常検知を分布外検知として定式化し、複数のTPPと組み合わせられる検定を提案する。
- Data and results: 人工・実データで、通常の適合度検定と異常検知の両方における有効性を示す。
- Novelty: モデルの次事象予測を、列が通常の分布に属するかの検査へつなぐ。
- Limitations: 編者の注意: 統計的な分布外判定から異常の業務上の重要性や原因まで確定するわけではない。

### Paper: Neural Spectral Marked Point Processes
- Source: arXiv
- Canonical ID: arxiv:2106.10773
- Publication date: 2021-06-20
- URL: https://arxiv.org/abs/2106.10773
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Neural Spectral MPPは、文脈を含む非定常な影響カーネルを学ぶ。
- Objective: 一定の時間差だけで決まらない、複雑な時空間依存を表す。
- Methods: 神経網による柔軟な非定常カーネルを導入し、理論的性質と人工・実データの性能を検証する。
- Data and results: 比較法に対する良好な性能を報告。要旨には保証の具体的な仮定や課題別数値がない。
- Novelty: マークの文脈を取り込める非定常な影響関数の設計。
- Limitations: 編者の注意: 理論保証の適用範囲は本文の仮定次第で、任意の非定常データへの保証として読まない。

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

### Paper: Individual Mobility Prediction via Attentive Marked Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2109.02715
- Publication date: 2021-09-06
- URL: https://arxiv.org/abs/2109.02715
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: AMTPPは次の移動の開始時刻・出発地・目的地を共同予測する。
- Objective: 場所の並びだけでなく、移動全体の時空間依存を捉える。
- Methods: 日週周期の埋め込みを持つattention、非対称log-Laplace混合の時刻分布、OD行列学習を組み合わせる。
- Data and results: 大規模な地下鉄移動2データで既存法を上回ると報告。要旨に利用者数や絶対誤差はない。
- Novelty: 移動の三属性を一つのmarked TPPとして学習する。
- Limitations: 編者の注意: 地下鉄で観測される移動の性能から、徒歩・自動車を含む全移動の予測性能は確定しない。

### Paper: TimeTraveler: Reinforcement Learning for Temporal Knowledge Graph Forecasting
- Source: arXiv
- Canonical ID: arxiv:2109.04101
- Publication date: 2021-09-09
- URL: https://arxiv.org/abs/2109.04101
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: TimeTravelerは履歴graph内を移動する強化学習で将来の事実を予測する。
- Objective: 時間差と、後から出現する未見entityの推論を扱う。
- Methods: 相対時間符号、Dirichlet分布に基づく時間reward、未見entityの表現を導入する。
- Data and results: 4ベンチマークで性能を改善し、説明可能性・計算・パラメータ数の利点も報告。
- Novelty: 将来linkの候補を、時間を考慮したpath探索として学習する。
- Limitations: 編者の注意: 未見entityの表現に利用できる情報と、予測時点で実際に観測可能な情報をそろえて評価する。

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

### Paper: Neural Point Process for Learning Spatiotemporal Event Dynamics
- Source: arXiv
- Canonical ID: arxiv:2112.06351
- Publication date: 2021-12-12
- URL: https://arxiv.org/abs/2112.06351
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: DeepSTPPは潜在過程に駆動される時空間強度を変分学習する。
- Objective: 不規則な空間・時間の事象を、密度計算しやすく柔軟に予測する。
- Methods: 密度の積分を閉形式で扱う非母数強度を設計し、深層網によるamortized変分推論で潜在状態を推定する。
- Data and results: 人工データでは真の強度を復元し、実ベンチマークでは既存法より高い性能を報告。
- Novelty: 計算可能な時空間強度と潜在状態の不確実性を結ぶ。
- Limitations: 編者の注意: 変分事後分布は近似であり、潜在不確実性を持つことだけで予測区間の校正が保証されるわけではない。

### Paper: Temporal Attention Augmented Transformer Hawkes Process
- Source: arXiv
- Canonical ID: arxiv:2112.14472
- Publication date: 2021-12-29
- URL: https://arxiv.org/abs/2112.14472
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: TAA-THPはattention計算へ時刻情報を直接組み込む。
- Objective: 単に入力へ位置符号を足す以上に、非同期な発生時刻を利用する。
- Methods: 通常の内積attentionを変更し、時間符号をattention構造へ導入する。
- Data and results: 人工・実データで尤度・種別・時刻予測を改善し、時間attentionの除去実験で寄与を確認する。
- Novelty: 連続時間情報を履歴選択の重み計算へ明示的に入れる。
- Limitations: 編者の注意: 評価指標の改善は報告されるが、要旨には各課題の絶対成績や不確実性が示されない。

### Paper: Flexible Triggering Kernels for Hawkes Process Modeling
- Source: arXiv
- Canonical ID: arxiv:2202.01869
- Publication date: 2022-02-03
- URL: https://arxiv.org/abs/2202.01869
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 柔軟な励起カーネルで、重い多層attentionを置き換える点過程。
- Objective: 計算とメモリを減らし、時間局所的な影響を捉える。
- Methods: 種別・時刻埋め込みからカーネルを学び、sigmoid gateで局所の励起を表し履歴表現の重みに使う。
- Data and results: 人工・実データとCOVID-19の共変量付き設定で、予測・効率・解釈の利点を報告。
- Novelty: attentionに似た役割を、直接解釈できる時間カーネルへ持たせる。
- Limitations: 編者の注意: 解釈可能なカーネルでも観測外の要因は残り、疫学データから介入効果が確定するわけではない。

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

### Paper: CEP3: Community Event Prediction with Neural Point Process on Graph
- Source: arXiv
- Canonical ID: arxiv:2205.10624
- Publication date: 2022-05-21
- URL: https://arxiv.org/abs/2205.10624
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: CEP3は動的グラフのcommunity内で、複数の将来辺と時刻を同時予測する。
- Objective: 時刻既知のlink予測や、事象既知の時刻予測という条件を緩める。
- Methods: GNNとmarked TPPを結合し、結合予測を三つの条件付き確率問題へ分解して規模に対応する。
- Data and results: 専用のbenchmarkと指標を設け、精度と学習効率の改善を報告する。
- Novelty: どの主体間にいつ事象が起こるかを共同で評価する。
- Limitations: 編者の注意: 時刻や候補辺が既知の従来設定と、そのままスコアを比較せず、候補集合と予測地平をそろえる。

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

### Paper: Online Learning for Mixture of Multivariate Hawkes Processes
- Source: arXiv
- Canonical ID: arxiv:2208.07961
- Publication date: 2022-08-16
- URL: https://arxiv.org/abs/2208.07961
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 多変量Hawkesの混合をオンラインで学び、主体の潜在構造と事象相互作用を表す。
- Objective: 流れるデータの中でcluster構造と相互作用を共に捉える。
- Methods: 混合多変量Hawkesをオンライン学習する方式を提案。要旨には更新式や計算量の詳細はない。
- Data and results: 人工・実データで有効性を報告し、医療・金融を動機に挙げる。要旨からデータ別の規模は確認できない。
- Novelty: 主体の潜在clusterと豊かな事象間相互作用を同時に扱う。
- Limitations: 編者の注意: 概念変化の速さや観測欠落に対する頑健性は、要旨だけでは判断できない。

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

### Paper: Temporal Knowledge Graph Forecasting Without Knowledge Using In-Context Learning
- Source: arXiv
- Canonical ID: arxiv:2305.10613
- Publication date: 2023-05-17
- URL: https://arxiv.org/abs/2305.10613
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: LLMのin-context学習が、意味ラベルなしでも時間graph予測に使えるか調べる。
- Objective: 成績が事前の意味知識によるのか、履歴内のpatternによるのかを切り分ける。
- Methods: 関連履歴をpromptへ変え、token確率で候補を順位付け。名前を数字に置き換えた条件も比較する。
- Data and results: 専用TKGモデルと同等の成績を示し、意味を隠してもHit@1の変化は±0.4%と報告。
- Novelty: 意味の知識と、その場の履歴patternの学習を実験的に分離する。
- Limitations: 編者の注意: このbenchmarkで意味が不要でも、説明文のある別分野や希少事象で同じとは限らない。

### Paper: Spatio-temporal Diffusion Point Processes
- Source: arXiv
- Canonical ID: arxiv:2305.12403
- Publication date: 2023-05-21
- URL: https://arxiv.org/abs/2305.12403
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 拡散モデルで位置と時刻の同時分布を学ぶ時空間点過程。
- Objective: 位置と時刻を条件付き独立に分けることによる表現制限を減らす。
- Methods: Gaussian段階の拡散過程と、時空間のco-attentionで両者の依存を学ぶ。
- Data and results: 疫学・地震・犯罪・移動のデータで比較し、平均50%超の改善を報告。ただし要旨から指標別の内訳は不明。
- Novelty: 拡散によって時空間の複雑な結合分布を直接表現する。
- Limitations: 編者の注意: 平均改善率を時刻誤差や尤度のすべてに同じ割合で当てはめず、指標と集計方法を本文で確認する。

### Paper: Intensity-free Convolutional Temporal Point Process: Incorporating Local and Global Event Contexts
- Source: arXiv
- Canonical ID: arxiv:2306.14072
- Publication date: 2023-06-24
- URL: https://arxiv.org/abs/2306.14072
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 連続時間convolutionとRNNを併用する、強度を直接使わないTPP。
- Objective: 局所の事象contextと長い履歴のcontextを両方利用する。
- Methods: 連続時間に対応させた畳み込みencoderをRNNと統合し、待ち時間・事象予測へ用いる。
- Data and results: 確率的系列のモデル化と事象予測の改善を報告。要旨にはデータ別の規模や成績はない。
- Novelty: 等間隔の画像・系列で使われる局所畳み込みを非同期事象へ拡張する。
- Limitations: 編者の注意: 局所contextの設計や観測密度への依存は、未知のデータで別途検証する必要がある。

### Paper: EasyTPP: Towards Open Benchmarking Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2307.08097
- Publication date: 2023-07-16
- URL: https://arxiv.org/abs/2307.08097
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: EasyTPPは神経TPPを共通条件で実装・評価する公開基盤。
- Objective: データ形式や評価実装の違いによる比較・再現の難しさを減らす。
- Methods: データの共通interface、評価プログラム、主要モデルと再利用可能な部品を提供する。
- Data and results: 論文の成果は研究資源と評価環境の整備。要旨は新モデルの一律な精度向上を主張するものではない。
- Novelty: 事象列モデルを比較・拡張できる共通の実装単位を作る。
- Limitations: 編者の注意: 共通基盤の使用だけで、データ漏洩や時間分割、調整予算の差が自動的に解消されるわけではない。

### Paper: Intensity-free Integral-based Learning of Marked Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2308.02360
- Publication date: 2023-08-04
- URL: https://arxiv.org/abs/2308.02360
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: IFIBは事象間時間とマークの条件付き同時密度を直接学ぶ。
- Objective: 強度形状の選択を避け、離散マークと多次元連続マークを扱う。
- Methods: 積分に基づく強度非明示の枠組みで密度を表し、必要な数学的制約を課す。
- Data and results: 理論的性質と、人工・実データでの良好な実験結果を報告。要旨には指標別の成績がない。
- Novelty: 時間とマークを別々に分けず、結合密度を直接構成する。
- Limitations: 編者の注意: 結合密度の妥当性と、実データの分布変化や外挿での精度は異なる問題である。

### Paper: Reinforcement Logic Rule Learning for Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2308.06094
- Publication date: 2023-08-11
- URL: https://arxiv.org/abs/2308.06094
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 強化学習で時間論理規則を探索し、TPPの説明規則を段階的に増やす。
- Objective: 膨大な規則候補から、観測列の尤度を改善するものを選ぶ。
- Methods: 既存規則の重みを更新する凸な主問題と、新規則を行動列として探す神経方策を交互に解く。
- Data and results: 人工データと医療データで有望な結果を報告。要旨では絶対スコアや評価集団の規模は不明。
- Novelty: 規則探索の組合せ問題を、学習可能な生成方策として扱う。
- Limitations: 編者の注意: 主問題の凸性は探索全体の最適性を保証せず、尤度を説明する規則は介入因果そのものではない。

### Paper: A Discussion on Generalization in Next-Activity Prediction
- Source: arXiv
- Canonical ID: arxiv:2309.09618
- Publication date: 2023-09-18
- URL: https://arxiv.org/abs/2309.09618
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 次活動予測の公開ログにあるexample leakageと一般化の評価を再検討する。
- Objective: 深層モデルの成績が、新しいcaseへの能力を本当に示すかを問う。
- Methods: 一般的なevent logで重複・漏洩の影響と簡単な予測法を調べ、必要な一般化の種類を分ける。
- Data and results: 著者が調べた通常のログでは漏洩が大量にあり、単純な方法でも深層法に近い成績となると報告。
- Novelty: 次活動予測の評価を、未知データという言葉の具体的な意味から見直す。
- Limitations: 編者の注意: 調べたログでの結論であり、あらゆる業務データで深層学習が不要という主張へ拡張しない。

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

### Paper: Automatic Integration for Spatiotemporal Neural Point Processes
- Source: arXiv
- Canonical ID: arxiv:2310.06179
- Publication date: 2023-10-09
- URL: https://arxiv.org/abs/2310.06179
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: AutoSTPPは時空間点過程の尤度に必要な積分を計算しやすくする。
- Objective: 三重積分の数値誤差と、固定的な強度形状の制約を減らす。
- Methods: 積分を表すdual networkを三次元へ拡張し、ProdNetによる分解可能な積分網を構成する。
- Data and results: 一致性を証明し、人工・実データ、特に局所的に鋭い強度の復元で利点を報告。
- Novelty: 一変量の自動積分を、計算可能な分解を用いて時空間へ広げる。
- Limitations: 編者の注意: 一致性は論文の仮定下の結果で、有限データでの強度復元や予測の完全性を保証しない。

### Paper: GenTKG: Generative Forecasting on Temporal Knowledge Graph with Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2310.07793
- Publication date: 2023-10-11
- URL: https://arxiv.org/abs/2310.07793
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: GenTKGは時間論理に基づく検索とLLMの少数例調整で将来の事実を生成する。
- Objective: 大きい時間graphをLLMへ渡す構造・計算の隔たりを減らす。
- Methods: 時間論理規則で履歴を検索し、PEFTによるinstruction tuningを組み合わせる。
- Data and results: 最少16例の調整で既存法を上回る結果と、再学習しない未見データへの転移を報告。
- Novelty: 構造を意識した検索と、少数例の生成的予測を統合する。
- Limitations: 編者の注意: 16例は調整用の例数であり、検索に使う履歴全体や事前学習の情報量が16件という意味ではない。

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

### Paper: Spatio-Temporal Graph Neural Point Process for Traffic Congestion Event Prediction
- Source: arXiv
- Canonical ID: arxiv:2311.08635
- Publication date: 2023-11-15
- URL: https://arxiv.org/abs/2311.08635
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: STGNPPは次の渋滞が起こる時刻と続く時間を同時予測する。
- Objective: 等間隔の交通量予測では扱いにくい、疎な連続時間の渋滞事象を捉える。
- Methods: 道路と過去の状態をgraph学習し、連続GRUと周期gateを持つ強度へ入力する。
- Data and results: 実データ2種類で既存法より良い予測を報告。要旨には絶対誤差や改善幅がない。
- Novelty: graph由来の交通状態と周期性を事象の開始・持続の予測へ使う。
- Limitations: 編者の注意: 渋滞の閾値や持続時間の定義が評価を左右し、交通量予測とは指標をそのまま比較できない。

### Paper: Distilling Event Sequence Knowledge From Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2401.07237
- Publication date: 2024-01-14
- URL: https://arxiv.org/abs/2401.07237
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: LLMから事象列を生成し、確率的な事象モデルの知識源にする。
- Objective: 清潔な構造化列が少ない場面で、知識graphの不足を補う。
- Methods: 部分的な因果関係を持つ概念graphで列生成を誘導し、pattern miningと確率モデルへ利用する。
- Data and results: 高品質な列の生成と入力graphの知識gapの補完を報告し、生成コード・評価枠組み・corpusを公開する。
- Novelty: LLMを最終予測器だけでなく、事象列の知識の抽出元として使う。
- Limitations: 編者の注意: 生成列は実際に観測した履歴ではなく、LLMの常識や偏りを含む。因果らしい並びを因果実証としない。

### Paper: SNAP: Semantic Stories for Next Activity Prediction
- Source: arXiv
- Canonical ID: arxiv:2401.15621
- Publication date: 2024-01-28
- URL: https://arxiv.org/abs/2401.15621
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: SNAPは業務ログを意味のある物語に変え、言語基盤モデルで次活動を予測する。
- Objective: カテゴリ符号化だけでは使い切れない文章の意味を利用する。
- Methods: 過去のprocess event logから文脈付きstoryを組み立て、次活動分類へ入力する。
- Data and results: 6ベンチマークで9モデルと比較し、特に意味内容の豊かなデータで大きい改善を報告。
- Novelty: 事象履歴の意味を、言語モデルが扱える連続した記述へ変換する。
- Limitations: 改善は意味情報の豊かさに依存。編者の注意: story作成へ未来の属性や最終結果を混入させないことが重要。

### Paper: Chain-of-History Reasoning for Temporal Knowledge Graph Forecasting
- Source: arXiv
- Canonical ID: arxiv:2402.14382
- Publication date: 2024-02-22
- URL: https://arxiv.org/abs/2402.14382
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Chain-of-Historyは高次の履歴を段階的に探索し、時間知識graphの予測へ使う。
- Objective: 履歴不足と大量の履歴によるLLMの推論劣化を同時に減らす。
- Methods: 高次履歴を段階的に利用する推論moduleを作り、既存graphモデルへ追加できる形で設計する。
- Data and results: 3データと複数backboneで有効性を検証。要旨には指標別の絶対成績がない。
- Novelty: LLM単独の予測能力だけでなく、graph方式を補助する履歴探索として組み込む。
- Limitations: 編者の注意: 高次履歴を増やす効果は入力予算や検索品質に左右され、過去以外の情報の混入を避ける必要がある。

### Paper: PGTNet: A Process Graph Transformer Network for Remaining Time Prediction of Business Process Instances
- Source: arXiv
- Canonical ID: arxiv:2404.06267
- Publication date: 2024-04-09
- URL: https://arxiv.org/abs/2404.06267
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: PGTNetはevent logをgraph化し、processの残り時間を予測する。
- Objective: 複雑な制御flowと長い活動依存を捉える。
- Methods: 事象ログをgraph datasetへ変換し、複数のprocess視点を考慮するProcess Graph Transformerを学習する。
- Data and results: 公開実ログ20種類で既存の深層方式を上回り、特に複雑なprocessに有望と報告。
- Novelty: activityの順序だけでなく、graphとしての制御関係を表現へ組み込む。
- Limitations: 編者の注意: graph化にcase全体の未来情報を利用しないこと、processの複雑さ別に性能を確認することが重要。

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

### Paper: History repeats Itself: A Baseline for Temporal Knowledge Graph Forecasting
- Source: arXiv
- Canonical ID: arxiv:2404.16726
- Publication date: 2024-04-25
- URL: https://arxiv.org/abs/2404.16726
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 事実の繰り返しだけを使う、時間知識graph予測の単純な基準法。
- Objective: 大きいモデルの進歩が、単純な反復予測を超えているか確認する。
- Methods: 反復事実を予測する方式を作り、ほぼ調整不要・反復学習なしで既存11手法と比較する。
- Data and results: 5データ中3つで1位または3位となり、従来法の相対的評価が変わると報告。
- Novelty: 強い反復基準によって、複雑なモデルの失敗や見かけの改善を検出する。
- Limitations: 編者の注意: 反復率が低い・新しいentityが多い分布では事情が変わる。すべての時間graphで十分という結果ではない。

### Paper: A Comprehensive Evaluation on Event Reasoning of Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2404.17513
- Publication date: 2024-04-26
- URL: https://arxiv.org/abs/2404.17513
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: EV2はLLMの事象schema知識と具体例に対する推論を分けて評価する。
- Objective: 事象間関係や推論形式による能力の偏りを調べる。
- Methods: schemaとinstanceの二層を持つbenchmarkを作り、関係・推論形式を幅広く比較する。
- Data and results: 一定の能力はあるが性能は不十分で不均衡と報告。schemaを記憶として利用する誘導で改善を示す。
- Novelty: 事象推論の知識の保有と、その知識の利用方法を別々に検査する。
- Limitations: 知識の利用は人間と十分整合しないと著者が指摘。編者の注意: 推論benchmarkの成績を実時間の次事象予測へ直結させない。

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

### Paper: Large Language Models as Interpolated and Extrapolated Event Predictors
- Source: arXiv
- Canonical ID: arxiv:2406.10492
- Publication date: 2024-06-15
- URL: https://arxiv.org/abs/2406.10492
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: LEAPはLLMを使い、時間知識graphの対象推定と複数事象予測を扱う。
- Objective: 四つ組・説明文付き五つ組からの事象予測の構成を簡潔にする。
- Methods: 対象予測はQA形式でencoder-decoderを調整し、複数事象予測は固定LLM埋め込みとattention headで行う。
- Data and results: 複数の実データ・指標で有効性を示す。要旨にはデータ別の絶対成績はない。
- Novelty: 一つのLLM利用法に固定せず、予測課題に応じて調整型と固定表現型を使い分ける。
- Limitations: 編者の注意: 補間の対象推定と、観測期間より先の外挿予測は別の課題であり、結果を混ぜない。

### Paper: Mamba Hawkes Process for Event Sequence Modeling
- Source: arXiv
- Canonical ID: arxiv:2407.05302
- Publication date: 2024-07-07
- URL: https://arxiv.org/abs/2407.05302
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Mamba Hawkesは選択的状態空間モデルで長い事象履歴を処理する。
- Objective: RNNやattentionの計算負荷を抑え、長距離の依存を捉える。
- Methods: 時間依存の状態遷移と入力gateを使い、拡張版では時間scale調整と内容・時間の二つの遷移経路を加える。
- Data and results: 人工・実データ、特に長い列で予測改善を報告。古典的多指数Hawkesと減衰gate付きRNNを含む表現力も示す。
- Novelty: 線形の列長計算を持つ選択的状態空間表現をTPPへ接続する。
- Limitations: 編者の注意: 理論的な包含関係は実データでの一律な優位性ではない。記述は取得時点の改訂版要旨による。

### Paper: A Comprehensive Evaluation of Large Language Models on Temporal Event Forecasting
- Source: arXiv
- Canonical ID: arxiv:2407.11638
- Publication date: 2024-07-16
- URL: https://arxiv.org/abs/2407.11638
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: MidEast-TE-miniを作り、LLMによる時間事象予測を入力・検索条件別に評価する。
- Objective: graphと文章を併用するLLMが、将来への外挿に何を使えるかを調べる。
- Methods: 入力形式、文章による調整、RAGなどの基準法を比較する。
- Data and results: 生文章をそのまま足すzero-shotでは改善せず、調整では改善。検索は時間関係に役立つが、人気偏重とlong-tailが残る。
- Novelty: LLMへ情報を渡す形式・調整・検索の寄与を切り分ける。
- Limitations: 著者は人気偏重・希少事象の問題、特にRAGでの残存を指摘。地域・データ設定の範囲にも注意が必要。

### Paper: MM-Forecast: A Multimodal Approach to Temporal Event Forecasting with Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2408.04388
- Publication date: 2024-08-08
- URL: https://arxiv.org/abs/2408.04388
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: MM-Forecastは画像の役割を言語化し、時間事象予測へ利用する。
- Objective: 画像が事象の強調・補足にどう役立つかを調べる。
- Methods: multimodal LLMで画像の機能を記述し、その説明をLLM予測器へ入力する。既存データへ画像を加えたMidEast-TE-mmを作る。
- Data and results: 画像の役割の識別と、説明文を加えた予測の改善を実験で報告。
- Novelty: 画像を直接混ぜるだけでなく、予測における機能を文章化して渡す。
- Limitations: 編者の注意: 後から公開された画像やcaptionを使うと未来情報が入り得るため、予測時点の可用性をそろえる必要がある。

### Paper: Decomposable Transformer Point Processes
- Source: arXiv
- Canonical ID: arxiv:2409.18158
- Publication date: 2024-09-26
- URL: https://arxiv.org/abs/2409.18158
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Decomposable Transformer TPPは時間とマークの条件分布を分け、高速に予測する。
- Objective: attentionの利点を保ち、thinningによる推論の計算負荷を避ける。
- Methods: 時間差をMarkov性を持つlog-normal混合、マーク分布をTransformerで表す。
- Data and results: 次事象予測で高い性能を示し、長期専用の比較法より良い予測と短い推論時間を報告。
- Novelty: 待ち時間の直接分布とattentionによる種別予測を分解して組み合わせる。
- Limitations: 編者の注意: Markov性を課す時間モデルの制約と、長期評価に用いた比較法の条件を確認する必要がある。

### Paper: EarthquakeNPP: A Benchmark for Earthquake Forecasting with Neural Point Processes
- Source: arXiv
- Canonical ID: arxiv:2410.08226
- Publication date: 2024-09-27
- URL: https://arxiv.org/abs/2410.08226
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: EarthquakeNPPは神経点過程を地震学の強い基準法と比較するbenchmark。
- Objective: 従来データの漏洩、大きい地震列の欠落、不十分な比較対象を改善する。
- Methods: Californiaの1971–2021年のcatalogを領域・生成方法別に整備し、ETASと尤度・生成指標で比較する。
- Data and results: 試した神経点過程5方式はいずれもETASを上回らなかったと報告。
- Novelty: 機械学習内の比較を、対象分野の実用的なモデル・評価へ接続する。
- Limitations: 結論は試した実装とbenchmarkの範囲。編者の注意: あらゆる将来の神経モデルが地震予測に不適という結論ではない。

### Paper: TPP-LLM: Modeling Temporal Point Processes by Efficiently Fine-Tuning Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2410.02062
- Publication date: 2024-10-02
- URL: https://arxiv.org/abs/2410.02062
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: TPP-LLMは事象種別の文章説明と時間埋め込みでLLMを点過程へ適応させる。
- Objective: カテゴリ記号だけでは失われる意味を利用しつつ、時間パターンを学ぶ。
- Methods: 事象の記述を直接入力し、時間埋め込みとPEFTで少数のパラメータを調整する。
- Data and results: 複数の実データで列モデル化・予測を改善し、計算効率の利点も報告。要旨には費用の絶対値がない。
- Novelty: 意味の事前学習と連続時間の予測を、効率的な追加調整で接続する。
- Limitations: LLMだけでは時間パターンの把握が弱いという動機に基づく。編者の注意: 記述の質と事前学習由来の漏洩を確認する必要がある。

### Paper: EventFlow: Forecasting Temporal Point Processes with Flow Matching
- Source: arXiv
- Canonical ID: arxiv:2410.07430
- Publication date: 2024-10-09
- URL: https://arxiv.org/abs/2410.07430
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: EventFlowはflow matchingで将来の事象時刻の同時分布を直接学ぶ。
- Objective: 自己回帰予測の誤差累積と短期的な予測への偏りを減らす。
- Methods: 非自己回帰生成モデルとして事象列を学習し、標本化時のモデル呼び出しも減らす。
- Data and results: 標準TPPベンチマークで最も近い比較法より予測誤差を20–53%削減したと報告。
- Novelty: flow matchingを可変の事象列の将来生成へ適用する。
- Limitations: 編者の注意: 改善率は論文の予測誤差と評価条件に対応し、すべての単発事象の予測精度を表す値ではない。

### Paper: Navigating Tomorrow: Reliably Assessing Large Language Models Performance on Future Event Prediction
- Source: arXiv
- Canonical ID: arxiv:2501.05925
- Publication date: 2025-01-10
- URL: https://arxiv.org/abs/2501.05925
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: ニュースに基づき、LLMの未来事象予測を複数の質問形式で評価する。
- Objective: 訓練cutoff前後と対象の人気によって、見かけの予測能力がどう変わるかを調べる。
- Methods: entity種別・人気で記事を分類し、肯定/尤度質問、推論、反実仮想の三設定を比較する。
- Data and results: 将来予測の可能性と限界を報告。要旨ではモデル別の成績や校正の具体値を確認できない。
- Novelty: 訓練cutoffと対象の人気を予測評価の設計へ含める。
- Limitations: 編者の注意: cutoff後の記事でも、検索や後日のモデル改訂で情報が入る可能性があり、評価時の情報源の固定が重要。

### Paper: Advances in Temporal Point Processes: Bayesian, Neural, and LLM Approaches
- Source: arXiv
- Canonical ID: arxiv:2501.14291
- Publication date: 2025-01-24
- URL: https://arxiv.org/abs/2501.14291
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Bayes・神経モデル・LLMの三つの視点からTPPを整理するレビュー。
- Objective: 長い統計的蓄積と近年の意味情報の利用をつなぐ。
- Methods: 基礎概念、設計、パラメータ推定、応用を三つの枠組みで解説し、未解決課題を整理する。
- Data and results: 独自予測器の実験ではなく、古典的な応用と最近の学習方式を横断する見取り図を提供する。
- Novelty: Bayesと深層学習に、LLMの文脈理解を含めた比較の軸を加える。
- Limitations: レビューであり各方式の同条件での優位を保証しない。編者の注意: 掲載後の個別研究は一次資料でも確認する。

### Paper: Byte-token Enhanced Language Models for Temporal Point Processes Analysis
- Source: arXiv
- Canonical ID: arxiv:2502.07139
- Publication date: 2025-02-11
- URL: https://arxiv.org/abs/2502.07139
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: Language-TPPは時間差をbyte-tokenへ変え、言語モデルで事象列を扱う。
- Objective: 文章記述と時間動態を、TPP専用の構造変更を抑えて統合する。
- Methods: 連続時間差のbyte-token表現を通常の言語モデルへ組み込み、種別・時刻予測と事象説明生成を評価する。
- Data and results: 電子商取引・SNS・Q&AのWebデータで高い予測成績を報告。時間を加えるとROUGE-Lや感情分布の整合も改善する。
- Novelty: 時間の符号化をtoken語彙へ寄せ、予測と説明文生成を同じ枠組みに載せる。
- Limitations: 編者の注意: 公開時のLanguage-TPPから改題された取得時点の要旨を参照。文章の改善は将来事象の因果的理解の実証ではない。

### Paper: Enhancing Temporal Awareness in LLMs for Temporal Point Processes
- Source: arXiv
- Canonical ID: arxiv:2601.00845
- Publication date: 2025-12-29
- URL: https://arxiv.org/abs/2601.00845
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: TPP-TALはLLM入力の前に時間動態と事象の意味を整合させる。
- Objective: 単なる時刻・種別埋め込みの連結では捉えにくい相互作用を学ぶ。
- Methods: plug-and-play方式で時間と意味の表現を明示的に合わせ、長い履歴の依存をLLMへ伝える。
- Data and results: 複数のベンチマークで時間尤度と事象予測精度の改善を報告。要旨には絶対値がない。
- Novelty: LLMの時間認識を、入力interfaceの整合から改善する。
- Limitations: 編者の注意: 大きいLLMへの適用が自動的に効率的とは限らず、モデルサイズ・調整予算・推論費用を比較条件に含める。

### Paper: David vs. Goliath in Next Activity Prediction: Argmax vs. LSTM, Transformer, and LLM
- Source: arXiv
- Canonical ID: arxiv:2606.15868
- Publication date: 2026-06-14
- URL: https://arxiv.org/abs/2606.15868
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 次活動予測で、LLMから単純な頻度のargmaxまでを直接比較する。
- Objective: 大きな事前学習モデルが、この課題で本当に必要かを検証する。
- Methods: 語彙適応LLM、scratch Transformer、蒸留Transformer、LSTMと数え上げの基準法を実ログ7種類で評価する。
- Data and results: 事前学習の一貫した利得はなく、サイズの効果も小さい。多くのデータでargmaxが十億規模LLMに近い成績を示す。
- Novelty: 複雑なモデルと強い単純基準を同じ系列予測設定へ載せる。
- Limitations: 編者の注意: ラベル列中心の次活動課題での結果であり、豊富な自然言語属性を使う予測すべてへ一般化しない。

### Paper: Can LLMs Access their World Knowledge for Event Prediction?
- Source: arXiv
- Canonical ID: arxiv:2610.19021
- Publication date: 2026-10-13
- URL: https://arxiv.org/abs/2610.19021
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: DescribeEventは、LLMが事象の記述から既存知識を予測に使えるかを調べる。
- Objective: 専用モデルに劣る理由が知識不足か、入力・出力の設計かを検証する。
- Methods: 自然言語の事象記述を与え、意味と予測ラベルを分けるsymbolic labelを用いる。
- Data and results: 6分野7データ、約15万事象を評価。能力の高いLLMは記述と記号ラベルで改善したが、弱いモデルの利得は小さい。
- Novelty: 事象の意味情報と、ラベルの語義による偏りを分けて実験する。
- Limitations: モデル能力によって利得が異なる。編者の注意: 世界知識を利用できるという結果から、未知の将来を一般的に予見できるとは結論しない。

### Paper: Point Spectra of Some Mutually Exciting Point Processes
- Source: Publisher
- Canonical ID: doi:10.1111/j.2517-6161.1971.tb01530.x
- Publication date: 未記載
- URL: https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1971.tb01530.x
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: 相互に励起する点過程のpoint spectral matrixを導く古典。
- Objective: 事象の相互励起を周波数領域の二次的な関係として記述する。
- Methods: Wiener–Hopf積分方程式の解法に似た方法で、対象となる過程のスペクトル行列を求める。
- Data and results: 出版社要旨で確認できる結果はスペクトル行列の導出。予測benchmarkや実データの数値は記されていない。
- Novelty: 後続のHawkes研究を読む入口となる、相互励起のスペクトル解析。
- Limitations: 本文は未確認で、適用条件・導出式の細部は断言しない。刊行年1971年は確認、日単位の公開日は未確認。
- Publication date note: 出版社で刊行年1971年と巻33・号3を確認。日単位の初回公開日は未確認。後年のウェブ掲載・移管日を採用しない。出典: https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1971.tb01530.x

### Paper: Recurrent Marked Temporal Point Processes: Embedding Event History to Vector
- Source: Publisher
- Canonical ID: doi:10.1145/2939672.2939875
- Publication date: 未記載
- URL: https://doi.org/10.1145/2939672.2939875
- read_level: abstract
- Tags: 基礎文献, 次イベント予測・点過程
- Summary: RMTPPは履歴をRNNのvectorへ埋め込み、次の種別と時刻を予測する。
- Objective: 手で固定した過程の形への依存を弱め、大量の事象履歴から表現を学ぶ。
- Methods: 履歴の非線形表現で条件付き強度とマークをモデル化し、確率勾配法で学習する。
- Data and results: 人工・実データで固定的な母数モデルより良い予測を報告。要旨は百万規模の事象へ拡張可能と述べる。
- Novelty: 事象履歴の表現学習とmarked TPPを統合する初期の主要モデル。
- Limitations: 編者の注意: RNNで履歴を学んでも時間密度のパラメータ化は残るため、仮定不要のモデルとは扱わない。
- Publication date note: 著者版PDFでKDD 2016（8月13〜17日）の会議情報を確認。会期を論文の初回公開日へ流用せず、日単位の正式公開日は未確認として保持。出典: https://people.mpi-sws.org/~manuelgr/pubs/rmtpp.pdf

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
arxiv:2307.08097
arxiv:2410.07430
arxiv:2308.06094
arxiv:2106.04465
arxiv:2002.09291
arxiv:2006.02460
arxiv:2104.07932
arxiv:1907.07561
arxiv:1810.03730
arxiv:2006.07506
arxiv:2002.12501
arxiv:1602.04511
arxiv:1607.06333
arxiv:2407.05302
arxiv:1710.05115
arxiv:2208.07961
arxiv:1911.00292
arxiv:2112.14472
arxiv:1708.09252
arxiv:1702.07013
arxiv:2202.01869
arxiv:1802.04725
arxiv:1501.00725
arxiv:2409.18158
arxiv:2305.12403
arxiv:2112.06351
arxiv:2106.10773
arxiv:1612.09328
arxiv:2002.07281
arxiv:2205.10624
arxiv:2310.06179
arxiv:2106.00901
arxiv:2005.08665
arxiv:2311.08635
arxiv:1705.08982
arxiv:2109.02715
arxiv:1705.08051
arxiv:2007.14082
arxiv:2306.14072
arxiv:1806.00221
arxiv:2308.02360
arxiv:2601.00845
arxiv:2610.19021
arxiv:2401.07237
arxiv:2406.10492
arxiv:2404.17513
arxiv:2407.11638
arxiv:2410.02062
arxiv:2501.05925
arxiv:2408.04388
arxiv:2003.11268
arxiv:2008.10748
arxiv:1709.06033
arxiv:2401.15621
arxiv:1712.04165
arxiv:2309.09618
arxiv:1707.06766
arxiv:1711.03822
arxiv:2008.07993
arxiv:1804.02422
arxiv:1805.02896
arxiv:2404.06267
arxiv:2606.15868
arxiv:2402.14382
arxiv:2012.15537
arxiv:2101.05151
arxiv:2109.04101
arxiv:2305.10613
arxiv:2404.16726
arxiv:2104.10353
arxiv:2003.13432
arxiv:2310.07793
arxiv:1305.3409
arxiv:2103.11884
arxiv:2410.08226
arxiv:1905.09690
arxiv:2502.07139
arxiv:2501.14291
doi:10.1111/j.2517-6161.1971.tb01530.x
doi:10.1145/2939672.2939875
<!-- /PAPER_IDS -->
