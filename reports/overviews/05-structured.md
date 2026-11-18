# 表形式・時系列・因果推論：技術と実験を詳しく読む

改稿: 2026-11-18 / 対象文献スナップショット: 2026-11-16 / 論文公開日上限: 2026-11-12

表や時系列では強い専用モデルと基盤モデルが併存し、予測・補完・生成を共有する設計が進んでいる。最も大きな境界は、観測の続きを当てる能力から、介入した世界の変化を説明する能力へは自動的に進めない点にある。

## まず押さえる到達点

表の分類・回帰、時系列予測、欠損補完、合成データを用途に応じて学習・転移できる。

一つのモデルで全表に勝つことや、予測精度から因果効果が分かることは示されていない。 [1](https://arxiv.org/abs/2609.17895) [2](https://arxiv.org/abs/2611.13001) [3](https://arxiv.org/abs/2611.15009)

## 技術の中身と論文同士の関係

### 表形式で木が強い理由と、深層学習の得意分野を区別する

表の一列は年齢、カテゴリ、金額、識別子など意味と尺度が異なり、画像の画素のような共通の近傍構造がないことが多い。木の分岐は、特定の特徴と閾値、特徴間の相互作用を直接表し、特徴の尺度にも比較的扱いやすい。画像で成功したネットワークをそのまま大きくすれば表でも勝つ、とは考えにくい理由がここにある。 [5](https://arxiv.org/abs/1603.02754) [6](https://arxiv.org/abs/1706.09516) [8](https://arxiv.org/abs/2207.08815)

XGBoostやCatBoostの強みは、一つの新奇な表現だけではない。損失を改善する木の追加、カテゴリの扱い、正則化、欠損の扱い、計算上の実装が組み合わさっている。深層学習側も、単純なMLP、特徴間attention、近傍検索を使う方式などで仮定が異なる。比較する際には、探索予算と前処理を揃えずにアーキテクチャだけを評価しない。 [5](https://arxiv.org/abs/1603.02754) [6](https://arxiv.org/abs/1706.09516) [7](https://arxiv.org/abs/2106.11959) [29](https://arxiv.org/abs/2307.14338)

深層学習の重要な機会は、単一の表で最適化するだけでなく、複数データの事前学習、文字列・画像などの別の表現、関連する複数タスクを共有できる点にある。ただし、表ごとに列の意味や順序が違うため、何を共有単位にするかが問題になる。TabPFNは合成された学習問題を大量に解くことで、表の予測手順そのものを学ぶ方向を選んだ。 [9](https://arxiv.org/abs/2207.01848) [10](https://arxiv.org/abs/2305.11097) [1](https://arxiv.org/abs/2609.17895)

したがって現在の選択は「木かTransformerか」という単純な世代交代ではない。データの行数、列の型、非線形性、施設や時間の分割、必要な説明、推論費用で得意分野が変わる。データセット平均の順位に加えて、どのデータで他のモデルが代替できない強みを持つかを見ると、単一勝者を決めるだけでは見えない設計上の価値が分かる。 [8](https://arxiv.org/abs/2207.08815) [24](https://arxiv.org/abs/2608.18919)

### TabPFNの事前学習は、表を暗記するのでなく予測器を学ぶ

TabPFNには、ラベル付きの学習行とラベルを求めたい行を入力する。通常のようにその表ごとに重みを何度も更新する代わりに、一回の入力から予測を出す。事前学習では、事前分布から合成した多数のデータセットとその予測問題を使う。実データを使うときに高速なのは、学習の負担の一部を、それ以前の共通の事前学習へ移したからである。 [9](https://arxiv.org/abs/2207.01848) [10](https://arxiv.org/abs/2305.11097)

これは、どんな表にも仮定なしで最適なベイズ推論を行うという意味ではない。合成課題を作る事前分布は、単純な構造などへの好みを含み、現実の表との合い方が性能へ影響する。元論文が小さい数値表で示した結果を、巨大な関係データや強い時点変化へそのまま移せないのは、この仮定と計算規模の両方が変わるためである。 [9](https://arxiv.org/abs/2207.01848) [10](https://arxiv.org/abs/2305.11097)

後続の発展では、より多い行や特徴を扱うための文脈選択・分割、入力の型の拡張、タスクごとの実行基盤などが加わる。TabPFN-3.5は時間・グループ分割や文字列・画像などを含む表への拡張を報告する。これは単に元の同じ実験のスコアを上げた話ではなく、対象とするデータの条件を広げる方向の進歩として読む必要がある。 [11](https://arxiv.org/abs/2402.11137) [30](https://arxiv.org/abs/2311.10609) [1](https://arxiv.org/abs/2609.17895)

比較で見落としやすいのは費用の範囲である。事前学習済みモデルの一回の予測と、表ごとに行う全探索を比べた倍率は、利用回数や共通学習費をどう数えるかで意味が違う。利用者の待ち時間の短縮は実際に有用だが、それを全ライフサイクルの計算費用と同じものとして読まない。評価データへの適応や複数試行を伴う構成も、同じ条件に揃える必要がある。 [9](https://arxiv.org/abs/2207.01848) [11](https://arxiv.org/abs/2402.11137) [1](https://arxiv.org/abs/2609.17895)

### 時系列は、予測対象・表現・不確実性の三軸で整理できる

DeepARは複数の関連系列から自己回帰的な確率予測を学び、将来の一つの値だけでなく分布を扱う。N-BEATSは基底の展開による予測、PatchTSTは系列を区間のまとまりへ分ける表現を使う。点予測の誤差、予測区間の被覆、複数期間の同時分布は異なる目標であり、同じ「予測モデル」の数字でも直接比較できない場合がある。 [12](https://arxiv.org/abs/1704.04110) [13](https://arxiv.org/abs/1905.10437) [14](https://arxiv.org/abs/2211.14730)

PatchTSTのパッチ化は、隣接する時点の局所情報をまとめ、長い履歴を少ないトークンで扱う設計につながる。一方、特徴の系列を独立に扱って重みを共有する構成では、系列間の関係をどこへ持たせるかが別の問題になる。長い履歴が必要なのか、変数間の関係が必要なのか、外生変数が必要なのかを区別すると、attentionの使い方の違いを理解しやすい。 [14](https://arxiv.org/abs/2211.14730) [31](https://arxiv.org/abs/2310.06625)

Chronosは数値系列を尺度調整と量子化によってトークン列として扱い、複数系列で学習した予測器を転用する。MOMENTのような共通表現も、予測だけでなく分類・補完などへの展開を考える。数値をトークンにしたことだけで自然言語の意味知識を利用しているわけではなく、数値の表現、学習資料、下流の読出し方がそれぞれの貢献になる。 [15](https://arxiv.org/abs/2403.07815) [16](https://arxiv.org/abs/2402.03885)

評価では、同じ系列から切った近接窓が学習側と評価側へ混ざると、未知の未来や別の系列への適応を測りにくい。予測期間、系列ごとの尺度、季節性、欠測の仕方を揃え、単純な持続・季節基準や線形モデルも含める必要がある。Transformerが有効かという問いは、モデルの一般的な優劣ではなく、その系列と期間にどの構造が必要かという問いに置き換えると実りがある。 [17](https://arxiv.org/abs/2205.13504) [14](https://arxiv.org/abs/2211.14730) [15](https://arxiv.org/abs/2403.07815)

### 生成・補完・予測が共有する情報と、共有できない評価軸

表の全体を生成すること、空欄を他の列から補うこと、特徴から目的の列を予測することは、同じ同時分布の異なる条件付けとして考えられる。そのため共通の表現を学べば相互に助けられる可能性がある。一方、学習で重く扱う誤差が違えば、下流予測に必要な関係をよく保つモデルと、希少な組合せまで忠実に生成するモデルは一致しない。 [18](https://arxiv.org/abs/1907.00503) [19](https://arxiv.org/abs/2209.15421) [2](https://arxiv.org/abs/2611.13001)

例えば合成表で学習した分類器の精度が高くても、元の表のカテゴリの頻度や少数群の構成が合っているとは限らない。逆に、周辺分布がよく似ていても、予測に必要な列間の依存を壊すことがある。効用、分布の忠実性、補完の誤差を分けることが、一つの総合順位だけでは見えない違いを明らかにする。プライバシーも合成されたという事実だけからは保証されない。 [2](https://arxiv.org/abs/2611.13001) [32](https://arxiv.org/abs/2306.15636) [33](https://arxiv.org/abs/2402.06806)

One Tableの目的関数の組合せ実験は、この共有が本当に起きるかを調べる。予測の目的を足すと生成が改善するか、生成を足すと補完が改善するか、という問いを同じバックボーンへ向ける。二つの目的で良くなったことから、三つを足してさらに良くなるとは限らない。目的間の干渉があるため、足し合わせの効果を実際に比較する必要がある。 [2](https://arxiv.org/abs/2611.13001)

ここでの実用的な読み方は、万能な一モデルを探すより、必要な問い合わせの組合せに対して費用と精度の前線を見ることである。予測だけを使う場合と、欠損の不確実性を含む分析や合成データを使う場合では最適な構成が変わり得る。汎用モデルと専門モデルの比較は、用途の契約を明確にして初めて意味を持つ。 [2](https://arxiv.org/abs/2611.13001) [24](https://arxiv.org/abs/2608.18919)

### 因果推論は高精度の予測器へ目的変数を追加するだけでは成立しない

予測は観察された条件で将来の値を当てるのに対し、介入効果は処置を変えた場合の差を問う。処置の選ばれ方が結果と共通の要因を持つと、単純な条件付けで得た差は介入の差と一致しない。価格と売上なら、需要が弱そうなときに価格を下げるという判断が交絡になり得る。表や時系列のモデルが正確でも、この識別の問題は残る。 [21](https://arxiv.org/abs/1608.00060) [3](https://arxiv.org/abs/2611.15009)

DMLは、高次元の背景変数に関する補助的な予測問題を機械学習で解きつつ、対象の効果を推定する式をその予測誤差に鈍感な形へ整える。交差適合では、補助モデルを学習したデータと、それを使って効果を評価するデータを分ける。これは過適合と正則化バイアスに対処する仕組みであり、観測していない交絡を自動的に消す手法ではない。 [21](https://arxiv.org/abs/1608.00060)

因果フォレストは効果の異質性、NOTEARSは巡回しないグラフ構造の探索を扱うが、推定対象も前提も違う。NOTEARSの連続最適化はグラフ探索を扱いやすくする重要な工夫である一方、得られた矢印が観察情報から一意に同定されるかは別問題である。構造の候補、平均効果、個別の効果を、同じ「因果が分かった」という達成として数えない。 [22](https://arxiv.org/abs/1610.01271) [23](https://arxiv.org/abs/1803.01422)

操作変数などの補助情報にも、処置への関連や結果への直接経路がないことなどの前提がある。単に新しい列として予測モデルへ渡すだけで、その前提を利用した推定が実装されるわけではない。価格効果を扱う最近の研究は、予測器の能力と、因果の識別条件を使う能力の隔たりを測る。ここは時系列基盤モデルを世界モデルと呼ぶときの重要な境界になる。 [34](https://arxiv.org/abs/1612.09596) [21](https://arxiv.org/abs/1608.00060) [3](https://arxiv.org/abs/2611.15009)

## 手法を比較する

| 方法 | 何を変えるか | 得られる利点 | 前提と交換条件 |

| --- | --- | --- | --- |

| 木の集約 | 特徴の分岐と多数の木で予測関数を作る。 | 不均質な列を含む表の強い基準になる。 | 探索予算と分割を揃え、事前学習とは別に比較する。 [5](https://arxiv.org/abs/1603.02754) [6](https://arxiv.org/abs/1706.09516) |

| TabPFN | 合成課題で事前学習し、学習行を文脈として予測する。 | 表ごとの重み更新を省き、少数データへ素早く適応する。 | 事前分布と実データの差、文脈の規模と費用が残る。 [9](https://arxiv.org/abs/2207.01848) [10](https://arxiv.org/abs/2305.11097) |

| 時系列の事前学習 | 複数系列から表現や予測規則を転用する。 | データの少ない系列や複数の下流課題を支援できる。 | 未来の分割、尺度、季節、外生変数の条件を確認する。 [15](https://arxiv.org/abs/2403.07815) [16](https://arxiv.org/abs/2402.03885) |

| 生成・補完の共通モデル | 同じ表の異なる条件付き分布を学ぶ。 | 問い合わせを共有して正の転移を得る可能性がある。 | 効用と分布忠実性の順位は一致するとは限らない。 [2](https://arxiv.org/abs/2611.13001) |

| 因果効果・構造推定 | 識別仮定と推定手順を使い、介入の差や構造を問う。 | 予測だけでは答えられない意思決定の問いを扱う。 | 未観測交絡や識別不能性は予測精度で解消しない。 [21](https://arxiv.org/abs/1608.00060) [23](https://arxiv.org/abs/1803.01422) [3](https://arxiv.org/abs/2611.15009) |

## 具体的研究を読み解く

### One Table：大規模な比較と目的の介入実験を区別する

**研究の問い**: 生成・補完・予測はどこまで一つのモデルへ共有できるかを問う。総合ランキングを作るだけでなく、学習目的を足すことで何が変わるかを見る必要がある。

**設計と対照**: 比較の基盤は56データセット・46登録手法・20評価軸。一方、5バックボーンへ7種類の空でない目的の組合せを与える実験は、5データセット・3 seedで行う。二つの規模を混同しない。

**論文が報告する結果**: 予測効用と数値の補完には強い側面がある一方、分布の忠実性では専門化が有利な場合がある。目的を足した効果は、既に何を学習しているかやバックボーンによって異なる。

**位置づけ・編者の解釈**: 編者の解釈では、共通のデータを扱うことと共通の最適解を持つことを分離した研究である。個別指標の順位と、目的を変える比較を合わせて読むと、何の情報を共有できたかという機構上の仮説へ近づける。

**結論の範囲**: 全56表で同じ目的の介入実験を完了したわけではない。また、良い合成データの予測効用を、希少な関係の忠実性や秘密保護と同じ評価として扱わない。

[2](https://arxiv.org/abs/2611.13001) [32](https://arxiv.org/abs/2306.15636)

### 予測器に価格を変えて聞けば、価格効果が分かるのか

**研究の問い**: 将来の売上を当てるモデルへ価格を変えた入力を与えたとき、その出力差が実際の介入効果になるかを問う。観察分布の外側へ移す問題が含まれる。

**設計と対照**: 真の効果を確認できるシミュレーションと実小売記録で、表・時系列の基盤モデルなどを評価し、追加文脈と操作変数の与え方も比較する。

**論文が報告する結果**: 予測精度は価格効果の精度を示さず、追加文脈は予測を改善しても効果を改善しなかった。操作変数は特定の形でのみ助け、生の列では交絡下で全モデルの誤差を増やしたと報告する。

**位置づけ・編者の解釈**: 編者の解釈では、モデルが大規模になっても、因果の識別条件を利用する推定手順が必要なことを示す具体例である。予測の入力感度をそのまま政策や処置の効果と呼ぶ前に、何を一定として変えたかを検証する必要がある。

**結論の範囲**: 対象は価格介入の設定であり、あらゆる基盤モデルが因果を扱えないという結論ではない。DMLのような識別と推定の枠組みに、強い予測器を部品として使う方向とは両立する。

[3](https://arxiv.org/abs/2611.15009) [21](https://arxiv.org/abs/1608.00060)

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

## 関連する直近研究

### TabPFN-3.5：実データの複雑さへ対象を広げる

時間・グループ分割、文字列・画像を含む表、高カーディナリティなどへ対象を拡張。TabArenaでの優位と高速版の旧版比最大3倍高速化を著者が報告している。各業務データでの外部比較は引き続き必要である。 [1](https://arxiv.org/abs/2609.17895)

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

## 引用文献と確認範囲

1. [TabPFN-3.5: Technical Report](https://arxiv.org/abs/2609.17895) — 2026-09-15 / arxiv:2609.17895 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2609.17895) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://arxiv.org/abs/2609.17895v3)

2. [One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation, Imputation, and Prediction](https://arxiv.org/abs/2611.13001) — 2026-11-08 / arxiv:2611.13001 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.13001) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://arxiv.org/abs/2611.13001v1)

3. [From Forecasting to World Modeling: Can Temporal Foundation Models Recover Causal Response?](https://arxiv.org/abs/2611.15009) — 2026-11-11 / arxiv:2611.15009 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.15009) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://arxiv.org/abs/2611.15009v1)

4. [Random Forests](https://link.springer.com/article/10.1023/A:1010933404324) — 公開日未確認 / doi:10.1023/A:1010933404324 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=doi%3A10.1023%2FA%3A1010933404324)

5. [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754) — 2016-03-09 / arxiv:1603.02754 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1603.02754)

6. [CatBoost: unbiased boosting with categorical features](https://arxiv.org/abs/1706.09516) — 2017-06-28 / arxiv:1706.09516 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1706.09516)

7. [Revisiting Deep Learning Models for Tabular Data](https://arxiv.org/abs/2106.11959) — 2021-06-22 / arxiv:2106.11959 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2106.11959)

8. [Why do tree-based models still outperform deep learning on tabular data?](https://arxiv.org/abs/2207.08815) — 2022-07-18 / arxiv:2207.08815 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2207.08815)

9. [TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second](https://arxiv.org/abs/2207.01848) — 2022-07-05 / arxiv:2207.01848 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2207.01848) / 再確認: 2026-11-18、要旨、合成事前分布・元の評価条件、[確認先](https://arxiv.org/abs/2207.01848)

10. [Statistical Foundations of Prior-Data Fitted Networks](https://arxiv.org/abs/2305.11097) — 2023-05-18 / arxiv:2305.11097 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.11097)

11. [TuneTables: Context Optimization for Scalable Prior-Data Fitted Networks](https://arxiv.org/abs/2402.11137) — 2024-02-17 / arxiv:2402.11137 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2402.11137)

12. [DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks](https://arxiv.org/abs/1704.04110) — 2017-04-13 / arxiv:1704.04110 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1704.04110)

13. [N-BEATS: Neural basis expansion analysis for interpretable time series forecasting](https://arxiv.org/abs/1905.10437) — 2019-05-24 / arxiv:1905.10437 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1905.10437)

14. [A Time Series is Worth 64 Words: Long-term Forecasting with Transformers](https://arxiv.org/abs/2211.14730) — 2022-11-27 / arxiv:2211.14730 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2211.14730)

15. [Chronos: Learning the Language of Time Series](https://arxiv.org/abs/2403.07815) — 2024-03-12 / arxiv:2403.07815 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2403.07815)

16. [MOMENT: A Family of Open Time-series Foundation Models](https://arxiv.org/abs/2402.03885) — 2024-02-06 / arxiv:2402.03885 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2402.03885)

17. [Are Transformers Effective for Time Series Forecasting?](https://arxiv.org/abs/2205.13504) — 2022-05-26 / arxiv:2205.13504 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2205.13504)

18. [Modeling Tabular data using Conditional GAN](https://arxiv.org/abs/1907.00503) — 2019-07-01 / arxiv:1907.00503 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1907.00503)

19. [TabDDPM: Modelling Tabular Data with Diffusion Models](https://arxiv.org/abs/2209.15421) — 2022-09-30 / arxiv:2209.15421 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2209.15421)

20. [CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation](https://arxiv.org/abs/2107.03502) — 2021-07-07 / arxiv:2107.03502 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2107.03502)

21. [Double/Debiased Machine Learning for Treatment and Structural Parameters](https://arxiv.org/abs/1608.00060) — 2016-07-30 / arxiv:1608.00060 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1608.00060) / 再確認: 2026-11-18、要旨、直交スコアと交差適合、[確認先](https://arxiv.org/abs/1608.00060v7) / 照合先v7は表題がTreatment and Causal Parameters。ライブラリの登録原題と異なるが同一arXiv ID。

22. [Generalized Random Forests](https://arxiv.org/abs/1610.01271) — 2016-10-05 / arxiv:1610.01271 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1610.01271)

23. [DAGs with NO TEARS: Continuous Optimization for Structure Learning](https://arxiv.org/abs/1803.01422) — 2018-03-04 / arxiv:1803.01422 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1803.01422)

24. [Lost in Aggregation: How Benchmarks Overlook Irreplaceable Model Strengths](https://arxiv.org/abs/2608.18919) — 2026-08-19 / arxiv:2608.18919 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2608.18919)

25. [Benchmarking Distribution Shift in Tabular Data with TableShift](https://arxiv.org/abs/2312.07577) — 2023-12-10 / arxiv:2312.07577 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2312.07577)

26. [The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process](https://arxiv.org/abs/1612.09328) — 2016-12-29 / arxiv:1612.09328 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1612.09328)

27. [External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients](https://pubmed.ncbi.nlm.nih.gov/34152373/) — 2021-06-21 / pmid:34152373 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34152373)

28. [Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift](https://arxiv.org/abs/1906.02530) — 2019-06-06 / arxiv:1906.02530 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1906.02530)

29. [TabR: Tabular Deep Learning Meets Nearest Neighbors in 2023](https://arxiv.org/abs/2307.14338) — 2023-07-26 / arxiv:2307.14338 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.14338)

30. [Scaling TabPFN: Sketching and Feature Selection for Tabular Prior-Data Fitted Networks](https://arxiv.org/abs/2311.10609) — 2023-11-17 / arxiv:2311.10609 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2311.10609)

31. [iTransformer: Inverted Transformers Are Effective for Time Series Forecasting](https://arxiv.org/abs/2310.06625) — 2023-10-10 / arxiv:2310.06625 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2310.06625)

32. [On the Usefulness of Synthetic Tabular Data Generation](https://arxiv.org/abs/2306.15636) — 2023-06-27 / arxiv:2306.15636 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2306.15636)

33. [Systematic Assessment of Tabular Data Synthesis](https://arxiv.org/abs/2402.06806) — 2024-02-09 / arxiv:2402.06806 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2402.06806)

34. [Counterfactual Prediction with Deep Instrumental Variables Networks](https://arxiv.org/abs/1612.09596) — 2016-12-30 / arxiv:1612.09596 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1612.09596)

## 収録範囲と読み方

対象は2026-11-16時点の収録スナップショット（基礎774件・新着264件）です。2026-11-18の改稿は、この範囲の技術・比較・事例の詳説です。

全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断レビューです。基礎・新着は収録先の区別で、古さは個々の公開日から確認できます。

技術の系譜、論文間の位置づけ、実験から導く解釈と次の課題は編者の整理です。直接の引用関係や商用普及率を確定するものではありません。

初版の22件に加え、改稿では25件の一次資料を確認しました（重複あり）。要旨・本文・検索掲載箇所の範囲を引用文献に記録しています。全件の全文精読や独立再現を意味しません。

数値は論文の報告値です。異なるデータ・分割・指標の比較を統一順位へ変換していません。説明用の計算例は実測値と区別しています。
