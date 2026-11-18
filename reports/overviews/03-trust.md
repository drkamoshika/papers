# 評価・安全性・解釈可能性：技術と実験を詳しく読む

改稿: 2026-11-18 / 対象文献スナップショット: 2026-11-16 / 論文公開日上限: 2026-11-12

正解率だけを測る段階から、いつ間違うか、何を根拠にするか、どんな攻撃や分布変化で崩れるかを評価する段階へ進んだ。現在は、評価そのものの妥当性と、実行システム全体の制御がボトルネックになっている。

## まず押さえる到達点

ベンチマーク、事実性検査、棄権・不確実性、攻撃試験、説明によって失敗を切り分けられる。

高い平均点、もっともらしい説明、安全指示だけで、未知環境の安全性を認定できない。 [1](https://arxiv.org/abs/2211.09110) [2](https://arxiv.org/abs/2611.14661) [3](https://arxiv.org/abs/2611.17280)

## 技術の中身と論文同士の関係

### 正解率・識別・校正・再現性は、別の性質を測っている

分類の正解率は、決めた閾値で何件正しいかを測る。AUROCは正例を負例より上へ並べる識別の性質を測り、確率の値そのものの正しさは測らない。同じ順位を保ったまま確率を極端に変換すれば、AUROCが変わらなくても「90%」の意味は変わる。確率に基づいて人へ回すかを決める場面では、順位が良いだけでは足りない。 [25](https://arxiv.org/abs/1906.02530) [5](https://arxiv.org/abs/1705.08500)

校正は、例えば0.8と予測した集団で実際にどの程度正解するかという対応を見る。ただし全体での校正が良くても、ある施設、言語、患者層などの部分集団で崩れる可能性がある。校正誤差の平均を一つ出すだけでは、稀だが重要な失敗や、行動を切り替える閾値付近の誤差を十分に表せない。誰にどの判断を適用するのかを先に決める必要がある。 [25](https://arxiv.org/abs/1906.02530) [7](https://arxiv.org/abs/2202.13415)

再現性はさらに別で、同じ入力を繰り返したときに同じ答えや評価が出るかを問う。出力が一貫していても全て誤っていることはあり、平均点が同じでも、実行ごとに失敗する項目が入れ替わることもある。モデル、プロンプト、実行基盤のどれを固定した再現性かを記録しないと、改善がモデルの性質か偶然の実行かを区別できない。 [22](https://pubmed.ncbi.nlm.nih.gov/42995166) [20](https://arxiv.org/abs/2611.08285) [17](https://arxiv.org/abs/2611.08417)

LLMでは、次のトークンの確率、自己申告する自信、回答が正しい確率は同じものではない。表現は違っても同じ意味の回答をまとめて不確実性を測る研究もあるが、意味の同値性をどう判定するかが新たな測定問題になる。自信らしい数値を得られることと、その値を根拠に安全な行動を選べることの間に、校正と運用条件の検証が入る。 [26](https://arxiv.org/abs/2302.09664) [27](https://arxiv.org/abs/2205.14334) [2](https://arxiv.org/abs/2611.14661)

### 棄権と予測集合が保証する範囲を正確に捉える

選択的分類は、全ての入力へ答える代わりに一部で棄権し、答えた集合の誤りと回答率の関係を見る。難しい入力を全て拒否すれば残りの精度は上がり得るため、精度と回答範囲を組にして評価する必要がある。棄権後の人の確認費用や見逃しも含めると、棄権率の高さそのものが良い結果ではない。 [5](https://arxiv.org/abs/1705.08500) [28](https://arxiv.org/abs/1901.09192)

conformal predictionは、一つのラベルを断定する代わりに、正解を含むことを目標とした予測集合を返す。標準的な交換可能性などの条件の下で被覆率を扱える点に価値があるが、全ての入力で同じ大きさの集合や、全ての部分集団で同じ保証が得られるわけではない。非常に大きな集合なら被覆できても意思決定に役立たないため、集合の大きさも評価に必要になる。 [6](https://arxiv.org/abs/0706.3188) [29](https://arxiv.org/abs/1111.1418)

時系列や実運用では、過去と未来の分布が同じとは限らない。Conformal prediction beyond exchangeabilityは、重み付きの分位点やランダム化を使い、分布の変化や対称でない学習手順に対して保証の劣化を扱う。これは任意の分布変化の下でも元の保証が無条件に保たれるという主張ではない。変化の仕方と保証が結び付いた理論として読む必要がある。 [7](https://arxiv.org/abs/2202.13415)

文章で「この閾値以上の自信があるときだけ答える」と指示する方法は、以上の統計的な手順と違う。モデルが数値の意味を理解し、同じ問題で閾値を変えたときに適切に判断を変えるかまで検証する必要がある。外部で確率へ閾値を当てれば回答範囲の単調性は構成できるが、その確率が別の分布でも正しいかは別の問題として残る。 [2](https://arxiv.org/abs/2611.14661) [25](https://arxiv.org/abs/1906.02530)

### 説明できることと、判断の原因が分かることを分ける

LIMEは対象入力の近傍で元モデルを単純なモデルへ近似し、局所の予測に関係する特徴を示す。SHAPは特徴が加わるときの寄与を、選んだ特徴集合と背景の定義の下で配分する。いずれも、どの範囲で近似したか、特徴をどのように変えたかという前提を持つ。説明の図が分かりやすいことから、モデルが学習した世界の因果構造までは決まらない。 [11](https://arxiv.org/abs/1602.04938) [12](https://arxiv.org/abs/1705.07874)

例えば相関する二つの特徴があるとき、一方を消す操作が現実には起こりにくい入力を作る可能性がある。背景集団を変えれば「通常からの差」の意味も変わる。特徴寄与を読むときは、説明の対象が一入力の予測なのか、集団全体の傾向なのか、現実に変更可能な要因なのかを区別する必要がある。予測の説明を、そのまま介入の推奨へ変換しない。 [11](https://arxiv.org/abs/1602.04938) [12](https://arxiv.org/abs/1705.07874) [30](https://arxiv.org/abs/1608.00060)

Chain-of-Thoughtの文章も検証の対象である。Measuring Faithfulnessは、途中の説明を変更・誤記・言い換えしたときの最終回答の変化などから、回答が説明へどの程度依存するかを調べた。読みやすい推論文を出すことと、その文が実際の判断を忠実に説明していることを分離した点が重要で、全モデルの推論文が常に無意味だという結論ではない。 [13](https://arxiv.org/abs/2307.13702)

回路への介入や表現の操作は、単なる出力の説明より機構へ近づくが、ある課題で見つけた部分が他の入力やモデルでも同じ働きをするかは別に問う必要がある。局所の説明、統計的な寄与、内部への因果介入は、証拠の種類が異なる。安全性のレビューでは、これらを全て「解釈できた」という一つの達成度にまとめない方が研究の進歩を正しく捉えられる。 [19](https://arxiv.org/abs/2611.13885) [13](https://arxiv.org/abs/2307.13702)

### 安全性は、モデルだけでなく評価器と実行経路の問題になる

間接プロンプト注入では、利用者が正当に依頼した作業中に、検索先やツール出力が別の命令を含む。通常の仕事をこなしながら、どの入力を命令として信頼するかを保つ必要がある。外部文章を全て拒めば攻撃は減るかもしれないが、仕事も終わらない。攻撃への耐性と正当な仕事の完了を同時に測るベンチマークが必要になる理由である。 [14](https://arxiv.org/abs/2302.12173) [15](https://arxiv.org/abs/2403.02691) [16](https://arxiv.org/abs/2406.13352)

さらに、禁止されたツール呼び出しがないだけでは安全とはいえない。Synthesis Smugglingは、攻撃用に学習したモデルが推定した属性を普通の生成文へ符号化し、利用者がその文を共有することを漏洩経路にする。これは一般モデルでの発生頻度の測定ではないが、通信先だけでなく、生成された成果物の情報内容も検討対象になることを示す。 [3](https://arxiv.org/abs/2611.17280)

評価器そのものにも誤りがある。LLMを採点者にすると、同じ系統のモデルへの選好や採点プロンプトの影響が入り得るし、人の参照ラベルがある場合も課題の定義が異なる。医療評価器の研究で課題をまたいで順位が安定しなかったことは、一つの試験で良かった採点者を他へ無条件に転用できない具体例になる。 [22](https://pubmed.ncbi.nlm.nih.gov/42995166) [1](https://arxiv.org/abs/2211.09110)

Terminal-Benchの保守研究は、固定された採点プログラムでも永続的に正しいとは限らないことを示す。有効な別解を古い採点器が拒む場合や、時間予算が方式の差を作る場合がある。安全性・能力の主張には、データ、採点器、実行環境、資源上限の版が全て関わる。点数の変化を能力の変化と解釈する前に、測定系が同じかを確認する必要がある。 [17](https://arxiv.org/abs/2611.08417)

## 手法を比較する

| 方法 | 何を変えるか | 得られる利点 | 前提と交換条件 |

| --- | --- | --- | --- |

| 正解率・AUROC | 閾値での正誤や正負の順位を測る。 | 課題の基本的な識別性能を比べる。 | 確率の校正、部分集団、実行の副作用は別の性質。 [25](https://arxiv.org/abs/1906.02530) [1](https://arxiv.org/abs/2211.09110) |

| 校正・選択的予測 | 確率と実際の頻度、回答率と誤りを対応させる。 | 答えるか人へ引き継ぐかを検討できる。 | 適用先の分布と棄権後の費用に依存する。 [5](https://arxiv.org/abs/1705.08500) [2](https://arxiv.org/abs/2611.14661) |

| 予測集合 | 条件の下で正解を含む集合を構成する。 | 単一の断定より不確実性を保てる。 | 被覆率と集合の有用性、集団別の保証は同じではない。 [6](https://arxiv.org/abs/0706.3188) [7](https://arxiv.org/abs/2202.13415) |

| 説明・内部介入 | 局所の寄与や表現の働きを検査する。 | 誤りの手掛かりや機構の仮説を得る。 | 背景や介入方法と、他の条件への移転を確かめる。 [12](https://arxiv.org/abs/1705.07874) [13](https://arxiv.org/abs/2307.13702) [19](https://arxiv.org/abs/2611.13885) |

| 対話的な攻撃評価 | 攻撃者と正当な依頼を含む実行を測る。 | 実際の情報経路や副作用を評価対象にできる。 | 脅威モデルと環境の範囲を超える保証ではない。 [16](https://arxiv.org/abs/2406.13352) [3](https://arxiv.org/abs/2611.17280) |

## 具体的研究を読み解く

### 「棄権率91%」を安全性の改善と即断しない

**研究の問い**: 閾値tより正解確率が高いときだけ答えるという指示が、本当に閾値に応じた方策として実装されているかを問う。単に拒否や棄権の文体を学んだだけの可能性を分ける。

**設計と対照**: 複数のオープンなモデルと学習段階で共通の問題を使い、閾値、回答／棄権の形式、自己評価信号、外部校正の条件を変える。判断する問題自体が変わらない比較が鍵になる。

**論文が報告する結果**: t=0.75で棄権形式の指示により平均棄権率20%が91%になった一方、同じ形式でtを0.5から0.9へ上げた変化は−0.8ポイントだった。

**位置づけ・編者の解釈**: 編者の解釈では、文面への従順さと確率的な規則への従順さを分ける重要な実験である。回答率、回答した項目、閾値に対する反応を別々に示して初めて、実際の判断方策を評価できる。

**結論の範囲**: 外部校正も、評価分布で後から合わせた場合と、別分布へ移した場合で結果が異なる。棄権指示か外部閾値かの二択で一般的な優劣を結論しない。

[2](https://arxiv.org/abs/2611.14661) [5](https://arxiv.org/abs/1705.08500) [25](https://arxiv.org/abs/1906.02530)

### Terminal-Benchの更新は、モデル以外で順位が変わる例

**研究の問い**: 能力の高いエージェントが別の正当な解を見つけたとき、古い採点器はその解を誤りにする場合がある。採点器が公開時に検査されていても、その後の環境・モデルで妥当性が続くかが問題となる。

**設計と対照**: 課題の資料、実行履歴、報告、自動検査、人による修正確認を組み合わせ、Terminal-Bench 2.0を監査する。修正後の版と資源予算を変えた条件を評価する。

**論文が報告する結果**: 約30%に問題を特定し、修正後の成績は10ポイント超上昇、順位は最大3位変化した一方、全体の順位相関は0.958と高かったと報告。

**位置づけ・編者の解釈**: 編者の解釈では、全体相関が高くても個別の導入判断に十分とは限らない。同じベンチマーク名であっても、版、修正項目、実行時間を保存して初めて差を比較できる。

**結論の範囲**: 監査された範囲は対象ベンチマークであり、全てのベンチマークに同じ割合の不備があると一般化しない。また、時間を伸ばした性能は、同じ予算内の性能と分けて記録する。

[17](https://arxiv.org/abs/2611.08417) [1](https://arxiv.org/abs/2211.09110)

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

## 関連する直近研究

### 通常の生成物が漏洩経路になる

Synthesis Smugglingは、攻撃用に学習したモデルが会話から推定した属性を不可視文字や語彙選択へ符号化する実証。配備済みモデルでの発生率の測定ではないが、ツール通信以外にも検査対象が広がる。 [3](https://arxiv.org/abs/2611.17280)

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

## 引用文献と確認範囲

1. [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) — 2022-11-16 / arxiv:2211.09110 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2211.09110)

2. [Abstention Is Not Threshold Compliance: Stated Scoring Rules in Open Language Models](https://arxiv.org/abs/2611.14661) — 2026-11-10 / arxiv:2611.14661 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14661) / 再確認: 2026-11-18、要旨、棄権率と閾値への反応、[確認先](https://arxiv.org/abs/2611.14661v1)

3. [Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs](https://arxiv.org/abs/2611.17280) — 2026-11-12 / arxiv:2611.17280 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17280) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://arxiv.org/abs/2611.17280v1)

4. [Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning](https://arxiv.org/abs/1506.02142) — 2015-06-06 / arxiv:1506.02142 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1506.02142)

5. [Selective Classification for Deep Neural Networks](https://arxiv.org/abs/1705.08500) — 2017-05-23 / arxiv:1705.08500 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1705.08500)

6. [A tutorial on conformal prediction](https://arxiv.org/abs/0706.3188) — 2007-06-21 / arxiv:0706.3188 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A0706.3188) / 再確認: 2026-11-18、要旨、予測集合と保証の条件、[確認先](https://arxiv.org/abs/0706.3188)

7. [Conformal prediction beyond exchangeability](https://arxiv.org/abs/2202.13415) — 2022-02-27 / arxiv:2202.13415 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2202.13415) / 再確認: 2026-11-18、要旨、交換可能性と分布変化、[確認先](https://arxiv.org/abs/2202.13415v5)

8. [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300) — 2020-09-07 / arxiv:2009.03300 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2009.03300)

9. [TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://arxiv.org/abs/2109.07958) — 2021-09-08 / arxiv:2109.07958 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2109.07958)

10. [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251) — 2023-05-23 / arxiv:2305.14251 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.14251)

11. ["Why Should I Trust You?": Explaining the Predictions of Any Classifier](https://arxiv.org/abs/1602.04938) — 2016-02-16 / arxiv:1602.04938 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1602.04938)

12. [A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874) — 2017-05-22 / arxiv:1705.07874 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1705.07874)

13. [Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702) — 2023-07-17 / arxiv:2307.13702 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.13702) / 再確認: 2026-11-18、要旨、推論文への介入と忠実性、[確認先](https://arxiv.org/abs/2307.13702)

14. [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — 2023-02-23 / arxiv:2302.12173 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2302.12173)

15. [InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](https://arxiv.org/abs/2403.02691) — 2024-03-05 / arxiv:2403.02691 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2403.02691)

16. [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352) — 2024-06-19 / arxiv:2406.13352 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2406.13352)

17. [Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks](https://arxiv.org/abs/2611.08417) — 2026-11-05 / arxiv:2611.08417 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.08417) / 再確認: 2026-11-18、要旨、採点器・版・資源予算の影響、[確認先](https://arxiv.org/abs/2611.08417)

18. [VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](https://arxiv.org/abs/2611.03575) — 2026-11-02 / arxiv:2611.03575 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.03575)

19. [Are Causal Neuron Circuits Unique and Transferable?](https://arxiv.org/abs/2611.13885) — 2026-11-10 / arxiv:2611.13885 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.13885)

20. [Hard Issue, Weak Model, or Bad Run? Rethinking Failure Prediction for Coding Agents](https://arxiv.org/abs/2611.08285) — 2026-11-05 / arxiv:2611.08285 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.08285)

21. [Knowing When to Intervene: Causal Evaluation of AI Agents](https://arxiv.org/abs/2611.09792) — 2026-11-06 / arxiv:2611.09792 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.09792)

22. [Large language models are unstable as autonomous medical evaluators across clinical tasks](https://pubmed.ncbi.nlm.nih.gov/42995166) — 2026-11-06 / pmid:42995166 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42995166) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://pubmed.ncbi.nlm.nih.gov/42995166)

23. [Calibration diagnostics for point process models via the probability integral transform](https://arxiv.org/abs/1305.3409) — 2013-05-15 / arxiv:1305.3409 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1305.3409)

24. [Navigating Tomorrow: Reliably Assessing Large Language Models Performance on Future Event Prediction](https://arxiv.org/abs/2501.05925) — 2025-01-10 / arxiv:2501.05925 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2501.05925)

25. [Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift](https://arxiv.org/abs/1906.02530) — 2019-06-06 / arxiv:1906.02530 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1906.02530)

26. [Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation](https://arxiv.org/abs/2302.09664) — 2023-02-19 / arxiv:2302.09664 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2302.09664)

27. [Teaching Models to Express Their Uncertainty in Words](https://arxiv.org/abs/2205.14334) — 2022-05-28 / arxiv:2205.14334 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2205.14334)

28. [SelectiveNet: A Deep Neural Network with an Integrated Reject Option](https://arxiv.org/abs/1901.09192) — 2019-01-26 / arxiv:1901.09192 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1901.09192)

29. [Efficient Nonparametric Conformal Prediction Regions](https://arxiv.org/abs/1111.1418) — 2011-11-06 / arxiv:1111.1418 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1111.1418)

30. [Double/Debiased Machine Learning for Treatment and Structural Parameters](https://arxiv.org/abs/1608.00060) — 2016-07-30 / arxiv:1608.00060 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1608.00060) / 再確認: 2026-11-18、要旨、直交スコアと交差適合、[確認先](https://arxiv.org/abs/1608.00060v7) / 照合先v7は表題がTreatment and Causal Parameters。ライブラリの登録原題と異なるが同一arXiv ID。

## 収録範囲と読み方

対象は2026-11-16時点の収録スナップショット（基礎774件・新着264件）です。2026-11-18の改稿は、この範囲の技術・比較・事例の詳説です。

全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断レビューです。基礎・新着は収録先の区別で、古さは個々の公開日から確認できます。

技術の系譜、論文間の位置づけ、実験から導く解釈と次の課題は編者の整理です。直接の引用関係や商用普及率を確定するものではありません。

初版の22件に加え、改稿では25件の一次資料を確認しました（重複あり）。要旨・本文・検索掲載箇所の範囲を引用文献に記録しています。全件の全文精読や独立再現を意味しません。

数値は論文の報告値です。異なるデータ・分割・指標の比較を統一順位へ変換していません。説明用の計算例は実測値と区別しています。
