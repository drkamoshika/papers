# 神経科学とAI：基礎から現在へのレビュー

レビュー日: 2026-11-16。収録論文の公開日上限: 2026-11-12。

配線図、集団活動、学習・記憶、AIとの表現比較を重ねることで、脳を検証可能なモデルとして調べられる範囲が広がった。ハエの大規模な回路地図と、人の脳を全て再現できることの間には、対象・解像度・機能同定の大きな隔たりがある。

収録基礎文献 106件／本レビューで引用する基礎文献 30件・新着論文 3件。分野横断の文献を含み、件数は引用IDの集合から計算。

## いま何ができるか

ハエの回路追跡、マウス局所の構造と活動の対応、人の粗視化ネットワーク解析や条件付きの信号復号。

収録研究は、人間全脳の細胞レベル再現や、配線図だけでの感情・意識の説明までは示していない。 [1](https://pubmed.ncbi.nlm.nih.gov/39358518/) [2](https://pubmed.ncbi.nlm.nih.gov/40205214/) [3](https://pubmed.ncbi.nlm.nih.gov/38723085/) [4](https://pubmed.ncbi.nlm.nih.gov/37127759/)

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

## 直近研究の位置づけ

### 2024〜2026：ハエは脳から中枢全体と性差へ

成虫脳の資源は139,255ニューロンを報告し、2026年の雄中枢神経系資源は脳と神経索を含む166,700ニューロンと11,710型を報告。別の脳・神経索資源は局所フィードバックと分散的な制御を分析する。標本と版の異なる数値を一つの地図として足し合わせない。 [1](https://pubmed.ncbi.nlm.nih.gov/39358518/) [20](https://pubmed.ncbi.nlm.nih.gov/42691995/) [21](https://pubmed.ncbi.nlm.nih.gov/42259917/)

### MICrONSと人の局所EM：構造と機能の対応へ

MICrONSは約75,000ニューロンの機能記録と、20万超の細胞・約5億シナプスを含む局所地図を対応。人の約1立方mmの局所EMは約57,000細胞・約1.5億シナプスで、細胞数にはグリアも含む。いずれも人間全脳の単一細胞地図ではない。 [2](https://pubmed.ncbi.nlm.nih.gov/40205214/) [3](https://pubmed.ncbi.nlm.nih.gov/38723085/)

### SeeEEG：専用の大規模事前学習だけが道ではない

凍結DINOv3 ViT-BへEEGを画像として提示し、表示方法を学習する構成が、8データセット全てで7種の凍結EEG基盤モデルよりbalanced accuracyで良かった。全モデルの再学習比較や前向き臨床評価ではない。 [23](https://arxiv.org/abs/2611.17031)

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

## 参考文献と確認範囲

1. [Neuronal wiring diagram of an adult brain](https://pubmed.ncbi.nlm.nih.gov/39358518/) — 2024-10-02 / pmid:39358518 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A39358518)

2. [Functional connectomics spanning multiple areas of mouse visual cortex](https://pubmed.ncbi.nlm.nih.gov/40205214/) — 2025-04-09 / pmid:40205214 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A40205214) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://pubmed.ncbi.nlm.nih.gov/40205214/)

3. [A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution](https://pubmed.ncbi.nlm.nih.gov/38723085/) — 2024-05-10 / pmid:38723085 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A38723085) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://pubmed.ncbi.nlm.nih.gov/38723085/)

4. [Semantic reconstruction of continuous language from non-invasive brain recordings](https://pubmed.ncbi.nlm.nih.gov/37127759/) — 2023-05-01 / pmid:37127759 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A37127759)

5. [A neural substrate of prediction and reward](https://pubmed.ncbi.nlm.nih.gov/9054347/) — 1997-03-14 / pmid:9054347 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A9054347)

6. [Spike timing-dependent plasticity: a Hebbian learning rule](https://pubmed.ncbi.nlm.nih.gov/18275283/) — 2008-07-21 / pmid:18275283 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A18275283)

7. [Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory](https://pubmed.ncbi.nlm.nih.gov/7624455/) — 公開日未確認 / pmid:7624455 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A7624455)

8. [Backpropagation and the brain](https://pubmed.ncbi.nlm.nih.gov/32303713/) — 2020-04-17 / pmid:32303713 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32303713)

9. [Neural population dynamics during reaching](https://pubmed.ncbi.nlm.nih.gov/22722855/) — 2012-07-05 / pmid:22722855 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A22722855)

10. [Gaussian-process factor analysis for low-dimensional single-trial analysis of neural population activity](https://pubmed.ncbi.nlm.nih.gov/19357332/) — 2009-04-08 / pmid:19357332 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A19357332)

11. [Neural population geometry: An approach for understanding biological and artificial neural networks](https://pubmed.ncbi.nlm.nih.gov/34801787/) — 2021-11-19 / pmid:34801787 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A34801787)

12. [Single-trial neural dynamics are dominated by richly varied movements](https://pubmed.ncbi.nlm.nih.gov/31551604/) — 2019-09-24 / pmid:31551604 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A31551604)

13. [The WU-Minn Human Connectome Project: an overview](https://pubmed.ncbi.nlm.nih.gov/23684880/) — 2013-05-16 / pmid:23684880 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A23684880)

14. [The organization of the human cerebral cortex estimated by intrinsic functional connectivity](https://pubmed.ncbi.nlm.nih.gov/21653723/) — 2011-06-08 / pmid:21653723 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A21653723)

15. [Predicting human resting-state functional connectivity from structural connectivity](https://pubmed.ncbi.nlm.nih.gov/19188601/) — 2009-02-02 / pmid:19188601 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A19188601)

16. [A Drosophila computational brain model reveals sensorimotor processing](https://pubmed.ncbi.nlm.nih.gov/39358519/) — 2024-10-02 / pmid:39358519 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A39358519)

17. [Connectome-constrained networks predict neural activity across the fly visual system](https://pubmed.ncbi.nlm.nih.gov/39261740/) — 2024-09-11 / pmid:39261740 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A39261740)

18. [Performance-optimized hierarchical models predict neural responses in higher visual cortex](https://pubmed.ncbi.nlm.nih.gov/24812127/) — 2014-05-08 / pmid:24812127 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A24812127)

19. [Brains and algorithms partially converge in natural language processing](https://pubmed.ncbi.nlm.nih.gov/35173264/) — 2022-02-16 / pmid:35173264 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A35173264)

20. [Sexual dimorphism in the complete Drosophila male central nervous system connectome](https://pubmed.ncbi.nlm.nih.gov/42691995/) — 2026-09-03 / pmid:42691995 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A42691995) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://pubmed.ncbi.nlm.nih.gov/42691995/)

21. [Distributed control circuits across a brain-and-cord connectome](https://pubmed.ncbi.nlm.nih.gov/42259917/) — 2026-06-08 / pmid:42259917 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A42259917) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://pubmed.ncbi.nlm.nih.gov/42259917/)

22. [The challenge of mapping the human connectome based on diffusion tractography](https://pubmed.ncbi.nlm.nih.gov/29116093/) — 2017-11-07 / pmid:29116093 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A29116093)

23. [Your Vision Foundation Model Is Secretly an EEG Foundation Model](https://arxiv.org/abs/2611.17031) — 2026-11-12 / arxiv:2611.17031 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17031) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.17031v1)

24. [Continuous-Latent Predictive Modeling with Semantic Alignment for EEG-Language Foundation Models](https://arxiv.org/abs/2608.11656) — 2026-08-12 / arxiv:2608.11656 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2608.11656)

25. [The hippocampus as a predictive map](https://pubmed.ncbi.nlm.nih.gov/28967910/) — 2017-10-02 / pmid:28967910 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A28967910)

26. [A distributional code for value in dopamine-based reinforcement learning](https://pubmed.ncbi.nlm.nih.gov/31942076/) — 2020-01-15 / pmid:31942076 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A31942076)

27. [A solution to the learning dilemma for recurrent networks of spiking neurons](https://pubmed.ncbi.nlm.nih.gov/32681001/) — 2020-07-17 / pmid:32681001 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A32681001)

28. [The influence of head motion on intrinsic functional connectivity MRI](https://pubmed.ncbi.nlm.nih.gov/21810475/) — 2011-07-23 / pmid:21810475 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A21810475)

29. [Benchmarking of participant-level confound regression strategies for the control of motion artifact in studies of functional connectivity](https://pubmed.ncbi.nlm.nih.gov/28302591/) — 2017-03-14 / pmid:28302591 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A28302591)

30. [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320) — 2026-11-10 / arxiv:2611.14320 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14320) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.14320v1)

31. [A Differentiable Point Process with Its Application to Spiking Neural Networks](https://arxiv.org/abs/2106.00901) — 2021-06-02 / arxiv:2106.00901 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2106.00901)

32. [Dopamine neurons report an error in the temporal prediction of reward during learning](https://pubmed.ncbi.nlm.nih.gov/10195164/) — 公開日未確認 / pmid:10195164 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A10195164)

33. [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://pubmed.ncbi.nlm.nih.gov/35585198/) — 2022-05-18 / pmid:35585198 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A35585198)

## このレビューの範囲

母集団はこのライブラリの収録論文。全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断的レビューです。

基礎文献・新着論文は収録先の区別です。基礎文献側にも2026年の研究が含まれるため、古さや新しさは個々の公開日で確認できます。

技術の系譜、分野間の接点、次の課題は編者の整理であり、論文間の直接の引用関係や、商用普及の程度を確定するものではありません。

個別論文の確認範囲は要旨または本文の関連箇所です。今回、代表的な22件の一次資料を追加で照合しました。全件の全文再精読や独立再現を意味しません。

実験の数字は論文の報告値です。異なるデータ・分割・指標の数値を統一順位へ変換していません。

[7分野の全体マップ](https://drkamoshika.github.io/papers/?view=map)
