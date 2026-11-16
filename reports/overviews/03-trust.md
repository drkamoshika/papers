# 評価・安全性・解釈可能性：基礎から現在へのレビュー

レビュー日: 2026-11-16。収録論文の公開日上限: 2026-11-12。

正解率だけを測る段階から、いつ間違うか、何を根拠にするか、どんな攻撃や分布変化で崩れるかを評価する段階へ進んだ。現在は、評価そのものの妥当性と、実行システム全体の制御がボトルネックになっている。

収録基礎文献 104件／本レビューで引用する基礎文献 16件・新着論文 8件。分野横断の文献を含み、件数は引用IDの集合から計算。

## いま何ができるか

ベンチマーク、事実性検査、棄権・不確実性、攻撃試験、説明によって失敗を切り分けられる。

高い平均点、もっともらしい説明、安全指示だけで、未知環境の安全性を認定できない。 [1](https://arxiv.org/abs/2211.09110) [2](https://arxiv.org/abs/2611.14661) [3](https://arxiv.org/abs/2611.17280)

## 基礎からの積み上げ

### 予測の信頼性を統計的に扱う

ベイズ的な不確実性、選択的分類、conformal predictionは、予測値に加えて不確実性や回答しない選択を扱う。保証が成立する分布・交換可能性などの条件を確認することが出発点になる。 [4](https://arxiv.org/abs/1506.02142) [5](https://arxiv.org/abs/1705.08500) [6](https://arxiv.org/abs/0706.3188) [7](https://arxiv.org/abs/2202.13415)

### 広い課題と事実性を評価する

MMLUは幅広い知識課題、HELMは複数の評価軸、TruthfulQAとFActScoreは誤った知識や文章中の個々の事実を扱う。各指標は違う失敗を測る。 [8](https://arxiv.org/abs/2009.03300) [1](https://arxiv.org/abs/2211.09110) [9](https://arxiv.org/abs/2109.07958) [10](https://arxiv.org/abs/2305.14251)

### 説明の見やすさと忠実性を分ける

LIMEやSHAPは局所的な予測への寄与を整理する一方、Chain-of-Thoughtの説明が実際の判断に忠実かという別の問いが生じた。説明を見せることと機構を特定することを分けて読む。 [11](https://arxiv.org/abs/1602.04938) [12](https://arxiv.org/abs/1705.07874) [13](https://arxiv.org/abs/2307.13702)

### 外部入力から実行システムを守る

間接プロンプト注入、InjecAgent、AgentDojoにより、検索先やツール出力を通じた攻撃を対話的な環境で測るようになった。個々のモデルの拒否率だけでは、仕事の成功と攻撃耐性の両方を把握できない。 [14](https://arxiv.org/abs/2302.12173) [15](https://arxiv.org/abs/2403.02691) [16](https://arxiv.org/abs/2406.13352)

## 到達点・適用条件・残る境界

### できること・苦手なことを比較する — 比較が蓄積

できていること: 広い課題集合や事実の単位で評価し、モデル間・条件間の失敗を可視化できる。

条件: データ汚染、採点器の誤り、時間予算、実行基盤、母集団の偏りを揃える。

残る境界: 順位を一つ出しても、対象業務への適合や稀な重大事故の率までは決まらない。 [1](https://arxiv.org/abs/2211.09110) [10](https://arxiv.org/abs/2305.14251) [17](https://arxiv.org/abs/2611.08417)

### 自信が低い回答を控える — 条件付きの手法

できていること: 確率や予測集合と外部の判断ルールを使って、回答範囲と誤りの関係を管理できる。

条件: 校正用のデータと適用先の関係、時系列依存、棄権した場合の引き継ぎ先を決める。

残る境界: 「自信75%以上なら答える」と指示するだけで、確率的な閾値遵守は実現しない。 [5](https://arxiv.org/abs/1705.08500) [7](https://arxiv.org/abs/2202.13415) [2](https://arxiv.org/abs/2611.14661)

### 攻撃経路と有害な成功を検査する — 限定条件で実証

できていること: ツール出力経由の命令、秘密の持ち出し、仕事を終えながら起こす副作用を評価できる。

条件: 攻撃者が変更できる部分と守る情報、許された実行、正当な完了条件を区別して試験する。

残る境界: 既知攻撃を防いだことから、全経路の情報フローや未知攻撃への安全性までは言えない。 [16](https://arxiv.org/abs/2406.13352) [18](https://arxiv.org/abs/2611.03575) [3](https://arxiv.org/abs/2611.17280)

### 判断の手掛かりを説明する — 限定条件で実証

できていること: 特徴寄与や介入実験で、特定入力に対するモデルの振る舞いを検査できる。

条件: 説明手法の仮定と、別の入力・モデルへ移した際の安定性を確かめる。

残る境界: 相関的な寄与表示を因果機構の完全な説明にしない。出力された推論文も忠実性の評価対象になる。 [11](https://arxiv.org/abs/1602.04938) [12](https://arxiv.org/abs/1705.07874) [13](https://arxiv.org/abs/2307.13702) [19](https://arxiv.org/abs/2611.13885)

## 直近研究の位置づけ

### 棄権率と閾値遵守は違う

オープンモデルの検証では棄権形式の指示で棄権率が20%から91%へ増えたが、閾値0.5から0.9への変更に対する変化は−0.8ポイント。棄権が多いだけでは指示した判断規則を守った証拠にならない。 [2](https://arxiv.org/abs/2611.14661)

### 通常の生成物が漏洩経路になる

Synthesis Smugglingは、攻撃用に学習したモデルが会話から推定した属性を不可視文字や語彙選択へ符号化する実証。配備済みモデルでの発生率の測定ではないが、ツール通信以外にも検査対象が広がる。 [3](https://arxiv.org/abs/2611.17280)

### ベンチマークも保守が必要になる

Terminal-Benchの分析では、採点や条件の修正で成績と順位が変わると報告された。これは能力の増減と評価器の変化を切り分け、版・実行条件を残す必要を示している。 [17](https://arxiv.org/abs/2611.08417)

### 失敗予測は何を予測しているか

Coding agentの失敗予測では、課題難度・モデル能力を統制すると軌跡固有の予測利得がゼロと区別できないとの報告がある。高い識別性能から、途中介入が有効とは結論できない。 [20](https://arxiv.org/abs/2611.08285)

## 次の課題（編者の整理）

### 安全性をシステムの性質として測る

モデルの拒否だけでなく、権限制御、実行の隔離、記憶・検索・生成物を含む情報フローの検証へ評価をつなぐ必要がある。 [16](https://arxiv.org/abs/2406.13352) [3](https://arxiv.org/abs/2611.17280)

### 予測から有効な介入へ進めるか

失敗しそうと分かるだけでなく、その場で止める・モデルを変えるなどの介入が結果を改善するかを測る。 [20](https://arxiv.org/abs/2611.08285) [21](https://arxiv.org/abs/2611.09792)

## 分野間の接点（編者の整理）

- [医療・生体信号・創薬AI](https://drkamoshika.github.io/papers/?view=map&topic=medical): 同じLLM評価器でも診療課題が変わると順位や失敗の型が変わる。分野固有の外部検証が要る。 [22](https://pubmed.ncbi.nlm.nih.gov/42995166)

- [次イベント予測・点過程](https://drkamoshika.github.io/papers/?view=map&topic=events): 待ち時間や次イベントの確率にも、校正と将来情報の混入を避ける設計が必要になる。 [23](https://arxiv.org/abs/1305.3409) [24](https://arxiv.org/abs/2501.05925)

- [エージェント・検索・記憶・協調](https://drkamoshika.github.io/papers/?view=map&topic=agents): 行動を実行できるエージェントは、仕事を達成したかと、有害な副作用を起こさなかったかの両方で評価する。 [18](https://arxiv.org/abs/2611.03575)

## 読む順番

1. [Selective Classification for Deep Neural Networks](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1705.08500)

2. [Holistic Evaluation of Language Models](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2211.09110)

3. [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.14251)

4. [Measuring Faithfulness in Chain-of-Thought Reasoning](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.13702)

5. [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2406.13352)

6. [Abstention Is Not Threshold Compliance: Stated Scoring Rules in Open Language Models](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14661)

7. [Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17280)

## 参考文献と確認範囲

1. [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) — 2022-11-16 / arxiv:2211.09110 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2211.09110)

2. [Abstention Is Not Threshold Compliance: Stated Scoring Rules in Open Language Models](https://arxiv.org/abs/2611.14661) — 2026-11-10 / arxiv:2611.14661 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14661) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.14661v1)

3. [Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs](https://arxiv.org/abs/2611.17280) — 2026-11-12 / arxiv:2611.17280 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17280) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.17280v1)

4. [Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning](https://arxiv.org/abs/1506.02142) — 2015-06-06 / arxiv:1506.02142 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1506.02142)

5. [Selective Classification for Deep Neural Networks](https://arxiv.org/abs/1705.08500) — 2017-05-23 / arxiv:1705.08500 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1705.08500)

6. [A tutorial on conformal prediction](https://arxiv.org/abs/0706.3188) — 2007-06-21 / arxiv:0706.3188 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A0706.3188)

7. [Conformal prediction beyond exchangeability](https://arxiv.org/abs/2202.13415) — 2022-02-27 / arxiv:2202.13415 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2202.13415)

8. [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300) — 2020-09-07 / arxiv:2009.03300 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2009.03300)

9. [TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://arxiv.org/abs/2109.07958) — 2021-09-08 / arxiv:2109.07958 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2109.07958)

10. [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251) — 2023-05-23 / arxiv:2305.14251 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.14251)

11. ["Why Should I Trust You?": Explaining the Predictions of Any Classifier](https://arxiv.org/abs/1602.04938) — 2016-02-16 / arxiv:1602.04938 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1602.04938)

12. [A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874) — 2017-05-22 / arxiv:1705.07874 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1705.07874)

13. [Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702) — 2023-07-17 / arxiv:2307.13702 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.13702)

14. [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — 2023-02-23 / arxiv:2302.12173 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2302.12173)

15. [InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](https://arxiv.org/abs/2403.02691) — 2024-03-05 / arxiv:2403.02691 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2403.02691)

16. [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352) — 2024-06-19 / arxiv:2406.13352 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2406.13352)

17. [Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks](https://arxiv.org/abs/2611.08417) — 2026-11-05 / arxiv:2611.08417 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.08417)

18. [VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](https://arxiv.org/abs/2611.03575) — 2026-11-02 / arxiv:2611.03575 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.03575)

19. [Are Causal Neuron Circuits Unique and Transferable?](https://arxiv.org/abs/2611.13885) — 2026-11-10 / arxiv:2611.13885 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.13885)

20. [Hard Issue, Weak Model, or Bad Run? Rethinking Failure Prediction for Coding Agents](https://arxiv.org/abs/2611.08285) — 2026-11-05 / arxiv:2611.08285 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.08285)

21. [Knowing When to Intervene: Causal Evaluation of AI Agents](https://arxiv.org/abs/2611.09792) — 2026-11-06 / arxiv:2611.09792 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.09792)

22. [Large language models are unstable as autonomous medical evaluators across clinical tasks](https://pubmed.ncbi.nlm.nih.gov/42995166) — 2026-11-06 / pmid:42995166 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42995166) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://pubmed.ncbi.nlm.nih.gov/42995166)

23. [Calibration diagnostics for point process models via the probability integral transform](https://arxiv.org/abs/1305.3409) — 2013-05-15 / arxiv:1305.3409 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1305.3409)

24. [Navigating Tomorrow: Reliably Assessing Large Language Models Performance on Future Event Prediction](https://arxiv.org/abs/2501.05925) — 2025-01-10 / arxiv:2501.05925 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2501.05925)

## このレビューの範囲

母集団はこのライブラリの収録論文。全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断的レビューです。

基礎文献・新着論文は収録先の区別です。基礎文献側にも2026年の研究が含まれるため、古さや新しさは個々の公開日で確認できます。

技術の系譜、分野間の接点、次の課題は編者の整理であり、論文間の直接の引用関係や、商用普及の程度を確定するものではありません。

個別論文の確認範囲は要旨または本文の関連箇所です。今回、代表的な22件の一次資料を追加で照合しました。全件の全文再精読や独立再現を意味しません。

実験の数字は論文の報告値です。異なるデータ・分割・指標の数値を統一順位へ変換していません。

[7分野の全体マップ](https://drkamoshika.github.io/papers/?view=map)
