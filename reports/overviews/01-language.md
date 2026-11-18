# 言語モデルの学習・推論・効率化：技術と実験を詳しく読む

改稿: 2026-11-18 / 対象文献スナップショット: 2026-11-16 / 論文公開日上限: 2026-11-12

汎用の言語表現を、指示に従う生成器へ、さらに計算量を配分して解く推論器へ発展させてきた。現在は、能力だけでなく学習・推論・運用コストを含めて設計する段階にある。

## まず押さえる到達点

少数例での適応、指示に沿う生成、検証器を使う推論、小型化と推論処理の効率化。

長く考えれば必ず正しい、量子化しても全用途で同等、という保証はない。 [1](https://arxiv.org/abs/2005.14165) [2](https://arxiv.org/abs/2611.17320) [3](https://arxiv.org/abs/2611.13410)

## 技術の中身と論文同士の関係

### 何を学習したモデルなのかを、三つの目的関数から読む

自己回帰型の事前学習が直接最適化するのは、文脈を与えたときに実際に現れた次のトークンへ高い確率を置くことだ。これは大量の文章から語法、事実、推論の型を取り込む有力な手段だが、「利用者にとって正しく有用な応答」を直接採点しているわけではない。BERTのように一部を隠して復元する目的とも異なり、同じTransformerでも学習時に利用する文脈と下流への使い方が違う。 [1](https://arxiv.org/abs/2005.14165) [7](https://arxiv.org/abs/1810.04805)

指示学習では、指示と望ましい応答の組を使い、学習済みの知識や生成能力をどのように呼び出すかを整える。少数例をプロンプトへ入れる文脈内学習は重みを更新しないのに対し、教師あり微調整は重みを変える。この違いは、変更を取り消しやすいか、新しい資料を即時に使えるか、利用のたびに長い入力を送るかという運用上の違いにもつながる。 [1](https://arxiv.org/abs/2005.14165) [10](https://arxiv.org/abs/2109.01652) [11](https://arxiv.org/abs/2203.02155)

選好学習は、二つの応答のうちどちらが望ましいかという比較を使う。RLHFでは選好から報酬モデルを学び、その報酬を高めつつ参照モデルから離れすぎないように方策を更新する。DPOは、選好の確率モデルとKLで制約した目的の関係を使い、参照モデルに対する応答の相対的な対数確率を直接学習する。報酬の明示的な学習と、その後の強化学習ループを簡略化することが中心的な貢献である。 [11](https://arxiv.org/abs/2203.02155) [12](https://arxiv.org/abs/2305.18290)

ここから「DPOはRLHFより必ず安全」「選好が高いほど事実に忠実」という結論は出ない。どちらも、収集した選好が何を評価しているかに依存する。読みやすさや利用者への同意が好まれるデータなら、その方向の最適化と事実性がずれる可能性がある。方法の比較では、学習目標の簡潔さ、評価者の好みへの適合、外部に正解のある課題の成績を分けて読む必要がある。 [12](https://arxiv.org/abs/2305.18290) [26](https://arxiv.org/abs/2310.13548) [27](https://arxiv.org/abs/2305.14251)

### スケーリングは「大きくする」だけでなく、予算をどこへ置くかという問題

モデルのパラメータ数、学習トークン数、計算量は独立に無限には増やせない。Chinchillaの問題設定は、与えられた学習計算量でモデルとデータにどのように配分するかだった。大きいモデルを同じデータ量で学習する場合と、小さいモデルへより多くのデータを読ませる場合を区別すると、「規模」の意味が変わる。損失の傾向を測る法則は、この予算配分の経験的な指針である。 [8](https://arxiv.org/abs/2001.08361) [9](https://arxiv.org/abs/2203.15556)

同じパラメータ数でも、データの質、重複、専門領域、指示学習によって下流の使いやすさは変わる。逆に、事前学習損失が低いことから、稀な安全上の失敗や複雑な業務手順への強さまでは一意に決まらない。スケーリング則の曲線と特定課題の正答率を、同じ尺度のように重ねないことが重要になる。モデルの規模を説明する論文と、能力を測る論文は役割が異なる。 [8](https://arxiv.org/abs/2001.08361) [9](https://arxiv.org/abs/2203.15556) [28](https://arxiv.org/abs/2211.09110)

推論時にも配分の問題がある。同じ入力で長い思考を一つ生成する、独立の候補を複数作る、途中から枝分かれさせる、検証器で候補を選ぶ、という方式は同じ追加計算ではない。正解候補が生成されなければ選別は成功せず、候補に正解があっても検証器が区別できなければ落とす。探索と検証のどちらが律速かを見ないまま、生成トークン数だけを増やしても効率は分からない。 [14](https://arxiv.org/abs/2203.11171) [29](https://arxiv.org/abs/2305.10601) [15](https://arxiv.org/abs/2305.20050) [20](https://arxiv.org/abs/2408.03314)

したがって推論能力の比較には、モデルの重みだけでなく、候補数、最大出力長、検証器の学習と実行、停止条件まで含む必要がある。小さいモデルと強い検証器の組合せが、大きいモデルの一回生成を上回ることはあり得るが、それは小さい生成器だけの能力ではない。利用者が実際に支払う費用と待ち時間は、これらの部品を合計したシステムの性質になる。 [20](https://arxiv.org/abs/2408.03314) [2](https://arxiv.org/abs/2611.17320)

### attention・長い文脈・記憶は、解決する問題が異なる

attentionは、現在の表現を問い合わせとして、入力中のどの表現をどの程度混ぜるかを計算する。Transformerはこの操作を複数の層とヘッドで使い、位置ごとの変換と組み合わせる。長い入力を受け取れることは必要な情報を渡すための容量を増やすが、その情報を正しい位置から取り出して判断に使えることとは別である。 [6](https://arxiv.org/abs/1706.03762) [30](https://arxiv.org/abs/2307.03172)

長文検索、外部の記憶、重みに埋め込まれた知識は、更新と参照の仕方が違う。プロンプト中の根拠は今回の回答へすぐ使える一方、入力長と参照費用が増える。検索は必要部分を選べるが、検索漏れが起こる。重みへの学習は利用時の入力を短くし得るが、何を記憶し、どこから得たかを追跡しにくい。この三者を、文脈長という一つの数字だけで比較することはできない。 [31](https://arxiv.org/abs/2005.11401) [30](https://arxiv.org/abs/2307.03172) [32](https://arxiv.org/abs/2310.08560)

KVキャッシュは、モデルが過去の入力について計算したattention用のキーと値を再利用する実装上の仕組みで、事実を覚える外部メモリとは異なる。PagedAttentionはそのメモリ管理、Nebulaは複数の利用者やサーバにまたがる共有部分の再利用を扱う。検索で根拠が改善したのか、同じ根拠を安く処理できるようになったのかを分けると、最新の推論基盤論文の位置が理解しやすくなる。 [19](https://arxiv.org/abs/2309.06180) [22](https://arxiv.org/abs/2611.09474)

この区別はエージェントの長期作業にも効く。長いログをそのまま渡す方式、必要な記録だけ検索する方式、教訓へ圧縮する方式は、それぞれ情報欠落の場所が異なる。圧縮が高速でも、後の検証に必要な証拠を失えば仕事の質は落ちる。言語モデルの文脈処理と、エージェントの根拠管理は接続しているが、同じ能力を測っているわけではない。 [30](https://arxiv.org/abs/2307.03172) [33](https://arxiv.org/abs/2611.14320) [22](https://arxiv.org/abs/2611.09474)

### 効率化は、何を変えずに何を近似するかで比較する

LoRAは重みの変化を低ランクの行列積で表し、学習で更新するパラメータや保存量を減らす。元の重みを全て低ビットにする量子化とは違う。QLoRAは両方を組み合わせる。少ない更新パラメータで十分かという近似と、数値の表現精度を落としてよいかという近似を分けることで、学習時のメモリ削減と、推論時の速度・品質を別々に評価できる。 [16](https://arxiv.org/abs/2106.09685) [17](https://arxiv.org/abs/2210.17323) [21](https://arxiv.org/abs/2305.14314)

FlashAttentionはattentionの数式を近似するのではなく、GPUのメモリ階層に合わせて計算順序を変え、読み書きを減らす。これは量子化のような品質との交換とは性質が異なる。ただし、数式上同じ操作でも、実測の速度は入力長、GPU、バッチサイズに依存するため、論文の高速化率を別の環境へそのまま移せるわけではない。 [18](https://arxiv.org/abs/2205.14135) [34](https://arxiv.org/abs/2307.08691)

推測的デコードでは、小さいモデルが先の候補を作り、大きいモデルがまとめて検証する。適切な受理・補正を行う原方式は、対象モデルの生成分布を維持しながら逐次実行を減らすことを狙う。小さいモデルの答えを無条件に採用する蒸留とは違い、対象モデルの検証費用も残る。受理率が低い負荷では、候補作成の費用が増えるため利点は小さくなる。 [35](https://arxiv.org/abs/2211.17192)

SteerDistillのような行動上の修正は、圧縮後の出力誤差が環境を変え、次の入力まで変えてしまう問題を扱う。文章一回の誤差が小さくても、ツール呼び出しや引数が変われば行動系列は別の分布へ進む。言語モデルの圧縮をエージェントへ適用するときは、重みの再構成誤差だけでなく、目的達成率と失敗の累積を測る必要がある。 [3](https://arxiv.org/abs/2611.13410) [24](https://arxiv.org/abs/2210.03629)

## 手法を比較する

| 方法 | 何を変えるか | 得られる利点 | 前提と交換条件 |

| --- | --- | --- | --- |

| 文脈内学習 | 入力に例や根拠を置き、重みを変えずに予測する。 | 新しい資料を即時に利用でき、設定を取り替えやすい。 | 入力費用と長文の参照失敗が残り、永続的な学習とは異なる。 [1](https://arxiv.org/abs/2005.14165) [30](https://arxiv.org/abs/2307.03172) |

| 教師あり微調整・LoRA | 例の応答を再現するよう重みの一部または全体を更新する。 | 用途への応答形式や振る舞いを継続的に整えられる。 | 学習データの範囲と副作用を検証する必要がある。 [10](https://arxiv.org/abs/2109.01652) [16](https://arxiv.org/abs/2106.09685) |

| 選好最適化 | 望ましい応答の相対的な選択を学ぶ。 | 応答の好ましさを直接の教師信号にできる。 | 選好の正しさ・偏り・対象外への一般化が残る。 [11](https://arxiv.org/abs/2203.02155) [12](https://arxiv.org/abs/2305.18290) |

| 探索と検証 | 生成候補へ追加計算を割り当て、評価して選ぶ。 | 対象課題で、一回生成では得られない正答を拾える。 | 生成器と検証器の両方の誤りと総費用に依存する。 [20](https://arxiv.org/abs/2408.03314) [2](https://arxiv.org/abs/2611.17320) |

| 推論基盤の最適化 | メモリの読み書き、キャッシュ、逐次処理を減らす。 | 同じモデル・負荷で待ち時間や収容効率を改善する。 | 能力の改善と区別し、対象機器と負荷で測る。 [18](https://arxiv.org/abs/2205.14135) [35](https://arxiv.org/abs/2211.17192) [22](https://arxiv.org/abs/2611.09474) |

## 具体的研究を読み解く

### DiVRを「拡散モデルの正答率が上がった」以上に読む

**研究の問い**: 拡散言語モデルが既に作った部分を見直すとき、誤りを示す信号と、どこまで一緒に再生成するかが問題になる。局所的な誤トークンだけ直しても周辺が同じなら再び同じ誤りへ戻り得る。

**設計と対照**: 生成器の軌跡と最終的な正否から、途中の系列が正答へ至るかを予測する検証器を学ぶ。検証器が再生成するブロックと候補の選択を担い、生成器自体の変更とは区別する。

**論文が報告する結果**: 微調整済みLLaDA-8B-Baseの5推論課題で平均35.3%から43.4%。greedyに対する計算量は1.9〜3.5倍で、比較された探索法は3.8〜7.4倍だった。

**位置づけ・編者の解釈**: 編者の解釈では、これは全ての誤りを検知できるという結果ではなく、「追加計算をどこへ使うか」という制御を別の学習問題にした例である。生成能力と選別能力の分離が、従来の自己整合性や過程検証との接点になる。

**結論の範囲**: 比較する際は、同じ生成器・微調整状態・課題・費用の基準を確認する。この改善幅から、実業務の納品率や別のモデル群での速度まで推定しない。

[2](https://arxiv.org/abs/2611.17320) [14](https://arxiv.org/abs/2203.11171) [15](https://arxiv.org/abs/2305.20050)

### SteerDistillで、量子化の評価単位が変わる

**研究の問い**: 低ビット化したモデルが途中で要件を見落とすと、以後の環境が教師の成功軌跡からずれる。教師の記録をそのまま見せるだけでは、学生が実際に失敗した状態を十分に学べない。

**設計と対照**: 教師が失敗応答の修正を指導し、学生の再実行結果で指導を改善する。局所的に確認した修正を、指導なしで動く学生へ取り込む構成であり、実行のフィードバックを学習資料へ変換する。

**論文が報告する結果**: 5ベンチマーク・3モデルのW4A16条件で、最良量子化比較法より平均1.67〜2.18ポイント改善、BF16との差は1ポイント以内と報告された。

**位置づけ・編者の解釈**: 編者の解釈では、圧縮とエージェント学習が交わる点が重要である。量子化の誤差を数値上だけ補うのではなく、仕事を失敗する文脈で補っている。反面、教師と再実行の費用を含めて圧縮の利益を測る必要がある。

**結論の範囲**: 量子化方式やモデル、環境が違えば失敗分布も変わる。低ビット化一般の無損失化を示した論文としては読まない。

[3](https://arxiv.org/abs/2611.13410) [17](https://arxiv.org/abs/2210.17323) [21](https://arxiv.org/abs/2305.14314)

## 基礎からの積み上げ

### 分散表現から文脈表現へ

単語の近さをベクトルで扱う段階から、attentionで入力間の関係を計算し、文脈ごとの表現を作る段階へ進んだ。Transformerは現在の多くのモデルの構成上の出発点になる。 [4](https://arxiv.org/abs/1301.3781) [5](https://arxiv.org/abs/1409.0473) [6](https://arxiv.org/abs/1706.03762) [7](https://arxiv.org/abs/1810.04805)

### 事前学習と規模の設計

GPT-3は少数例を文脈に置く適応を示し、スケーリング則とChinchillaはモデル規模だけでなくデータ量・計算量の配分を設計対象にした。これは性能の増加傾向を扱う知見で、個々の回答の正しさを保証する法則ではない。 [1](https://arxiv.org/abs/2005.14165) [8](https://arxiv.org/abs/2001.08361) [9](https://arxiv.org/abs/2203.15556)

### 人間の指示・選好へ合わせる

指示学習と人間のフィードバック、DPOによる選好最適化が、事前学習モデルを利用目的へ合わせる道筋を整えた。選好への適合と、事実性・安全性の達成は別の評価が必要になる。 [10](https://arxiv.org/abs/2109.01652) [11](https://arxiv.org/abs/2203.02155) [12](https://arxiv.org/abs/2305.18290)

### 推論時の探索と実装の最適化

Chain-of-Thought、自己整合性、過程の検証が推論時の計算配分へつながる。一方、LoRA・量子化・FlashAttention・PagedAttentionは、更新パラメータ、メモリ、入出力、バッチ実行の別々のボトルネックを扱う。 [13](https://arxiv.org/abs/2201.11903) [14](https://arxiv.org/abs/2203.11171) [15](https://arxiv.org/abs/2305.20050) [16](https://arxiv.org/abs/2106.09685) [17](https://arxiv.org/abs/2210.17323) [18](https://arxiv.org/abs/2205.14135) [19](https://arxiv.org/abs/2309.06180)

## 到達点・適用条件・残る境界

### 指示に沿う生成と用途適応 — 比較が蓄積

できていること: 共通の事前学習モデルを、少数例や追加学習で要約・質問応答などの用途へ適応できる。

条件: 対象言語・入力長・専門領域を合わせて評価し、検索や外部ツールで不足する知識を補う。

残る境界: 流暢さや指示遵守から、未知事実の正確性や分布外への一般化までは導けない。 [1](https://arxiv.org/abs/2005.14165) [11](https://arxiv.org/abs/2203.02155) [16](https://arxiv.org/abs/2106.09685)

### 計算を追加して推論を改善する — 限定条件で実証

できていること: 複数解候補の探索・再生成と検証により、対象の数学・推論課題の成績を改善できる。

条件: 候補を区別できる検証器と、正答率の増加に見合う追加計算の予算が要る。

残る境界: 検証器が誤れば誤答を選び直す。推論ベンチマークでの改善を、長期業務の完遂能力へそのまま移せない。 [14](https://arxiv.org/abs/2203.11171) [20](https://arxiv.org/abs/2408.03314) [2](https://arxiv.org/abs/2611.17320)

### 小型化してエージェントを動かす — 限定条件で実証

できていること: 重みの低ビット化と教師からの行動修正を組み合わせ、対象エージェント課題で精度低下を抑えられる。

条件: 圧縮後のモデルを実際の行動系列で評価する。単発テキストの誤差だけでは環境との相互作用の失敗を捕まえにくい。

残る境界: 対象のモデル・量子化方式・課題以外で同じ性能差になるとは限らず、学習用教師の費用も残る。 [17](https://arxiv.org/abs/2210.17323) [21](https://arxiv.org/abs/2305.14314) [3](https://arxiv.org/abs/2611.13410)

### 長文・複数利用者の推論を効率化する — 限定条件で実証

できていること: attentionの入出力削減、KVメモリの管理、繰り返し部分の分散再利用で処理時間や収容効率を改善できる。

条件: GPU構成、バッチサイズ、文脈の共有率、通信量を含めたワークロードで測る。

残る境界: 最初のトークンが速くなることと、回答全体の完了時間や正答率が改善することは同じ指標ではない。 [18](https://arxiv.org/abs/2205.14135) [19](https://arxiv.org/abs/2309.06180) [22](https://arxiv.org/abs/2611.09474)

## 関連する直近研究

### Nebula：再利用をクラスタ全体で管理する

4モデル・4種のRAG／エージェント負荷で、最良比較法に対する最初のトークンまでの待ち時間の中央値を平均61.4%削減。長い文脈の共有パターンを実装の設計へ取り込む研究である。 [22](https://arxiv.org/abs/2611.09474)

## 次の課題（編者の整理）

### 能力・計算量・費用を同時に比べる

モデル単体の成績に加え、検証器、生成回数、教師、キャッシュを含む総費用と遅延を揃えた比較が次の焦点になる。 [20](https://arxiv.org/abs/2408.03314) [3](https://arxiv.org/abs/2611.13410) [22](https://arxiv.org/abs/2611.09474)

### 推論手順を能力の説明に使えるか

途中の説明がもっともらしくても、実際の判断理由と一致するかは別に検証する必要がある。 [23](https://arxiv.org/abs/2307.13702)

## 分野間の接点（編者の整理）

- [エージェント・検索・記憶・協調](https://drkamoshika.github.io/papers/?view=map&topic=agents): 言語生成を外部ツールと組み合わせると、評価単位が一回答から行動系列へ変わる。 [24](https://arxiv.org/abs/2210.03629) [3](https://arxiv.org/abs/2611.13410)

- [評価・安全性・解釈可能性](https://drkamoshika.github.io/papers/?view=map&topic=trust): 選好最適化・長い推論・高い自信のどれも、事実性や校正の代わりにはならない。 [12](https://arxiv.org/abs/2305.18290) [25](https://arxiv.org/abs/2611.14661)

## 読む順番

1. [Attention Is All You Need](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1706.03762)

2. [Language Models are Few-Shot Learners](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2005.14165)

3. [Training Compute-Optimal Large Language Models](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2203.15556)

4. [Training language models to follow instructions with human feedback](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2203.02155)

5. [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2201.11903)

6. [Learning When Diffusion Language Models Should Regenerate](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17320)

7. [SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.13410)

## 引用文献と確認範囲

1. [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — 2020-05-28 / arxiv:2005.14165 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2005.14165)

2. [Learning When Diffusion Language Models Should Regenerate](https://arxiv.org/abs/2611.17320) — 2026-11-12 / arxiv:2611.17320 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17320) / 再確認: 2026-11-18、要旨、事例の方法・実験条件・報告値、[確認先](https://arxiv.org/abs/2611.17320v1)

3. [SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering](https://arxiv.org/abs/2611.13410) — 2026-11-10 / arxiv:2611.13410 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.13410) / 再確認: 2026-11-18、要旨、事例の方法・実験条件・報告値、[確認先](https://arxiv.org/abs/2611.13410v1)

4. [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) — 2013-01-16 / arxiv:1301.3781 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1301.3781)

5. [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) — 2014-09-01 / arxiv:1409.0473 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1409.0473)

6. [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — 2017-06-12 / arxiv:1706.03762 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1706.03762)

7. [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) — 2018-10-11 / arxiv:1810.04805 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1810.04805)

8. [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — 2020-01-23 / arxiv:2001.08361 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2001.08361)

9. [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) — 2022-03-29 / arxiv:2203.15556 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2203.15556) / 再確認: 2026-11-18、要旨、計算量とデータ配分、[確認先](https://arxiv.org/abs/2203.15556)

10. [Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652) — 2021-09-03 / arxiv:2109.01652 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2109.01652)

11. [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — 2022-03-04 / arxiv:2203.02155 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2203.02155)

12. [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) — 2023-05-29 / arxiv:2305.18290 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.18290) / 再確認: 2026-11-18、本文§3–4、RLHFとDPOの目的・導出、[確認先](https://arxiv.org/html/2305.18290v3)

13. [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) — 2022-01-28 / arxiv:2201.11903 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2201.11903)

14. [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) — 2022-03-21 / arxiv:2203.11171 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2203.11171)

15. [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) — 2023-05-31 / arxiv:2305.20050 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.20050)

16. [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) — 2021-06-17 / arxiv:2106.09685 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2106.09685)

17. [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323) — 2022-10-31 / arxiv:2210.17323 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2210.17323)

18. [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135) — 2022-05-27 / arxiv:2205.14135 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2205.14135)

19. [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — 2023-09-12 / arxiv:2309.06180 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2309.06180)

20. [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) — 2024-08-06 / arxiv:2408.03314 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2408.03314)

21. [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) — 2023-05-23 / arxiv:2305.14314 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.14314)

22. [Nebula: Distributed Position-Independent Caching for LLM Serving](https://arxiv.org/abs/2611.09474) — 2026-11-06 / arxiv:2611.09474 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.09474) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://arxiv.org/abs/2611.09474v1)

23. [Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702) — 2023-07-17 / arxiv:2307.13702 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.13702) / 再確認: 2026-11-18、要旨、推論文への介入と忠実性、[確認先](https://arxiv.org/abs/2307.13702)

24. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — 2022-10-06 / arxiv:2210.03629 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2210.03629)

25. [Abstention Is Not Threshold Compliance: Stated Scoring Rules in Open Language Models](https://arxiv.org/abs/2611.14661) — 2026-11-10 / arxiv:2611.14661 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14661) / 再確認: 2026-11-18、要旨、棄権率と閾値への反応、[確認先](https://arxiv.org/abs/2611.14661v1)

26. [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548) — 2023-10-20 / arxiv:2310.13548 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2310.13548)

27. [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251) — 2023-05-23 / arxiv:2305.14251 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.14251)

28. [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) — 2022-11-16 / arxiv:2211.09110 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2211.09110)

29. [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) — 2023-05-17 / arxiv:2305.10601 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.10601)

30. [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — 2023-07-06 / arxiv:2307.03172 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.03172)

31. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — 2020-05-22 / arxiv:2005.11401 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2005.11401) / 再確認: 2026-11-18、要旨、RAGの構成と二方式、[確認先](https://arxiv.org/abs/2005.11401)

32. [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — 2023-10-12 / arxiv:2310.08560 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2310.08560)

33. [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320) — 2026-11-10 / arxiv:2611.14320 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14320) / 再確認: 2026-11-18、要旨、事例の方法・実験条件・報告値、[確認先](https://arxiv.org/abs/2611.14320v1)

34. [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691) — 2023-07-17 / arxiv:2307.08691 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.08691)

35. [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192) — 2022-11-30 / arxiv:2211.17192 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2211.17192) / 再確認: 2026-11-18、要旨、推測的デコードと分布の維持、[確認先](https://arxiv.org/abs/2211.17192)

## 収録範囲と読み方

対象は2026-11-16時点の収録スナップショット（基礎774件・新着264件）です。2026-11-18の改稿は、この範囲の技術・比較・事例の詳説です。

全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断レビューです。基礎・新着は収録先の区別で、古さは個々の公開日から確認できます。

技術の系譜、論文間の位置づけ、実験から導く解釈と次の課題は編者の整理です。直接の引用関係や商用普及率を確定するものではありません。

初版の22件に加え、改稿では25件の一次資料を確認しました（重複あり）。要旨・本文・検索掲載箇所の範囲を引用文献に記録しています。全件の全文精読や独立再現を意味しません。

数値は論文の報告値です。異なるデータ・分割・指標の比較を統一順位へ変換していません。説明用の計算例は実測値と区別しています。
