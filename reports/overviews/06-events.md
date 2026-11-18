# 次イベント予測・点過程：技術と実験を詳しく読む

改稿: 2026-11-18 / 対象文献スナップショット: 2026-11-16 / 論文公開日上限: 2026-11-12

「次に何が起きるか」「いつ起きるか」「どこで起きるか」「介入したら変わるか」を分けると、研究の位置が見える。点過程の確率モデル、業務ログの系列予測、LLMの意味知識は競合するだけでなく、異なる不足を補う。

## まず押さえる到達点

不規則なイベントの種類・待ち時間・場所をモデル化し、業務ログや移動履歴で予測できる。

次ラベルの正解率だけでは時刻の校正や長期生成、介入の価値、LLMの必要性は判断できない。 [1](https://arxiv.org/abs/1612.09328) [2](https://arxiv.org/abs/2606.15868) [3](https://arxiv.org/abs/2610.19021) [4](https://arxiv.org/abs/2611.14220)

## 技術の中身と論文同士の関係

### 次イベント予測の対象は、ラベル・時刻・個数・系列を分けて定義する

イベント列を、発生時刻tと種類kの組として考える。次の種類だけを当てるなら離散的な分類問題にできるが、発生までの時間も必要なら、種類と待ち時間の同時分布を扱う。一定間隔のセンサ値を予測する時系列と違い、イベントのない期間そのものが情報になる。固定期間内に何件起きるか、複数の未来イベントを生成するかまで含めると、同じ「予測」という名前でも目標が変わる。 [6](https://arxiv.org/abs/1806.00221) [1](https://arxiv.org/abs/1612.09328) [12](https://arxiv.org/abs/2101.02815)

例えば機械のログで、次の記録が「警告」か「停止」かを当てる課題と、次の1時間以内に停止する確率を出す課題は違う。次の種類が停止でも、それが数分後か数週間後かで行動の価値は変わる。また、次のイベントの前に複数の警告が起きる場合には、一段先の停止確率と一定期間の停止リスクも一致しない。予測対象を文章で定義した後、どの分布を学習するかを決める必要がある。 [6](https://arxiv.org/abs/1806.00221) [25](https://arxiv.org/abs/2103.11884)

業務ログでは、次の活動名、案件が終わるまでの残り時間、最終結果といった異なる目的がある。時間付き知識グラフでは将来の関係の候補、移動履歴では次の場所の順位を測る場合が多い。全ての研究に同じ正解率を求めるのではなく、時刻が入力だけなのか出力でもあるのか、予測時点で何を知っているのかを比較の前に揃える。 [17](https://arxiv.org/abs/1711.03822) [18](https://arxiv.org/abs/2012.15537) [4](https://arxiv.org/abs/2611.14220)

長期生成では、直前までの真の履歴を使う一段先評価と、自分が生成した履歴を使い続ける評価の差も大きい。後者では時刻や種類の小さなずれが次の条件を変える。次の一つの成績が良いことから、将来の個数や種類の組合せが整合した系列を生成できるとはいえず、生成期間と制約を別途指定する必要がある。 [12](https://arxiv.org/abs/2101.02815) [13](https://arxiv.org/abs/2311.01139) [14](https://arxiv.org/abs/2410.07430)

### 強度と待ち時間を結ぶ式が、何を評価すべきかを教える

種類kの条件付き強度λ_k(t)は、「時刻tの直前までの履歴の下で、次の短い時間にその種類が起きる率」であり、それ自体は確率ではない。種類を足したΛ(t)=Σ_k λ_k(t)が全イベントの率になる。直前のイベント時刻t0から新しいイベントがまだない条件で、時刻tまで何も起きない確率はS(t)=exp(−∫[t0,t] Λ(u)du)と表せる。 [6](https://arxiv.org/abs/1806.00221) [1](https://arxiv.org/abs/1612.09328)

次の種類と時刻の同時密度は、p(k,t|履歴)=λ_k(t)S(t)となる。したがって、種類kが次である確率はこれを未来の時刻で積分して得る。λ_kがある瞬間に大きいことだけから、次の種類や平均待ち時間が一意に分かるわけではない。強度、時刻の密度、種類の確率を区別すると、同じ出力を異なる名前で評価する混乱を避けられる。 [6](https://arxiv.org/abs/1806.00221) [11](https://arxiv.org/abs/1909.12127)

観測窓[0,T]の対数尤度は、観測イベントのlog λを足す項から、観測窓全体での総強度の積分を引く形になる。前者だけを増やせば至る所で大きい率を出すモデルになり得るが、積分項はイベントのなかった期間にも費用を課す。観測終了まで次のイベントがない情報も含まれるため、最後の待ち時間を単に削除した学習とは違う。これは右打ち切りの扱いにも関係する。 [6](https://arxiv.org/abs/1806.00221) [28](https://arxiv.org/abs/2104.07932)

ここで、時刻を秒から日へ変えると密度の数値と対数尤度の定数部分は変わる。データの単位や観測窓を揃えない尤度比較は意味を失う。また、同じタイムスタンプに複数のイベントがあるデータは、同時点の順序を仮定するか、区間内の発生として扱うかで別の観測モデルになる。数式が同じでもデータの作り方を確認する必要がある。 [6](https://arxiv.org/abs/1806.00221) [28](https://arxiv.org/abs/2104.07932) [16](https://arxiv.org/abs/2307.08097)

### Hawkes、ニューラル強度、待ち時間分布、生成モデルは何を変えるか

基本的な多変量Hawkes過程では、背景の発生率へ、過去の各種類のイベントから時間とともに変化する影響を足す。非負のカーネルを使う標準形は、発生後の励起やクラスタを表しやすい。どの種類がどれへ影響するかを読みやすい一方、強い非線形性や抑制を同じ形で表すには工夫が必要になる。 [5](https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1971.tb01530.x) [6](https://arxiv.org/abs/1806.00221) [7](https://arxiv.org/abs/1602.04511)

Neural Hawkesなどは履歴を隠れ状態へまとめ、時間の経過に伴う状態変化から率を作る。自己注意型やTransformer型は、どの過去イベントを参照するかを柔軟にする。柔軟な表現は有利になり得るが、積分の計算、長い履歴の費用、サンプル数、解釈の一意性と交換になる。attentionの重みが大きいことだけで、介入による因果関係が分かったとはいえない。 [1](https://arxiv.org/abs/1612.09328) [10](https://arxiv.org/abs/1907.07561) [9](https://arxiv.org/abs/2002.09291)

Intensity-Freeは、率を先に作る代わりに条件付きの待ち時間分布を直接表す。元研究はflow型と混合分布型を検討し、柔軟性に加えて、サンプリングやモーメントの計算を扱いやすくする。適切な密度と生存確率があれば率f/Sへ対応できるため、点過程を捨てたという意味ではない。何を直接パラメータ化すると学習と生成が楽かという設計の違いである。 [11](https://arxiv.org/abs/1909.12127) [6](https://arxiv.org/abs/1806.00221)

拡散やflow matchingを使う将来系列の生成は、一つずつの条件付き率だけではなく、系列全体を生成対象へ置く方向を開く。ただし、生成できることと正規化した尤度を同じ費用で計算できることは同じではない。比較する際は、次の種類、時間、個数、系列の分布、サンプリング速度のうち、何を改善したかを明示する必要がある。 [13](https://arxiv.org/abs/2311.01139) [14](https://arxiv.org/abs/2410.07430) [12](https://arxiv.org/abs/2101.02815)

### LLMの価値は、ラベルの並び以外に何を渡したかで変わる

活動名を単なるIDの列として扱うと、予測に必要なのは過去の頻度や遷移だけかもしれない。LLMが持つ世界知識を利用できる形で渡していなければ、大きいモデルの費用に見合う利得がない可能性がある。Argmax、LSTM、Transformer、LLMを比較した研究が示すのは、この入力と対象の下で単純な計数基準が強いという結果である。 [2](https://arxiv.org/abs/2606.15868)

DescribeEventは各イベントの自然言語記述を与え、意味の表現と予測する記号ラベルを分離する。名前の印象で選ぶ偏りを抑えつつ、内容の知識を使えるかを問う設計である。重要なのは「LLMを追加した」という一点ではなく、どの情報を読み、どの空間の出力を選ぶかというインターフェースを変えた点にある。 [3](https://arxiv.org/abs/2610.19021)

SHARPでは、次の場所をそのまま巨大な候補から選ぶ代わりに、場所のカテゴリ、時間条件付きの遷移、利用者の移動記憶、個別の場所の表現を組み合わせる。意味知識と、個人の頻度・時間の規則を分業させる設計だ。これにより、LLMを使う方式でも専用の符号化・グラフ・予測器の寄与が大きいことが分かる。 [4](https://arxiv.org/abs/2611.14220)

これらの結果は、異なる情報量と課題なので直接の勝敗表にはならない。単純基準、同じラベル列を使う専用モデル、記述付きの専用モデル、LLMの順で比較すれば、意味知識の追加、モデル規模、外部記憶の効果を分離しやすい。記述が予測時点より後で書かれていないか、検索で将来の正解を知っていないかも確認する必要がある。 [2](https://arxiv.org/abs/2606.15868) [3](https://arxiv.org/abs/2610.19021) [22](https://arxiv.org/abs/2501.05925) [4](https://arxiv.org/abs/2611.14220)

### 評価から介入へ進むには、校正と観測の設計が必要になる

次の種類の正解率、待ち時間の平均絶対誤差、尤度は違う失敗を捉える。平均時刻が合っていても極端に狭い分布なら、必要な不確実性を表していない。逆に平均のずれがあっても、意思決定に必要な期間内の確率が適切な場合がある。どの誤りに費用があるかを、予測対象と対応させて評価する必要がある。 [20](https://arxiv.org/abs/1305.3409) [25](https://arxiv.org/abs/2103.11884)

モデルが正しければ、条件付き分布による確率積分変換や、強度を積分した残差には所定の分布が現れる。これを使って時間の校正や依存の取り残しを調べられる。ただし全体のヒストグラムが似ているだけでは、履歴や種類ごとの誤差が消えたとはいえない。条件別の検査と、予測の比較に適したスコアを併せて使う。 [20](https://arxiv.org/abs/1305.3409) [6](https://arxiv.org/abs/1806.00221) [25](https://arxiv.org/abs/2103.11884)

業務ログを無作為に接頭辞へ分割すると、同じ案件のほぼ同じ履歴が学習と試験へ入る可能性がある。長い案件を多くの接頭辞へ展開すれば、その案件が評価で重くなる。案件ごと、将来の時点ごとに分割し、どの単位を平均しているかを明記することが、実運用へ近い比較につながる。将来期間で業務手順自体が変わる問題も別に残る。 [21](https://arxiv.org/abs/1712.04165) [29](https://arxiv.org/abs/2309.09618) [2](https://arxiv.org/abs/2606.15868)

最後に、起こりそうな次イベントを当てることと、起こしてよい次の行動を選ぶことは違う。保守を実行すれば故障の分布は変わるし、警告を送る費用もある。反実仮想の点過程は介入後の系列を考える枠組みだが、その仮定と観測の仕方が必要になる。予測精度から介入の利益へ進む部分が、エージェントや因果推論との接点になる。 [23](https://arxiv.org/abs/2111.07603) [24](https://arxiv.org/abs/2611.15009) [7](https://arxiv.org/abs/1602.04511)

## 手法を比較する

| 方法 | 何を変えるか | 得られる利点 | 前提と交換条件 |

| --- | --- | --- | --- |

| 頻度・遷移の基準 | 観測された種類や遷移の規則で次の活動を選ぶ。 | 安価で強い対照になり、複雑さの必要性を測れる。 | 意味、外生情報、連続時間を扱うには別の設計が必要。 [2](https://arxiv.org/abs/2606.15868) |

| Hawkes過程 | 背景率と過去イベントの影響を重ねる。 | 励起の構造を明示し、発生時刻を確率的に扱える。 | 標準形の非負・加法的な影響の仮定に注意する。 [5](https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1971.tb01530.x) [6](https://arxiv.org/abs/1806.00221) |

| ニューラル強度 | 隠れ状態やattentionで履歴から率を作る。 | 非線形な履歴依存や抑制を含む柔軟な表現へ進む。 | 積分、生成、長い履歴の費用と解釈が課題になる。 [1](https://arxiv.org/abs/1612.09328) [9](https://arxiv.org/abs/2002.09291) |

| 待ち時間分布の直接モデル | 次の到着までの密度を混合分布やflowで表す。 | サンプリングや分布の計算を扱いやすくする。 | 種類と時間の依存、観測窓の定義を別途確かめる。 [11](https://arxiv.org/abs/1909.12127) |

| 系列の拡散・flow生成 | 複数の将来イベントを生成対象にする。 | 次の一つを超えた個数や長期系列を扱う。 | 尤度、制約、長期整合性、生成費用を分けて比較する。 [13](https://arxiv.org/abs/2311.01139) [14](https://arxiv.org/abs/2410.07430) |

| LLMと意味・記憶の組合せ | 記述や意味IDを、履歴や専用の予測器へ接続する。 | ラベル列では利用できなかった意味情報を加えられる。 | 情報量、将来情報の混入、遅延を同じ条件で測る。 [3](https://arxiv.org/abs/2610.19021) [4](https://arxiv.org/abs/2611.14220) |

## 具体的研究を読み解く

### ArgmaxとDescribeEventは、同じ問いへの相反する答えではない

**研究の問い**: LLMの事前知識はイベント予測に必要なのか、という問いは、予測器へ意味情報を渡しているかで変わる。二つの研究を同じベンチマークの前後比較として読むことはできない。

**設計と対照**: 前者は7実業務ログでラベル列の直接予測を比べる。後者は6領域・7データセット・約15万イベントの記述を持ち、意味と予測ラベルの表現を分ける。対象と入力条件を先に確認する。

**論文が報告する結果**: 前者では事前学習に一貫した利益がなく、多くで計数基準が十億規模LLMに近い。後者では強いLLMが記述と記号ラベルから利益を得たが、弱いモデルの利益は小さいと報告された。

**位置づけ・編者の解釈**: 編者の解釈では、「大きい言語モデルか」より、追加の意味情報が予測へ寄与する条件を研究すべきことを示す組合せである。頻度だけで十分な課題と、内容理解が必要な課題を分ける仮説につながる。

**結論の範囲**: 二論文は入力もデータも異なり、両者の差が全て意味記述の効果だという因果的な比較ではない。同じデータで記述の有無や情報量を揃えた対照が必要になる。

[2](https://arxiv.org/abs/2606.15868) [3](https://arxiv.org/abs/2610.19021)

### SHARPは次の場所の順位を改善し、時刻の全てを解決したわけではない

**研究の問い**: 長い個人履歴を保持しつつ、時間帯ごとの場所カテゴリの遷移と、個別の地点の意味を予測へ利用する問題を扱う。

**設計と対照**: 動的な移動記憶、全体および時間条件付きのカテゴリ遷移グラフ、RQ-VAEによる意味ID、カテゴリを利用した地点予測器を組み合わせる。LLM単体へ地点名を尋ねる方式ではない。

**論文が報告する結果**: 3実世界移動データで、最良比較法に対するAcc@5の平均改善は5.29ポイント、Acc@10は4.52ポイントと報告した。

**位置づけ・編者の解釈**: 編者の解釈では、意味、長期の個人差、時間依存、候補の表現を分担する具体例として重要である。どの部品が必要かは部品を外す比較で読み、エージェントという名称だけを効果の説明にしない。

**結論の範囲**: 評価されるのは次の地点の上位候補に正解が入るかという順位の指標である。待ち時間の校正や、推薦によって本人の移動が変わった場合の効果は、この数値からは分からない。

[4](https://arxiv.org/abs/2611.14220) [20](https://arxiv.org/abs/1305.3409) [23](https://arxiv.org/abs/2111.07603)

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

## 引用文献と確認範囲

1. [The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process](https://arxiv.org/abs/1612.09328) — 2016-12-29 / arxiv:1612.09328 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1612.09328)

2. [David vs. Goliath in Next Activity Prediction: Argmax vs. LSTM, Transformer, and LLM](https://arxiv.org/abs/2606.15868) — 2026-06-14 / arxiv:2606.15868 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2606.15868) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://arxiv.org/abs/2606.15868v1)

3. [Can LLMs Access their World Knowledge for Event Prediction?](https://arxiv.org/abs/2610.19021) — 2026-10-13 / arxiv:2610.19021 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2610.19021) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://arxiv.org/abs/2610.19021v1)

4. [SHARP: Semantic Hierarchical Agentic Reasoning for Next POI Prediction with Dynamic Memory](https://arxiv.org/abs/2611.14220) — 2026-11-10 / arxiv:2611.14220 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14220) / 再確認: 2026-11-18、要旨、事例の方法・実験条件・報告値、[確認先](https://arxiv.org/abs/2611.14220v1)

5. [Point Spectra of Some Mutually Exciting Point Processes](https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1971.tb01530.x) — 公開日未確認 / doi:10.1111/j.2517-6161.1971.tb01530.x / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=doi%3A10.1111%2Fj.2517-6161.1971.tb01530.x)

6. [Lecture Notes: Temporal Point Processes and the Conditional Intensity Function](https://arxiv.org/abs/1806.00221) — 2018-06-01 / arxiv:1806.00221 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1806.00221) / 再確認: 2026-11-18、本文§2.3・§3.1、強度・生存確率・尤度、[確認先](https://arxiv.org/pdf/1806.00221)

7. [Learning Granger Causality for Hawkes Processes](https://arxiv.org/abs/1602.04511) — 2016-02-14 / arxiv:1602.04511 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1602.04511)

8. [Recurrent Marked Temporal Point Processes: Embedding Event History to Vector](https://www.kdd.org/kdd2016/subtopic/view/recurrent-temporal-point-process) — 公開日未確認 / doi:10.1145/2939672.2939875 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=doi%3A10.1145%2F2939672.2939875)

9. [Transformer Hawkes Process](https://arxiv.org/abs/2002.09291) — 2020-02-21 / arxiv:2002.09291 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2002.09291)

10. [Self-Attentive Hawkes Processes](https://arxiv.org/abs/1907.07561) — 2019-07-17 / arxiv:1907.07561 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1907.07561)

11. [Intensity-Free Learning of Temporal Point Processes](https://arxiv.org/abs/1909.12127) — 2019-09-26 / arxiv:1909.12127 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1909.12127) / 再確認: 2026-11-18、要旨、待ち時間分布の直接モデル、[確認先](https://arxiv.org/abs/1909.12127)

12. [Long Horizon Forecasting With Temporal Point Processes](https://arxiv.org/abs/2101.02815) — 2021-01-08 / arxiv:2101.02815 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2101.02815)

13. [Add and Thin: Diffusion for Temporal Point Processes](https://arxiv.org/abs/2311.01139) — 2023-11-02 / arxiv:2311.01139 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2311.01139)

14. [EventFlow: Forecasting Temporal Point Processes with Flow Matching](https://arxiv.org/abs/2410.07430) — 2024-10-09 / arxiv:2410.07430 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2410.07430)

15. [Neural Spatio-Temporal Point Processes](https://arxiv.org/abs/2011.04583) — 2020-11-09 / arxiv:2011.04583 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2011.04583)

16. [EasyTPP: Towards Open Benchmarking Temporal Point Processes](https://arxiv.org/abs/2307.08097) — 2023-07-16 / arxiv:2307.08097 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.08097)

17. [LSTM Networks for Data-Aware Remaining Time Prediction of Business Process Instances](https://arxiv.org/abs/1711.03822) — 2017-11-10 / arxiv:1711.03822 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1711.03822)

18. [xERTE: Explainable Reasoning on Temporal Knowledge Graphs for Forecasting Future Links](https://arxiv.org/abs/2012.15537) — 2020-12-31 / arxiv:2012.15537 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2012.15537)

19. [TPP-LLM: Modeling Temporal Point Processes by Efficiently Fine-Tuning Large Language Models](https://arxiv.org/abs/2410.02062) — 2024-10-02 / arxiv:2410.02062 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2410.02062)

20. [Calibration diagnostics for point process models via the probability integral transform](https://arxiv.org/abs/1305.3409) — 2013-05-15 / arxiv:1305.3409 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1305.3409)

21. [Temporal Stability in Predictive Process Monitoring](https://arxiv.org/abs/1712.04165) — 2017-12-12 / arxiv:1712.04165 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1712.04165)

22. [Navigating Tomorrow: Reliably Assessing Large Language Models Performance on Future Event Prediction](https://arxiv.org/abs/2501.05925) — 2025-01-10 / arxiv:2501.05925 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2501.05925)

23. [Counterfactual Temporal Point Processes](https://arxiv.org/abs/2111.07603) — 2021-11-15 / arxiv:2111.07603 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2111.07603)

24. [From Forecasting to World Modeling: Can Temporal Foundation Models Recover Causal Response?](https://arxiv.org/abs/2611.15009) — 2026-11-11 / arxiv:2611.15009 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.15009) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://arxiv.org/abs/2611.15009v1)

25. [Comparative evaluation of point process forecasts](https://arxiv.org/abs/2103.11884) — 2021-03-22 / arxiv:2103.11884 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2103.11884)

26. [A Differentiable Point Process with Its Application to Spiking Neural Networks](https://arxiv.org/abs/2106.00901) — 2021-06-02 / arxiv:2106.00901 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2106.00901)

27. [A solution to the learning dilemma for recurrent networks of spiking neurons](https://pubmed.ncbi.nlm.nih.gov/32681001/) — 2020-07-17 / pmid:32681001 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32681001)

28. [Interval-censored Hawkes processes](https://arxiv.org/abs/2104.07932) — 2021-04-16 / arxiv:2104.07932 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2104.07932)

29. [A Discussion on Generalization in Next-Activity Prediction](https://arxiv.org/abs/2309.09618) — 2023-09-18 / arxiv:2309.09618 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2309.09618)

## 収録範囲と読み方

対象は2026-11-16時点の収録スナップショット（基礎774件・新着264件）です。2026-11-18の改稿は、この範囲の技術・比較・事例の詳説です。

全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断レビューです。基礎・新着は収録先の区別で、古さは個々の公開日から確認できます。

技術の系譜、論文間の位置づけ、実験から導く解釈と次の課題は編者の整理です。直接の引用関係や商用普及率を確定するものではありません。

初版の22件に加え、改稿では25件の一次資料を確認しました（重複あり）。要旨・本文・検索掲載箇所の範囲を引用文献に記録しています。全件の全文精読や独立再現を意味しません。

数値は論文の報告値です。異なるデータ・分割・指標の比較を統一順位へ変換していません。説明用の計算例は実測値と区別しています。
