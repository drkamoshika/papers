# 医療・生体信号・創薬AI：技術と実験を詳しく読む

改稿: 2026-11-18 / 対象文献スナップショット: 2026-11-16 / 論文公開日上限: 2026-11-12

画像や診療記録から特徴を学ぶ段階から、事前学習した表現を使い、文章・生体信号・分子を横断して支援する段階へ進んだ。現在の到達点は用途ごとに異なり、診療現場の効果は精度の高いベンチマークとは分けて評価する必要がある。

## まず押さえる到達点

画像の領域抽出、記録の構造化、生体信号解析、分子・タンパク質の候補探索で有用性を示す。

医学試験の高得点や記録の読解から、自律診療・個別予後予測・治療効果までは確定しない。 [1](https://pubmed.ncbi.nlm.nih.gov/33288961/) [2](https://pubmed.ncbi.nlm.nih.gov/42957896/) [3](https://pubmed.ncbi.nlm.nih.gov/43019548/)

## 技術の中身と論文同士の関係

### 医療AIの「できる」は、測定・判断・介入のどこかを明示して初めて意味を持つ

医療画像から領域を切り出す、記録から所見を抽出する、病気を予測する、治療を変えて転帰を改善する、という課題は連続して見えるが、正解と必要な証拠が異なる。領域抽出が正しくても病変の意味を誤ることはあり、リスクの高い人を並べられても、介入で利益が得られるとは限らない。モデルの入出力と臨床の行動を分けて追うことが、分野を俯瞰する出発点になる。 [4](https://arxiv.org/abs/1505.04597) [15](https://pubmed.ncbi.nlm.nih.gov/35585198/) [14](https://pubmed.ncbi.nlm.nih.gov/32908283/)

画像の領域抽出で使う重なりの指標は、誤りの位置や臨床的重要性を全て同じには扱わない。診断の感度・特異度、患者あたりの見逃し、読影に要する時間は別の指標である。nnU-Netがデータごとに前処理や構成を整えることの価値も、モデル構造の目新しさだけでは測れない。対象データと一連の処理を揃えた比較が進歩の重要な部分を占める。 [1](https://pubmed.ncbi.nlm.nih.gov/33288961/) [4](https://arxiv.org/abs/1505.04597) [27](https://pubmed.ncbi.nlm.nih.gov/30104768/)

診療記録ではラベルの生成過程にも注意が必要になる。記録された診断や請求上のコードは病態そのものと同じではなく、受診頻度、検査の実施、医師の方針を反映する。モデルが「病気になりそうな患者」を捉えたのか、「その施設で記録されやすい患者」を捉えたのかが変わり得る。表現学習を大規模化しても、こうした観測とラベルの問題は消えない。 [5](https://pubmed.ncbi.nlm.nih.gov/27185194/) [6](https://pubmed.ncbi.nlm.nih.gov/32346050/) [16](https://pubmed.ncbi.nlm.nih.gov/34152373/)

LLMが記録を読み、既に書かれている情報を構造化する課題は有力な用途である。ただし、分散した記述の整合、否定、推測、時間関係を区別する必要がある。「過去に疑われた副作用」と「今起きている確定した副作用」は違う。現時点のイベント検出、重症度、帰属、将来のリスクを一つの正解率でまとめると、どこまで使えるかが見えなくなる。 [2](https://pubmed.ncbi.nlm.nih.gov/42957896/) [17](https://arxiv.org/abs/2611.01527)

### 外部検証、サイレント運用、人との比較、介入試験は段階が違う

同じ施設で学習・検証を分ける内部評価は、モデルが対象の分布で学習できるかを示す。一方、別の施設や将来時点へ移す外部評価では、患者層、記録方法、装置、診療方針の差が現れる。ランダムに患者を分けただけで、将来の患者へ使う場面が再現されるとは限らない。施設でよく使われる予測モデルであっても外部検証が必要になる理由である。 [16](https://pubmed.ncbi.nlm.nih.gov/34152373/) [21](https://pubmed.ncbi.nlm.nih.gov/38207039/) [28](https://pubmed.ncbi.nlm.nih.gov/33564405/)

サイレント運用は、実際に入ってくる新しいデータでモデルを動かし、その結果を診療の行動へまだ反映させずに評価する方式である。現場のデータ遅延や入力の欠落を捉えやすいが、モデルが医療者の行動をどう変えたかまでは測らない。前向きにデータが来ることと、AIを用いた介入の効果を前向きに比較することを区別する必要がある。 [2](https://pubmed.ncbi.nlm.nih.gov/42957896/) [15](https://pubmed.ncbi.nlm.nih.gov/35585198/)

人とAIを組み合わせた評価では、人だけ、AIだけ、人とAIの組合せを比べる視点が重要になる。使いやすさや説明によって人の判断が変わるため、モデル単体が高性能でも、組合せが改善するとは限らない。時間短縮、注釈の一致、患者への説明、見逃し、再確認の回数などを、対象業務に沿って評価する必要がある。 [15](https://pubmed.ncbi.nlm.nih.gov/35585198/) [2](https://pubmed.ncbi.nlm.nih.gov/42957896/) [29](https://pubmed.ncbi.nlm.nih.gov/39466245/)

介入試験は、AIを使うことによって結果がどう変わるかを比較する。診断の精度や作業の速度を示す研究から、死亡や合併症などの患者転帰の改善を推定してはならない。TRIPOD、DECIDE-AI、CONSORT-AIはそれぞれ報告・早期評価・試験の記載を助けるが、チェックリストを満たすこと自体が有効性の証明ではない。研究の質を判断する入口として使う。 [13](https://pubmed.ncbi.nlm.nih.gov/25569120/) [15](https://pubmed.ncbi.nlm.nih.gov/35585198/) [14](https://pubmed.ncbi.nlm.nih.gov/32908283/)

### 予後予測は、文章を理解するだけでは解けない

現在の状態整理は、入力に既に含まれる情報を同じ時点のラベルへ写す課題である。予後予測では、まだ観測していない病態変化、今後の治療や生活、測定誤差などを含む将来の分布を扱う。現在の重症度の相関を学ぶだけでも見かけ上の予測はできるため、「現在と同じ」と予測する持続モデルを超えた価値があるかを見る必要がある。 [3](https://pubmed.ncbi.nlm.nih.gov/43019548/) [18](https://pubmed.ncbi.nlm.nih.gov/31367026/)

時点の設計を誤ると、未来の情報が入力へ混ざる。例えば予測したい診断が確定した後の記録や、結果を知ってから整えた文章を使うと、実運用では得られない情報で問題を解くことになる。同じ患者の複数記録が学習側と評価側へ分かれる場合も、患者を覚えることと将来の予測を分けにくい。予測時点で利用可能な情報を固定することが、モデル選択より先の要件になる。 [6](https://pubmed.ncbi.nlm.nih.gov/32346050/) [28](https://pubmed.ncbi.nlm.nih.gov/33564405/) [3](https://pubmed.ncbi.nlm.nih.gov/43019548/)

予測が実測値と高く相関することと、個別の値が十分に正確であることも違う。全員を一貫して高めに予測しても相関は保てるため、平均絶対誤差、系統的な偏り、校正、繰り返し実行したときの患者単位の一致を併記する必要がある。ある閾値で行動を変える用途では、その付近での誤りも別に検討する。 [3](https://pubmed.ncbi.nlm.nih.gov/43019548/) [20](https://pubmed.ncbi.nlm.nih.gov/42995166)

さらに、ある治療を受けた人の将来を予測できても、治療を変更した場合の結果が分かるとは限らない。治療の選ばれ方に交絡がある観察データでは、悪化した人ほど強い治療を受けるという関係もあり得る。予測器の高精度を根拠に、そのまま処置の比較を行わない。ここで医療AIは、表・時系列モデルと因果推論の問題へ接続する。 [30](https://arxiv.org/abs/1608.00060) [23](https://arxiv.org/abs/2611.15009) [6](https://pubmed.ncbi.nlm.nih.gov/32346050/)

### 創薬では、構造・配列・機能・臨床効果をつなぐ複数の関門がある

AlphaFoldの構造予測、ProteinMPNNの配列設計、RFdiffusionの構造生成は、同じ生成AIという言葉で括られても条件と出力が違う。構造予測は与えられた配列に対する形を扱い、配列設計は望む構造に適する配列を探し、生成設計は狙う形や機能の候補を作る。どの方向の写像を学んだかを明示すると、互いに置き換えられない役割が分かる。 [10](https://pubmed.ncbi.nlm.nih.gov/34265844/) [11](https://pubmed.ncbi.nlm.nih.gov/36108050/) [12](https://pubmed.ncbi.nlm.nih.gov/37433327/)

構造が妥当に見えても、その分子が発現し、安定に存在し、望む条件で結合し、目的の機能を持つとは限らない。機能があっても、体内で届く場所や分解、毒性、製造上の問題が残る。計算の成績、試験管内の実験、動物や臨床の結果を段階別に読むことが重要で、構造予測の成功率を新薬の開発成功率へ変換することはできない。 [10](https://pubmed.ncbi.nlm.nih.gov/34265844/) [11](https://pubmed.ncbi.nlm.nih.gov/36108050/) [12](https://pubmed.ncbi.nlm.nih.gov/37433327/)

AIの価値は、最終的な成功を一度で当てることだけではない。候補を狭め、異なる仮説を試す実験を選び、失敗の情報を次の設計へ戻すことにもある。この場合の評価は、一つのベンチマークの精度だけでなく、必要な実験数、候補の多様性、同じ予算で得られる検証済み候補の数へ広がる。生成モデルから実験を含むエージェントへ進む接点である。 [12](https://pubmed.ncbi.nlm.nih.gov/37433327/) [19](https://pubmed.ncbi.nlm.nih.gov/42984375/) [31](https://pubmed.ncbi.nlm.nih.gov/42509322)

ただし実験系を自動化しても、判断基準の妥当性は別に残る。測りやすい代理指標を改善した候補が、本当に欲しい生物学的な結果を改善するかを確認しなければならない。医学試験の高得点を診療の有効性へ移せないのと同様に、分子の代理スコアを臨床的な価値と同一視しないことが、医療と創薬を一つのレビューで読む際の共通軸になる。 [19](https://pubmed.ncbi.nlm.nih.gov/42984375/) [12](https://pubmed.ncbi.nlm.nih.gov/37433327/) [15](https://pubmed.ncbi.nlm.nih.gov/35585198/)

### 二つの具体的な処理系：患者の系列表現とタンパク質の逆設計

BEHRTは患者の診療履歴を系列として扱い、隠した病名を文脈から予測する事前学習を行う。病名と年齢などから作る入力表現に、受診の順序や位置を組み合わせ、学習した表現を将来の病態の予測へ使う。ここでの「言語」は自由文だけを意味せず、診療コードの系列をTransformerへ渡すという表現の選択である。 [6](https://pubmed.ncbi.nlm.nih.gov/32346050/)

この系列化によって、単一の時点の特徴量へ履歴を集約する場合より、併存する病気と順序の関係を学べる。ただし、受診がなかった期間が健康だったのか未観測だったのかは入力設計に依存する。病名コードの並びを学べることと、病態の連続的な進行を同定することを分けると、生体信号の時間モデルや点過程へ接続すべき不足が見える。 [6](https://pubmed.ncbi.nlm.nih.gov/32346050/) [24](https://arxiv.org/abs/1612.09328)

RFdiffusionでは、既知構造へノイズを加え、それを戻すよう構造予測ネットワークRoseTTAFoldを学習し直す。生成時はランダムな残基の配置から少しずつ骨格を作り、対称性や機能に必要な部分構造などの条件を与える。全体の骨格候補を生成する工程と、その骨格へ適する配列を設計する工程を分けることで、構造予測器を逆方向の設計へ利用している。 [12](https://pubmed.ncbi.nlm.nih.gov/37433327/) [11](https://pubmed.ncbi.nlm.nih.gov/36108050/)

この処理系の進歩は、「文章で指示したら薬が完成する」ことではなく、以前は手作業や個別の仕組みが必要だった複数の設計課題を、条件付き生成と後続の配列設計・実験の組合せで扱えるようにした点にある。どの条件を与え、何候補を作り、どの実験で選別したかまで追うと、計算モデルが実験のどの部分を置き換えたかを理解できる。 [12](https://pubmed.ncbi.nlm.nih.gov/37433327/) [11](https://pubmed.ncbi.nlm.nih.gov/36108050/) [19](https://pubmed.ncbi.nlm.nih.gov/42984375/)

## 手法を比較する

| 方法 | 何を変えるか | 得られる利点 | 前提と交換条件 |

| --- | --- | --- | --- |

| 画像・信号の判別 | 画像や波形を領域、所見、分類へ写す。 | 対象を限定した測定支援の比較が蓄積している。 | 装置・施設差と、指標の臨床的な意味を検証する。 [1](https://pubmed.ncbi.nlm.nih.gov/33288961/) [9](https://pubmed.ncbi.nlm.nih.gov/32903191/) |

| 臨床文章の構造化 | 記録から存在、時間、重症度などを抽出する。 | 人の確認と組み合わせた作業を支援しやすい。 | 記録の欠落、否定、推測、時点の混同が残る。 [2](https://pubmed.ncbi.nlm.nih.gov/42957896/) |

| 将来の患者状態の予測 | 予測時点の情報から未来の分布を推定する。 | リスクの層別化や追跡の研究へ使える。 | 持続基準、校正、施設外・時間外の検証が必要。 [18](https://pubmed.ncbi.nlm.nih.gov/31367026/) [3](https://pubmed.ncbi.nlm.nih.gov/43019548/) |

| 人とAIを組み合わせた介入 | AIの情報を人が使った結果を比較する。 | 作業時間や判断品質への効果を測れる。 | 患者転帰の改善には別途、対応する試験が必要。 [15](https://pubmed.ncbi.nlm.nih.gov/35585198/) [2](https://pubmed.ncbi.nlm.nih.gov/42957896/) |

| 分子・タンパク質の設計 | 配列・構造・機能の候補を予測や生成で絞る。 | 実験へ進める候補の探索を効率化できる。 | 計算の妥当性から薬としての有効性は導けない。 [10](https://pubmed.ncbi.nlm.nih.gov/34265844/) [11](https://pubmed.ncbi.nlm.nih.gov/36108050/) [12](https://pubmed.ncbi.nlm.nih.gov/37433327/) |

## 具体的研究を読み解く

### 有害事象抽出：三種類の評価を足し合わせずに読む

**研究の問い**: 免疫治療の記録から現在の有害事象、時間関係、重症度、帰属などを抽出し、人の確認を支援できるかを問う研究である。自動診療全体の試験としては扱わない。

**設計と対照**: 要旨で確認できる設計は、後ろ向き評価、3か月の前向きサイレント運用、臨床試験スタッフによるランダム化クロスオーバーの三段階である。詳しい各コホートの構成や運用変更の影響は本文の検証が必要になる。

**論文が報告する結果**: 後ろ向きの現イベント検出macro-F1は0.92、重症度は0.66。サイレント運用の二値F1は0.72〜0.79。人の試験では注釈時間が2.71分短縮した。

**位置づけ・編者の解釈**: 編者の解釈では、イベントの有無を拾うことと、重症度を精密に分類することの難しさの差、さらに人の作業への寄与まで分けた点が重要である。F1の種類と対象が違うため、前向きで何ポイント悪化したと単純には計算しない。

**結論の範囲**: この結果は、注釈支援の有用性の証拠であり、患者転帰の改善や、確認する人を外せることの証拠ではない。ここでの追加照合は原著要旨の範囲である。

[2](https://pubmed.ncbi.nlm.nih.gov/42957896/) [15](https://pubmed.ncbi.nlm.nih.gov/35585198/)

### 膝関節症：同じ入力で現状は整理できても予後は難しい

**研究の問い**: 標準化された面接記録と画像の報告文から、現時点の評価と6か月後の状態を同じLLMに求める。状態の抽出能力が予測能力へつながるかを直接分ける。

**設計と対照**: 128人を登録し、追跡を完了した111人を解析。コホートは前向きだがLLMの評価自体は追跡完了後の後ろ向き評価で、医師、別の医師による転帰、持続予測との比較を行う。画像そのものをLLMが読影した試験ではない。

**論文が報告する結果**: 既に膝関節症のある患者で診断一致は105/111。6か月のWOMAC平均絶対誤差はLLM 5.92〜6.58、医師3.86、持続モデル5.43で、現在の評価と将来予測に差があった。

**位置づけ・編者の解釈**: 編者の解釈では、単純な持続予測の位置が重要である。現在の重症度を言い換えるだけで得られる成績を超えたかを判定できるからだ。診断一致の高い数字だけを抜き出すと、この中心的な結果を取り逃す。

**結論の範囲**: 全員が既に当該疾患を持つ集団なので一般診断精度とは呼べない。単施設、一つの構成、追跡脱落、LLM評価の時点という条件を保った結論として読む。

[3](https://pubmed.ncbi.nlm.nih.gov/43019548/) [28](https://pubmed.ncbi.nlm.nih.gov/33564405/)

## 基礎からの積み上げ

### 画像と患者記録から表現を学ぶ

U-Netは領域の切り出し、Deep Patientは電子カルテの表現学習を進めた。nnU-Netはデータセットごとの設定を体系化し、設計の自動化と再現可能な比較を重視した。 [4](https://arxiv.org/abs/1505.04597) [5](https://pubmed.ncbi.nlm.nih.gov/27185194/) [1](https://pubmed.ncbi.nlm.nih.gov/33288961/)

### タスクごとの学習から事前学習へ

BEHRTとMed-BERTは診療記録の系列、RETFoundは眼底画像、ECG研究は心電図を扱う。データの種類ごとに事前学習した表現を別の課題へ移す流れだが、施設や機器の差も持ち越す。 [6](https://pubmed.ncbi.nlm.nih.gov/32346050/) [7](https://pubmed.ncbi.nlm.nih.gov/34017034/) [8](https://pubmed.ncbi.nlm.nih.gov/37704728/) [9](https://pubmed.ncbi.nlm.nih.gov/32903191/)

### 分子とタンパク質を探索する

AlphaFoldは構造予測、ProteinMPNNは配列設計、RFdiffusionは構造・機能を狙う生成設計へと対象を広げた。計算上の候補を作ることと、生体内での有効性・安全性を確かめることは別の段階になる。 [10](https://pubmed.ncbi.nlm.nih.gov/34265844/) [11](https://pubmed.ncbi.nlm.nih.gov/36108050/) [12](https://pubmed.ncbi.nlm.nih.gov/37433327/)

### 実臨床の評価を設計する

TRIPOD、CONSORT-AI、DECIDE-AIは、予測モデルの報告、介入試験、早期の臨床評価をそれぞれ支える。外部検証や人とAIの組合せを評価しなければ、モデル精度から診療への貢献を判断しにくい。 [13](https://pubmed.ncbi.nlm.nih.gov/25569120/) [14](https://pubmed.ncbi.nlm.nih.gov/32908283/) [15](https://pubmed.ncbi.nlm.nih.gov/35585198/) [16](https://pubmed.ncbi.nlm.nih.gov/34152373/)

## 到達点・適用条件・残る境界

### 医用画像・生体信号を解析する — 比較が蓄積

できていること: 領域抽出、所見の検出、心電図などの分類で、対象のデータと手順を定めた評価が積み重なっている。

条件: 施設・装置・患者層を分けた外部検証と、判定の閾値、医療者と組み合わせた効果を確認する。

残る境界: 単施設の高精度から、異なる施設での安全性や患者転帰の改善は推定できない。 [1](https://pubmed.ncbi.nlm.nih.gov/33288961/) [9](https://pubmed.ncbi.nlm.nih.gov/32903191/) [16](https://pubmed.ncbi.nlm.nih.gov/34152373/) [15](https://pubmed.ncbi.nlm.nih.gov/35585198/)

### 臨床記録を構造化し、人の確認を支援する — 前向き評価の例あり

できていること: 診療記録から有害事象などを抽出し、人による確認と組み合わせて注釈時間や一致度を改善した例がある。

条件: 対象イベント・重症度・時間関係を分けて測り、後ろ向き検証、サイレント運用、人との比較を区別する。

残る境界: 注釈支援の改善から、自律的な治療判断や患者の長期予後の改善までは言えない。 [2](https://pubmed.ncbi.nlm.nih.gov/42957896/) [17](https://arxiv.org/abs/2611.01527)

### 将来の患者状態を予測する — 用途ごとの検証が必要

できていること: 電子カルテや生体信号から特定の将来イベントを予測するモデルが作られている。

条件: 予測時点で使える情報だけを入力し、時系列・施設外検証、校正、単純な持続予測との比較を行う。

残る境界: 現時点の状態を正しく整理できるLLMでも、数か月後の個別予後が当たるとは限らない。 [18](https://pubmed.ncbi.nlm.nih.gov/31367026/) [6](https://pubmed.ncbi.nlm.nih.gov/32346050/) [3](https://pubmed.ncbi.nlm.nih.gov/43019548/)

### 創薬・タンパク質設計を支援する — 実験検証を伴う研究

できていること: 構造予測や候補生成を使って、実験へ進める候補を絞り、設計と検証の循環を作れる。

条件: 結合・機能・毒性・合成可能性など、目的に対応した実験を設計する。

残る境界: 構造がもっともらしいことや試験管内の機能から、治療薬としての有効性・臨床成功率は導けない。 [10](https://pubmed.ncbi.nlm.nih.gov/34265844/) [11](https://pubmed.ncbi.nlm.nih.gov/36108050/) [12](https://pubmed.ncbi.nlm.nih.gov/37433327/) [19](https://pubmed.ncbi.nlm.nih.gov/42984375/)

## 関連する直近研究

### 医学的評価器：課題を替えると信頼性が変わる

10 LLMを3種の医療評価に用いた研究では、全課題で上位3位に入るモデルはなかった。最重症トリアージで重大な過小評価が報告され、別課題で良い評価器をそのまま転用できないことが示された。 [20](https://pubmed.ncbi.nlm.nih.gov/42995166)

## 次の課題（編者の整理）

### 支援が現場の結果を改善するか

人の確認を残した業務時間・判断品質の改善と、患者転帰の改善を段階別に検証する。モデル単体の結果だけで判断しない。 [15](https://pubmed.ncbi.nlm.nih.gov/35585198/) [2](https://pubmed.ncbi.nlm.nih.gov/42957896/)

### 外部施設と将来時点に耐えられるか

施設・時点・患者層をまたいだ校正と、監視・更新後の性能を確かめる必要がある。 [16](https://pubmed.ncbi.nlm.nih.gov/34152373/) [21](https://pubmed.ncbi.nlm.nih.gov/38207039/) [22](https://pubmed.ncbi.nlm.nih.gov/42066927)

## 分野間の接点（編者の整理）

- [表形式・時系列・因果推論](https://drkamoshika.github.io/papers/?view=map&topic=structured): EHRの予後予測は表・時系列の問題でもあり、観察データから治療の介入効果を推定する問題とは区別する。 [6](https://pubmed.ncbi.nlm.nih.gov/32346050/) [23](https://arxiv.org/abs/2611.15009)

- [次イベント予測・点過程](https://drkamoshika.github.io/papers/?view=map&topic=events): 診断・投薬・合併症の次イベントと発生時刻を扱うには、点過程の評価と観察の欠落・打ち切りの扱いが重要になる。 [24](https://arxiv.org/abs/1612.09328) [3](https://pubmed.ncbi.nlm.nih.gov/43019548/)

- [神経科学とAI](https://drkamoshika.github.io/papers/?view=map&topic=neuroscience): EEGの表現学習と脳の機構理解は接点を持つが、信号を分類できることと脳回路を説明できることは別である。 [25](https://arxiv.org/abs/2611.17031) [26](https://pubmed.ncbi.nlm.nih.gov/39358519/)

## 読む順番

1. [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1505.04597)

2. [BEHRT: Transformer for Electronic Health Records](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32346050)

3. [Highly accurate protein structure prediction with AlphaFold](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34265844)

4. [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A35585198)

5. [An agentic AI system enhances clinical detection of immune-related adverse events in a multi-phase validation study](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42957896)

6. [Performance of a Large Language Model for Predicting Clinical and Radiographic Outcomes in Knee Osteoarthritis: Single-Center Prospective Observational Study](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A43019548)

7. [Large language models are unstable as autonomous medical evaluators across clinical tasks](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42995166)

## 引用文献と確認範囲

1. [nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation](https://pubmed.ncbi.nlm.nih.gov/33288961/) — 2020-12-07 / pmid:33288961 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A33288961)

2. [An agentic AI system enhances clinical detection of immune-related adverse events in a multi-phase validation study](https://pubmed.ncbi.nlm.nih.gov/42957896/) — 2026-10-29 / pmid:42957896 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42957896) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://pubmed.ncbi.nlm.nih.gov/42957896/)

3. [Performance of a Large Language Model for Predicting Clinical and Radiographic Outcomes in Knee Osteoarthritis: Single-Center Prospective Observational Study](https://pubmed.ncbi.nlm.nih.gov/43019548/) — 2026-11-12 / pmid:43019548 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A43019548) / 再確認: 2026-11-18、出版社本文の要旨・Methods。初版の本文確認記録も参照、[確認先](https://medinform.jmir.org/2026/1/e107092/)

4. [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597) — 2015-05-18 / arxiv:1505.04597 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1505.04597)

5. [Deep Patient: An Unsupervised Representation to Predict the Future of Patients from the Electronic Health Records](https://pubmed.ncbi.nlm.nih.gov/27185194/) — 2016-05-17 / pmid:27185194 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A27185194)

6. [BEHRT: Transformer for Electronic Health Records](https://pubmed.ncbi.nlm.nih.gov/32346050/) — 2020-04-28 / pmid:32346050 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32346050) / 再確認: 2026-11-18、要旨・図の説明、EHR入力とMLM事前学習、[確認先](https://pubmed.ncbi.nlm.nih.gov/32346050/)

7. [Med-BERT: pretrained contextualized embeddings on large-scale structured electronic health records for disease prediction](https://pubmed.ncbi.nlm.nih.gov/34017034/) — 2021-05-20 / pmid:34017034 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34017034)

8. [A foundation model for generalizable disease detection from retinal images](https://pubmed.ncbi.nlm.nih.gov/37704728/) — 2023-09-13 / pmid:37704728 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A37704728)

9. [Deep Learning for ECG Analysis: Benchmarks and Insights from PTB-XL](https://pubmed.ncbi.nlm.nih.gov/32903191/) — 2021-05-11 / pmid:32903191 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32903191)

10. [Highly accurate protein structure prediction with AlphaFold](https://pubmed.ncbi.nlm.nih.gov/34265844/) — 2021-07-15 / pmid:34265844 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34265844)

11. [Robust deep learning-based protein sequence design using ProteinMPNN](https://pubmed.ncbi.nlm.nih.gov/36108050/) — 2022-09-15 / pmid:36108050 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A36108050)

12. [De novo design of protein structure and function with RFdiffusion](https://pubmed.ncbi.nlm.nih.gov/37433327/) — 2023-07-11 / pmid:37433327 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A37433327) / 再確認: 2026-11-18、出版社の検索掲載本文、構造のノイズ除去と生成手順、[確認先](https://www.nature.com/articles/s41586-023-06415-8)

13. [Transparent reporting of a multivariable prediction model for individual prognosis or diagnosis (TRIPOD): the TRIPOD statement](https://pubmed.ncbi.nlm.nih.gov/25569120/) — 2015-01-07 / pmid:25569120 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A25569120)

14. [Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension](https://pubmed.ncbi.nlm.nih.gov/32908283/) — 2020-09-09 / pmid:32908283 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32908283)

15. [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://pubmed.ncbi.nlm.nih.gov/35585198/) — 2022-05-18 / pmid:35585198 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A35585198)

16. [External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients](https://pubmed.ncbi.nlm.nih.gov/34152373/) — 2021-06-21 / pmid:34152373 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34152373)

17. [From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents](https://arxiv.org/abs/2611.01527) — 2026-11-01 / arxiv:2611.01527 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.01527)

18. [A clinically applicable approach to continuous prediction of future acute kidney injury](https://pubmed.ncbi.nlm.nih.gov/31367026/) — 2019-07-31 / pmid:31367026 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A31367026)

19. [From Generative Molecular Design to Agentic Artificial Intelligence in Drug Discovery](https://pubmed.ncbi.nlm.nih.gov/42984375/) — 2026-11-12 / pmid:42984375 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42984375)

20. [Large language models are unstable as autonomous medical evaluators across clinical tasks](https://pubmed.ncbi.nlm.nih.gov/42995166) — 2026-11-06 / pmid:42995166 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42995166) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://pubmed.ncbi.nlm.nih.gov/42995166)

21. [Illusory generalizability of clinical prediction models](https://pubmed.ncbi.nlm.nih.gov/38207039/) — 2024-01-11 / pmid:38207039 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A38207039)

22. [ACR's Assess-AI: A Registry for Real-World Performance Monitoring of Clinical Imaging Artificial Intelligence](https://pubmed.ncbi.nlm.nih.gov/42066927) — 2026-04-29 / pmid:42066927 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42066927)

23. [From Forecasting to World Modeling: Can Temporal Foundation Models Recover Causal Response?](https://arxiv.org/abs/2611.15009) — 2026-11-11 / arxiv:2611.15009 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.15009) / 再確認: 2026-11-16、一次資料の要旨・該当記述、[確認先](https://arxiv.org/abs/2611.15009v1)

24. [The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process](https://arxiv.org/abs/1612.09328) — 2016-12-29 / arxiv:1612.09328 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1612.09328)

25. [Your Vision Foundation Model Is Secretly an EEG Foundation Model](https://arxiv.org/abs/2611.17031) — 2026-11-12 / arxiv:2611.17031 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17031) / 再確認: 2026-11-18、要旨、事例の方法・実験条件・報告値、[確認先](https://arxiv.org/abs/2611.17031v1)

26. [A Drosophila computational brain model reveals sensorimotor processing](https://pubmed.ncbi.nlm.nih.gov/39358519/) — 2024-10-02 / pmid:39358519 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A39358519) / 再確認: 2026-11-18、公開論文本文Connectome models・Computational modelling limitations・164予測の集計、[確認先](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11446845/fullTextXML)

27. [Clinically applicable deep learning for diagnosis and referral in retinal disease](https://pubmed.ncbi.nlm.nih.gov/30104768/) — 2018-08-13 / pmid:30104768 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A30104768)

28. [External validation of prognostic models: what, why, how, when and where?](https://pubmed.ncbi.nlm.nih.gov/33564405/) — 2020-11-24 / pmid:33564405 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A33564405)

29. [Large Language Model Influence on Diagnostic Reasoning: A Randomized Clinical Trial](https://pubmed.ncbi.nlm.nih.gov/39466245/) — 2024-10-28 / pmid:39466245 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A39466245)

30. [Double/Debiased Machine Learning for Treatment and Structural Parameters](https://arxiv.org/abs/1608.00060) — 2016-07-30 / arxiv:1608.00060 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1608.00060) / 再確認: 2026-11-18、要旨、直交スコアと交差適合、[確認先](https://arxiv.org/abs/1608.00060v7) / 照合先v7は表題がTreatment and Causal Parameters。ライブラリの登録原題と異なるが同一arXiv ID。

31. [Designing fiber-gut microbiome interactions with active learning](https://pubmed.ncbi.nlm.nih.gov/42509322) — 2026-07-27 / pmid:42509322 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=pmid%3A42509322)

## 収録範囲と読み方

対象は2026-11-16時点の収録スナップショット（基礎774件・新着264件）です。2026-11-18の改稿は、この範囲の技術・比較・事例の詳説です。

全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断レビューです。基礎・新着は収録先の区別で、古さは個々の公開日から確認できます。

技術の系譜、論文間の位置づけ、実験から導く解釈と次の課題は編者の整理です。直接の引用関係や商用普及率を確定するものではありません。

初版の22件に加え、改稿では25件の一次資料を確認しました（重複あり）。要旨・本文・検索掲載箇所の範囲を引用文献に記録しています。全件の全文精読や独立再現を意味しません。

数値は論文の報告値です。異なるデータ・分割・指標の比較を統一順位へ変換していません。説明用の計算例は実測値と区別しています。
