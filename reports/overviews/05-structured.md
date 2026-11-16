# 表形式・時系列・因果推論：基礎から現在へのレビュー

レビュー日: 2026-11-16。収録論文の公開日上限: 2026-11-12。

表や時系列では強い専用モデルと基盤モデルが併存し、予測・補完・生成を共有する設計が進んでいる。最も大きな境界は、観測の続きを当てる能力から、介入した世界の変化を説明する能力へは自動的に進めない点にある。

収録基礎文献 119件／本レビューで引用する基礎文献 24件・新着論文 4件。分野横断の文献を含み、件数は引用IDの集合から計算。

## いま何ができるか

表の分類・回帰、時系列予測、欠損補完、合成データを用途に応じて学習・転移できる。

一つのモデルで全表に勝つことや、予測精度から因果効果が分かることは示されていない。 [1](https://arxiv.org/abs/2609.17895) [2](https://arxiv.org/abs/2611.13001) [3](https://arxiv.org/abs/2611.15009)

## 基礎からの積み上げ

### 木の集約と深層学習を比較する

Random Forests、XGBoost、CatBoostは異なる特徴の混じる表の強い基準になる。表形式の深層学習研究は、特徴量やデータ規模に応じた得手不得手と、比較条件の重要性を明らかにしてきた。 [4](https://link.springer.com/article/10.1023/A:1010933404324) [5](https://arxiv.org/abs/1603.02754) [6](https://arxiv.org/abs/1706.09516) [7](https://arxiv.org/abs/2106.11959) [8](https://arxiv.org/abs/2207.08815)

### 表に対して事前学習する

TabPFNは合成課題の事前学習で、学習データを文脈として使う表の推論を実現した。統計的な基礎づけ、スケーリング、文脈最適化を経て、より複雑な実データの分割や型へ対象が広がる。 [9](https://arxiv.org/abs/2207.01848) [10](https://arxiv.org/abs/2305.11097) [11](https://arxiv.org/abs/2402.11137) [1](https://arxiv.org/abs/2609.17895)

### 系列の予測から共通表現へ

DeepAR、N-BEATS、PatchTSTなどの専用モデルから、Chronos、MOMENTなど、複数系列を使って事前学習する流れへ進んだ。単純な線形手法との比較も、構造の複雑さが必要かを見分ける材料になる。 [12](https://arxiv.org/abs/1704.04110) [13](https://arxiv.org/abs/1905.10437) [14](https://arxiv.org/abs/2211.14730) [15](https://arxiv.org/abs/2403.07815) [16](https://arxiv.org/abs/2402.03885) [17](https://arxiv.org/abs/2205.13504)

### 生成・補完と因果推論を分けて発展させる

CTGAN、TabDDPM、CSDIは欠損や生成を扱う。因果推論側ではDMLや因果フォレスト、NOTEARSが、効果推定や構造学習をそれぞれ異なる仮定の下で扱っている。 [18](https://arxiv.org/abs/1907.00503) [19](https://arxiv.org/abs/2209.15421) [20](https://arxiv.org/abs/2107.03502) [21](https://arxiv.org/abs/1608.00060) [22](https://arxiv.org/abs/1610.01271) [23](https://arxiv.org/abs/1803.01422)

## 到達点・適用条件・残る境界

### 表を予測する — 比較が蓄積

できていること: 木の集約、深層学習、事前学習モデルから、対象データに応じた有力な予測器を選べる。

条件: 時間・施設・グループ単位の分割、欠損とカテゴリ、ハイパーパラメータ探索の予算を揃える。

残る境界: あるベンチマークの総合順位から、あらゆる業務表に最良の方法は決まらない。 [5](https://arxiv.org/abs/1603.02754) [8](https://arxiv.org/abs/2207.08815) [1](https://arxiv.org/abs/2609.17895) [24](https://arxiv.org/abs/2608.18919)

### 時系列を予測・分類・補完する — 比較が蓄積

できていること: 系列ごとの学習と、事前学習済み表現の利用で、予測や分類、欠損の補完を行える。

条件: 予測期間、観測間隔、外生変数、季節性、将来を混ぜない分割を定める。

残る境界: 数値系列の続きを当てることは、不規則なイベントの種類・発生時刻・介入反応の全てを扱うことではない。 [12](https://arxiv.org/abs/1704.04110) [14](https://arxiv.org/abs/2211.14730) [15](https://arxiv.org/abs/2403.07815) [16](https://arxiv.org/abs/2402.03885)

### 同じ表から生成・補完・予測を行う — 限定条件で実証

できていること: 複数のタスクを一つのモデルに共有させ、予測や数値の復元、合成データの有用性を改善する例がある。

条件: 予測効用と分布の忠実性、カテゴリの再現、希少事象、プライバシーを別の軸で評価する。

残る境界: 下流予測が良い合成データでも、同時分布が忠実とは限らず、専門モデルが勝る軸もある。 [18](https://arxiv.org/abs/1907.00503) [19](https://arxiv.org/abs/2209.15421) [2](https://arxiv.org/abs/2611.13001)

### 因果効果・構造を推定する — 仮定に依存する手法

できていること: 交絡、処置割当、関数形やグラフ構造についての仮定を置き、効果の推定や因果構造の候補を得られる。

条件: 識別可能性、未観測交絡、操作変数の妥当性、感度分析を、予測の評価とは別に確認する。

残る境界: 高精度の予測器や発見された有向グラフだけで、介入効果が正しく識別されたとはいえない。 [21](https://arxiv.org/abs/1608.00060) [22](https://arxiv.org/abs/1610.01271) [23](https://arxiv.org/abs/1803.01422) [3](https://arxiv.org/abs/2611.15009)

## 直近研究の位置づけ

### TabPFN-3.5：実データの複雑さへ対象を広げる

時間・グループ分割、文字列・画像を含む表、高カーディナリティなどへ対象を拡張。TabArenaでの優位と高速版の旧版比最大3倍高速化を著者が報告している。各業務データでの外部比較は引き続き必要である。 [1](https://arxiv.org/abs/2609.17895)

### One Table：万能性を複数の軸で測る

56データセット、46登録手法、20評価軸を整理。目的関数の組合せ実験自体は5データセット・5バックボーン・3 seedで行った。予測効用と分布忠実度にトレードオフがあり、全実験が56データセットで行われたと誤読しない。 [2](https://arxiv.org/abs/2611.13001)

### 予測から世界モデルへの飛躍を検証する

価格変更のシミュレーションと実小売記録では、予測精度が価格効果の精度を示さなかった。追加文脈は予測を改善しても効果推定を改善せず、生の操作変数の追加も交絡下で悪化した。 [3](https://arxiv.org/abs/2611.15009)

## 次の課題（編者の整理）

### どのタスクを共有すると得か

同一モデルが得る正の転移と、目的関数間の干渉を分け、効用・分布再現・費用を同時に比べる必要がある。 [2](https://arxiv.org/abs/2611.13001)

### 分布変化と介入を混同しない

未知施設や将来時点への予測、処置を変えた反実仮想、変数間の因果構造は別の問いとして評価する。 [25](https://arxiv.org/abs/2312.07577) [3](https://arxiv.org/abs/2611.15009)

## 分野間の接点（編者の整理）

- [次イベント予測・点過程](https://drkamoshika.github.io/papers/?view=map&topic=events): 一定間隔の数値系列と、不規則に起こる出来事の系列では、予測対象と尤度の定義が異なる。 [12](https://arxiv.org/abs/1704.04110) [26](https://arxiv.org/abs/1612.09328)

- [医療・生体信号・創薬AI](https://drkamoshika.github.io/papers/?view=map&topic=medical): 患者を行として分けるだけでなく、施設・時点を分けた評価が医療の外的妥当性へ直結する。 [25](https://arxiv.org/abs/2312.07577) [27](https://pubmed.ncbi.nlm.nih.gov/34152373/)

- [評価・安全性・解釈可能性](https://drkamoshika.github.io/papers/?view=map&topic=trust): 平均順位だけでなく、データごとの強みと分布変化時の校正を見る必要がある。 [24](https://arxiv.org/abs/2608.18919) [28](https://arxiv.org/abs/1906.02530)

## 読む順番

1. [XGBoost: A Scalable Tree Boosting System](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1603.02754)

2. [Why do tree-based models still outperform deep learning on tabular data?](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2207.08815)

3. [TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2207.01848)

4. [Chronos: Learning the Language of Time Series](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2403.07815)

5. [Double/Debiased Machine Learning for Treatment and Structural Parameters](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1608.00060)

6. [One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation, Imputation, and Prediction](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.13001)

7. [From Forecasting to World Modeling: Can Temporal Foundation Models Recover Causal Response?](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.15009)

## 参考文献と確認範囲

1. [TabPFN-3.5: Technical Report](https://arxiv.org/abs/2609.17895) — 2026-09-15 / arxiv:2609.17895 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2609.17895) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2609.17895v3)

2. [One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation, Imputation, and Prediction](https://arxiv.org/abs/2611.13001) — 2026-11-08 / arxiv:2611.13001 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.13001) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.13001v1)

3. [From Forecasting to World Modeling: Can Temporal Foundation Models Recover Causal Response?](https://arxiv.org/abs/2611.15009) — 2026-11-11 / arxiv:2611.15009 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.15009) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.15009v1)

4. [Random Forests](https://link.springer.com/article/10.1023/A:1010933404324) — 公開日未確認 / doi:10.1023/A:1010933404324 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=doi%3A10.1023%2FA%3A1010933404324)

5. [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754) — 2016-03-09 / arxiv:1603.02754 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1603.02754)

6. [CatBoost: unbiased boosting with categorical features](https://arxiv.org/abs/1706.09516) — 2017-06-28 / arxiv:1706.09516 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1706.09516)

7. [Revisiting Deep Learning Models for Tabular Data](https://arxiv.org/abs/2106.11959) — 2021-06-22 / arxiv:2106.11959 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2106.11959)

8. [Why do tree-based models still outperform deep learning on tabular data?](https://arxiv.org/abs/2207.08815) — 2022-07-18 / arxiv:2207.08815 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2207.08815)

9. [TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second](https://arxiv.org/abs/2207.01848) — 2022-07-05 / arxiv:2207.01848 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2207.01848)

10. [Statistical Foundations of Prior-Data Fitted Networks](https://arxiv.org/abs/2305.11097) — 2023-05-18 / arxiv:2305.11097 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.11097)

11. [TuneTables: Context Optimization for Scalable Prior-Data Fitted Networks](https://arxiv.org/abs/2402.11137) — 2024-02-17 / arxiv:2402.11137 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2402.11137)

12. [DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks](https://arxiv.org/abs/1704.04110) — 2017-04-13 / arxiv:1704.04110 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1704.04110)

13. [N-BEATS: Neural basis expansion analysis for interpretable time series forecasting](https://arxiv.org/abs/1905.10437) — 2019-05-24 / arxiv:1905.10437 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1905.10437)

14. [A Time Series is Worth 64 Words: Long-term Forecasting with Transformers](https://arxiv.org/abs/2211.14730) — 2022-11-27 / arxiv:2211.14730 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2211.14730)

15. [Chronos: Learning the Language of Time Series](https://arxiv.org/abs/2403.07815) — 2024-03-12 / arxiv:2403.07815 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2403.07815)

16. [MOMENT: A Family of Open Time-series Foundation Models](https://arxiv.org/abs/2402.03885) — 2024-02-06 / arxiv:2402.03885 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2402.03885)

17. [Are Transformers Effective for Time Series Forecasting?](https://arxiv.org/abs/2205.13504) — 2022-05-26 / arxiv:2205.13504 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2205.13504)

18. [Modeling Tabular data using Conditional GAN](https://arxiv.org/abs/1907.00503) — 2019-07-01 / arxiv:1907.00503 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1907.00503)

19. [TabDDPM: Modelling Tabular Data with Diffusion Models](https://arxiv.org/abs/2209.15421) — 2022-09-30 / arxiv:2209.15421 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2209.15421)

20. [CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation](https://arxiv.org/abs/2107.03502) — 2021-07-07 / arxiv:2107.03502 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2107.03502)

21. [Double/Debiased Machine Learning for Treatment and Structural Parameters](https://arxiv.org/abs/1608.00060) — 2016-07-30 / arxiv:1608.00060 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1608.00060)

22. [Generalized Random Forests](https://arxiv.org/abs/1610.01271) — 2016-10-05 / arxiv:1610.01271 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1610.01271)

23. [DAGs with NO TEARS: Continuous Optimization for Structure Learning](https://arxiv.org/abs/1803.01422) — 2018-03-04 / arxiv:1803.01422 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1803.01422)

24. [Lost in Aggregation: How Benchmarks Overlook Irreplaceable Model Strengths](https://arxiv.org/abs/2608.18919) — 2026-08-19 / arxiv:2608.18919 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2608.18919)

25. [Benchmarking Distribution Shift in Tabular Data with TableShift](https://arxiv.org/abs/2312.07577) — 2023-12-10 / arxiv:2312.07577 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2312.07577)

26. [The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process](https://arxiv.org/abs/1612.09328) — 2016-12-29 / arxiv:1612.09328 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1612.09328)

27. [External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients](https://pubmed.ncbi.nlm.nih.gov/34152373/) — 2021-06-21 / pmid:34152373 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34152373)

28. [Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift](https://arxiv.org/abs/1906.02530) — 2019-06-06 / arxiv:1906.02530 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1906.02530)

## このレビューの範囲

母集団はこのライブラリの収録論文。全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断的レビューです。

基礎文献・新着論文は収録先の区別です。基礎文献側にも2026年の研究が含まれるため、古さや新しさは個々の公開日で確認できます。

技術の系譜、分野間の接点、次の課題は編者の整理であり、論文間の直接の引用関係や、商用普及の程度を確定するものではありません。

個別論文の確認範囲は要旨または本文の関連箇所です。今回、代表的な22件の一次資料を追加で照合しました。全件の全文再精読や独立再現を意味しません。

実験の数字は論文の報告値です。異なるデータ・分割・指標の数値を統一順位へ変換していません。

[7分野の全体マップ](https://drkamoshika.github.io/papers/?view=map)
