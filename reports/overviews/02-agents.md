# エージェント・検索・記憶・協調：技術と実験を詳しく読む

改稿: 2026-11-18 / 対象文献スナップショット: 2026-11-16 / 論文公開日上限: 2026-11-12

外部知識を検索する仕組みから、道具を使って環境を変え、経験を保存し、複数の役割を調整する仕組みへ進んだ。現在の境界は、局所的な成功を長い仕事全体の整合性へつなげられるかにある。

## まず押さえる到達点

検索付き回答、コード・Web操作、経験の再利用、複数エージェントによる調査を特定環境で実行。

任意の仕事を無監督で最後まで納品し、権限・費用・安全性も守れるとはいえない。 [1](https://arxiv.org/abs/2210.03629) [2](https://arxiv.org/abs/2611.17041) [3](https://arxiv.org/abs/2611.03412)

## 技術の中身と論文同士の関係

### RAGは知識への入口を変え、エージェントは環境への出口を変える

RAGの基本形は、質問に関連する文書を取り出し、その内容を条件に文章を生成する構成である。元の研究は重み中の知識と外部の文書索引を組み合わせ、生成全体で同じ文書を使う方式と、生成の位置ごとに異なる文書を使う方式を比較した。今日の検索付き回答を全て元論文と同じ学習方式と見なすのではなく、検索と生成を分ける考え方が基盤になったと捉えるとよい。 [5](https://arxiv.org/abs/2005.11401) [4](https://arxiv.org/abs/2004.04906)

検索で正しい文書が取れない失敗と、取れた文書を読み違える失敗は対処が違う。検索件数を増やすと取り逃しを減らせる場合がある一方、無関係な情報や悪意ある文章も入力へ入る。Self-RAGは検索や自己評価を生成の判断へ組み込み、Corrective RAGは検索結果の品質を判断する。どちらも、文書を付ければ根拠に忠実になるという単純な前提を見直している。 [6](https://arxiv.org/abs/2310.11511) [7](https://arxiv.org/abs/2401.15884) [16](https://arxiv.org/abs/2302.12173)

エージェントでは、出力が説明文で終わらず、検索、編集、API、ロボットなどへの行動となる。行動で環境が変わり、その観測が次の入力になるため、一つの誤りが次の問題設定まで変える。ReActの意義は考察文が長くなったことではなく、観測を取り直しながら行動を修正するループを明示した点にある。外部状態と会話ログを混同しない設計が重要になる。 [1](https://arxiv.org/abs/2210.03629) [8](https://arxiv.org/abs/2302.04761) [19](https://arxiv.org/abs/2209.07753)

このため、ツールを正しい形式で呼べること、適切な時点で呼べること、結果が要求を満たすことは別の段階になる。コードの構文が正しくても対象ファイルを間違えることはあり、Webのクリックが成功しても利用者の目的を満たさないことはある。AgentBench、WebArena、SWE-benchは、対象環境と完了条件を具体化することで、文章の評価から行動の評価へ移る役割を担った。 [26](https://arxiv.org/abs/2308.03688) [10](https://arxiv.org/abs/2307.13854) [9](https://arxiv.org/abs/2310.06770)

### 長期タスクでは、状態・仕様・検証の三つを失いやすい

長期の仕事が難しいのは、単に手順数が多いからではない。途中で判明した制約、変更された要件、自分が既に作った成果物の状態を後の判断へ持ち越す必要がある。DeliverBenchのように後工程が前の成果物へ依存する評価では、局所的に良い回答を並べても、全体が矛盾すれば納品としては低く評価される。 [3](https://arxiv.org/abs/2611.03412) [9](https://arxiv.org/abs/2310.06770)

説明用の単純な例として、各段階が独立に95%の確率で正しく、20段階の全成功が必要なら、全体の確率は0.95の20乗、約36%になる。これは特定モデルの実測値ではなく、局所精度だけで長い仕事を説明できないことを示す計算例だ。実際には失敗の相関や修復があり、同じ誤認が繰り返される場合も、人の介入で回復する場合もある。 [3](https://arxiv.org/abs/2611.03412)

仕様を保持する手段として、作業状態をファイルへ出す、検証可能な中間成果物を残す、決定と根拠を記録する、といった方式が考えられる。ただしログを保存しただけでは不十分で、次の判断時に必要な部分を取り出せる必要がある。会話の長文化、圧縮した要約、外部のファイルシステムは、同じ記憶量でも利用できる証拠が違う。 [13](https://arxiv.org/abs/2310.08560) [14](https://arxiv.org/abs/2307.03172) [17](https://arxiv.org/abs/2611.14320)

検証側にも境界がある。固定テストを通ることと、依頼者が求める成果物であることは一致しない場合があるし、成功条件の見せ方が近道を誘発することもある。したがって、課題の成功、仕様への適合、禁止された副作用の不在を別に記録することが必要になる。自律性を評価するときは、人が何回修正・再開したかも結果に含めるべきである。 [3](https://arxiv.org/abs/2611.03412) [21](https://arxiv.org/abs/2611.03575) [27](https://arxiv.org/abs/2611.08318)

### 記憶は増やすほど良いのではなく、適用条件を持つ知識として扱う

Reflexionが保存する言語的な教訓、Voyagerの実行可能なスキル、MemGPTの外部へ退避する記憶は、再利用単位が異なる。言語の教訓は幅広い仕事へ移しやすいが曖昧さが残り、コードは動かせる一方で前提とするAPIや環境へ依存する。外部記憶は容量を広げるが、何をいつ読み直すかという制御が必要になる。 [11](https://arxiv.org/abs/2303.11366) [12](https://arxiv.org/abs/2305.16291) [13](https://arxiv.org/abs/2310.08560)

ある失敗の後で書いた教訓が、失敗の真の原因を表すとは限らない。例えば「まず検索する」と保存しても、検索が必要でない仕事へ適用すれば余計な費用になるし、「前回と同じ修正」を環境の変化後に再利用すれば壊れる。成功・失敗のラベル一つから一般則を作ると、原因でない相関を覚える危険がある。記憶の正しさと、今回への適用可能性は二段階で確かめる必要がある。 [17](https://arxiv.org/abs/2611.14320) [11](https://arxiv.org/abs/2303.11366)

WikiTraceは、教訓を成功・失敗の説明と原軌跡へ結び付け、細部が不足したり教訓が衝突したりすると根拠へ降りて確認する。単に記憶を長くするのではなく、必要に応じて証拠を回収できる階層が中核である。これにより、誤った要約をそのまま信じる方式との差を検証できる。出典を持つ記憶は、性能だけでなく後からの監査にも接続する。 [17](https://arxiv.org/abs/2611.14320)

CoReMemが扱うように、記憶の価値は未来の未知課題での利益から読み書き費用を差し引いて考える必要がある。保存した情報の数や過去課題の再現率だけでは、次の仕事へ役立つかは分からない。記憶なし、同じ予算の単純検索、同じ教訓だけを使う対照などを置くことで、記憶方式が本当に追加した価値を評価しやすくなる。 [18](https://arxiv.org/abs/2611.17316) [17](https://arxiv.org/abs/2611.14320)

### 複数エージェントの利益は、並列化と責任分配を分けると見える

複数化の利益には、独立に調べて探索範囲を広げること、主担当の文脈から長い実行ログを分離すること、専門的な役割を分担することがある。一方、同じ情報を重複して探す、誤りを相互に補強する、引き継ぎで根拠が失われる、といった損失も増える。人数や会話量そのものを協調能力の指標にすることはできない。 [15](https://arxiv.org/abs/2308.08155) [2](https://arxiv.org/abs/2611.17041)

全員へ最終結果と同じ報酬を与えると、有用な報告をした担当が他の担当の誤りで罰され、誤った報告をした担当が他の成功に便乗することが起こる。LEAD-RLは、報告が役に立ったかを訓練中に判定し、受け継ぐチームの学習信号を調整する。最終回答の正否をチームの目的として残し、報告の寄与を報酬の誤配分を減らすために使う点が重要である。 [2](https://arxiv.org/abs/2611.17041)

並列実行では、全担当が消費したトークンの総和と、完了を待つ最長経路の費用は違う。並列の調査が増えれば総量が増えても待ち時間が短くなる可能性がある。逆に、報告を受けて主担当が逐次やり直せば並列化の利益は消える。LEAD-RLのコスト指標を読む際にも、何を足し、何を最大値としているかを確認し、金額や実測秒数と同一視しないことが必要になる。 [2](https://arxiv.org/abs/2611.17041)

現時点で示されているのは、特定の調査ベンチマークや実行環境で、役割と学習信号の設計が品質と費用の関係を改善することだ。組織の役割を模倣すれば実組織と同じ判断ができるという証拠ではない。複数担当へ増やす前に、単体の強い担当が同じ計算予算を使った対照と比べる必要がある。 [2](https://arxiv.org/abs/2611.17041) [15](https://arxiv.org/abs/2308.08155) [3](https://arxiv.org/abs/2611.03412)

## 手法を比較する

| 方法 | 何を変えるか | 得られる利点 | 前提と交換条件 |

| --- | --- | --- | --- |

| RAG | 根拠となる文書を検索し、生成の条件にする。 | 知識の更新と出典を外部へ置ける。 | 検索漏れ、文書の信頼性、読み違いを分けて検証する。 [5](https://arxiv.org/abs/2005.11401) [7](https://arxiv.org/abs/2401.15884) |

| ツール使用・ReAct | 行動と観測のループで環境を更新する。 | 外部計算や実行結果を次の判断へ使える。 | 実行形式の正しさと目的達成・副作用の不在は別。 [1](https://arxiv.org/abs/2210.03629) [8](https://arxiv.org/abs/2302.04761) |

| 経験記憶・スキル | 過去の教訓や実行可能な解法を再利用する。 | 毎回の探索や同じ失敗を減らせる。 | 誤った一般化、環境の陳腐化、参照費用が生じる。 [12](https://arxiv.org/abs/2305.16291) [17](https://arxiv.org/abs/2611.14320) [18](https://arxiv.org/abs/2611.17316) |

| 複数担当の協調 | 調査・実行を分け、報告を統合する。 | 並列化と文脈の分離を利用できる。 | 寄与の評価、重複、通信・統合の費用を含める。 [15](https://arxiv.org/abs/2308.08155) [2](https://arxiv.org/abs/2611.17041) |

| 固定プログラムへの技能化 | 開発中の推論を、再実行できるコードへ残す。 | 同じ課題の再実行でモデルへの逐次依存を減らす。 | 作った技能の前提が変わると再検証・改修が必要。 [19](https://arxiv.org/abs/2209.07753) [20](https://arxiv.org/abs/2611.16872) |

## 具体的研究を読み解く

### WikiTraceの比較で分かること、分からないこと

**研究の問い**: 失敗のラベルから抽出した教訓を信じるため、記憶のないモデルなら解ける課題をかえって失敗することがある。問うべきなのは保存量ではなく、根拠へ戻る設計がこの悪化を減らすかである。

**設計と対照**: 短い教訓、成功・失敗の説明、原軌跡を結び、必要時に端末のツールで下位の証拠を読む。既存の記憶法に加えて、同じ教訓だけを与える対照とも比較する。

**論文が報告する結果**: 5エージェントベンチマークで性能と記憶による悪化の減少を報告した。要旨には全条件を一つにまとめた改善率はないため、数値を補って万能な利益として示さない。

**位置づけ・編者の解釈**: 編者の解釈では、同じ教訓の対照は重要である。抽出された教訓そのものの良さと、証拠を確認できる構造の価値を切り分ける方向の実験だからだ。ただし、参照を多くしたことによる追加計算の寄与も合わせて読む必要がある。

**結論の範囲**: この評価から、何年も更新し続けた個人記憶の正確性や、秘密情報を含む原記録の安全な管理まで確認されたとは言えない。性能上の記憶問題と権限・保持期間の問題は別に残る。

[17](https://arxiv.org/abs/2611.14320) [18](https://arxiv.org/abs/2611.17316)

### DeliverBenchが測るのは、単発回答でなく依存する成果物の連鎖

**研究の問い**: 一つずつの課題で高得点を取る構成が、資料追加や依頼者の意見変更を受けながら仕事全体を完了できるかを問う。前の誤りを引き継ぐ仕組みが、単発ベンチマークと異なる。

**設計と対照**: 実資料と13人の専門家を基に、11プロジェクト・150下位課題を構成し、各仕事で2〜15回の資料・フィードバック追加を行う。個別提出物と最終の納品物をルーブリックで評価する。

**論文が報告する結果**: 7モデル・実行基盤の構成を比較した最高値は、最終納品65.0/100、90点を閾値にした下位課題合格率50.0%。この65点は一般的な仕事の成功率65%を意味しない。

**位置づけ・編者の解釈**: 編者の解釈では、進歩の単位を「難しい問題の正答」から「変化する仕様に対する一貫した成果物」へ広げる評価である。記憶、計画、根拠管理、検証の改善が同じ仕事全体に寄与するかを調べる接点になる。

**結論の範囲**: 11プロジェクトは実業務全体の無作為標本ではなく、専門家採点にも定義がある。別の職種・言語・会社の生産性を、この点数から直接推定しない。

[3](https://arxiv.org/abs/2611.03412) [9](https://arxiv.org/abs/2310.06770) [21](https://arxiv.org/abs/2611.03575)

## 基礎からの積み上げ

### 検索で知識を外に持つ

DPRとRAGは、モデルの重みだけに依存せず、文書を探して回答に使う構成を整えた。Self-RAGやCorrective RAGは、検索する必要や検索結果の質も判断対象にした。 [4](https://arxiv.org/abs/2004.04906) [5](https://arxiv.org/abs/2005.11401) [6](https://arxiv.org/abs/2310.11511) [7](https://arxiv.org/abs/2401.15884)

### 推論と道具の実行をつなぐ

ReActは考察と行動・観測を交互に進め、Toolformerは道具の使用を学習対象にした。SWE-benchとWebArenaにより、外部環境で目的を達成する能力を測れるようになった。 [1](https://arxiv.org/abs/2210.03629) [8](https://arxiv.org/abs/2302.04761) [9](https://arxiv.org/abs/2310.06770) [10](https://arxiv.org/abs/2307.13854)

### 経験を次の仕事へ持ち越す

Reflexionの言語による反省、Voyagerの実行可能なスキル、MemGPTのメモリ管理は、経験を再利用する異なる単位を示した。長い履歴を持つだけで必要な情報を使えるとは限らない。 [11](https://arxiv.org/abs/2303.11366) [12](https://arxiv.org/abs/2305.16291) [13](https://arxiv.org/abs/2310.08560) [14](https://arxiv.org/abs/2307.03172)

### 役割分担から協調の学習へ

AutoGenなどの複数役割の構成から、誰の調査が最終回答へ寄与したかを学習するLEAD-RLへ接続する。複数化自体ではなく、情報の受け渡しと評価が課題になる。 [15](https://arxiv.org/abs/2308.08155) [2](https://arxiv.org/abs/2611.17041)

## 到達点・適用条件・残る境界

### 根拠を探して回答する — 比較が蓄積

できていること: 検索した文書を根拠に回答し、質問に応じて検索・再検索の仕方を変えられる。

条件: 信頼できる文書、更新管理、引用先と記述の対応確認が必要になる。

残る境界: 検索で取り逃した事実、検索先の誤情報、外部文書の悪意ある命令までは自動的に解決しない。 [5](https://arxiv.org/abs/2005.11401) [6](https://arxiv.org/abs/2310.11511) [7](https://arxiv.org/abs/2401.15884) [16](https://arxiv.org/abs/2302.12173)

### 長い仕事と複数役割を進める — 限定条件で実証

できていること: コード修正・Web操作・調査の複数手順を、環境の観測と修正を繰り返しながら進められる。

条件: 実行環境、成功条件、費用、途中成果物の整合性、人の介入点を明確にする。

残る境界: 単発課題の成績が高くても、変わる要件と依存する成果物を含む最終納品の品質は別問題である。 [9](https://arxiv.org/abs/2310.06770) [10](https://arxiv.org/abs/2307.13854) [2](https://arxiv.org/abs/2611.17041) [3](https://arxiv.org/abs/2611.03412)

### 記憶を選んで再利用する — 限定条件で実証

できていること: 過去の経験を教訓・コード・原記録として保存し、根拠をたどって使い分ける研究が進む。

条件: 記憶なしの対照と比較し、記憶の読み書き費用、古さ、適用条件を測る。

残る境界: 誤った教訓や正しい教訓の誤用で、記憶なしより悪化する。蓄積量だけでは改善を判断できない。 [11](https://arxiv.org/abs/2303.11366) [12](https://arxiv.org/abs/2305.16291) [17](https://arxiv.org/abs/2611.14320) [18](https://arxiv.org/abs/2611.17316)

### 実機で使えるスキルをプログラムに残す — 限定条件で実証

できていること: 人間の実演とシミュレーションを必要時に用い、実機で繰り返し実行する固定プログラムを作れる。

条件: センサ・制御APIと対象課題を固定し、開発試行と評価試行を分ける。

残る境界: 少数の実機課題での信頼性から、未知の物体・機体・環境での汎用自律性までは言えない。 [19](https://arxiv.org/abs/2209.07753) [20](https://arxiv.org/abs/2611.16872)

## 関連する直近研究

### LEAD-RL：調査の貢献を評価する

5ベンチマーク・2モデル系列で評価。BrowseCompで共有チーム報酬方式より正答率2.49ポイント増、実行のクリティカルパスに沿った費用24.5%減。実組織の調査全体の効率を直接測った結果ではない。 [2](https://arxiv.org/abs/2611.17041)

### ACE-CaP-0：開発と実行を分ける

8実機操作課題で固定したプログラムを各30回評価し、221/240試行に成功。評価時にも知覚・制御は動くが、人間やコード生成エージェントは介入しない。開発方法の比較は1課題・各条件1回である。 [20](https://arxiv.org/abs/2611.16872)

## 次の課題（編者の整理）

### 記憶・探索・協調の純増分を測る

モデルの強さ、試行回数、長い入力の効果と、新しい記憶・協調方式の効果を分離する対照が重要になる。 [17](https://arxiv.org/abs/2611.14320) [18](https://arxiv.org/abs/2611.17316) [2](https://arxiv.org/abs/2611.17041)

### 仕事の完了をどう定義するか

一部のテスト通過に加え、要件変更、成果物間の矛盾、有害な副作用、権限と費用の遵守を評価に含める必要がある。 [3](https://arxiv.org/abs/2611.03412) [21](https://arxiv.org/abs/2611.03575)

## 分野間の接点（編者の整理）

- [評価・安全性・解釈可能性](https://drkamoshika.github.io/papers/?view=map&topic=trust): 環境を変更できるようになるほど、正答率に加えてアクセス権・情報漏洩・副作用を測る必要がある。 [22](https://arxiv.org/abs/2406.13352) [21](https://arxiv.org/abs/2611.03575)

- [次イベント予測・点過程](https://drkamoshika.github.io/papers/?view=map&topic=events): 次の行動を予測することと、望ましい行動を選ぶことは別。介入の価値を評価する必要がある。 [23](https://arxiv.org/abs/2111.07603) [24](https://arxiv.org/abs/2611.09792)

- [神経科学とAI](https://drkamoshika.github.io/papers/?view=map&topic=neuroscience): 記憶の分業や再利用は脳の学習理論とも接点があるが、同じ機構を実装した証拠とは区別する。 [13](https://arxiv.org/abs/2310.08560) [25](https://pubmed.ncbi.nlm.nih.gov/7624455/)

## 読む順番

1. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2005.11401)

2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2210.03629)

3. [Reflexion: Language Agents with Verbal Reinforcement Learning](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2303.11366)

4. [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2310.06770)

5. [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14320)

6. [From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17041)

7. [DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.03412)

## 引用文献と確認範囲

1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — 2022-10-06 / arxiv:2210.03629 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2210.03629)

2. [From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research](https://arxiv.org/abs/2611.17041) — 2026-11-12 / arxiv:2611.17041 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17041) / 再確認: 2026-11-18、本文Introduction・Method概要、寄与の信用割当、[確認先](https://arxiv.org/html/2611.17041v1)

3. [DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://arxiv.org/abs/2611.03412) — 2026-11-02 / arxiv:2611.03412 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.03412) / 再確認: 2026-11-18、要旨、事例の方法・実験条件・報告値、[確認先](https://arxiv.org/abs/2611.03412v3)

4. [Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906) — 2020-04-10 / arxiv:2004.04906 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2004.04906)

5. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — 2020-05-22 / arxiv:2005.11401 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2005.11401) / 再確認: 2026-11-18、要旨、RAGの構成と二方式、[確認先](https://arxiv.org/abs/2005.11401)

6. [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511) — 2023-10-17 / arxiv:2310.11511 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2310.11511)

7. [Corrective Retrieval Augmented Generation](https://arxiv.org/abs/2401.15884) — 2024-01-29 / arxiv:2401.15884 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2401.15884)

8. [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — 2023-02-09 / arxiv:2302.04761 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2302.04761)

9. [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — 2023-10-10 / arxiv:2310.06770 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2310.06770)

10. [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) — 2023-07-25 / arxiv:2307.13854 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.13854)

11. [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — 2023-03-20 / arxiv:2303.11366 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2303.11366)

12. [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — 2023-05-25 / arxiv:2305.16291 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.16291)

13. [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — 2023-10-12 / arxiv:2310.08560 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2310.08560)

14. [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — 2023-07-06 / arxiv:2307.03172 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.03172)

15. [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) — 2023-08-16 / arxiv:2308.08155 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2308.08155)

16. [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — 2023-02-23 / arxiv:2302.12173 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2302.12173)

17. [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320) — 2026-11-10 / arxiv:2611.14320 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14320) / 再確認: 2026-11-18、要旨、事例の方法・実験条件・報告値、[確認先](https://arxiv.org/abs/2611.14320v1)

18. [CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation](https://arxiv.org/abs/2611.17316) — 2026-11-12 / arxiv:2611.17316 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17316)

19. [Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753) — 2022-09-16 / arxiv:2209.07753 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2209.07753)

20. [ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience](https://arxiv.org/abs/2611.16872) — 2026-11-12 / arxiv:2611.16872 / 登録時の確認範囲: 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.16872)

21. [VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](https://arxiv.org/abs/2611.03575) — 2026-11-02 / arxiv:2611.03575 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.03575)

22. [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352) — 2024-06-19 / arxiv:2406.13352 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2406.13352)

23. [Counterfactual Temporal Point Processes](https://arxiv.org/abs/2111.07603) — 2021-11-15 / arxiv:2111.07603 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2111.07603)

24. [Knowing When to Intervene: Causal Evaluation of AI Agents](https://arxiv.org/abs/2611.09792) — 2026-11-06 / arxiv:2611.09792 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.09792)

25. [Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory](https://pubmed.ncbi.nlm.nih.gov/7624455/) — 公開日未確認 / pmid:7624455 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A7624455)

26. [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) — 2023-08-07 / arxiv:2308.03688 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2308.03688)

27. [Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement](https://arxiv.org/abs/2611.08318) — 2026-11-05 / arxiv:2611.08318 / 登録時の確認範囲: 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.08318)

## 収録範囲と読み方

対象は2026-11-16時点の収録スナップショット（基礎774件・新着264件）です。2026-11-18の改稿は、この範囲の技術・比較・事例の詳説です。

全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断レビューです。基礎・新着は収録先の区別で、古さは個々の公開日から確認できます。

技術の系譜、論文間の位置づけ、実験から導く解釈と次の課題は編者の整理です。直接の引用関係や商用普及率を確定するものではありません。

初版の22件に加え、改稿では25件の一次資料を確認しました（重複あり）。要旨・本文・検索掲載箇所の範囲を引用文献に記録しています。全件の全文精読や独立再現を意味しません。

数値は論文の報告値です。異なるデータ・分割・指標の比較を統一順位へ変換していません。説明用の計算例は実測値と区別しています。
