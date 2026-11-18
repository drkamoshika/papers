# 神経科学とAI：技術と実験を詳しく読む

改稿: 2026-11-18 / 対象文献スナップショット: 2026-11-16 / 論文公開日上限: 2026-11-12

配線図、集団活動、学習・記憶、AIとの表現比較を重ねることで、脳を検証可能なモデルとして調べられる範囲が広がった。ハエの大規模な回路地図と、人の脳を全て再現できることの間には、対象・解像度・機能同定の大きな隔たりがある。

## まず押さえる到達点

ハエの回路追跡、マウス局所の構造と活動の対応、人の粗視化ネットワーク解析や条件付きの信号復号。

収録研究は、人間全脳の細胞レベル再現や、配線図だけでの感情・意識の説明までは示していない。 [1](https://pubmed.ncbi.nlm.nih.gov/39358518/) [2](https://pubmed.ncbi.nlm.nih.gov/40205214/) [3](https://pubmed.ncbi.nlm.nih.gov/38723085/) [4](https://pubmed.ncbi.nlm.nih.gov/37127759/)

## 技術の中身と論文同士の関係

### 配線図、活動の相関、計算上の因果は異なる地図である

電子顕微鏡のコネクトームは、細胞の突起とシナプスを再構成した構造の地図である。一方、fMRIなどの機能結合は、測った信号がどの程度一緒に変動するかを表す。前者に接続があっても常に信号を伝えるとは限らず、後者に相関があっても直接の接続とは限らない。共通入力や、別の領域を経由した経路でも相関が生じ得る。 [1](https://pubmed.ncbi.nlm.nih.gov/39358518/) [15](https://pubmed.ncbi.nlm.nih.gov/19188601/) [14](https://pubmed.ncbi.nlm.nih.gov/21653723/)

構造の地図でも、見つかったシナプスの数は、そのまま実際の機能的な重みではない。伝達物質、受容体、状態、短期・長期の可塑性、伝導の遅れによって働きは変わる。配線は可能な経路を強く制約するが、同じ経路でどの動態が生じるかを全て決定しない。このため、配線から作るモデルには、地図以外の仮定が必ず入る。 [16](https://pubmed.ncbi.nlm.nih.gov/39358519/) [17](https://pubmed.ncbi.nlm.nih.gov/39261740/)

人のMRIでは、脳の領域をノードとして結ぶ全体のネットワークを分析できるが、ノードの分割方法や前処理も結果に影響する。頭部運動などが相関を変えるため、ハブやネットワークの違いを病態や個人の能力に直結させる前に、測定の交絡を検討する必要がある。全体を見渡せることと、シナプス単位で正確であることは別の利点である。 [13](https://pubmed.ncbi.nlm.nih.gov/23684880/) [28](https://pubmed.ncbi.nlm.nih.gov/21810475/) [29](https://pubmed.ncbi.nlm.nih.gov/28302591/) [22](https://pubmed.ncbi.nlm.nih.gov/29116093/)

有効な因果的影響を考えるには、モデルに基づく方向の推定や、特定の細胞・回路を操作したときの変化を確かめる必要がある。構造、同時記録、刺激、行動を対応させる研究が重要なのは、それぞれ別の曖昧さを減らせるからだ。単にネットワークのノード数が増えたという一軸で比較するより、何の種類の証拠が対応したかを見る方が到達点を理解しやすい。 [2](https://pubmed.ncbi.nlm.nih.gov/40205214/) [16](https://pubmed.ncbi.nlm.nih.gov/39358519/)

### ハエ全脳モデルは、地図に単純な動態を載せて検証可能な予測を作る

Shiuらのモデルは、脳全体の接続と伝達物質の予測を、leaky integrate-and-fire型の神経モデルへ接続する。各細胞は入力を膜電位に蓄積し、時間とともに漏れ、閾値を越えると発火する単純な素子として扱われる。入力する感覚ニューロンを活性化し、他のニューロンの発火の変化を見ることで、回路の候補を予測する。 [16](https://pubmed.ncbi.nlm.nih.gov/39358519/)

グラフ上で経路が短いか、接続数が多いかを調べるだけなら、活動がどこで増減するかまでは表せない。逆に、ある行動課題を解くよう大きなニューラルネットを訓練すると、配線以外の多くの自由度で結果を説明できる。単純な動態を載せる方針は、この間で、少ない追加仮定から具体的な発火と感覚運動の予測を作る狙いを持つ。 [16](https://pubmed.ncbi.nlm.nih.gov/39358519/) [17](https://pubmed.ncbi.nlm.nih.gov/39261740/)

単純化は成功の理由でも限界でもある。一律の発火素子を使い、形態、受容体の動態、電気シナプス、神経ペプチド、内部状態などを省く。基底発火を0とすると、元から活動していない細胞への抑制は効果を持たない。そのため、抑制の解除や神経調節に依存する回路を、配線だけから同じ精度で再現できるとは限らない。 [16](https://pubmed.ncbi.nlm.nih.gov/39358519/)

著者らは、絶対的な発火頻度よりも、入力条件を変えたときの広い差として出力を解釈する。例えば刺激を強めると下流の活動が増えるか減るかを試す。したがって、全てのニューロンの時間波形を精密に再現したモデルと読むのは誤りである。一方、特定回路について次にどの細胞を操作して確かめるかを提案できる点は、静的な地図を超える具体的な進歩である。 [16](https://pubmed.ncbi.nlm.nih.gov/39358519/) [21](https://pubmed.ncbi.nlm.nih.gov/42259917/)

### 集団活動の低次元性は、脳の計算を考える座標を与える

多数のニューロンを同時に記録すると、各細胞を別々の特徴検出器として説明するだけでは、活動の関係を捉えにくい。神経集団の活動を低次元の状態へ写し、その軌道と行動の関係を見ると、運動の準備や実行などの変化を力学系として整理できる。これは次元を減らすだけでなく、何が時間発展する状態なのかという計算上の仮説を作る方法である。 [9](https://pubmed.ncbi.nlm.nih.gov/22722855/) [10](https://pubmed.ncbi.nlm.nih.gov/19357332/) [34](https://pubmed.ncbi.nlm.nih.gov/32640928/)

ただし、低次元の軌道を発見したことから、その軌道が行動を生む唯一の機構だとはいえない。測っていない顔や体の動き、覚醒、感覚入力も広い活動を説明する場合がある。課題のラベルだけを使って表現へ名前を付けると、実際には運動に由来する変化を抽象的な判断だと誤解することもある。行動の同時測定と条件を変えた検証が重要になる。 [12](https://pubmed.ncbi.nlm.nih.gov/31551604/) [11](https://pubmed.ncbi.nlm.nih.gov/34801787/)

AIとの比較では、課題を解くネットワークの中間表現が、脳活動や刺激間の類似関係をどの程度予測するかを調べられる。予測性能は、モデルが何を共有して捉えたかの証拠になるが、異なるモデルも同じ有限のデータへ合う可能性がある。良い符号化モデルであること、良い復号器であること、生物学的な機構を同定したことを分けて主張する必要がある。 [18](https://pubmed.ncbi.nlm.nih.gov/24812127/) [19](https://pubmed.ncbi.nlm.nih.gov/35173264/) [11](https://pubmed.ncbi.nlm.nih.gov/34801787/)

非侵襲の言語復号もこの区別で読むと分かりやすい。脳活動からその人が聞いた内容に合う候補を選べても、生成言語モデルの事前知識が流暢さを補っている。脳の情報がどこへ寄与したかを対照条件で確かめなければ、もっともらしい文章を作っただけなのかを区別できない。逐語一致と意味の再構成を分けることも同じ理由で必要になる。 [4](https://pubmed.ncbi.nlm.nih.gov/37127759/)

### 人・マウス・ハエの地図は、解像度と対応する情報で比較する

成虫ハエの脳や脳と神経索をつなぐ資源は、細胞単位で感覚から出力への経路を追う機会を広げた。性差を含む細胞型の比較は、共通する回路と変わる回路を探す手段にもなる。ただし、雌雄や標本の異なる地図は、一つの個体の全ての状態を測ったものではない。型の対応付けや再構成精度も考慮する必要がある。 [1](https://pubmed.ncbi.nlm.nih.gov/39358518/) [20](https://pubmed.ncbi.nlm.nih.gov/42691995/) [21](https://pubmed.ncbi.nlm.nih.gov/42259917/)

MICrONSはマウス視覚皮質の複数領域で、約75,000ニューロンの機能記録と、20万超の細胞・約5億シナプスを含む局所的な電子顕微鏡の地図を対応させる。活動と接続を同じ対象で結べることが重要である。ここで細胞数と機能記録されたニューロン数は異なり、マウス全脳を覆ったという意味でもない。 [2](https://pubmed.ncbi.nlm.nih.gov/40205214/)

人の約1立方mmの皮質を再構成した資源は、約57,000細胞と約1.5億シナプスを含むが、細胞にはグリアも含まれる。一人の局所組織で得た精密さを、人間全脳の機能再現へ一般化しない。一方、人のMRIの広域ネットワークには、生きた状態と行動の関係や個体差を調べられる別の価値がある。両者は精密さの異なる同じ地図ではなく、測定対象も違う。 [3](https://pubmed.ncbi.nlm.nih.gov/38723085/) [13](https://pubmed.ncbi.nlm.nih.gov/23684880/) [35](https://pubmed.ncbi.nlm.nih.gov/28182017/)

このため、AIに使える知見も二種類に分かれる。配線を制約にした回路の動作仮説、低次元の状態や記憶・学習の分業といった計算原理を考えることと、脳信号から分類器を作ることは別の研究である。前者が良いAI設計を生むか、後者が診療へ役立つかは、それぞれ工学的・臨床的な評価を必要とする。 [16](https://pubmed.ncbi.nlm.nih.gov/39358519/) [7](https://pubmed.ncbi.nlm.nih.gov/7624455/) [23](https://arxiv.org/abs/2611.17031) [33](https://pubmed.ncbi.nlm.nih.gov/35585198/)

### 予測・記憶・局所学習の理論を、AIとの対応で読み違えない

相補的学習システムの考え方では、個々の経験を速く保持する仕組みと、共通する構造をゆっくり学ぶ仕組みの分業を考える。再活性化や経験の再利用は、速い学習と干渉を減らす問題へつながる。エージェントの外部記憶と重みの更新を考える手掛かりになるが、ファイルに教訓を保存しただけで海馬の学習を再現したとはいえない。 [7](https://pubmed.ncbi.nlm.nih.gov/7624455/) [36](https://pubmed.ncbi.nlm.nih.gov/8036517/) [37](https://pubmed.ncbi.nlm.nih.gov/28292907/) [30](https://arxiv.org/abs/2611.14320)

報酬予測誤差は、得られた報酬と将来価値の見込みのずれを学習へ使う考え方である。ドーパミン系との対応や、価値分布の表現を扱う研究は、強化学習との具体的な接点を持つ。ただし、次のトークンの誤差を減らす言語学習や、次イベントの尤度を上げる学習と、同じ目的関数であるわけではない。「予測する」という共通語だけで同一視しない。 [5](https://pubmed.ncbi.nlm.nih.gov/9054347/) [26](https://pubmed.ncbi.nlm.nih.gov/31942076/) [38](https://arxiv.org/abs/1612.09328)

スパイク時刻依存可塑性は、前後の発火のタイミングと結合の変化を結ぶ局所的な学習則を考える。第三の調節信号や時間的な痕跡を加える理論は、過去の活動と後で到着する学習信号を結び付ける問題を扱う。再帰ネットワークの学習へ使う研究もあるが、生体が通常の誤差逆伝播をそのまま実行しているという証明とは別である。 [6](https://pubmed.ncbi.nlm.nih.gov/18275283/) [39](https://pubmed.ncbi.nlm.nih.gov/26834568/) [27](https://pubmed.ncbi.nlm.nih.gov/32681001/) [8](https://pubmed.ncbi.nlm.nih.gov/32303713/)

AIへの示唆を評価するには、計算として何を実装し、どんな学習課題で何が改善したかを明確にする必要がある。脳らしい構造だから良いのではなく、記憶の干渉、少数例での適応、時間的な信用割当、計算やエネルギーの制約へ具体的な解を与えたかを問う。この視点を保つことで、脳の理解とAIの性能改善を、相互に参考にしつつ別の達成として追える。 [7](https://pubmed.ncbi.nlm.nih.gov/7624455/) [8](https://pubmed.ncbi.nlm.nih.gov/32303713/) [27](https://pubmed.ncbi.nlm.nih.gov/32681001/) [19](https://pubmed.ncbi.nlm.nih.gov/35173264/)

## 手法を比較する

| 方法 | 何を変えるか | 得られる利点 | 前提と交換条件 |

| --- | --- | --- | --- |

| 電子顕微鏡の構造コネクトーム | 細胞とシナプスの接続を再構成する。 | 細胞単位の経路や接続の仮説を検討できる。 | 重み、状態、電気シナプス、全ての動態は含まれない。 [1](https://pubmed.ncbi.nlm.nih.gov/39358518/) [16](https://pubmed.ncbi.nlm.nih.gov/39358519/) |

| MRIの広域ネットワーク | 領域間の構造的・機能的な関係を測る。 | 人の広域の組織化や個体差を生体で調べられる。 | 相関と直接の結合・因果を区別し、運動などを補正する。 [13](https://pubmed.ncbi.nlm.nih.gov/23684880/) [28](https://pubmed.ncbi.nlm.nih.gov/21810475/) |

| 機能的コネクトミクス | 活動記録と構造地図を同じ対象へ対応させる。 | どの接続がどの応答と関わるかを絞れる。 | 標本の範囲、対応の誤差、測った刺激や状態が限られる。 [2](https://pubmed.ncbi.nlm.nih.gov/40205214/) |

| 潜在状態・集団動態 | 大量の活動を低次元の状態と時間発展で表す。 | 行動と内部の計算について検証可能な仮説を作る。 | 未測定行動の交絡とモデルの非一意性が残る。 [9](https://pubmed.ncbi.nlm.nih.gov/22722855/) [12](https://pubmed.ncbi.nlm.nih.gov/31551604/) |

| 脳信号のAI読出し | EEGやfMRIからラベルや意味表現を推定する。 | 定めた課題で信号の情報を利用できる。 | 機構同定や個体を超えた利用、臨床的な有用性は別。 [4](https://pubmed.ncbi.nlm.nih.gov/37127759/) [23](https://arxiv.org/abs/2611.17031) |

| 学習・記憶の計算理論 | 速い経験学習、価値、局所則をモデル化する。 | AIの記憶や信用割当を考える仮説を与える。 | 生体への適合と工学的な性能をそれぞれ検証する。 [7](https://pubmed.ncbi.nlm.nih.gov/7624455/) [26](https://pubmed.ncbi.nlm.nih.gov/31942076/) [27](https://pubmed.ncbi.nlm.nih.gov/32681001/) |

## 具体的研究を読み解く

### ハエ全脳モデルの91%は、何についての精度か

**研究の問い**: 接続から単純な発火モデルを作り、感覚入力から下流ニューロンや運動への関係を予測できるかを問う。全ての行動を再現する総合試験ではない。

**設計と対照**: 基底発火0、一律の発火モデル、伝達物質からの興奮・抑制などの仮定を置く。実験で確かめられる164の予測を比較し、特定の摂食・感覚運動の変換を検証する。

**論文が報告する結果**: 確認した164予測の91%が実験と整合。多数の陰性例を含む光遺伝学のscreenを除くと84%と報告される。陰性例を多く含む構成が総合精度に影響する点を保って読む。

**位置づけ・編者の解釈**: 編者の解釈では、単純化を明示しても有用な回路仮説が出ることが成果である。同時に、どの回路で失敗しやすいかを、基底抑制や神経調節を省いた仮定から説明できる。地図から次の実験へ進めるモデルとして位置づけられる。

**結論の範囲**: 91%を全ニューロンの活動の一致率や、あらゆる行動の成功率と呼ばない。絶対発火率や精密な時間動態、強い神経調節を必要とする状態は対象外の可能性がある。

[16](https://pubmed.ncbi.nlm.nih.gov/39358519/) [1](https://pubmed.ncbi.nlm.nih.gov/39358518/)

### 非侵襲の言語復号は、生成器と脳の証拠を組み合わせる

**研究の問い**: 時間分解能の低いfMRIから、聞いている言語の意味をどこまで再構成できるかを問う。脳画像一枚へ一単語が対応するような単純な転写ではない。

**設計と対照**: 主要な評価では3人について長時間の物語聴取で個人別に学習し、言語モデルが候補を作り、候補の意味から予測される脳反応との整合性で候補を選ぶ。本人の学習データと協力を必要とする。

**論文が報告する結果**: 未見の物語などで意味に対応する再構成を示した一方、逐語一致は限定的だった。別の物語を考えるなどの課題では復号を妨げられ、他人のデータへそのまま移す性能にも限界があった。

**位置づけ・編者の解釈**: 編者の解釈では、生成言語モデルの事前知識と個人の脳信号が、逆問題の異なる不足を補う点が重要である。流暢さ、意味の近さ、単語の一致、本人の意図や協力はそれぞれ別に測る必要がある。

**結論の範囲**: 訓練した少人数の条件から、無条件に他人の思考を読めることは導けない。一方、将来の復号技術のプライバシー問題を不要だと結論する根拠にもならない。

[4](https://pubmed.ncbi.nlm.nih.gov/37127759/) [19](https://pubmed.ncbi.nlm.nih.gov/35173264/)

### SeeEEGは、専用基盤モデルの比較条件を問い直す

**研究の問い**: EEGを見たことのない視覚モデルへ適した画像として信号を提示すると、専用に事前学習した凍結EEGモデルより良い特徴が得られるかを問う。

**設計と対照**: 波形や時間周波数の表示を学習し、視覚のバックボーンは凍結する。比較するEEGモデルも凍結し、同じ読出し器を用いる。全パラメータを課題ごとに再学習する比較とは区別する。

**論文が報告する結果**: 8データセット全てで凍結DINOv3 ViT-Bが7種のEEGモデルよりbalanced accuracyで良かったと報告。ランダム初期化ViTに置くと平均15.2ポイント低下し、視覚事前学習の寄与も検査した。

**位置づけ・編者の解釈**: 編者の解釈では、専用データでの事前学習量だけでなく、入力をどう表し、どの成分を固定するかが重要だと分かる。異なるモダリティの表現を使う結果であり、画像モデルが脳の機構を理解したという主張ではない。

**結論の範囲**: 凍結特徴の転用という条件での成績であり、全EEG用途で専用モデルが不要とは言えない。施設・装置・モンタージュの差や、前向きの臨床利益は別に検証する。

[23](https://arxiv.org/abs/2611.17031) [33](https://pubmed.ncbi.nlm.nih.gov/35585198/)

## 基礎からの積み上げ

### 学習と記憶を計算原理として捉える

報酬予測誤差、スパイク時刻依存可塑性、海馬と皮質の相補的学習は、どの情報を速く覚え、どう長く保持するかを説明する基盤になった。AIの学習と関係するが、生体と同じ最適化法が実装されているとは限らない。 [5](https://pubmed.ncbi.nlm.nih.gov/9054347/) [6](https://pubmed.ncbi.nlm.nih.gov/18275283/) [7](https://pubmed.ncbi.nlm.nih.gov/7624455/) [8](https://pubmed.ncbi.nlm.nih.gov/32303713/)

### 単一ニューロンから集団の状態へ

神経集団の低次元の軌道や幾何を調べることで、刺激や運動と内部状態の関係をモデル化する。運動などに伴う広範な活動が解釈を変えるため、潜在表現を見つけるだけで機能を確定しない。 [9](https://pubmed.ncbi.nlm.nih.gov/22722855/) [10](https://pubmed.ncbi.nlm.nih.gov/19357332/) [11](https://pubmed.ncbi.nlm.nih.gov/34801787/) [12](https://pubmed.ncbi.nlm.nih.gov/31551604/)

### 脳を複数の解像度のネットワークとして測る

人ではHCPなどのMRIによる領域間ネットワーク、昆虫では電子顕微鏡による細胞とシナプスの地図が発展した。構造結合、活動の相関を表す機能結合、有効な因果的影響を区別する必要がある。 [13](https://pubmed.ncbi.nlm.nih.gov/23684880/) [14](https://pubmed.ncbi.nlm.nih.gov/21653723/) [15](https://pubmed.ncbi.nlm.nih.gov/19188601/) [1](https://pubmed.ncbi.nlm.nih.gov/39358518/)

### 地図と活動と計算モデルを対応させる

ハエの配線を制約にしたモデル、MICrONSの構造と機能の対応、学習済みAIと脳活動の比較により、候補の機構を試験できるようになった。予測が合うモデルが唯一の生物学的機構だという結論ではない。 [16](https://pubmed.ncbi.nlm.nih.gov/39358519/) [17](https://pubmed.ncbi.nlm.nih.gov/39261740/) [2](https://pubmed.ncbi.nlm.nih.gov/40205214/) [18](https://pubmed.ncbi.nlm.nih.gov/24812127/) [19](https://pubmed.ncbi.nlm.nih.gov/35173264/)

## 到達点・適用条件・残る境界

### ハエの感覚から運動までの回路を追う — 大規模資源と機能仮説

できていること: 成虫脳や脳と腹側神経索をつなぐ資源から、細胞型・回路・感覚運動経路を追跡し、機能仮説を作れる。

条件: 再構成誤り、標本の範囲、化学／電気シナプス、性差や個体差、神経調節と状態依存を考慮する。

残る境界: 「全脳地図」は全行動や感情の説明を完了した意味ではない。配線からの予測を活動記録や操作で検証する必要がある。 [1](https://pubmed.ncbi.nlm.nih.gov/39358518/) [16](https://pubmed.ncbi.nlm.nih.gov/39358519/) [20](https://pubmed.ncbi.nlm.nih.gov/42691995/) [21](https://pubmed.ncbi.nlm.nih.gov/42259917/)

### マウス・人の構造と機能を調べる — 解像度ごとに到達点が異なる

できていること: マウス視覚皮質の局所では大量の細胞の活動とシナプス地図を対応させられる。人では局所EM地図とMRIによる広域ネットワークが得られる。

条件: 細胞レベルの局所と、領域レベルの全体を分け、測定方法・標本・状態の差を明記する。

残る境界: 人の局所組織の再構成を全脳の完成と呼ばない。MRIの機能結合も単一シナプスの配線ではない。 [2](https://pubmed.ncbi.nlm.nih.gov/40205214/) [3](https://pubmed.ncbi.nlm.nih.gov/38723085/) [13](https://pubmed.ncbi.nlm.nih.gov/23684880/) [22](https://pubmed.ncbi.nlm.nih.gov/29116093/)

### 集団活動の状態や表現をモデル化する — 比較が蓄積

できていること: 潜在状態、神経多様体、課題に最適化したニューラルネットで、活動と行動・刺激の対応を検討できる。

条件: 観測していない動きや内部状態などの交絡を測り、独立データと操作実験で説明を比較する。

残る境界: 良い復号や表現の類似性だけでは、脳が同じアルゴリズムを使うことの証明にならない。 [9](https://pubmed.ncbi.nlm.nih.gov/22722855/) [12](https://pubmed.ncbi.nlm.nih.gov/31551604/) [11](https://pubmed.ncbi.nlm.nih.gov/34801787/) [18](https://pubmed.ncbi.nlm.nih.gov/24812127/)

### 脳信号をAIの入力として使う — 限定条件で実証

できていること: EEG表現の転用や、協力した被験者のfMRIから言語の意味を再構成する研究がある。

条件: 個人別訓練、センサ構成、施設差、読出し器、本人の協力、評価の単位を揃える。

残る境界: 意味の近い文章が生成できても逐語転写や無条件の思考読取ではなく、凍結特徴の比較から臨床有用性は確定しない。 [4](https://pubmed.ncbi.nlm.nih.gov/37127759/) [23](https://arxiv.org/abs/2611.17031) [24](https://arxiv.org/abs/2608.11656)

### 脳の原理をAIの仮説へ使う — 理論とモデルの接点

できていること: 相補的な記憶、予測表現、報酬予測誤差、局所学習則を、AIの記憶・探索・学習の設計と照らして考えられる。

条件: 生物学的な説明、計算モデルの再現、工学的な性能改善を別々の証拠として扱う。

残る境界: 脳に似ていることから、AIとしての性能・効率や人の認知機能との同等性は導けない。 [7](https://pubmed.ncbi.nlm.nih.gov/7624455/) [25](https://pubmed.ncbi.nlm.nih.gov/28967910/) [26](https://pubmed.ncbi.nlm.nih.gov/31942076/) [27](https://pubmed.ncbi.nlm.nih.gov/32681001/)

## 関連する直近研究

### 2024〜2026：ハエは脳から中枢全体と性差へ

成虫脳の資源は139,255ニューロンを報告し、2026年の雄中枢神経系資源は脳と神経索を含む166,700ニューロンと11,710型を報告。別の脳・神経索資源は局所フィードバックと分散的な制御を分析する。標本と版の異なる数値を一つの地図として足し合わせない。 [1](https://pubmed.ncbi.nlm.nih.gov/39358518/) [20](https://pubmed.ncbi.nlm.nih.gov/42691995/) [21](https://pubmed.ncbi.nlm.nih.gov/42259917/)

### MICrONSと人の局所EM：構造と機能の対応へ

MICrONSは約75,000ニューロンの機能記録と、20万超の細胞・約5億シナプスを含む局所地図を対応。人の約1立方mmの局所EMは約57,000細胞・約1.5億シナプスで、細胞数にはグリアも含む。いずれも人間全脳の単一細胞地図ではない。 [2](https://pubmed.ncbi.nlm.nih.gov/40205214/) [3](https://pubmed.ncbi.nlm.nih.gov/38723085/)

## 次の課題（編者の整理）

### 構造から動態・行動へつなげられるか

欠けた神経調節、学習則、内的状態、身体と環境を補い、回路を操作したときの行動まで予測することが次の焦点になる。 [16](https://pubmed.ncbi.nlm.nih.gov/39358519/) [21](https://pubmed.ncbi.nlm.nih.gov/42259917/)

### 人の個体差と測定の交絡をどう扱うか

頭部運動、測定機器、課題・安静状態、個人別学習の影響を分け、個体をまたぐ再現性とプライバシーを検討する。 [28](https://pubmed.ncbi.nlm.nih.gov/21810475/) [29](https://pubmed.ncbi.nlm.nih.gov/28302591/) [4](https://pubmed.ncbi.nlm.nih.gov/37127759/)

## 分野間の接点（編者の整理）

- [エージェント・検索・記憶・協調](https://drkamoshika.github.io/papers/?view=map&topic=agents): 速い記憶と遅い知識の分業はエージェント記憶を考える手掛かりだが、工学的な有効性は別に測る。 [7](https://pubmed.ncbi.nlm.nih.gov/7624455/) [30](https://arxiv.org/abs/2611.14320)

- [次イベント予測・点過程](https://drkamoshika.github.io/papers/?view=map&topic=events): 神経発火列のモデル化や報酬の時間予測は、点過程や次イベント予測と接点を持つ。 [31](https://arxiv.org/abs/2106.00901) [32](https://pubmed.ncbi.nlm.nih.gov/10195164/)

- [医療・生体信号・創薬AI](https://drkamoshika.github.io/papers/?view=map&topic=medical): EEGの分類・予後予測を診療に使うには、機構の理解に加えて臨床的な外部検証が必要になる。 [23](https://arxiv.org/abs/2611.17031) [33](https://pubmed.ncbi.nlm.nih.gov/35585198/)

## 読む順番

1. [Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A7624455)

2. [Neural population dynamics during reaching](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A22722855)

3. [The WU-Minn Human Connectome Project: an overview](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A23684880)

4. [Neuronal wiring diagram of an adult brain](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A39358518)

5. [A Drosophila computational brain model reveals sensorimotor processing](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A39358519)

6. [Functional connectomics spanning multiple areas of mouse visual cortex](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A40205214)

7. [A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A38723085)

8. [Your Vision Foundation Model Is Secretly an EEG Foundation Model](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17031)

## 引用文献と確認範囲

1. [Neuronal wiring diagram of an adult brain](https://pubmed.ncbi.nlm.nih.gov/39358518/) — 2024-10-02 / pmid:39358518 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A39358518)

2. [Functional connectomics spanning multiple areas of mouse visual cortex](https://pubmed.ncbi.nlm.nih.gov/40205214/) — 2025-04-09 / pmid:40205214 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A40205214) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://pubmed.ncbi.nlm.nih.gov/40205214/)

3. [A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution](https://pubmed.ncbi.nlm.nih.gov/38723085/) — 2024-05-10 / pmid:38723085 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A38723085) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://pubmed.ncbi.nlm.nih.gov/38723085/)

4. [Semantic reconstruction of continuous language from non-invasive brain recordings](https://pubmed.ncbi.nlm.nih.gov/37127759/) — 2023-05-01 / pmid:37127759 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A37127759) / 再確認: 2026-11-18、PMC・出版社の検索掲載本文Experimental tasks・データ量。既存の本文確認記録も参照、[確認先](https://pmc.ncbi.nlm.nih.gov/articles/PMC11304553/)

5. [A neural substrate of prediction and reward](https://pubmed.ncbi.nlm.nih.gov/9054347/) — 1997-03-14 / pmid:9054347 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A9054347)

6. [Spike timing-dependent plasticity: a Hebbian learning rule](https://pubmed.ncbi.nlm.nih.gov/18275283/) — 2008-07-21 / pmid:18275283 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A18275283)

7. [Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory](https://pubmed.ncbi.nlm.nih.gov/7624455/) — 公開日未確認 / pmid:7624455 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A7624455)

8. [Backpropagation and the brain](https://pubmed.ncbi.nlm.nih.gov/32303713/) — 2020-04-17 / pmid:32303713 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32303713)

9. [Neural population dynamics during reaching](https://pubmed.ncbi.nlm.nih.gov/22722855/) — 2012-07-05 / pmid:22722855 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A22722855)

10. [Gaussian-process factor analysis for low-dimensional single-trial analysis of neural population activity](https://pubmed.ncbi.nlm.nih.gov/19357332/) — 2009-04-08 / pmid:19357332 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A19357332)

11. [Neural population geometry: An approach for understanding biological and artificial neural networks](https://pubmed.ncbi.nlm.nih.gov/34801787/) — 2021-11-19 / pmid:34801787 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34801787)

12. [Single-trial neural dynamics are dominated by richly varied movements](https://pubmed.ncbi.nlm.nih.gov/31551604/) — 2019-09-24 / pmid:31551604 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A31551604)

13. [The WU-Minn Human Connectome Project: an overview](https://pubmed.ncbi.nlm.nih.gov/23684880/) — 2013-05-16 / pmid:23684880 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A23684880)

14. [The organization of the human cerebral cortex estimated by intrinsic functional connectivity](https://pubmed.ncbi.nlm.nih.gov/21653723/) — 2011-06-08 / pmid:21653723 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A21653723)

15. [Predicting human resting-state functional connectivity from structural connectivity](https://pubmed.ncbi.nlm.nih.gov/19188601/) — 2009-02-02 / pmid:19188601 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A19188601)

16. [A Drosophila computational brain model reveals sensorimotor processing](https://pubmed.ncbi.nlm.nih.gov/39358519/) — 2024-10-02 / pmid:39358519 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A39358519) / 再確認: 2026-11-18、公開論文本文Connectome models・Computational modelling limitations・164予測の集計、[確認先](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11446845/fullTextXML)

17. [Connectome-constrained networks predict neural activity across the fly visual system](https://pubmed.ncbi.nlm.nih.gov/39261740/) — 2024-09-11 / pmid:39261740 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A39261740)

18. [Performance-optimized hierarchical models predict neural responses in higher visual cortex](https://pubmed.ncbi.nlm.nih.gov/24812127/) — 2014-05-08 / pmid:24812127 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A24812127)

19. [Brains and algorithms partially converge in natural language processing](https://pubmed.ncbi.nlm.nih.gov/35173264/) — 2022-02-16 / pmid:35173264 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A35173264)

20. [Sexual dimorphism in the complete Drosophila male central nervous system connectome](https://pubmed.ncbi.nlm.nih.gov/42691995/) — 2026-09-03 / pmid:42691995 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A42691995) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://pubmed.ncbi.nlm.nih.gov/42691995/)

21. [Distributed control circuits across a brain-and-cord connectome](https://pubmed.ncbi.nlm.nih.gov/42259917/) — 2026-06-08 / pmid:42259917 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A42259917) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://pubmed.ncbi.nlm.nih.gov/42259917/)

22. [The challenge of mapping the human connectome based on diffusion tractography](https://pubmed.ncbi.nlm.nih.gov/29116093/) — 2017-11-07 / pmid:29116093 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A29116093)

23. [Your Vision Foundation Model Is Secretly an EEG Foundation Model](https://arxiv.org/abs/2611.17031) — 2026-11-12 / arxiv:2611.17031 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17031) / 再確認: 2026-11-18、要旨、事例の方法・実験条件・報告値、[確認先](https://arxiv.org/abs/2611.17031v1)

24. [Continuous-Latent Predictive Modeling with Semantic Alignment for EEG-Language Foundation Models](https://arxiv.org/abs/2608.11656) — 2026-08-12 / arxiv:2608.11656 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2608.11656)

25. [The hippocampus as a predictive map](https://pubmed.ncbi.nlm.nih.gov/28967910/) — 2017-10-02 / pmid:28967910 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A28967910)

26. [A distributional code for value in dopamine-based reinforcement learning](https://pubmed.ncbi.nlm.nih.gov/31942076/) — 2020-01-15 / pmid:31942076 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A31942076)

27. [A solution to the learning dilemma for recurrent networks of spiking neurons](https://pubmed.ncbi.nlm.nih.gov/32681001/) — 2020-07-17 / pmid:32681001 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32681001)

28. [The influence of head motion on intrinsic functional connectivity MRI](https://pubmed.ncbi.nlm.nih.gov/21810475/) — 2011-07-23 / pmid:21810475 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A21810475)

29. [Benchmarking of participant-level confound regression strategies for the control of motion artifact in studies of functional connectivity](https://pubmed.ncbi.nlm.nih.gov/28302591/) — 2017-03-14 / pmid:28302591 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A28302591)

30. [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320) — 2026-11-10 / arxiv:2611.14320 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14320) / 再確認: 2026-11-18、要旨、事例の方法・実験条件・報告値、[確認先](https://arxiv.org/abs/2611.14320v1)

31. [A Differentiable Point Process with Its Application to Spiking Neural Networks](https://arxiv.org/abs/2106.00901) — 2021-06-02 / arxiv:2106.00901 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2106.00901)

32. [Dopamine neurons report an error in the temporal prediction of reward during learning](https://pubmed.ncbi.nlm.nih.gov/10195164/) — 公開日未確認 / pmid:10195164 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A10195164)

33. [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://pubmed.ncbi.nlm.nih.gov/35585198/) — 2022-05-18 / pmid:35585198 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A35585198)

34. [Computation Through Neural Population Dynamics](https://pubmed.ncbi.nlm.nih.gov/32640928/) — 2020-07-08 / pmid:32640928 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32640928)

35. [Using connectome-based predictive modeling to predict individual behavior from brain connectivity](https://pubmed.ncbi.nlm.nih.gov/28182017/) — 2017-02-09 / pmid:28182017 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A28182017)

36. [Reactivation of hippocampal ensemble memories during sleep](https://pubmed.ncbi.nlm.nih.gov/8036517/) — 1994-07-29 / pmid:8036517 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A8036517)

37. [Overcoming catastrophic forgetting in neural networks](https://pubmed.ncbi.nlm.nih.gov/28292907/) — 2017-03-14 / pmid:28292907 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A28292907)

38. [The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process](https://arxiv.org/abs/1612.09328) — 2016-12-29 / arxiv:1612.09328 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1612.09328)

39. [Neuromodulated Spike-Timing-Dependent Plasticity, and Theory of Three-Factor Learning Rules](https://pubmed.ncbi.nlm.nih.gov/26834568/) — 2016-01-19 / pmid:26834568 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A26834568)

## 収録範囲と読み方

対象は2026-11-16時点の収録スナップショット（基礎774件・新着264件）です。2026-11-18の改稿は、この範囲の技術・比較・事例の詳説です。

全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断レビューです。基礎・新着は収録先の区別で、古さは個々の公開日から確認できます。

技術の系譜、論文間の位置づけ、実験から導く解釈と次の課題は編者の整理です。直接の引用関係や商用普及率を確定するものではありません。

初版の22件に加え、改稿では25件の一次資料を確認しました（重複あり）。要旨・本文・検索掲載箇所の範囲を引用文献に記録しています。全件の全文精読や独立再現を意味しません。

数値は論文の報告値です。異なるデータ・分割・指標の比較を統一順位へ変換していません。説明用の計算例は実測値と区別しています。
