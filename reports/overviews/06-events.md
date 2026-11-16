# 次イベント予測・点過程：基礎から現在へのレビュー

レビュー日: 2026-11-16。収録論文の公開日上限: 2026-11-12。

「次に何が起きるか」「いつ起きるか」「どこで起きるか」「介入したら変わるか」を分けると、研究の位置が見える。点過程の確率モデル、業務ログの系列予測、LLMの意味知識は競合するだけでなく、異なる不足を補う。

収録基礎文献 100件／本レビューで引用する基礎文献 25件・新着論文 2件。分野横断の文献を含み、件数は引用IDの集合から計算。

## いま何ができるか

不規則なイベントの種類・待ち時間・場所をモデル化し、業務ログや移動履歴で予測できる。

次ラベルの正解率だけでは時刻の校正や長期生成、介入の価値、LLMの必要性は判断できない。 [1](https://arxiv.org/abs/1612.09328) [2](https://arxiv.org/abs/2606.15868) [3](https://arxiv.org/abs/2610.19021) [4](https://arxiv.org/abs/2611.14220)

## 基礎からの積み上げ

### 条件付き強度で履歴依存を表す

Hawkes過程は過去のイベントが将来の発生率に影響する相互励起を表す。種類ごとの条件付き強度から、何がいつ起こるかの確率分布を作る。観測履歴から推定した励起の関係を、介入による因果効果と同一視しない。 [5](https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1971.tb01530.x) [6](https://arxiv.org/abs/1806.00221) [7](https://arxiv.org/abs/1602.04511)

### ニューラルな履歴表現へ拡張する

RMTPPとNeural Hawkesは履歴を学習表現へ写し、Transformer Hawkesや自己注意型へ展開した。Intensity-Freeは待ち時間分布を直接表す別経路であり、全てが同じ強度関数を使うわけではない。 [8](https://www.kdd.org/kdd2016/subtopic/view/recurrent-temporal-point-process) [1](https://arxiv.org/abs/1612.09328) [9](https://arxiv.org/abs/2002.09291) [10](https://arxiv.org/abs/1907.07561) [11](https://arxiv.org/abs/1909.12127)

### 次の一つから系列全体へ広げる

長期予測、拡散やflow matching、時空間モデルは、将来の複数イベントと個数・時刻の整合性を扱う。EasyTPPは比較の実装条件を揃える基盤となる。 [12](https://arxiv.org/abs/2101.02815) [13](https://arxiv.org/abs/2311.01139) [14](https://arxiv.org/abs/2410.07430) [15](https://arxiv.org/abs/2011.04583) [16](https://arxiv.org/abs/2307.08097)

### 意味知識と業務・知識グラフを接続する

業務ログは次活動や残り時間、時間付き知識グラフは将来の関係、LLM型はイベント記述に含まれる意味を主に利用する。名称が似ていても、予測対象、情報量、評価時点を揃えないと成績を比較できない。 [17](https://arxiv.org/abs/1711.03822) [18](https://arxiv.org/abs/2012.15537) [19](https://arxiv.org/abs/2410.02062) [3](https://arxiv.org/abs/2610.19021)

## 到達点・適用条件・残る境界

### 次の種類と待ち時間の分布を出す — 比較が蓄積

できていること: 履歴に依存したイベント種類と到着時刻の確率を、強度または待ち時間分布で表現できる。

条件: 尤度の定義、観測窓、打ち切り、欠測、同時イベントの扱いを定める。校正と単純な頻度・更新過程などの基準も比較する。

残る境界: 次種類の正解率が高くても、待ち時間の分布や低頻度イベントの確率が正しいとは限らない。 [1](https://arxiv.org/abs/1612.09328) [11](https://arxiv.org/abs/1909.12127) [20](https://arxiv.org/abs/1305.3409) [16](https://arxiv.org/abs/2307.08097)

### 長い将来の系列を生成する — 研究が進展

できていること: 将来の複数イベントや発生個数を、自己回帰・拡散・flowなどで生成する研究がある。

条件: 次の一つだけの誤差に加え、時間範囲内の個数、種類構成、長期の分布、計算費用を評価する。

残る境界: 短期の尤度の改善から、長期間の実現可能性や業務上の制約遵守までは保証できない。 [12](https://arxiv.org/abs/2101.02815) [13](https://arxiv.org/abs/2311.01139) [14](https://arxiv.org/abs/2410.07430)

### 業務ログの次活動・残り時間を予測する — 比較が蓄積

できていること: 履歴の接頭辞から次の活動や完了までの時間を予測できる。単純な頻度方式が強い条件も明確になってきた。

条件: 案件単位と時間単位の分割、同じ案件の漏洩、活動ラベルや属性を揃え、頻度基準との追加価値を測る。

残る境界: 活動ラベル列だけの課題で複雑なモデルが勝たないことを、自然言語属性や時刻を含む全イベント予測へ広げない。 [17](https://arxiv.org/abs/1711.03822) [21](https://arxiv.org/abs/1712.04165) [2](https://arxiv.org/abs/2606.15868)

### LLMの意味知識で予測を補う — 限定条件で実証

できていること: 自然言語のイベント記述、カテゴリの意味、外部知識を予測器に取り込める。

条件: 予測時点に存在する説明だけを使い、事前学習の混入と検索の時点、推論遅延、専用モデルとの情報量を揃える。

残る境界: 言葉の知識があるだけで一貫して優れるわけではない。種類の改善が発生時刻の改善を意味するわけでもない。 [19](https://arxiv.org/abs/2410.02062) [22](https://arxiv.org/abs/2501.05925) [3](https://arxiv.org/abs/2610.19021) [4](https://arxiv.org/abs/2611.14220)

### 予測を介入へつなげる — 仮定に依存する研究

できていること: 反実仮想の点過程などで、特定の操作をした場合のイベント系列を検討できる。

条件: どの操作が可能か、交絡や観測過程をどう扱うか、行動した場合の便益・費用を定義する。

残る境界: 観察下で起こりやすい出来事を当てるだけでは、行動によって良い結果へ変えられるとはいえない。 [23](https://arxiv.org/abs/2111.07603) [7](https://arxiv.org/abs/1602.04511) [24](https://arxiv.org/abs/2611.15009)

## 直近研究の位置づけ

### ArgmaxとLLM：ラベル列だけなら単純な基準が強い

7実業務ログの直接系列予測で、事前学習の一貫した利得やモデル規模の強い効果がなく、多くで計数ベースのargmaxが十億規模LLMに近いと報告。まず単純基準の強さを測る根拠になる。 [2](https://arxiv.org/abs/2606.15868)

### DescribeEvent：意味を渡す方法で結果が変わる

6領域・7データセット・約15万イベントで、記述と記号ラベルを組み合わせると能力の高いLLMに利得があり、弱いモデルの利得は小さかった。ラベル列だけの比較とは入力情報と予測のインターフェースが異なる。 [3](https://arxiv.org/abs/2610.19021)

### SHARP：意味・時間・移動記憶を分業する

3移動データセットで、時間条件付きカテゴリ遷移、動的記憶、意味IDを用い、最良比較法に対し平均Acc@5が5.29ポイント、Acc@10が4.52ポイント改善。これは次の場所の順位評価であり、到着時刻の校正を示す数値ではない。 [4](https://arxiv.org/abs/2611.14220)

## 次の課題（編者の整理）

### どの情報が本当に効いているか

ラベル頻度、直近の繰り返し、時刻、記述、外部知識を段階的に加え、同じ分割と費用で純増分を測ると、LLMが必要な条件を整理しやすい。 [2](https://arxiv.org/abs/2606.15868) [3](https://arxiv.org/abs/2610.19021) [4](https://arxiv.org/abs/2611.14220)

### 確率と時間を意思決定に耐える形にする

正解率、時間誤差、尤度、校正、長期生成の整合性、介入後の効用は別の評価軸として並べる。未来情報が混入しない評価の保存も重要になる。 [20](https://arxiv.org/abs/1305.3409) [25](https://arxiv.org/abs/2103.11884) [22](https://arxiv.org/abs/2501.05925) [23](https://arxiv.org/abs/2111.07603)

## 分野間の接点（編者の整理）

- [言語モデルの学習・推論・効率化](https://drkamoshika.github.io/papers/?view=map&topic=language): LLMは意味の表現を供給できるが、イベントの確率や時刻をどう符号化・学習するかは追加の設計課題になる。 [19](https://arxiv.org/abs/2410.02062) [3](https://arxiv.org/abs/2610.19021)

- [表形式・時系列・因果推論](https://drkamoshika.github.io/papers/?view=map&topic=structured): 数値予測とイベント予測の接点は大きいが、介入反応は予測精度から分離して評価する。 [24](https://arxiv.org/abs/2611.15009) [23](https://arxiv.org/abs/2111.07603)

- [神経科学とAI](https://drkamoshika.github.io/papers/?view=map&topic=neuroscience): 神経発火もイベント列として扱える。微分可能な点過程はスパイク型ネットワークとの接続を持つ。 [26](https://arxiv.org/abs/2106.00901) [27](https://pubmed.ncbi.nlm.nih.gov/32681001/)

## 読む順番

1. [Lecture Notes: Temporal Point Processes and the Conditional Intensity Function](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1806.00221)

2. [The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1612.09328)

3. [Intensity-Free Learning of Temporal Point Processes](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1909.12127)

4. [EasyTPP: Towards Open Benchmarking Temporal Point Processes](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.08097)

5. [Calibration diagnostics for point process models via the probability integral transform](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1305.3409)

6. [David vs. Goliath in Next Activity Prediction: Argmax vs. LSTM, Transformer, and LLM](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2606.15868)

7. [Can LLMs Access their World Knowledge for Event Prediction?](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2610.19021)

8. [SHARP: Semantic Hierarchical Agentic Reasoning for Next POI Prediction with Dynamic Memory](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14220)

## 参考文献と確認範囲

1. [The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process](https://arxiv.org/abs/1612.09328) — 2016-12-29 / arxiv:1612.09328 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1612.09328)

2. [David vs. Goliath in Next Activity Prediction: Argmax vs. LSTM, Transformer, and LLM](https://arxiv.org/abs/2606.15868) — 2026-06-14 / arxiv:2606.15868 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2606.15868) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2606.15868v1)

3. [Can LLMs Access their World Knowledge for Event Prediction?](https://arxiv.org/abs/2610.19021) — 2026-10-13 / arxiv:2610.19021 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2610.19021) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2610.19021v1)

4. [SHARP: Semantic Hierarchical Agentic Reasoning for Next POI Prediction with Dynamic Memory](https://arxiv.org/abs/2611.14220) — 2026-11-10 / arxiv:2611.14220 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14220) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.14220v1)

5. [Point Spectra of Some Mutually Exciting Point Processes](https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1971.tb01530.x) — 公開日未確認 / doi:10.1111/j.2517-6161.1971.tb01530.x / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=doi%3A10.1111%2Fj.2517-6161.1971.tb01530.x)

6. [Lecture Notes: Temporal Point Processes and the Conditional Intensity Function](https://arxiv.org/abs/1806.00221) — 2018-06-01 / arxiv:1806.00221 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1806.00221)

7. [Learning Granger Causality for Hawkes Processes](https://arxiv.org/abs/1602.04511) — 2016-02-14 / arxiv:1602.04511 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1602.04511)

8. [Recurrent Marked Temporal Point Processes: Embedding Event History to Vector](https://www.kdd.org/kdd2016/subtopic/view/recurrent-temporal-point-process) — 公開日未確認 / doi:10.1145/2939672.2939875 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=doi%3A10.1145%2F2939672.2939875)

9. [Transformer Hawkes Process](https://arxiv.org/abs/2002.09291) — 2020-02-21 / arxiv:2002.09291 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2002.09291)

10. [Self-Attentive Hawkes Processes](https://arxiv.org/abs/1907.07561) — 2019-07-17 / arxiv:1907.07561 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1907.07561)

11. [Intensity-Free Learning of Temporal Point Processes](https://arxiv.org/abs/1909.12127) — 2019-09-26 / arxiv:1909.12127 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1909.12127)

12. [Long Horizon Forecasting With Temporal Point Processes](https://arxiv.org/abs/2101.02815) — 2021-01-08 / arxiv:2101.02815 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2101.02815)

13. [Add and Thin: Diffusion for Temporal Point Processes](https://arxiv.org/abs/2311.01139) — 2023-11-02 / arxiv:2311.01139 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2311.01139)

14. [EventFlow: Forecasting Temporal Point Processes with Flow Matching](https://arxiv.org/abs/2410.07430) — 2024-10-09 / arxiv:2410.07430 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2410.07430)

15. [Neural Spatio-Temporal Point Processes](https://arxiv.org/abs/2011.04583) — 2020-11-09 / arxiv:2011.04583 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2011.04583)

16. [EasyTPP: Towards Open Benchmarking Temporal Point Processes](https://arxiv.org/abs/2307.08097) — 2023-07-16 / arxiv:2307.08097 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.08097)

17. [LSTM Networks for Data-Aware Remaining Time Prediction of Business Process Instances](https://arxiv.org/abs/1711.03822) — 2017-11-10 / arxiv:1711.03822 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1711.03822)

18. [xERTE: Explainable Reasoning on Temporal Knowledge Graphs for Forecasting Future Links](https://arxiv.org/abs/2012.15537) — 2020-12-31 / arxiv:2012.15537 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2012.15537)

19. [TPP-LLM: Modeling Temporal Point Processes by Efficiently Fine-Tuning Large Language Models](https://arxiv.org/abs/2410.02062) — 2024-10-02 / arxiv:2410.02062 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2410.02062)

20. [Calibration diagnostics for point process models via the probability integral transform](https://arxiv.org/abs/1305.3409) — 2013-05-15 / arxiv:1305.3409 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1305.3409)

21. [Temporal Stability in Predictive Process Monitoring](https://arxiv.org/abs/1712.04165) — 2017-12-12 / arxiv:1712.04165 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1712.04165)

22. [Navigating Tomorrow: Reliably Assessing Large Language Models Performance on Future Event Prediction](https://arxiv.org/abs/2501.05925) — 2025-01-10 / arxiv:2501.05925 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2501.05925)

23. [Counterfactual Temporal Point Processes](https://arxiv.org/abs/2111.07603) — 2021-11-15 / arxiv:2111.07603 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2111.07603)

24. [From Forecasting to World Modeling: Can Temporal Foundation Models Recover Causal Response?](https://arxiv.org/abs/2611.15009) — 2026-11-11 / arxiv:2611.15009 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.15009) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.15009v1)

25. [Comparative evaluation of point process forecasts](https://arxiv.org/abs/2103.11884) — 2021-03-22 / arxiv:2103.11884 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2103.11884)

26. [A Differentiable Point Process with Its Application to Spiking Neural Networks](https://arxiv.org/abs/2106.00901) — 2021-06-02 / arxiv:2106.00901 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2106.00901)

27. [A solution to the learning dilemma for recurrent networks of spiking neurons](https://pubmed.ncbi.nlm.nih.gov/32681001/) — 2020-07-17 / pmid:32681001 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32681001)

## このレビューの範囲

母集団はこのライブラリの収録論文。全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断的レビューです。

基礎文献・新着論文は収録先の区別です。基礎文献側にも2026年の研究が含まれるため、古さや新しさは個々の公開日で確認できます。

技術の系譜、分野間の接点、次の課題は編者の整理であり、論文間の直接の引用関係や、商用普及の程度を確定するものではありません。

個別論文の確認範囲は要旨または本文の関連箇所です。今回、代表的な22件の一次資料を追加で照合しました。全件の全文再精読や独立再現を意味しません。

実験の数字は論文の報告値です。異なるデータ・分割・指標の数値を統一順位へ変換していません。

[7分野の全体マップ](https://drkamoshika.github.io/papers/?view=map)
