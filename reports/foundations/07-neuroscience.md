# 基礎文献 — 神経科学とAI

> schema_version: 1
> report_date: 2026-11-15

## ダイジェスト

選定106件中、一次資料へ照合した106件を掲載する。要旨確認と本文の関連箇所確認を区別し、要旨にない数値は補わない。「編者の注意」は著者の自己申告した限界と区別する。

研究の流れ・読み順・比較軸は[総覧](README.md)を参照。

## 完全版レポート

### Paper: Reactivation of hippocampal ensemble memories during sleep
- Source: PubMed
- Canonical ID: pmid:8036517
- Publication date: 1994-07-29
- URL: https://pubmed.ncbi.nlm.nih.gov/8036517/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 経験中に共活動したplace cellが、後の睡眠で再び共活動しやすくなる。
- Objective: 記憶固定の理論が予測する睡眠中の再活性化を検証する。
- Methods: rat3匹で多数の海馬細胞を同時記録し、空間課題の前後の徐波睡眠を比較する。
- Data and results: 同じ場所で発火した細胞群だけで、課題後の共発火が増加し、睡眠session中に徐々に弱まった。
- Novelty: 行動の経験が、後の睡眠の集団活動へ再表出する証拠を示す。
- Limitations: 共発火の再活性化を測った研究で、完全な順序付き軌跡の再生を示したという説明とは区別する。標本は3匹。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/8036517/

### Paper: A neural substrate of prediction and reward
- Source: PubMed
- Canonical ID: pmid:9054347
- Publication date: 1997-03-14
- URL: https://pubmed.ncbi.nlm.nih.gov/9054347/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: dopamine応答を、報酬予測の変化・誤差と適応制御の理論へ結び付ける。
- Objective: 報酬を得る際のドーパミン神経の応答を、単に快い刺激への反応として説明すると、報酬を予期できるようになった後の発火変化や、期待した報酬が来なかった場合の低下を統一して説明できない。学習による将来報酬の予測更新という共通の計算概念で説明できるかを検討した。
- Methods: 動物行動・中脳ドーパミン神経の電気生理研究を、時間差学習の報酬予測誤差という理論へ対応させる統合研究。予期しない報酬、報酬を予告する刺激、予期した報酬の欠落という条件で神経応答がどう変わるかを比較して解釈した。新たな大規模患者実験や機械学習ベンチマークの論文ではない。
- Data and results: 予期しない報酬では短い活動増加、報酬を予告する刺激へ学習が進むと反応が移動、期待した報酬が現れない場合は活動低下というパターンを報酬予測誤差で解釈できると示した。単一の統一性能スコアを出したのではなく、異なる実験現象を同じ学習信号の枠組みで説明したことが成果である。
- Novelty: 強化学習で使う『予測と実際との差によって価値推定を修正する』という計算と、神経活動で見える時間的な応答を結びつけた。機械学習の更新則を神経科学へ持ち込むだけでなく、時間的な予測誤差が生理的な信号として意味を持つ可能性を示した。
- Limitations: 既存実験を統合した理論的解釈であり、ドーパミン神経のあらゆる活動を単一の報酬予測誤差へ還元するものではない。学習と行動への因果的な寄与や、不確実性・複数次元の価値表現は後続の実証・理論と合わせて読む必要がある。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/9054347/

### Paper: Interpreting neuronal population activity by reconstruction: unified framework with application to hippocampal place cells
- Source: PubMed
- Canonical ID: pmid:9463459
- Publication date: 1998-02-01
- URL: https://pubmed.ncbi.nlm.nih.gov/9463459/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: population発火から位置などを復元するBayes・基底関数の方法を統一整理する。
- Objective: 神経集団に含まれる情報量と、読み出しの精度を定量化する。
- Methods: 自由行動ratの海馬place cellで複数decoderを比較し、情報理論的な最小誤差とも対比する。
- Data and results: 連続性制約を持つBayes法が高精度で、最良誤差は理論限界の2倍以内。停止時には推定位置が飛ぶ現象も報告。
- Novelty: decoder比較を、表現の情報限界と共通の神経網実装へ結ぶ。
- Limitations: 編者の注意: 連続性の事前情報が精度へ寄与する。decoderで復元できることは脳が同じ読み出しを使う証明ではない。
- Publication date note: 出版社Journal of NeurophysiologyにPublished online: 1 February 1998と明示。便宜的な月初補完ではなく、その日付を採用。出典: https://journals.physiology.org/doi/full/10.1152/jn.1998.79.2.1017

### Paper: Stable Hebbian learning from spike timing-dependent plasticity
- Source: PubMed
- Canonical ID: pmid:11102489
- Publication date: 2000-12-01
- URL: https://pubmed.ncbi.nlm.nih.gov/11102489/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 重みに依存するSTDPを使い、安定したHebbian学習をモデル化する。
- Objective: 可塑性の安定性に、synapse間競争が必須かを調べる。
- Methods: 強いsynapseほど増強が小さく、抑圧は強度に依存しないruleをrandom入力でsimulationする。
- Data and results: 安定・単峰・正の歪みを持つ重み分布が生じる。競争は別の活動依存scale機構で加えられると示す。
- Novelty: 安定な可塑性と競争を、常に同居する機構として扱わず分離する。
- Limitations: モデル研究であり、分布の実測との類似が生体の唯一の機構を示すわけではない。重み依存のruleが結果の前提。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/11102489/

### Paper: Functional connectivity in the resting brain: a network analysis of the default mode hypothesis
- Source: PubMed
- Canonical ID: pmid:12506194
- Publication date: 2002-12-27
- URL: https://pubmed.ncbi.nlm.nih.gov/12506194/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 安静時の相関からdefault mode networkのまとまりを検証する。
- Objective: 安静・視覚処理・認知課題で、default系がどう変わるかを調べる。
- Methods: 作業記憶で活動が下がるPCC・vACCをseedとし、安静と視覚課題の結合、前頭領域との相関を分析する。
- Data and results: PCCとdefault系の強い結合、安静と視覚課題で似た地図、外側前頭領域との逆相関を報告。
- Novelty: default系を単なる活動減少の領域群でなく、結合したnetworkとして検証する。
- Limitations: 編者の注意: 相関・逆相関は情報の向きや直接抑制を証明せず、処理手順の影響も考慮する必要がある。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/12506194/

### Paper: Discrete coding of reward probability and uncertainty by dopamine neurons
- Source: PubMed
- Canonical ID: pmid:12649484
- Publication date: 2003-03-21
- URL: https://pubmed.ncbi.nlm.nih.gov/12649484/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: dopamineの速い応答と持続的変化が、報酬確率と不確実性を別々に反映する。
- Objective: 予測誤差に加えて、不確実性がどのように符号化されるかを調べる。
- Methods: 刺激で報酬確率を操作し、dopamine neuronのphasic応答と報酬時刻までの漸増活動を測る。
- Data and results: phasic応答は確率に沿って単調変化し、漸増活動は確率0.5で最大となる不確実性と共変した。
- Novelty: 予測される報酬と、その予測の不確実性を時間的に区別する。
- Limitations: 編者の注意: reward不確実性の課題であり、任意の認知的不確実性や主観的risk選好を直接説明したものではない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/12649484/

### Paper: Midbrain dopamine neurons encode a quantitative reward prediction error signal
- Source: PubMed
- Canonical ID: pmid:15996553
- Publication date: 2005-07-07
- URL: https://pubmed.ncbi.nlm.nih.gov/15996553/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: dopamine単一細胞の活動が、正の報酬予測誤差を定量的に表すことを示す。
- Objective: 強化学習の誤差信号と実際の発火の数値的関係を検証する。
- Methods: juice報酬を得る眼球運動を試行錯誤で学ぶ課題で、報酬履歴とneuron活動を対応付ける。
- Data and results: 現在の報酬と過去報酬の加重平均との差を、期待より良い結果で符号化。行動方策への影響が弱くても信号は続いた。
- Novelty: 理論の予測誤差を、報酬履歴に基づく定量的な発火予測へ落とす。
- Limitations: 論文の定量結果は正の誤差側が中心。編者の注意: 正負両方向を対称な精度で符号化するという結果へ広げない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/15996553/

### Paper: Dynamic predictive coding by the retina
- Source: PubMed
- Canonical ID: pmid:16001064
- Publication date: 2005-07-07
- URL: https://pubmed.ncbi.nlm.nih.gov/16001064/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 網膜が新しい視覚統計へ数秒で適応し、予測的な符号化を変えることを示す。
- Objective: 環境の平均統計に固定された符号化を超え、動的適応を調べる。
- Methods: 異なる視覚環境で神経節細胞の時空間受容野を測り、可塑的synapseを持つモデルと比較する。
- Data and results: 数秒の受容野変化が新環境の予測符号化を改善し、network modelが多様な適応を説明する。
- Novelty: 予測符号化を、進化で固定した戦略だけでなく短期の動的調整へ広げる。
- Limitations: 編者の注意: 網膜の局所的な符号化の研究であり、皮質の高次の予測処理と同一の機構を実証するものではない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/16001064/

### Paper: The human connectome: A structural description of the human brain
- Source: PubMed
- Canonical ID: pmid:16201007
- Publication date: 2005-09-30
- URL: https://pubmed.ncbi.nlm.nih.gov/16201007/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 人間のconnectomeを収集・保存・共有する研究戦略を提案した概念的基礎論文。
- Objective: ほぼ未知だった人間の解剖学的接続行列を、共同研究の目標に据える。
- Methods: 他の哺乳類の資源と人間の不足を整理し、接続地図を作る研究戦略と影響を論じる。
- Data and results: 新たな完成脳地図や予測実験ではなく、human connectome研究を進める構想を提示する。
- Novelty: connectomeを神経科学の基盤情報として明確に定義・提案する。
- Limitations: 2005年時点の計画論文であり、現在の全細胞単位の人間全脳地図の完成を報告したものではない。
- Publication date note: 出版社PLOSのPublished: September 30, 2005を確認。PubMedの年月だけの記録を補い、論文公開日として採用。出典: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0010042

### Paper: Dopamine-dependent prediction errors underpin reward-seeking behaviour in humans
- Source: PubMed
- Canonical ID: pmid:16929307
- Publication date: 2006-08-23
- URL: https://pubmed.ncbi.nlm.nih.gov/16929307/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 人間でdopamine機能を薬理操作し、報酬予測誤差と選択を結び付ける。
- Objective: 動物の理論を、人間の線条体応答と学習へ対応付ける。
- Methods: L-DOPAとhaloperidolを用い、道具的学習中の線条体信号と行動を行動価値学習モデルで解析する。
- Data and results: 薬物条件で予測誤差信号が変わり、L-DOPA群はhaloperidol群より高報酬の行動を選びやすかった。モデルも選択を再現する。
- Novelty: dopamine・線条体予測誤差・人の選択の間を、薬理操作で検討する。
- Limitations: 編者の注意: 薬物には複数の作用があり、fMRI信号の変化を単一neuronの発火へ直接対応付けない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/16929307/

### Paper: Unsupervised learning of visual features through spike timing dependent plasticity
- Source: PubMed
- Canonical ID: pmid:17305422
- Publication date: 2007-01-02
- URL: https://pubmed.ncbi.nlm.nih.gov/17305422/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 非同期のspiking視覚網で、STDPから中間的な視覚特徴が生じる。
- Objective: 速く選択的な応答を、spike時刻と局所学習で説明する。
- Methods: 腹側視覚路を模すfeedforward網へ自然画像を提示し、早く発火する入力の重みを強める。
- Data and results: 目立ち、繰り返し現れる特徴への選択性が形成され、複数分類課題で頑健な物体認識を示す。
- Novelty: 時間符号とSTDPを、視覚特徴の自己組織化へつなぐ。
- Limitations: 編者の注意: モデルの認識結果であり、脳全体が同じfeedforward ruleだけで認識するという実証ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/17305422/

### Paper: Resting-state functional connectivity reflects structural connectivity in the default mode network
- Source: PubMed
- Canonical ID: pmid:18403396
- Publication date: 2008-04-09
- URL: https://pubmed.ncbi.nlm.nih.gov/18403396/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: default modeの機能結合を、拡散画像の構造経路と対応付ける。
- Objective: 安静時のBOLD相関が、単なる非神経artifactでないかを調べる。
- Methods: 安静時fMRIをseedにDTI tractographyを行い、内側前頭・側頭・後部帯状/脳梁膨大後領域の経路を探す。
- Data and results: MTL–retrosplenial cortexとMPFC–PCCの構造的な経路を報告し、二つのmodalitiesの対応を示す。
- Novelty: 機能的なdefault系へ、非侵襲の構造情報を併せて検証する。
- Limitations: 編者の注意: 対応する経路があることは、すべての機能相関が直接接続に由来する証明ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/18403396/

### Paper: Spike timing-dependent plasticity: a Hebbian learning rule
- Source: PubMed
- Canonical ID: pmid:18275283
- Publication date: 2008-07-21
- URL: https://pubmed.ncbi.nlm.nih.gov/18275283/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: STDPの細胞機構と、基本的な時間窓を超える複雑さをreviewする。
- Objective: 前後spikeの順序で変わる可塑性を、回路機能へ結び付ける。
- Methods: 興奮・抑制synapse、樹状突起位置、複雑な列の非線形統合、調節入力とin vivo研究を整理する。
- Data and results: 数十msの窓だけでは足りず、位置・抑制・neuromodulationなどに依存する多層の構造を示す。
- Novelty: 単一のHebbian曲線から、回路・細胞contextを持つ学習則へ視野を広げる。
- Limitations: 編者の注意: 実装の便宜で使う単純なSTDP曲線を、生体のすべてのsynapseに共通するruleと扱わない。
- Publication date note: 出版社Annual ReviewsがPublication Date: 21 Jul 2008と明示する刊行日を採用。Volume publicationはJuly 2008。これより先のオンライン先行公開日の日精度は未確認。出典: https://www.annualreviews.org/content/journals/10.1146/annurev.neuro.31.060407.125639

### Paper: Predicting human resting-state functional connectivity from structural connectivity
- Source: PubMed
- Canonical ID: pmid:19188601
- Publication date: 2009-02-02
- URL: https://pubmed.ncbi.nlm.nih.gov/19188601/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 人間の構造的配線から、安静時機能結合の特徴を力学モデルで予測する。
- Objective: 変動する機能networkが解剖構造にどれだけ拘束されるかを調べる。
- Methods: 同じ人のfMRIと拡散tractographyを測り、構造結合を巨視的な皮質動態モデルの結合に使う。
- Data and results: 直接構造結合のない領域にも強い機能結合があり、間接経路と距離が一部を説明。走査・モデル間の変動も認める。
- Novelty: 構造・機能・計算モデルを同じ対象で対応付ける。
- Limitations: 機能結合から直接配線を逆推定することは難しいと著者が指摘。間接経路と時間変動を無視できない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/19188601/

### Paper: Cortical hubs revealed by intrinsic functional connectivity: mapping, assessment of stability, and relation to Alzheimer's disease
- Source: PubMed
- Canonical ID: pmid:19211893
- Publication date: 2009-02-11
- URL: https://pubmed.ncbi.nlm.nih.gov/19211893/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 機能結合のhubを人間の皮質で同定し、状態間の安定性を調べる。
- Objective: network統合の中心と、病理の分布との関係を検討する。
- Methods: 独立fMRI2群各24人、別群12人で検証し、127人の合意hub地図をamyloid PETと比較する。
- Data and results: 連合皮質にhubを見いだし、課題間で位置が安定。AD10人・対照29人の比較ではhub位置に高いamyloidを認める。
- Novelty: hubの位置・再現性・病理との対応を複数datasetで結ぶ。
- Limitations: 編者の注意: hubと病理の空間的対応は、hub活動が疾患を起こすという因果実証ではない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/19211893/

### Paper: Gaussian-process factor analysis for low-dimensional single-trial analysis of neural population activity
- Source: PubMed
- Canonical ID: pmid:19357332
- Publication date: 2009-04-08
- URL: https://pubmed.ncbi.nlm.nih.gov/19357332/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: GPFAは時間平滑化と次元削減を一つの確率モデルで行う。
- Objective: 単一trialの多neuron発火から、滑らかな潜在軌跡を推定する。
- Methods: Gaussian processとfactor analysisを統合し、他neuronからの発火予測で二段階手法と比較する。
- Data and results: macaque運動前野・運動皮質の61neuronで予測を改善。既知のsimulationでは最良の二段階法より数十%良い結果を報告。
- Novelty: 時間の滑らかさと発火の変動を、低次元推定の内部で同時に扱う。
- Limitations: 編者の注意: simulationの改善率を生体データでの真の潜在状態復元率としない。平滑性や潜在次元にも仮定がある。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/19357332/

### Paper: Predictive coding under the free-energy principle
- Source: PubMed
- Canonical ID: pmid:19528002
- Publication date: 2009-05-12
- URL: https://pubmed.ncbi.nlm.nih.gov/19528002/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: free-energyの枠組みで、知覚を階層的な動的生成モデルの推論として表す。
- Objective: 感覚の原因を認識し、感覚状態の列を予測する計算法を導く。
- Methods: モデルevidenceのfree-energy boundを最適化し、階層動的モデルの逆推論の式を導く。
- Data and results: 人工の鳥による鳥歌の認識・分類simulationで説明する。生体脳での一般的な原理の直接証明ではない。
- Novelty: 階層、動態、予測誤差を、変分的なモデル推論へ統合する。
- Limitations: 脳が階層的な動的モデルを持つという仮定に基づく。編者の注意: simulationの実装可能性と、生物の実際の計算を区別する。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/19528002/

### Paper: Modular and hierarchically modular organization of brain networks
- Source: PubMed
- Canonical ID: pmid:21151783
- Publication date: 2010-12-08
- URL: https://pubmed.ncbi.nlm.nih.gov/21151783/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: moduleの中にさらにmoduleを持つ、脳networkの階層構造を整理する。
- Objective: 専門化・統合・頑健性を支える複数scaleの組織を理解する。
- Methods: 階層modularityの数学と、人間の構造・機能画像から得られた研究をreviewする。
- Data and results: module内の高密度結合、比較的長距離のmodule間結合、頑健性・適応性などの含意を論じる。
- Novelty: 単一scaleの分割を超えた、階層的なnetwork構造の見取り図。
- Limitations: レビューであり頑健性の一般的な因果実証ではない。編者の注意: 階層の検出は解像度・比較基準に左右される。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/21151783/

### Paper: The human connectome: a complex network
- Source: PubMed
- Canonical ID: pmid:21251014
- Publication date: 2011-01-04
- URL: https://pubmed.ncbi.nlm.nih.gov/21251014/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: human connectomeを複雑networkとして捉え、構造が機能動態を拘束する関係を整理する。
- Objective: 大規模な配線地図から、統合と専門化の組織原理を理解する。
- Methods: 非侵襲画像による構造network研究をreviewし、cluster・module・経路長・効率を検討する。
- Data and results: 高いcluster・modularityと短い経路などの非ランダム構造を整理し、構造と機能の関係は複雑で非線形と述べる。
- Novelty: connectomeの地図をgraph理論と機能的な解釈へつなぐ。
- Limitations: レビューのため独自の全脳再構築や介入実験ではない。構造・機能に共通の指標があっても両者は同一ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/21251014/

### Paper: Dynamic reconfiguration of human brain networks during learning
- Source: PubMed
- Canonical ID: pmid:21502525
- Publication date: 2011-04-18
- URL: https://pubmed.ncbi.nlm.nih.gov/21502525/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 人間の学習に伴う機能networkのmodule変化を、将来の学習量と結び付ける。
- Objective: 柔軟な再構成が技能習得へどう関わるかを調べる。
- Methods: 単純運動技能の初期から習熟までの機能結合を測り、複数時間scaleの動的communityを解析する。
- Data and results: moduleへの所属が変わる柔軟性が、後のsessionの相対的な学習量を予測したと報告。
- Novelty: 固定したnetwork構造から、学習過程で動くmoduleと個人予測へ展開する。
- Limitations: 編者の注意: 将来学習との予測関係は因果を確定せず、単純運動課題から全認知学習へ一般化しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/21502525/

### Paper: The organization of the human cerebral cortex estimated by intrinsic functional connectivity
- Source: PubMed
- Canonical ID: pmid:21653723
- Publication date: 2011-06-08
- URL: https://pubmed.ncbi.nlm.nih.gov/21653723/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 安静時の機能結合から、人間の皮質を大規模networkへ区分する。
- Objective: 感覚運動の局所系と、連合皮質の分散系の構成を明らかにする。
- Methods: 1,000人のsurface位置合わせ済みfMRIをcluster化し、networkの再現性と境界を調べる。
- Data and results: 感覚運動では地形的な隣接構造、連合皮質では急な境界と並列に入り組む分散networkを報告。
- Novelty: 大標本の機能結合による、皮質networkの共通の区分を提供する。
- Limitations: 編者の注意: 機能的な相関からの区分は、細胞・シナプス単位の解剖学的配線ではなく、個体差も残る。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/21653723/

### Paper: The influence of head motion on intrinsic functional connectivity MRI
- Source: PubMed
- Canonical ID: pmid:21810475
- Publication date: 2011-07-23
- URL: https://pubmed.ncbi.nlm.nih.gov/21810475/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 頭の動きが、人間の安静時機能結合へ系統的な偏りを生むことを調べる。
- Objective: 年齢群・患者群・個体差の比較で、動きを神経の差と誤認しないようにする。
- Methods: 健康若年者1,000人の安静時2走査で、変位・微小運動・回転と複数network指標を対応付ける。
- Data and results: 動きでdefault・前頭頭頂の遠距離結合が下がり、局所結合などが上がる。小さい群間の動き差でも神経差に似た地図が生じる。
- Novelty: 機能networkの個体差・集団差の解釈に、motionの具体的な影響を示す。
- Limitations: 変動の大部分がmotionによるとは報告していない。編者の注意: 相関のすべてをartifactとするのも不適切。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/21810475/

### Paper: Rich-club organization of the human connectome
- Source: PubMed
- Canonical ID: pmid:22049421
- Publication date: 2011-11-02
- URL: https://pubmed.ncbi.nlm.nih.gov/22049421/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 人間の脳hub同士が、密につながるrich clubを形成するか検証する。
- Objective: 高い次数の中心領域の間に、次数だけでは説明できない接続があるかを調べる。
- Methods: 21人の拡散tensor画像から全脳構造networkを作り、hub間の密度を次数に基づく期待と比較する。
- Data and results: 両半球の12hub領域で強い相互結合を見いだし、次数だけからの予想以上に密なrich clubを報告。
- Novelty: hubの存在だけでなく、hub間を結ぶ高次のcore構造を示す。
- Limitations: 編者の注意: MRI由来の巨視的networkであり、hub間の密結合が情報統合を生むという機能的因果は別途検証する。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/22049421/

### Paper: Neural dynamics as sampling: a model for stochastic computation in recurrent networks of spiking neurons
- Source: PubMed
- Canonical ID: pmid:22096452
- Publication date: 2011-11-03
- URL: https://pubmed.ncbi.nlm.nih.gov/22096452/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: spiking網の確率的発火を、ある条件下でMCMC samplingとして実装する。
- Objective: 抽象的な確率推論と、具体的なspike動態を結び付ける。
- Methods: 通常のGibbsとは異なる非可逆Markov chainを構成し、離散・連続時間の理論解析を行う。
- Data and results: 提案網の活動が与えられた分布をsamplingすることを、条件付きで厳密に示す。
- Novelty: 発火の時間構造に合う確率推論の実装を導く。
- Limitations: 条件を満たす提案モデルの結果。編者の注意: 脳の試行間変動すべてがBayes samplingであるという観測的証明ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/22096452/

### Paper: Neural population dynamics during reaching
- Source: PubMed
- Canonical ID: pmid:22722855
- Publication date: 2012-07-05
- URL: https://pubmed.ncbi.nlm.nih.gov/22722855/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: reaching中の運動皮質の集団活動に、短いが強い振動構造を見いだす。
- Objective: 運動皮質の一つのニューロンが速度や方向を『表現しているか』という問いでは、複雑に変動する集団活動の構造を捉えにくい。多数の細胞の時間発展を一つの力学系として捉えられるかを調べる。
- Methods: サルが異なる方向へ到達運動する際の運動皮質の集団活動を記録・解析し、準備状態から運動実行にかけて低次元の活動軌跡を抽出。個々の細胞のチューニングに還元せず、集団に共通する位相・振幅や短い振動パターンを調べ、試行ごとの動きの違いと対応させた。
- Data and results: 身体の到達動作が周期的でないにもかかわらず神経集団活動に回転的・振動的なパターンを認め、準備段階の状態がその後の活動位相や振幅と結びつくと示した。これは運動皮質が必ず周期運動を指令しているという主張ではなく、集団の時間変化が簡潔な内部動態として記述できることを示す。
- Novelty: 個々のニューロンを『何の変数を表しているか』という静的な観点だけでなく、神経集団が状態空間内でどう動くかを研究対象にした。脳内の計算を潜在状態のダイナミクスとして解析する研究の基礎になる。
- Limitations: 特定の到達運動・記録領域に対する分析であり、集団軌跡の相関から運動の因果的制御機構をすべて同定したわけではない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/22722855/

### Paper: The minimal preprocessing pipelines for the Human Connectome Project
- Source: PubMed
- Canonical ID: pmid:23668970
- Publication date: 2013-05-11
- URL: https://pubmed.ncbi.nlm.nih.gov/23668970/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: HCPの構造・機能・拡散MRIを統合する標準的な前処理を記述する。
- Objective: 高品質な大標本データを、共通空間で再利用できるようにする。
- Methods: 歪み除去、surface生成、modalities間位置合わせ、標準化を行い、CIFTI/grayordinateで皮質と皮質下を扱う。
- Data and results: 最小限の取得条件と処理手順、実施上の助言を提供。予測モデルの独自精度を主成果としていない。
- Novelty: 複数MRIを高い解像度で統合する、connectome解析の共通入口を作る。
- Limitations: HCPの取得条件に合わせたpipelineで、任意の低品質・別protocolデータでも同じ妥当性が得られるとは限らない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/23668970/

### Paper: The WU-Minn Human Connectome Project: an overview
- Source: PubMed
- Canonical ID: pmid:23684880
- Publication date: 2013-05-16
- URL: https://pubmed.ncbi.nlm.nih.gov/23684880/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: WU-Minn HCPの、人間の巨視的回路と行動を測る計画・資源のoverview。
- Objective: 構造MRIや機能MRIを別々の少数の被験者で測定する研究では、脳全体の結合と個人差・行動の関係を共通条件で調べにくい。多数の健康成人で高品質の多様な脳計測と行動情報を統合・公開する基盤を作る。
- Methods: Washington University–Minnesota Human Connectome Projectの5年計画で、構造MRI、安静・課題fMRI、拡散MRI、行動評価を共通の取得プロトコル・前処理へ統一し、データ品質の初期検証とConnectomeDBを通じた段階的公開を実施した。論文は計画初期の設計・進捗を記録する概要であり神経接続の新しい一つの仮説を検証する実験ではない。
- Data and results: 2013年時点で高品質な初期データと最初の四半期データ公開を実現し、研究者が同じ被験者の構造・機能・行動を比較できるようにした。以後の大規模データ活用の前提となるインフラを示すが、この概要論文自体が特定の認知機能の因果効果を確定したものではない。
- Novelty: 単一研究室ごとの小規模データを超え、統一された取得・解析・公開により異なる研究を比較可能にする基盤を整えた。神経活動のモデル評価における共通データの価値を示す。
- Limitations: MRIの接続は巨視的・間接的で、シナプス単位のヒト全脳接続図ではない。計画の開始段階の資料であり、後年の全データセットの完成状況をこの論文だけから読み取るべきではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/23684880/

### Paper: A causal link between prediction errors, dopamine neurons and learning
- Source: PubMed
- Canonical ID: pmid:23708143
- Publication date: 2013-05-26
- URL: https://pubmed.ncbi.nlm.nih.gov/23708143/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: dopamineの短い活動を操作し、予測誤差とcue–reward学習の因果的な接点を検証する。
- Objective: 報酬に応じた発火と学習が、単なる相関を超えて結び付くか調べる。
- Methods: ratのblockingとextinctionで、報酬と同時にoptogeneticにdopamine neuronを活性化する。
- Data and results: 予測誤差を模す活性化が、cueによるreward-seekingを長く増加させるのに十分だった。
- Novelty: 理論上の誤差信号を、時間をそろえた神経操作で検証する。
- Limitations: 特定の操作が学習を生む十分性の結果。編者の注意: すべてのdopamine活動の機能や感情全体を同定したものではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/23708143/

### Paper: Connectomic reconstruction of the inner plexiform layer in the mouse retina
- Source: PubMed
- Canonical ID: pmid:23925239
- Publication date: 2013-08-08
- URL: https://pubmed.ncbi.nlm.nih.gov/23925239/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: mouse網膜のinner plexiform layerを密に再構築し、局所計算の候補を調べる。
- Objective: 広い領域と細かい接続を両立するconnectomicsを実装する。
- Methods: serial block-face EMに、群衆による注釈と機械学習の体積分割を組み合わせる。
- Data and results: 950 neuronと相互contactを復元し、新しいbipolar型と接続による型の細分を示す。局所運動の候補motifも導く。
- Novelty: 自動分割と人手注釈から、細胞型と機能仮説を持つ密な哺乳類回路図を作る。
- Limitations: mouse網膜の局所領域であり全脳ではない。編者の注意: contactからの候補機能は生理・操作実験での確認が必要。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/23925239/

### Paper: A visual motion detection circuit suggested by Drosophila connectomics
- Source: PubMed
- Canonical ID: pmid:23925240
- Publication date: 2013-08-08
- URL: https://pubmed.ncbi.nlm.nih.gov/23925240/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: ハエ視覚系の局所connectomeから、動きの方向検出の候補回路を導く。
- Objective: 長く不明だった局所運動計算の細胞・結合構造を特定する。
- Methods: 半自動EM再構築と光学像の細胞型matchingを使い、medullaの反復moduleを調べる。
- Data and results: 379 neuronと8,637化学シナプスを復元。方向選択性と整合する運動感受性neuronへの結合を見いだす。
- Novelty: 細胞型を伴う局所の密な配線図から、具体的な計算回路を提案する。
- Limitations: 著者は将来の機能実験の標的として位置付ける。編者の注意: 接続との整合性は、回路の機能を直接操作で確定したこととは異なる。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/23925240/

### Paper: Orbitofrontal cortex as a cognitive map of task space
- Source: PubMed
- Canonical ID: pmid:24462094
- Publication date: 2014-01-22
- URL: https://pubmed.ncbi.nlm.nih.gov/24462094/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: OFCを、強化学習で必要な潜在課題状態の認知地図として捉える理論。
- Objective: OFCの意思決定への役割を、複数の実験結果に一貫して説明する。
- Methods: 観測されない作業記憶などを含む状態labelをOFCが供給すると仮定し、逆転・消去・価値低下や損傷結果を説明する。
- Data and results: rodentでのOFC損傷とdopamine応答などを統合し、他理論と区別できる実験予測を導く。
- Novelty: 価値そのものの保存に限らず、学習が参照する状態表現の役割を提案する。
- Limitations: 仮説・理論の論文であり、全OFC機能を同定した研究ではない。生成した予測は後続の操作実験による検証が必要。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/24462094/

### Paper: A mesoscale connectome of the mouse brain
- Source: PubMed
- Canonical ID: pmid:24695228
- Publication date: 2014-04-02
- URL: https://pubmed.ncbi.nlm.nih.gov/24695228/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: Allen Mouse Brain Connectivity Atlasは、マウスの全脳投射をmesoscaleで地図化する。
- Objective: 局所と全体の情報処理を結ぶ標準的な構造資源を作る。
- Methods: EGFPを発現するAAVで領域・細胞型からの軸索を標識し、serial二光子tomographyと共通3D空間へ登録する。
- Data and results: 全脳接続行列を公開し、強度分布・対称性・皮質視床の並列経路の統合と分離を分析する。
- Novelty: 系統的なtracingを標準空間で統合した、全脳の投射atlas。
- Limitations: mesoscaleの投射情報であり、すべての細胞・シナプスを復元した全脳connectomeではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/24695228/

### Paper: Performance-optimized hierarchical models predict neural responses in higher visual cortex
- Source: PubMed
- Canonical ID: pmid:24812127
- Publication date: 2014-05-08
- URL: https://pubmed.ncbi.nlm.nih.gov/24812127/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 視覚課題で最適化した階層網が、高次視覚皮質の応答を予測する。
- Objective: 課題性能の最適化が、生体の神経処理モデルを作る原理になるか調べる。
- Methods: 生物的に適した階層モデル群で物体認識性能とIT応答予測を比べ、高性能網を神経記録と対応付ける。
- Data and results: 神経データへ直接適合させなくても最上層がIT、途中層がV4応答をよく予測し、課題性能との強い関係を報告。
- Novelty: 目的を解くための最適化と、脳応答を説明する表現の出現をつなぐ。
- Limitations: 編者の注意: 応答予測の一致は、脳が同じarchitectureや学習ruleを使う証明ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/24812127/

### Paper: Neural dynamics for landmark orientation and angular path integration
- Source: PubMed
- Canonical ID: pmid:25971509
- Publication date: 2015-05-14
- URL: https://pubmed.ncbi.nlm.nih.gov/25971509/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: ハエの方向表象が、視覚landmarkと自己運動を統合することを示す。
- Objective: 方向を保つnavigation回路の動態を、行動と同時に調べる。
- Methods: 頭部固定で球上を歩くハエにVRを提示し、ellipsoid bodyの二光子calcium画像を測る。
- Data and results: 明所ではlandmark、暗所では自己運動を追い、両手掛かりがなくても方向表象を保持。ring attractorを示唆する。
- Novelty: 環状の解剖と持続活動を、方向積分の計算へ結ぶ。
- Limitations: ring attractorは観察に整合する示唆。編者の注意: 頭部固定・VRの結果を、自然下の全navigation能力へ直接拡張しない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/25971509/

### Paper: PLACE CELLS. Autoassociative dynamics in the generation of sequences of hippocampal place cells
- Source: PubMed
- Canonical ID: pmid:26160946
- Publication date: 2015-07-10
- URL: https://pubmed.ncbi.nlm.nih.gov/26160946/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 海馬のsharp-wave ripple中の再活性化列を、離散attractorの連続として捉える。
- Objective: 自己持続する記憶系列の生成機構を調べる。
- Methods: place cell集団の活動を時間的に解析し、空間表現の先鋭化と遷移をgamma rhythmと対応付ける。
- Data and results: 各場所の表現が数msで鋭くなった後、非連続な別位置へ急に移り、これが25–50Hzのslow gammaに同期する。
- Novelty: 記憶の列を滑らかな再生だけでなく、離散状態の先鋭化・跳躍として記述する。
- Limitations: 編者の注意: attractor動態を支持する証拠であり、すべてのreplayや記憶検索が同じ離散機構で動くという結論ではない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/26160946/

### Paper: Unsupervised learning of digit recognition using spike-timing-dependent plasticity
- Source: PubMed
- Canonical ID: pmid:26941637
- Publication date: 2015-08-03
- URL: https://pubmed.ncbi.nlm.nih.gov/26941637/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 教師なしSTDPで、spiking網が数字の特徴を学ぶ例を示す。
- Objective: rate網からの変換に頼らず、spike型の局所学習で認識を行う。
- Methods: conductance synapse、時間依存STDP、側方抑制、適応閾値を組み合わせ、訓練時の教示・class labelを使わない。
- Data and results: MNISTで95%の精度を報告し、neuron数の増加と異なる4学習ruleへの頑健性も調べる。
- Novelty: 複数の比較的生物に近い機構を統合し、教師なしのpattern学習を実装する。
- Limitations: 編者の注意: 訓練時の教師なし学習と、評価時のclass対応の決め方は別であり、数字以外への一般性は別途検証する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/26941637/

### Paper: Modular Brain Networks
- Source: PubMed
- Canonical ID: pmid:26393868
- Publication date: 2015-09-21
- URL: https://pubmed.ncbi.nlm.nih.gov/26393868/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 脳networkのcommunity検出法と、moduleの構造・機能的意味を整理する。
- Objective: 密な部分networkを、専門的な機能の構成要素として理解する。
- Methods: community検出の複数方式の長短をreviewし、構造・機能地図での主要な観察をまとめる。
- Data and results: 進化、配線量、専門化、複雑な動態におけるmoduleの役割を検討する。新予測器の精度比較ではない。
- Novelty: moduleの存在と検出法の選択を、network neuroscienceの中心問題として整理する。
- Limitations: 検出法ごとに長短がある。編者の注意: 分割のscale・最適化・null modelによって得られるmoduleが変わる。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/26393868/

### Paper: Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity
- Source: PubMed
- Canonical ID: pmid:26457551
- Publication date: 2015-10-12
- URL: https://pubmed.ncbi.nlm.nih.gov/26457551/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 機能結合のpatternが、個人を識別するfingerprintとなることを示す。
- Objective: 人間の脳ネットワークには集団で共通する組織化がある一方、個体ごとに再現する特徴があるか、またそれが行動の差と関係するかは区別して確かめる必要がある。MRI機能結合が本人識別の指紋として使えるかを検証する。
- Methods: Human Connectome Projectの安静時・課題中の機能MRIから脳領域間の相関行列を作成。異なる撮像セッションや安静／課題条件でも、結合パターンを使って同一人物を識別できるか検証した。識別に寄与するネットワークを特定し、流動性知能などの行動指標との関係も解析した。
- Data and results: 撮像条件をまたいで同一人物の機能結合パターンから識別が可能で、前頭・頭頂ネットワークが特に識別性に寄与した。また一部の個人差は認知指標との関連を示した。本人を区別できることと、知能・将来の疾病を高精度に予測できることは異なる。
- Novelty: 集団平均の機能結合を記述する研究から、個体ごとの安定したネットワーク特性を検出する方向を示した。匿名化した神経画像でも個体識別に使える可能性があるというプライバシー上の示唆もある。
- Limitations: 同一のHCPデータ取得・前処理条件に基づき、装置・施設の異なる条件での精度保持には追加検証が必要。結合の相関を構造的な軸索や因果的情報伝達と同義とみなせない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/26457551/

### Paper: Neuromodulated Spike-Timing-Dependent Plasticity, and Theory of Three-Factor Learning Rules
- Source: PubMed
- Canonical ID: pmid:26834568
- Publication date: 2016-01-19
- URL: https://pubmed.ncbi.nlm.nih.gov/26834568/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 前後の活動にneuromodulatorを加える三因子学習ruleを整理する。
- Objective: 感覚入力と遅れて来る報酬・新規性信号の時間gapを埋める。
- Methods: 理論・概念モデルを中心に、前synapse活動、後synapse変数、phasic調節信号のtimingを整理し実験証拠も検討する。
- Data and results: 短い活動をsynapseの機構で保持し、後の調節信号で学習を成立させる枠組みを提示する。
- Novelty: Hebbianな局所相関を、報酬や新規性に応じて学ぶtimingへ接続する。
- Limitations: 編者の注意: 三因子ruleは一つの固定式ではなく一群の理論で、特定の生体回路での実装は個別に確認が必要。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/26834568/

### Paper: Dynamics of scene representations in the human brain revealed by magnetoencephalography and deep neural networks
- Source: PubMed
- Canonical ID: pmid:27039703
- Publication date: 2016-04-01
- URL: https://pubmed.ncbi.nlm.nih.gov/27039703/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: MEGとDNNで、sceneの見た目から空間layoutへ至る表現の時間経過を調べる。
- Objective: scene認識で異なる情報がいつ現れるかを定量化する。
- Methods: MEGの多変量patternを解析し、scene分類DNNの内部表現と対応付ける。
- Data and results: 約100msに低次視覚、約250msにsceneの実際の大きさを反映する信号を報告。DNNでも大きさ表現が自然に現れる。
- Novelty: 時間分解能の高い脳記録と、課題学習の表現を結ぶ。
- Limitations: 編者の注意: 時間的・表現的な対応は同じ回路の証明ではなく、使った静止画像・課題の範囲内で解釈する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/27039703/

### Paper: Demixed principal component analysis of neural population data
- Source: PubMed
- Canonical ID: pmid:27067378
- Publication date: 2016-04-12
- URL: https://pubmed.ncbi.nlm.nih.gov/27067378/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: dPCAは混合した集団活動を、課題変数に対応する少数の成分へ分ける。
- Objective: 多数のニューロンは刺激、選択、報酬、時間など複数の課題要因に混合して反応するため、通常のPCAだけでは各要因の寄与を読み解きにくい。大きな分散を保持しながら、その変動がどの課題因子に対応するかを分けて表示できるかを問う。
- Methods: 実験の刺激・判断・報酬・時間などのラベルを使い、集団活動の変動を各因子に周辺化したうえで、因子別の成分が混ざらないよう分解するdemixed PCA（dPCA）を提案。異なる動物・脳領域・課題に由来する4つの既存の神経活動データを再解析して、従来の次元削減では見えにくい時間・課題依存応答を可視化した。
- Data and results: 4つの実データに適用し、個々の細胞が複数の要因に反応しても、集団レベルの成分として刺激・選択・時間依存の変動を比較的明瞭に分離できることを報告。これは分類器の診断精度を何%改善したという研究ではなく、低次元表現の解釈可能性を改良する方法論である。
- Novelty: 分散を最大化する通常のPCAと異なり、実験因子のラベルを利用してどの種類の変動かを見分けられるようにした。数値センサーの潜在表現を意味のある要因へ分離する研究に接続できる。
- Limitations: 分離に使う課題ラベルは外部から与えられており、成分が独立した神経回路や原因を表すことを自動的に証明しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/27067378/

### Paper: Small-World Brain Networks Revisited
- Source: PubMed
- Canonical ID: pmid:27655008
- Publication date: 2016-09-21
- URL: https://pubmed.ncbi.nlm.nih.gov/27655008/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: small-worldを、binary graphだけでなく重み付きの脳配線で再検討する。
- Objective: 高解像度tracingに合うtopologyの解釈へ更新する。
- Methods: 基礎理論と過去10年の進展をreviewし、macaque・mouseの新しいtracing結果を検討する。
- Data and results: 強い辺・弱い辺を保持する重み付きnetworkの重要性を強調し、weighted small-worldnessの課題を示す。
- Novelty: つながる/つながらないだけの地図から、結合強度を含む組織の評価へ進む。
- Limitations: 編者の注意: binary化や重みの処理で結論が変わるため、small-world指標の値だけで種・測定法を横断比較しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/27655008/

### Paper: Situating the default-mode network along a principal gradient of macroscale cortical organization
- Source: PubMed
- Canonical ID: pmid:27791099
- Publication date: 2016-10-18
- URL: https://pubmed.ncbi.nlm.nih.gov/27791099/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: default modeを、感覚運動から離れた皮質の主要gradientの端に位置付ける。
- Objective: 皮質の空間配置と抽象的な機能の関係を整理する。
- Methods: 人間・macaqueの結合データを分解し、皮質上のgeodesic距離と機能meta解析へ対応付ける。
- Data and results: 感覚運動からtransmodalのDMNへ至る軸を報告。DMNは感覚運動landmarkから遠く、複数networkの配置を整理できた。
- Novelty: 離散したnetwork群を、共通の連続的な空間軸へ結ぶ。
- Limitations: 編者の注意: 空間的位置による機能解釈は支持されるが、gradientだけが抽象思考を起こすという因果証明ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/27791099/

### Paper: Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning
- Source: PubMed
- Canonical ID: pmid:27814352
- Publication date: 2016-11-04
- URL: https://pubmed.ncbi.nlm.nih.gov/27814352/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 運動皮質の回転動態を、表象tuningと力学系の両方から検証する。
- Objective: 回転patternだけで力学系を支持してよいかを確かめる。
- Methods: 遅延付き速度tuningのsimulation、共分散を保つ置換検定、RNN、生体活動を比較する。
- Data and results: 単純な表象モデルも回転を作るが条件構造への依存が異なる。生体・力学モデルはその依存を保ち、RNNは両性質を再現する。
- Novelty: 回転の見た目でなく、条件と共分散を保つ検定でモデルを区別する。
- Limitations: 著者は少数neuron・少数条件の解釈に注意を促す。表象と力学を完全な二者択一とせず、検定の構造を確認する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/27814352/

### Paper: Random synaptic feedback weights support error backpropagation for deep learning
- Source: PubMed
- Canonical ID: pmid:27824044
- Publication date: 2016-11-08
- URL: https://pubmed.ncbi.nlm.nih.gov/27824044/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: feedback alignmentは、ランダムな逆向き重みでも多層の誤差学習が可能と示す。
- Objective: backpropに必要とされる、正確に対称な逆向き接続の制約を緩める。
- Methods: 固定的なランダムfeedbackで誤差を伝え、多層網を複数の課題で訓練する。
- Data and results: 多くの課題でbackpropに匹敵する成績と、有効な教示信号の伝達をモデル上で示す。
- Novelty: 重みの正確な対称性を、深い信用割当の必要条件から外す。
- Limitations: 編者の注意: ランダムfeedbackで学べる計算例であり、脳でこのruleが働くことや他の生物学的制約まで解決した証明ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/27824044/

### Paper: Neural Elements for Predictive Coding
- Source: PubMed
- Canonical ID: pmid:27917138
- Publication date: 2016-11-18
- URL: https://pubmed.ncbi.nlm.nih.gov/27917138/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 予測符号化の計算構造を、皮質の層・microcircuitへ対応付ける論考。
- Objective: 予測と誤差の往復が、既知の神経要素とどう対応するかを整理する。
- Methods: 一般化free-energy式とcanonical microcircuitを合わせ、霊長類視覚皮質・mouseの回路知見で検討する。
- Data and results: 前向き・後向き投射群の分離などを論じ、interneuron多様性や単一細胞の接続から理論を更新する道筋を示す。
- Novelty: 抽象的な計算と細胞・層の実装を、双方向に検討するtemplate。
- Limitations: 著者はmicrocircuitがまだ完全には記述されていないとする。計算上の対応候補を確定した生理機能と混同しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/27917138/

### Paper: Using connectome-based predictive modeling to predict individual behavior from brain connectivity
- Source: PubMed
- Canonical ID: pmid:28182017
- Publication date: 2017-02-09
- URL: https://pubmed.ncbi.nlm.nih.gov/28182017/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: CPMは機能・構造結合から、新しい人の行動を予測する実用protocol。
- Objective: 脳–行動の関連を、交差検証された個人予測として評価する。
- Methods: 特徴選択、要約、線形model構築、有意性検定を交差検証へ組み込み、予測的な辺も可視化する。
- Data and results: 既存の脳–行動予測に匹敵または上回るprotocolを提示。計算目安は構築10–100分、置換検定1–48時間。
- Novelty: 複雑な最適化なしに、再利用可能な予測と検定の手順を提供する。
- Limitations: 編者の注意: 特徴選択を検証foldの外で行うと漏洩になる。予測的な辺の表示は、その辺の因果的役割の証明ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/28182017/

### Paper: Overcoming catastrophic forgetting in neural networks
- Source: PubMed
- Canonical ID: pmid:28292907
- Publication date: 2017-03-14
- URL: https://pubmed.ncbi.nlm.nih.gov/28292907/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: EWCは過去課題に重要な重みの変更を遅らせ、逐次学習の忘却を抑える。
- Objective: 新課題を学びながら、長く経験していない課題の能力を保持する。
- Methods: 重みごとの過去課題への重要性を使い、後続学習での変更に選択的な制約を加える。
- Data and results: 手書き数字の複数分類課題と複数Atari 2600 gameの逐次学習で有効性と拡張性を示す。
- Novelty: 記憶を完全に再学習する代わりに、重要なパラメータの保護で干渉を減らす。
- Limitations: 編者の注意: 忘却を普遍的に解決した保証ではなく、課題の関係・重要性推定・利用可能な容量に性能が依存する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/28292907/

### Paper: Benchmarking of participant-level confound regression strategies for the control of motion artifact in studies of functional connectivity
- Source: PubMed
- Canonical ID: pmid:28302591
- Publication date: 2017-03-14
- URL: https://pubmed.ncbi.nlm.nih.gov/28302591/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: motion artifactを減らす14種類の回帰・除去法を比較する。
- Objective: 脳networkの結果を歪める動きを、目的に応じて処理できるようにする。
- Methods: 若年者393人でmotion残差、距離依存、network識別、自由度損失の4軸を評価する。
- Data and results: global signal回帰はmotionとの関係を減らすが距離依存を残す。censoringは両方を減らす一方、自由度を消費する。
- Novelty: 単一の残差指標でなく、処理のtrade-offを複数の軸で明示する。
- Limitations: 著者は目的別の方法選択を推奨。編者の注意: 一つの処理がすべての研究・集団で最適という結論ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/28302591/

### Paper: The complete connectome of a learning and memory centre in an insect brain
- Source: PubMed
- Canonical ID: pmid:28796202
- Publication date: 2017-08-09
- URL: https://pubmed.ncbi.nlm.nih.gov/28796202/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 幼虫ハエのキノコ体を完全再構築し、連合学習の回路を調べる。
- Objective: 刺激と正負の強化を結ぶ高次記憶回路の構造を明らかにする。
- Methods: シナプス地図でKenyon細胞の入力と再帰結合を解析し、刺激弁別の出力neuronモデルを比較する。
- Data and results: 大半の入力組合せはランダム、一部は定型的。modulatory neuronとの相互結合など、新しい標準回路を見いだす。
- Novelty: ランダムな混合表現と再帰的・modulatoryな回路を、完全地図上で同時に示す。
- Limitations: 幼虫の特定の記憶中枢が対象。編者の注意: モデルでの刺激弁別と、個体の学習行動の再現は区別する。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/28796202/

### Paper: The hippocampus as a predictive map
- Source: PubMed
- Canonical ID: pmid:28967910
- Publication date: 2017-10-02
- URL: https://pubmed.ncbi.nlm.nih.gov/28967910/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 海馬の空間表象を、将来の状態を表すpredictive mapとしてモデル化する。
- Objective: place cellの報酬・方策依存を、純粋な幾何地図より広く説明する。
- Methods: 将来報酬に有用な表現を強化学習の視点で導き、grid cellをその低次元基底として解釈する。
- Data and results: 従来の幾何地図では説明しにくいplace cell特性を捉え、多scale構造と階層計画への役割を議論する。
- Novelty: 認知地図を、経験・方策に依存する将来の予測表現へ拡張する。
- Limitations: 編者の注意: 理論的な解釈とモデルによる説明であり、海馬が唯一この算法で全記憶を表すという実証ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/28967910/

### Paper: The challenge of mapping the human connectome based on diffusion tractography
- Source: PubMed
- Canonical ID: pmid:29116093
- Publication date: 2017-11-07
- URL: https://pubmed.ncbi.nlm.nih.gov/29116093/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 拡散tractographyを既知の線維を持つsimulationで比較し、限界を定量化する。
- Objective: 非侵襲connectomeの接続がどれだけ信頼できるか調べる。
- Methods: 20研究groupから96方式の提出を集め、ground truthのbundleの回収と無効なbundleを評価する。
- Data and results: 多くの方式は真のbundleの90%を一部でも含むが、正しいもの以上に多い無効bundleも作り、その半分はgroup間で系統的だった。
- Novelty: 検出率だけでなく、構造推定の多義性と偽の経路を共通のchallengeで示す。
- Limitations: 90%は全線維の90%を正確に復元した値ではない。simulationに基づく結果で、生体のground truthを直接網羅したものでもない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/29116093/

### Paper: Large-Scale Gradients in Human Cortical Organization
- Source: PubMed
- Canonical ID: pmid:29203085
- Publication date: 2017-12-01
- URL: https://pubmed.ncbi.nlm.nih.gov/29203085/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 感覚運動からtransmodal領域へ続く、皮質の主要gradientを整理する。
- Objective: 領域の並びと構造制約から、機能の連続的な範囲を理解する。
- Methods: 複数の皮質特徴に現れる優勢なgradientを解説し、内在的な座標系を提案する。
- Data and results: 感覚運動–transmodalという組織軸を、皮質機能の分布を読む座標として位置付ける。
- Novelty: 境界で分かれた領域だけでなく、連続軸による皮質の記述を強調する。
- Limitations: 解説・統合の論文で独自の汎用予測精度を示すものではない。gradientが単一の神経計算機構を意味するとは限らない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/29203085/

### Paper: Towards deep learning with segregated dendrites
- Source: PubMed
- Canonical ID: pmid:29205151
- Publication date: 2017-12-05
- URL: https://pubmed.ncbi.nlm.nih.gov/29205151/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 隔てられた樹状突起区画を使い、多層の局所学習をモデル化する。
- Objective: 深層学習の信用割当を、皮質錐体細胞に近い形で実装できるか調べる。
- Methods: 感覚入力と上位feedbackを電気的に分けたmulti-compartment neuronで、層間のsynapse更新を協調させる。
- Data and results: 単層より良い画像分類と高次表現の獲得を示し、樹状突起の分離が深い学習を支え得ると報告。
- Novelty: 細胞内の区画構造を、層間の教示信号を処理する計算資源として使う。
- Limitations: 編者の注意: 生物的な着想を持つ計算モデルであり、生体の全区画で同じ学習手順が実行されると確認した研究ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/29205151/

### Paper: Distinct contributions of functional and deep neural network features to representational similarity of scenes in human brain and behavior
- Source: PubMed
- Canonical ID: pmid:29513219
- Publication date: 2018-03-07
- URL: https://pubmed.ncbi.nlm.nih.gov/29513219/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: sceneの行動上の意味とDNN特徴が、脳・行動の類似性へどう寄与するかを分ける。
- Objective: 視覚と意味の相関による説明の混同を減らす。
- Methods: 刺激の事前選択で三つの特徴model間の相関を下げ、行動と脳応答の説明分散を分割する。
- Data and results: 行動には可能な行為と高次DNN特徴が独自に寄与。scene選択皮質では中・高次DNN特徴が独自に説明し、object labelは寄与しなかった。
- Novelty: 表現類似性の一致を、相関した複数の特徴へ分けて検証する。
- Limitations: scene選択皮質は行動に関連する情報の一部のみを表すと著者が指摘。使う特徴modelの範囲内の結論でもある。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/29513219/

### Paper: A Task-Optimized Neural Network Replicates Human Auditory Behavior, Predicts Brain Responses, and Reveals a Cortical Processing Hierarchy
- Source: PubMed
- Canonical ID: pmid:29681533
- Publication date: 2018-04-19
- URL: https://pubmed.ncbi.nlm.nih.gov/29681533/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 音声・音楽認識を解く網から、人間の聴覚行動と皮質応答を予測する。
- Objective: 自然音を扱う聴覚系の定量モデルを作る。
- Methods: 階層網を音声・音楽の課題で最適化し、行動の誤りとfMRI応答を比較する。
- Data and results: 高性能網は人並みの課題性能と似た誤りを示し、従来filterより皮質応答を予測。中間・後段層が一次・非一次領域へ対応した。
- Novelty: 課題駆動モデルから、聴覚処理の分岐と階層の候補を導く。
- Limitations: 編者の注意: 生体の配線を直接復元した網ではなく、選ぶ課題や刺激の範囲で階層対応の解釈が変わる。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/29681533/

### Paper: Vector-based navigation using grid-like representations in artificial agents
- Source: PubMed
- Canonical ID: pmid:29743670
- Publication date: 2018-05-09
- URL: https://pubmed.ncbi.nlm.nih.gov/29743670/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: path integrationを学ぶ人工agentにgrid様表現が現れ、navigationへ役立つことを示す。
- Objective: 哺乳類の空間表現の計算機能を、柔軟なagent設計へ利用する。
- Methods: RNNに自己運動の積分を学ばせ、得た表現を深層強化学習の目標探索へ組み込む。
- Data and results: 未知・変化する環境で比較agentと熟練者を上回る結果、shortcut行動、vector計算に必要な量の抽出を報告。
- Novelty: grid様表現の自然な出現と、行動上の効用を同じagentで示す。
- Limitations: 編者の注意: 比較は設計した仮想環境と課題の範囲であり、哺乳類の全般的なnavigationや学習能力を超えたという意味ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/29743670/

### Paper: Unsupervised Discovery of Demixed, Low-Dimensional Neural Dynamics across Multiple Timescales through Tensor Component Analysis
- Source: PubMed
- Canonical ID: pmid:29887338
- Publication date: 2018-06-07
- URL: https://pubmed.ncbi.nlm.nih.gov/29887338/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: TCAはneuron・trial内時間・trial間変化を分け、学習に伴う集団動態を抽出する。
- Objective: millisecondsの活動と数日にわたる変化を同じ表現で捉える。
- Methods: 神経データのtensorをneuron因子、時間因子、trial因子の三つの低次元成分へ分解する。
- Data and results: 人工網、rodent前頭皮質のmaze、macaqueのBMI学習のデータで、速い動態と遅い学習変化を分析する。
- Novelty: 短時間の回路活動と長期学習を、連結した三因子で分離する。
- Limitations: 編者の注意: 分解成分は数学的に抽出した表現で、細胞assemblyや認知状態との対応は追加の解釈・検証を要する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/29887338/

### Paper: Inferring single-trial neural population dynamics using sequential auto-encoders
- Source: PubMed
- Canonical ID: pmid:30224673
- Publication date: 2018-09-17
- URL: https://pubmed.ncbi.nlm.nih.gov/30224673/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: LFADSは単一trialのspikeから、潜在的な神経力学を深層学習で推定する。
- Objective: 試行平均では失われる動態を、部分的で雑音のある記録から復元する。
- Methods: sequential autoencoderによるlatent factor analysis via dynamical systemsを用いる。
- Data and results: macaque・人間の運動皮質で行動予測、精密な発火率、選択と相関する摂動を推定し、月をまたぐ非重複sessionも統合する。
- Novelty: 単一trialの発火を、生成的な潜在力学モデルとして推定する。
- Limitations: 編者の注意: 推定状態はモデル依存であり、観測されなかったneuronや摂動の真の生理量を直接測ったものではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/30224673/

### Paper: Cortical population activity within a preserved neural manifold underlies multiple motor behaviors
- Source: PubMed
- Canonical ID: pmid:30315158
- Publication date: 2018-10-12
- URL: https://pubmed.ncbi.nlm.nih.gov/30315158/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 複数の運動課題で、運動皮質の共通するneural modeが保持されることを示す。
- Objective: 多様な筋活動を、一つの集団表現がどう柔軟に生成するかを調べる。
- Methods: 手首・reach-to-grasp課題間で、神経共分散の主要modeとその活動を比較する。
- Data and results: 筋・単一unitのpatternは異なってもmodeは大部分保持。共通の時間特徴と筋出力への写像に対応するmode群を報告。
- Novelty: 行動間で変わる単一細胞活動と、保たれる集団manifoldを分ける。
- Limitations: 編者の注意: 調べた技能課題での保存であり、未学習のすべての行動を同じ固定manifoldで表せる保証ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/30315158/

### Paper: A Neural Population Mechanism for Rapid Learning
- Source: PubMed
- Canonical ID: pmid:30344047
- Publication date: 2018-10-18
- URL: https://pubmed.ncbi.nlm.nih.gov/30344047/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 速い運動適応を、回路の接続変更ではなく集団の活動部分空間で説明する。
- Objective: 一度の誤りでも起こる急な行動変化の神経機構を探る。
- Methods: 到達運動の摂動適応中に数百neuronのPMd–M1関係をモデル化し、output-null/potent部分空間を分ける。
- Data and results: PMdのoutput-null準備活動は適応とともに変化し、M1へ送るoutput-potent写像は保持されると報告。
- Novelty: 固定的な下流写像のもとで準備状態を変え、速く出力を調整する機構を示す。
- Limitations: 編者の注意: 接続変化なしで説明できる候補を示すが、あらゆる学習で可塑性が不要という結論ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/30344047/

### Paper: What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior
- Source: PubMed
- Canonical ID: pmid:30359611
- Publication date: 2018-10-24
- URL: https://pubmed.ncbi.nlm.nih.gov/30359611/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 空間だけでなく、抽象的な関係を整理する認知地図の原理をreviewする。
- Objective: 柔軟な一般化を支える共通の知識表現を探る。
- Methods: 空間・非空間課題の神経証拠と理論、地図様表現を学ぶ人工agentを比較する。
- Data and results: 異なる領域の関係を統合する原理を示し、人間の抽象化・推論への可能性を議論する。
- Novelty: 空間navigationを、一般的な関係知識とagentの柔軟性へ接続する。
- Limitations: 著者は人間の極端な一般化への含意を推測として扱う。編者の注意: 地図様表現の類似からすべての知識が同じ符号とは断言しない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/30359611/

### Paper: Towards reconstructing intelligible speech from the human auditory cortex
- Source: PubMed
- Canonical ID: pmid:30696881
- Publication date: 2019-01-29
- URL: https://pubmed.ncbi.nlm.nih.gov/30696881/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 人間の聴覚皮質から、深層回帰と音声合成で聞き取れる音声を再構成する。
- Objective: 従来の低品質な音声再構成を改善し、BCIへつなぐ。
- Methods: 線形・非線形回帰、spectrogram・合成器パラメータ、低・高周波の神経特徴を比較する。
- Data and results: 閉じた数字認識課題で、全周波数から合成器を推定するDNNが最高成績。線形spectrogram基準に対し明瞭度65%改善と報告。
- Novelty: 音響特徴の単純復元から、生成器のパラメータ推定へ接続する。
- Limitations: 数字の閉集合の再構成であり、自由な思考や任意の発話を読み取った実証ではない。65%は基準に対する改善値。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/30696881/

### Paper: Towards the neural population doctrine
- Source: PubMed
- Canonical ID: pmid:30877963
- Publication date: 2019-03-13
- URL: https://pubmed.ncbi.nlm.nih.gov/30877963/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 神経計算の単位としてpopulationを重視する研究の進展を整理する。
- Objective: 同時大規模記録が、単一neuronだけでは分からない何を明らかにしたかを示す。
- Methods: 相関変動、decoding、神経動態、人工neural networkの4領域をreviewする。
- Data and results: populationの共同解析による知見を統合し、集団が多くの領域の計算単位となる見方を提示する。
- Novelty: 装置のreviewより、それによって可能になった科学的理解に焦点を当てる。
- Limitations: 編者の注意: populationの重視は単一細胞の役割を否定するものではなく、全領域に同じ計算単位を仮定しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/30877963/

### Paper: Bayesian Computation through Cortical Latent Dynamics
- Source: PubMed
- Canonical ID: pmid:31320220
- Publication date: 2019-07-15
- URL: https://pubmed.ncbi.nlm.nih.gov/31320220/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 時間長を再現する課題で、事前分布が皮質の潜在表現を歪める仕組みを調べる。
- Objective: 再帰的なneuron集団がBayes統合をどう実装するかを探る。
- Methods: monkeyの時間間隔再現課題の前頭活動と、同じ課題を解くRNNを分析する。
- Data and results: 事前統計による表現の変形が感覚から運動への写像へ反映され、RNNでは低次元の曲がったmanifoldが支えていた。
- Novelty: Bayes的行動と、潜在力学の幾何学的な変形を対応付ける。
- Limitations: 編者の注意: RNNで調べた因果候補と、生体で同じ回路機構を直接操作して証明することは区別する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/31320220/

### Paper: Single-trial neural dynamics are dominated by richly varied movements
- Source: PubMed
- Canonical ID: pmid:31551604
- Publication date: 2019-09-24
- URL: https://pubmed.ncbi.nlm.nih.gov/31551604/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 課題中の神経活動に、指示されていない多様な運動が大きく寄与することを示す。
- Objective: 課題変数だけで活動を説明する際の見落としを調べる。
- Methods: video・sensorで運動を測り、widefield・二光子画像とNeuropixels記録を対応付ける。
- Data and results: 皮質全体の活動は運動に強く支配され、似たtrial平均のneuronでも異なる認知・運動の組合せを反映していた。
- Novelty: 単なるnoiseとされる試行間変動を、観測可能な行動で説明する。
- Limitations: 編者の注意: 認知活動が存在しないという結果ではない。課題と同期した微小運動を測ることが解釈の条件になる。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/31551604/

### Paper: A deep learning framework for neuroscience
- Source: PubMed
- Canonical ID: pmid:31659335
- Publication date: 2019-10-28
- URL: https://pubmed.ncbi.nlm.nih.gov/31659335/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 神経科学を、目的関数・学習rule・architectureの三軸で考えるframework。
- Objective: 脳が課題を実装する仕組みを、最適化の観点から研究する。
- Methods: AIで設計する三要素を神経科学へ対応付け、理論と実験を進める事例を論じる。
- Data and results: 多様な知覚・認知・運動を研究するための原理的な見方を提案。独自benchmarkの精度比較ではない。
- Novelty: 脳に似た構造を使うだけでなく、何をどう学ぶかを同等に重視する。
- Limitations: 論考であり脳の唯一の目的関数を同定した結果ではない。課題・rule・構造の寄与は実験で分離する必要がある。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/31659335/

### Paper: Towards spike-based machine intelligence with neuromorphic computing
- Source: PubMed
- Canonical ID: pmid:31776490
- Publication date: 2019-11-27
- URL: https://pubmed.ncbi.nlm.nih.gov/31776490/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: neuromorphic computingのspike符号・event駆動の算法とhardwareを整理する。
- Objective: 脳を参考にした計算を、機械知能とエネルギー効率へどうつなぐかを検討する。
- Methods: 生物回路のsilicon実装から、spike型algorithmのhardware化までをreviewし、学習と設計の基礎を示す。
- Data and results: algorithm–hardware共同設計の課題と展望を提示。要旨は特定装置の普遍的な省電力率を報告するものではない。
- Novelty: 生体模倣だけでなく、事象駆動表現と実装の整合を研究の中心へ据える。
- Limitations: 編者の注意: spikeを使えば自動的に低消費電力・高性能になるわけではなく、符号化、課題、hardware条件で評価する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/31776490/

### Paper: A distributional code for value in dopamine-based reinforcement learning
- Source: PubMed
- Canonical ID: pmid:31942076
- Publication date: 2020-01-15
- URL: https://pubmed.ncbi.nlm.nih.gov/31942076/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: distributional RLを参考に、dopamineが報酬の平均だけでなく分布を表すと提案する。
- Objective: 報酬予測誤差の理論ではドーパミン神経が将来報酬の期待値を知らせると捉えることが多い。しかし同じ平均でも大きく異なる不確実性や分布を持つ報酬を識別できるかは別の問いである。分布的強化学習の計算概念が神経活動にも存在するかを検証した。
- Methods: 分布的強化学習における価値分布の表現を参考に、報酬を異なる程度に過大・過小評価する神経群が並列に存在する場合の応答予測を導出。マウス腹側被蓋野の単一細胞活動を記録し、報酬確率分布を変える条件で、平均予測誤差モデルとは異なるパターンが現れるかを検証した。
- Data and results: 異なるドーパミンニューロンが報酬の分布の異なる側面を反映するという、分布的価値表現と整合する証拠を報告。確認範囲の要旨では対象単位数や統一した改善率の絶対値は示されず、標準的なMLベンチマークの比較研究ではない。
- Novelty: AIの分布的強化学習から生物の神経応答への検証可能な仮説を導き、単一の期待報酬より豊かな価値表現を示した。『平均値だけでは失われる不確実性』を保持する利点を生体から再検討できる。
- Limitations: 特定の報酬学習・マウスのドーパミン系を扱い、脳全体の意思決定や任意の将来事象の確率分布を同じ機構で表現する証拠ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/31942076/

### Paper: BrainSpace: a toolbox for the analysis of macroscale gradients in neuroimaging and connectomics datasets
- Source: PubMed
- Canonical ID: pmid:32139786
- Publication date: 2020-03-05
- URL: https://pubmed.ncbi.nlm.nih.gov/32139786/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: BrainSpaceは、皮質gradientの抽出・位置合わせ・可視化を行うtoolbox。
- Objective: 離散的な領域を超えた、脳の連続的な組織軸を比較できるようにする。
- Methods: Python/Matlabでmanifold解析とalignmentを実装し、空間自己相関を考慮するnull modelで関連を検証する。
- Data and results: 機能・微細構造のgradientを異なる空間scaleで検証し、手順の利用可能性と一貫性を示す。
- Novelty: gradient解析と、空間的に妥当な関連検定を共通の道具へまとめる。
- Limitations: 編者の注意: 近い領域同士は似るため独立標本とみなす単純検定は不適切。道具の利用だけで生物学的な因果は確定しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32139786/

### Paper: Backpropagation and the brain
- Source: PubMed
- Canonical ID: pmid:32303713
- Publication date: 2020-04-17
- URL: https://pubmed.ncbi.nlm.nih.gov/32303713/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: backpropと脳の学習の関係を、feedbackによる局所的な誤差近似から再検討する。
- Objective: 多層回路のsynapseが行動改善へどう信用割当するかを整理する。
- Methods: 過去・近年の知見を統合し、feedbackで生じる活動差が誤差信号を近似する枠組みを論じる。
- Data and results: 厳密なbackpropの生物学的な難しさを残しつつ、局所的な近似で深い学習が可能となる研究経路を示す。
- Novelty: 逆向きに正確な誤差を運ぶ要求から、活動の差を使う局所学習へ焦点を移す。
- Limitations: レビュー・論考であり、皮質で厳密なbackpropが直接確認されたという結果ではない。複数の実装候補と制約が残る。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32303713/

### Paper: Computation Through Neural Population Dynamics
- Source: PubMed
- Canonical ID: pmid:32640928
- Publication date: 2020-07-08
- URL: https://pubmed.ncbi.nlm.nih.gov/32640928/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 集団の動態がどのように計算を実装し、行動を駆動するかを整理するレビュー。
- Objective: neuronの活動patternから、実行される計算へ説明を進める。
- Methods: 力学系の数学と解析道具を導入し、運動・timing・意思決定・作業記憶の研究を検討する。
- Data and results: 集団動態を用いた成功例と今後の課題を提示。新しい一つの予測器の精度を示す論文ではない。
- Novelty: 計算を静的表象だけでなく、population状態の時間発展として捉える。
- Limitations: 編者の注意: 低次元の軌跡が見えることと、その軌跡が計算の因果的な実装であることは別途検証が必要。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32640928/

### Paper: A solution to the learning dilemma for recurrent networks of spiking neurons
- Source: PubMed
- Canonical ID: pmid:32681001
- Publication date: 2020-07-17
- URL: https://pubmed.ncbi.nlm.nih.gov/32681001/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: e-propは再帰spiking網を、局所情報と学習信号でオンライン学習する。
- Objective: 時間方向のbackpropが持つ生物学的・hardware実装上の負担を減らす。
- Methods: 神経科学の知見と数学的分解を組み合わせ、勾配に基づく逐次学習・強化学習を構成する。
- Data and results: 再帰網の学習でBPTTに近い成績を示すと報告し、chip上の省エネルギー学習への可能性を議論する。
- Novelty: spikeの履歴に依存する局所traceと、後の学習信号を結び付ける。
- Limitations: 編者の注意: BPTTへの近さは試した課題の結果で、脳で同じruleが動く証明や全hardwareでの省電力実測ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32681001/

### Paper: A connectome and analysis of the adult Drosophila central brain
- Source: PubMed
- Canonical ID: pmid:32880371
- Publication date: 2020-09-07
- URL: https://pubmed.ncbi.nlm.nih.gov/32880371/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 成虫ハエのcentral brainの大部分を、化学シナプス単位で再構築したhemibrain資源。
- Objective: 行動を支える回路の具体的な構成を、広い脳領域で調べられるようにする。
- Methods: 標本作製からEM撮像・位置合わせ・分割・シナプス検出・校正までを改善し、細胞型と区画を注釈する。
- Data and results: central brainの多くの回路を公開し、結合強度、motif、区画化の電気的影響などを分析する。
- Novelty: 密な回路地図と、遺伝学的reagentにつなぐ公開資源を統合する。
- Limitations: 脳全体を含む地図ではない。編者の注意: 化学シナプスの構造から、活動や行動の動態まで直接確定はできない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32880371/

### Paper: Training deep neural density estimators to identify mechanistic models of neural dynamics
- Source: PubMed
- Canonical ID: pmid:32940606
- Publication date: 2020-09-17
- URL: https://pubmed.ncbi.nlm.nih.gov/32940606/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: simulationで訓練した深層密度推定器で、神経の機構モデルの事後分布を求める。
- Objective: 複雑で確率的なデータに合うパラメータの範囲を効率的に調べる。
- Methods: 生データまたは特徴からBayes推論を行い、受容野・ion channel・Hodgkin–Huxleyなどで検証する。
- Data and results: 新データを迅速に解析し、甲殻類のrhythm回路の構成空間から補償機構の仮説を得る。
- Novelty: 一つの最良パラメータだけでなく、観測と両立する機構の範囲を推定する。
- Limitations: 編者の注意: 推論結果はsimulationモデル・事前分布・選んだ特徴に依存し、真の生物機構が候補に含まれるかは別問題。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32940606/

### Paper: Artificial Neural Networks for Neuroscientists: A Primer
- Source: PubMed
- Canonical ID: pmid:32970997
- Publication date: 2020-09-23
- URL: https://pubmed.ncbi.nlm.nih.gov/32970997/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 神経科学でANNを作り・解析するための教育的primer。
- Objective: 複雑な行動・活動・接続の仮説を、扱える計算モデルにする。
- Methods: ANNの基礎から、解析・構造・学習の生物学的なcustomizationまで説明し、PyTorchとNotebookの教材を付す。
- Data and results: 神経科学の具体的な問いにANNを使う方法と、手を動かすtutorialを提供する。
- Novelty: ANNをデータ処理だけでなく、神経機構の仮説を作る道具として導入する。
- Limitations: primerであり一つの脳モデルの正しさを検証する論文ではない。既存網の高精度をそのまま神経機構の説明としない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32970997/

### Paper: Topographic organization of the human subcortex unveiled with functional connectivity gradients
- Source: PubMed
- Canonical ID: pmid:32989295
- Publication date: 2020-09-28
- URL: https://pubmed.ncbi.nlm.nih.gov/32989295/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 皮質下の機能結合gradientから、複数scaleのatlasを作る。
- Objective: 皮質中心の地図で抜けやすい皮質下の構造を、全脳解析へ含める。
- Methods: fMRIの結合gradientを4scaleで分割し、超高磁場・課題fMRIで検証。個人差に合わせたatlasも作る。
- Data and results: 最細scaleで新しい両側性27領域を示し、海馬・扁桃体の細分、課題による変化と再現する脳–行動関係を報告。
- Novelty: 皮質下と皮質networkを結び、個人差にも対応する機能atlas。
- Limitations: 編者の注意: fMRI由来の境界はシナプス単位の細胞構築ではなく、scaleや状態による変化を伴う。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/32989295/

### Paper: The Tolman-Eichenbaum Machine: Unifying Space and Relational Memory through Generalization in the Hippocampal Formation
- Source: PubMed
- Canonical ID: pmid:33181068
- Publication date: 2020-11-11
- URL: https://pubmed.ncbi.nlm.nih.gov/33181068/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: TEMは空間と非空間の関係記憶を、共通の海馬–嗅内モデルへ統合する。
- Objective: 環境が変わっても移せる構造知識と、個別の感覚経験を結ぶ。
- Methods: 嗅内の構造基底と、それを感覚表現へ結び付ける海馬を持つモデルを学習する。
- Data and results: grid・border・place様細胞などを再現し、非空間課題にも整合。remapping中の構造転移を同時place/grid記録で確認する。
- Novelty: 関係構造の一般化を、複数細胞型と環境間転移へ一貫して対応付ける。
- Limitations: 編者の注意: 細胞応答の類似を持つ機構モデルで、すべての海馬機能や生体の学習則を同定したものではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/33181068/

### Paper: The connectome of the adult Drosophila mushroom body provides insights into function
- Source: PubMed
- Canonical ID: pmid:33315010
- Publication date: 2020-12-14
- URL: https://pubmed.ncbi.nlm.nih.gov/33315010/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 成虫ハエのキノコ体の配線から、感覚・記憶・出力の関係を解析する。
- Objective: 学習中枢が受ける情報と、行動・他領域へ渡す経路を把握する。
- Methods: 密なconnectomeで視覚入力、MB出力、dopamine系の調節とfeedbackを調べる。
- Data and results: 豊富な視覚入力、下行neuronへの直接結合、感覚modalitiesから出力への構造や中央複合体との連結を報告。
- Novelty: 記憶中枢を孤立した入力出力層としてでなく、全脳のfeedback回路へ位置付ける。
- Limitations: 著者は今後の理論・実験の基盤とする。編者の注意: 解剖から推定した情報の流れを実測の時間動態と同一視しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/33315010/

### Paper: Information flow, cell types and stereotypy in a full olfactory connectome
- Source: PubMed
- Canonical ID: pmid:34032214
- Publication date: 2021-05-25
- URL: https://pubmed.ncbi.nlm.nih.gov/34032214/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: ハエ嗅覚系の完全な経路と、個体内・個体間の型の安定性を解析する。
- Objective: 嗅覚入力から高次回路・下行出力までの情報の流れを整理する。
- Methods: hemibrainで一〜三次neuronを解析し、別datasetとの比較で2脳3半球の形態・接続を照合する。
- Data and results: 嗅覚葉の側性や下流の収束を発見。形態の類似と接続の関係、個体内と個体間の類似した変動を報告。
- Novelty: 情報flowの層構造を抽出する手法と、脳間の定型性の定量比較を示す。
- Limitations: 編者の注意: 脳間比較の標本は2脳3半球で、集団全体の個体差や性差の範囲を網羅するものではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/34032214/

### Paper: A connectome of the Drosophila central complex reveals network motifs suitable for flexible navigation and context-dependent action selection
- Source: PubMed
- Canonical ID: pmid:34696823
- Publication date: 2021-10-26
- URL: https://pubmed.ncbi.nlm.nih.gov/34696823/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: ハエ中央複合体の完全connectomeから、柔軟なnavigationの候補計算を読む。
- Objective: 頭方向の保持、vector navigation、内部状態に応じた行動選択の構造を特定する。
- Methods: EMで全neuronとシナプスを復元し、感覚・運動経路と再帰的motifを分析する。
- Data and results: 新しい細胞型と経路、attractor型の方向保持や感覚運動情報の統合に適するmotifを報告。
- Novelty: 全回路の配線を、navigationの力学系・計算モデルを拘束するblueprintへ変える。
- Limitations: 編者の注意: motifが計算に適することは、全条件で同じ力学が働くという実証ではなく、機能記録・操作が補完になる。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/34696823/

### Paper: The neural architecture of language: Integrative modeling converges on predictive processing
- Source: PubMed
- Canonical ID: pmid:34737231
- Publication date: 2021-11-09
- URL: https://pubmed.ncbi.nlm.nih.gov/34737231/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 多数の言語モデルを、人間の文理解の神経・行動データと比較する。
- Objective: 次単語予測が脳の言語表現を説明する計算目的かを検討する。
- Methods: fMRI・皮質電気記録など複数データでbrain scoreを測り、言語課題性能とarchitectureの寄与を見る。
- Data and results: 強いTransformerは文応答の説明可能分散のほぼ100%に達すると報告。神経・行動の適合は次単語予測と強く相関する。
- Novelty: モデル群を横断し、言語の予測目的と脳・行動の適合を統合比較する。
- Limitations: ほぼ100%は対象データの説明可能分散で、全脳活動・全言語能力の100%ではない。相関から学習則の同一性は確定しない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/34737231/

### Paper: Neural population geometry: An approach for understanding biological and artificial neural networks
- Source: PubMed
- Canonical ID: pmid:34801787
- Publication date: 2021-11-19
- URL: https://pubmed.ncbi.nlm.nih.gov/34801787/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 生物と人工網の表現を、population geometryで理解するレビュー。
- Objective: 高次元表現が情報を埋め込み、課題を解く原理を共通言語で記述する。
- Methods: 表現のuntangling、分類容量、disentanglement、認知地図、運動・認知の動態を幾何学的に整理する。
- Data and results: modalities・領域・architecture・時間scaleをまたぐ幾何学的な説明例を統合する。
- Novelty: 単一neuronと行動の間を、集団表現の形と変化でつなぐ。
- Limitations: 編者の注意: 幾何学的な類似は同じ生物学的実装の証明ではなく、選ぶ距離・次元・課題によって見え方が変わる。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/34801787/

### Paper: FlyWire: online community for whole-brain connectomics
- Source: PubMed
- Canonical ID: pmid:34949809
- Publication date: 2021-12-23
- URL: https://pubmed.ncbi.nlm.nih.gov/34949809/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: FlyWireは全脳の自動再構築を、多人数で校正するオンライン基盤。
- Objective: 膨大な人手校正を分散し、回路データの共有を進める。
- Methods: 空間分割したsupervoxel graphをbrowser上で共同編集し、変更履歴をprogramで利用可能にする。
- Data and results: 機械感覚neuronの再構築・解析で仕組みを実証。校正精度推定や参加の仕組みも利用目的として挙げる。
- Novelty: 画像処理の自動化と、校正の共同作業・公開をつなぐ社会的計算基盤。
- Limitations: 編者の注意: 校正を可能にする資源の論文であり、これ自体が2024年の完成全脳地図の論文ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/34949809/

### Paper: Brains and algorithms partially converge in natural language processing
- Source: PubMed
- Canonical ID: pmid:35173264
- Publication date: 2022-02-16
- URL: https://pubmed.ncbi.nlm.nih.gov/35173264/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 言語モデルと脳の表現の部分的な収束を、構造・学習・課題性能から調べる。
- Objective: 脳らしい文表現を生むモデルの要因を切り分ける。
- Methods: 102人のfMRI・MEGで400文の応答を測り、複数の言語モデルの表現がいつ・どこへ対応するか比較する。
- Data and results: 文脈から単語を予測する能力が主に類似性を説明し、各領域で知覚・語彙・構成的表現の出現と維持を示す。
- Novelty: 単一の強いモデルでなく、モデル群の差から脳対応の原理を検討する。
- Limitations: 編者の注意: isolated sentenceでの部分的な収束であり、自然会話・理解全般や学習則の同一性を実証したものではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/35173264/

### Paper: Evidence of a predictive coding hierarchy in the human brain listening to speech
- Source: PubMed
- Canonical ID: pmid:36864133
- Publication date: 2023-03-02
- URL: https://pubmed.ncbi.nlm.nih.gov/36864133/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 言語モデルと脳応答を比べ、複数時間scaleの階層的予測を検証する。
- Objective: 近い単語の予測だけで、人間の言語処理を十分説明できるか調べる。
- Methods: 短い物語を聞く304人のfMRIへ、通常の言語表現と複数時間scaleの予測表現を線形写像する。
- Data and results: 予測を長いscaleへ広げると脳対応が改善。前頭頭頂は側頭皮質より高次・長距離・文脈的な予測に対応する。
- Novelty: 言語モデルの予測範囲と、人間の階層的な処理の関係を実験で調べる。
- Limitations: 編者の注意: 線形mappingの改善は同一の学習則の証明ではなく、LLMの全般的な言語能力の不足を一因子で説明しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/36864133/

### Paper: The connectome of an insect brain
- Source: PubMed
- Canonical ID: pmid:36893230
- Publication date: 2023-03-10
- URL: https://pubmed.ncbi.nlm.nih.gov/36893230/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 幼虫ハエ全脳のconnectomeを作り、再帰・感覚統合・学習回路の構造を調べる。
- Objective: 行動・価値計算・行動選択を支える全体architectureを明らかにする。
- Methods: シナプス単位の地図から細胞型、hub、前向き・feedback、半球間・神経索との経路を解析する。
- Data and results: 3,016 neuronと548,000シナプスを復元。学習中枢の入出力で特に強い再帰構造と、多感覚・半球間統合を報告。
- Novelty: 局所でなく全脳を対象に、多層shortcutや入れ子の再帰loopを記述する。
- Limitations: 幼虫の脳であり成虫の約14万neuron地図とは別。AI構造との類似は、同じ学習則・能力の実証ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/36893230/

### Paper: Semantic reconstruction of continuous language from non-invasive brain recordings
- Source: PubMed
- Canonical ID: pmid:37127759
- Publication date: 2023-05-01
- URL: https://pubmed.ncbi.nlm.nih.gov/37127759/
- read_level: full_text
- Tags: 基礎文献, 神経科学とAI
- Summary: fMRIの意味表現から、連続した言語の内容を再構成する非侵襲decoder。
- Objective: 脳信号から何を聞いたかを推定する研究は選択肢を限定したラベル分類が中心だったが、自然な連続言語の意味を非侵襲的に復元できるかは別の問題である。fMRIの低い時間分解能から文章を逐語的に読むのではなく、脳で表現された意味を再構成することを目指す。
- Methods: 中心となる3人の参加者について、各約16時間の物語を聴取している間のfMRIを記録。言語表現とfMRI反応の対応を学習した個人別の意味エンコーディングモデルを作り、言語モデルが生成した候補文章の意味表現と観測脳活動をbeam searchで照合して文章を選ぶ。未見の物語、心の中で想像した発話、無音映像で検証した。
- Data and results: 原文との逐語一致は低く、主要3人の単語誤り率WERは約0.9243〜0.9407。それでも意味的に近い内容が再構成され、学習した入力と異なる種類の刺激への転移も報告した。他人の脳データだけで学習したモデルはうまく機能せず、参加者が別の物語を考えると復号を妨げられる。これは『任意の人の思考を無断で正確に文章化した』という意味ではない。
- Novelty: fMRIの測定信号だけで語を逐語的に検出するのではなく、脳活動の意味表現とLMの言語的事前分布を合わせて連続する内容を推定した。数値・信号から文章を生成する場合、言語モデルが補った情報と測定から支持された意味を分けて評価する必要があることが分かる。
- Limitations: 主要評価は3人で個人別の約16時間の学習が必要。fMRIの時間分解能と生成モデルの事前知識の影響が大きく、文章の事実性や逐語的復元は保証されない。協力しない対象への一般化は示していない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/37127759/

本文の照合箇所: [Introduction・ResultsのLanguage decoder・Privacy implications・Sources of decoding error](https://pmc.ncbi.nlm.nih.gov/articles/PMC11304553/)。

### Paper: Learnable latent embeddings for joint behavioural and neural analysis
- Source: PubMed
- Canonical ID: pmid:37138088
- Publication date: 2023-05-03
- URL: https://pubmed.ncbi.nlm.nih.gov/37138088/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: CEBRAは行動と神経記録を併用し、安定した低次元の潜在表現を学ぶ。
- Objective: 行動の仮説と教師なしの探索を、非線形の神経表現へ結び付ける。
- Methods: 教師あり・自己教師ありのembeddingを単一/複数sessionで学び、一貫性を比較やdecodingへ使う。
- Data and results: calcium・電気記録、複数種・感覚運動課題で検証。位置・運動・自然videoのdecodingやmodalities間の整合を示す。
- Novelty: 行動条件と神経状態を柔軟に組み合わせる、一貫性を重視した表現学習。
- Limitations: 編者の注意: 教師あり潜在空間には行動labelの情報が入るため、独立検証や教師なし条件を分けて解釈する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/37138088/

### Paper: A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution
- Source: PubMed
- Canonical ID: pmid:38723085
- Publication date: 2024-05-10
- URL: https://pubmed.ncbi.nlm.nih.gov/38723085/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 人間の側頭皮質約1立方mmを、超微細構造で再構築した公開資源。
- Objective: 人間の細胞・シナプスの組織を、高い解像度で調べる。
- Methods: てんかんfocusへ到達するために外科切除された組織を、計算量の大きいEM再構築で解析する。
- Data and results: 約57,000細胞、約1.5億シナプス、1.4PBを報告。gliaはneuronの約2倍で、最大50synapseのまれな強い軸索入力も観察。
- Novelty: 人間皮質の局所領域を、petavoxel規模の配線・形態資源へする。
- Limitations: 約57,000はneuronだけでなく全細胞の数。1人の局所切除組織であり、人間全脳や健康な全人口を代表する地図ではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/38723085/

### Paper: Connectome-constrained networks predict neural activity across the fly visual system
- Source: PubMed
- Canonical ID: pmid:39261740
- Publication date: 2024-09-11
- URL: https://pubmed.ncbi.nlm.nih.gov/39261740/
- read_level: full_text
- Tags: 基礎文献, 神経科学とAI
- Summary: 配線で制約したハエ視覚モデルを課題学習し、細胞ごとの活動を予測する。
- Objective: 接続以外の生物学的詳細が未知でも、計算から活動を推定できるか検証する。
- Methods: 視覚運動経路64細胞型の配線を固定し、主に非spiking・単一区画のneuronと線形閾値synapseを課題で最適化。細胞型間でパラメータを共有する。
- Data and results: 視覚運動課題を学んだ予測が、26研究の活動測定と整合。疎な接続のとき成功しやすいことも示す。
- Novelty: connectomeと課題最適化を使い、実験可能な細胞別の機構仮説を生成する。
- Limitations: 著者は電気シナプス・非線形化学synapse・神経調節を扱わないとする。課題は運動検出に限られ、同じ配線・課題でも異なる応答のモデルclusterが現れる。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/39261740/

本文の照合箇所: [DMN of the fly visual system・Predictions cluster across DMN ensemble・Discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC11525180/)。

### Paper: Neuronal wiring diagram of an adult brain
- Source: PubMed
- Canonical ID: pmid:39358518
- Publication date: 2024-10-02
- URL: https://pubmed.ncbi.nlm.nih.gov/39358518/
- read_level: full_text
- Tags: 基礎文献, 神経科学とAI
- Summary: 成虫雌ハエの全脳を、約14万neuronと約5千万化学シナプスで記述する地図。
- Objective: 脳の計算を回路レベルで調べるには個々の神経細胞の接続先を追える必要があるが、局所の配線図だけでは感覚入力から運動出力までの経路を一貫して見ることができない。成虫の一個体の全脳を細胞単位で再構築し、検索可能な接続資源を作る。
- Methods: 雌ショウジョウバエの全脳を電子顕微鏡で撮像・再構築し、細胞の形態、神経経路、細胞型、推定神経伝達物質、化学シナプスの接続を登録する。局所のニューロン間結合だけでなく脳領域間の投射、感覚入力から下行神経への経路を検索できるようにした。神経活動を直接測る実験とは異なり、主な成果は形態・接続の定量的な地図である。
- Data and results: 全脳139,255ニューロンと約5×10^7個の化学シナプスを再構築し、光受容系から運動系にいたる候補経路を追跡可能とした。これによって『どの細胞がどの細胞へ接続するか』の候補が細胞型・結合数に基づいて得られるが、シナプスの強さ、神経修飾、特定行動を起こす因果効果を配線図だけで測定したわけではない。
- Novelty: 局所地図の積み重ねから、成虫全脳を検索できるシナプス単位の接続資源へ進んだ。後続の全脳シミュレーションや実験で操作すべき神経経路の候補を絞る基盤となる。構造の網羅性と機能の理解は別の到達点である。
- Limitations: 電気シナプス、神経調節、細い枝の未回収、細胞型による分割精度の差がある。雌の一個体の地図を、全個体での結合の普遍性やハエの全行動の再現と混同できない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/39358518/

本文の照合箇所: [DiscussionのElectron microscopy data acquisition and reconstruction・Limitations of our reconstruction](https://pmc.ncbi.nlm.nih.gov/articles/PMC11446842/)。

### Paper: A Drosophila computational brain model reveals sensorimotor processing
- Source: PubMed
- Canonical ID: pmid:39358519
- Publication date: 2024-10-02
- URL: https://pubmed.ncbi.nlm.nih.gov/39358519/
- read_level: full_text
- Tags: 基礎文献, 神経科学とAI
- Summary: connectomeと伝達物質予測を使うハエ全脳モデルで、摂食・groomingの回路を予測する。
- Objective: 全脳配線図には神経細胞の接続関係が収録されていても、そのままでは味覚刺激がどの行動を引き起こすかという動的な予測にはならない。接続と伝達物質の情報を簡単なニューロンモデルに取り込み、感覚運動の仮説を作って実験で検証できるかを調べる。
- Methods: ハエ全脳のコネクトームにleaky integrate-and-fire型ニューロンを配置し、神経伝達物質の情報から興奮・抑制の条件を設定。味覚や機械感覚ニューロン群を刺激するシミュレーションにより下流の活動と摂食・毛づくろいに関係する回路を予測し、光遺伝学と行動実験の結果との一致を評価した。生体ニューロンの全てのダイナミクスを再現した計算モデルではない。
- Data and results: 検証可能だった164の予測のうち91%が操作実験と整合したと報告。ただし陰性例を多く含むスクリーニングを除くと84%であり、単純な全正解率の読み方には注意が必要。味覚モダリティの組合せと、摂食や毛づくろいに至る回路の複数の仮説を提示した。
- Novelty: 『どこに結合があるか』という静的データから、『刺激条件を変えたら何が起きるか』という検証可能な予測へ進んだ点。AIで構造や知識グラフを使う場合も、単なる結合の列挙と介入後の結果を予測する動力学モデルは異なる段階にあるという示唆を持つ。
- Limitations: 基底発火ゼロ、一律の単純ニューロン、未観測の神経修飾や電気シナプスの省略などがあり、抑制や内的状態が重要な回路では予測が弱くなり得る。164件の検証結果を全ハエ行動の再現率と読み替えることはできない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/39358519/

本文の照合箇所: [Connectome models・Drosophila taste coding・MethodsのComputational modelling limitations](https://pmc.ncbi.nlm.nih.gov/articles/PMC11446845/)。

### Paper: Whole-brain annotation and multi-connectome cell typing of Drosophila
- Source: PubMed
- Canonical ID: pmid:39358521
- Publication date: 2024-10-02
- URL: https://pubmed.ncbi.nlm.nih.gov/39358521/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: FlyWire全脳に細胞型・発生系列の体系的注釈を付け、別個体の地図と比較する。
- Objective: 脳間で再同定できる細胞型を定義し、比較connectomicsを可能にする。
- Methods: 形態と接続を跨ぐ定量比較から細胞型を定義し、FlyWireとhemibrainを共同解析する。
- Data and results: 8,453型を注釈し、そのうち4,581を新規型として報告。hemibrainで提案された型の約3分の1はFlyWireで確実に再同定できず、脳間比較による再定義を検証する。
- Novelty: 脳内だけの類似性でなく、脳間の対応による細胞型の定義を検証する。
- Limitations: すべての旧細胞型が脳間で安定に対応するわけではない。著者は細胞数・接続の定型性と変動の双方を示し、分類の信頼性の基準を提示する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/39358521/

### Paper: Neuronal parts list and wiring diagram for a visual system
- Source: PubMed
- Canonical ID: pmid:39358525
- Publication date: 2024-10-02
- URL: https://pubmed.ncbi.nlm.nih.gov/39358525/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 成虫ハエ視葉の細胞型一覧と、型の間の接続規則を整理する。
- Objective: 視覚系の計算を理解するための部品と配線をそろえる。
- Methods: 全connectomeの高次元特徴の距離と識別特徴を用い、細胞型の一貫性と領域間接続を分析する。
- Data and results: 一部の既存familyは型数が倍以上となり、新しいSm familyや領域横断の型を発見。運動・物体・色覚の候補機能を提案する。
- Novelty: 密な細胞地図を、細胞型単位の簡潔な回路図へ縮約する。
- Limitations: 編者の注意: 型の分離は接続特徴に基づき、すべての型の機能が生理実験で確定したわけではない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/39358525/

### Paper: Network statistics of the whole-brain connectome of Drosophila
- Source: PubMed
- Canonical ID: pmid:39358527
- Publication date: 2024-10-02
- URL: https://pubmed.ncbi.nlm.nih.gov/39358527/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 成虫ハエ全脳のmotif・hub・領域間構造をnetwork解析する。
- Objective: 配線の統計的な構成が、情報の統合・伝達をどう支えるかを調べる。
- Methods: 2・3節点motifの頻度と強さを、伝達物質・細胞型に対応付け、78領域のsubnetworkも比較する。
- Data and results: 約30%のneuronが関わるrich-club構造を報告し、統合役・broadcast役の候補集合を同定する。
- Novelty: 全脳のシナプス構造で、局所motifと広域hubを同じ資源から解析する。
- Limitations: 編者の注意: rich-clubの節点群の役割は構造からの候補であり、実際の情報伝達や行動への因果寄与は別途検証する。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/39358527/

### Paper: Connectome-driven neural inventory of a complete visual system
- Source: PubMed
- Canonical ID: pmid:40140576
- Publication date: 2025-03-26
- URL: https://pubmed.ncbi.nlm.nih.gov/40140576/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 雄ハエの右視葉の密な地図から、視覚neuronの型を体系化する。
- Objective: 形態・配線と視覚の空間計算を結び、操作のための道具もそろえる。
- Methods: FIB-SEMで再構築し、形態の定量、接続、伝達物質、専門家校正を統合して型分けする。
- Data and results: 約53,000 neuronを732型へ分類し、約半分を新たに命名。対応するsplit-GAL4系統を公開する。
- Novelty: connectome由来の型一覧と、型を標的化する遺伝学的資源を結ぶ。
- Limitations: 右視葉の地図であり全脳ではない。編者の注意: 型の命名・操作可能性と、その型の視覚機能の確定は別の到達点。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/40140576/

### Paper: Functional connectomics spanning multiple areas of mouse visual cortex
- Source: PubMed
- Canonical ID: pmid:40205214
- Publication date: 2025-04-09
- URL: https://pubmed.ncbi.nlm.nih.gov/40205214/
- read_level: full_text
- Tags: 基礎文献, 神経科学とAI
- Summary: MICrONSはmouse視覚皮質の大規模な活動記録とシナプス配線を対応付ける。
- Objective: シナプスを詳細に記録した配線図と、視覚刺激に応答する神経活動の測定を別の標本で得ても、どの接続がどの機能に結びつくかを直接検討するのは難しい。同じ皮質組織の構造と活動を対応づけて、回路モデルを検証可能な共有データ基盤を構築する。
- Methods: 覚醒マウスが自然・人工の視覚刺激を見ている間に一次視覚皮質と複数の高次視覚領域の大規模カルシウム画像を記録。その後同じ組織の電子顕微鏡によるシナプス配線を再構築し、機能記録したニューロンを形態・結合へ対応させる。接続だけのデータや活動だけのデータよりも、両者の一致を検証できる条件を整えた。
- Data and results: 約75,000ニューロンの機能記録と、20万超の細胞・約5億シナプスを含む電子顕微鏡再構築を提供した。活動と接続の対応から視覚応答に関わる回路仮説を検証するデータを得られる。ここで示す細胞数には活動記録対象以外の細胞も含まれ、75,000と20万超を同じ神経細胞の測定数として合算できない。
- Novelty: 大規模なコネクトーム資源に、同じ脳組織の刺激応答という機能を対応づけた点。結合の有無と活動の関連を統計的に説明し、モデルの予測を実測へ照合できる新しい基盤として意義がある。
- Limitations: 測定範囲はマウスの視覚皮質の一部で、全脳でも全行動でもない。電顕再構築には細い軸索・スパインの校正誤差があり、カルシウム測定は電気活動を直接測るものではない。相関と因果の区別には回路操作実験が必要。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/40205214/

本文の照合箇所: [DiscussionのAdvances and limits in large-scale EM](https://pmc.ncbi.nlm.nih.gov/articles/PMC11981939/)。

### Paper: Distributed control circuits across a brain-and-cord connectome
- Source: PubMed
- Canonical ID: pmid:42259917
- Publication date: 2026-06-08
- URL: https://pubmed.ncbi.nlm.nih.gov/42259917/
- read_level: full_text
- Tags: 基礎文献, 神経科学とAI
- Summary: ハエの脳と腹側神経索を結ぶ地図から、分散制御の組織を調べる。
- Objective: 局所の感覚feedbackと、全身行動を支える長距離制御の関係を明らかにする。
- Methods: 密な成虫connectomeで、motor・内分泌・内臓出力への経路と上行・下行neuronのmoduleを解析する。
- Data and results: 同じ身体部位の感覚から出力への局所loopと、複数部位や内臓を結ぶ行動中心moduleを報告。学習・navigation領域が監督する。
- Novelty: 単一の脳内中枢より、並列・分散・身体に対応した制御architectureを示す。
- Limitations: 標本はlamina・単眼系を欠き、一部の触角感覚神経に損傷があると著者が記す。型の自動matchingは人手で校正される。構造上の影響指標から実際の動態・因果作用まで確定しない。
- Publication date note: PubMedの電子公開日。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/42259917/

本文の照合箇所: [MethodsのSpecimen・Cell-type matching and annotation、AN/DN behaviour-centric modules](https://pmc.ncbi.nlm.nih.gov/articles/PMC13518251/)。

### Paper: Sexual dimorphism in the complete Drosophila male central nervous system connectome
- Source: PubMed
- Canonical ID: pmid:42691995
- Publication date: 2026-09-03
- URL: https://pubmed.ncbi.nlm.nih.gov/42691995/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 雄ハエの全中枢神経系を作り、雌とのシナプス単位の性差を比較する。
- Objective: 性に特異的なneuronが、感覚から運動までの回路へどう組み込まれるかを調べる。
- Methods: 脳と神経索の配線を校正・注釈し、fruitless/doublesex発現と細胞型を対応付ける。
- Data and results: 166,700 neuron・11,710型を含む資源を報告。比較では8,069同型、138異型、289雄特異・71雌特異型を示す。
- Novelty: 脳だけでなく中枢神経系全体と、雌雄比較をシナプス解像度でつなぐ。
- Limitations: 編者の注意: 性特異的接続は高次中枢へ偏るが、構造の性差から個々の行動・感情の差まで自動的に確定しない。
- Publication date note: PubMedの正確な冊子刊行日（先行電子公開日の日単位記録は未確認）。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/42691995/

### Paper: Dopamine neurons report an error in the temporal prediction of reward during learning
- Source: PubMed
- Canonical ID: pmid:10195164
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/10195164/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: monkeyのdopamine neuronが、報酬の発生と時刻の予測誤差を表す。
- Objective: 報酬学習の進行と、予期した時刻からのずれを調べる。
- Methods: 学習の各段階、予期しない時刻の報酬、予期した報酬の省略に対する発火を測定する。
- Data and results: 予測が成立すると報酬時の活性は弱まり、予期しない時刻では活性、予期時刻の省略では抑制が見られた。
- Novelty: 何が起きるかに加え、いつ起きるかの誤差を教示信号へ結ぶ。
- Limitations: 編者の注意: 報酬の時刻に関する結果であり、脳が一般的な事象時刻分布を同じ信号だけで表すという証明ではない。
- Publication date note: PubMedと出版社を照合したが、出版社のPublished表記もAugust 1998までで日単位は未確認。月初を推測で補わない。出典: https://www.nature.com/articles/nn0898_304

### Paper: Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects
- Source: PubMed
- Canonical ID: pmid:10195184
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/10195184/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 階層的な予測と誤差の往復で、視覚皮質の受容野の特徴を説明する。
- Objective: 古典的受容野の外側による効果に、feedbackを含む説明を与える。
- Methods: 上位から下位へ予測、下位から上位へ残差を送る網を自然画像で学習する。
- Data and results: 単純細胞に似た受容野と、一部の誤差neuronのendstoppingなどをモデルで再現する。
- Novelty: 予測誤差を伝える階層的な符号化を、具体的な視覚特性へ対応させる。
- Limitations: 編者の注意: 機能的なモデルの再現であり、生体がこの計算法を唯一の方法として使うという実証ではない。
- Publication date note: PubMedと出版社を照合したが、出版社のPublished表記もJanuary 1999までで日単位は未確認。月初を推測で補わない。出典: https://www.nature.com/articles/nn0199_79

### Paper: Competitive Hebbian learning through spike-timing-dependent synaptic plasticity
- Source: PubMed
- Canonical ID: pmid:10966623
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/10966623/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: STDPによる時間依存の可塑性だけで、入力間の競争が生じるモデルを示す。
- Objective: Hebbian学習に必要な競争を、spikeの相対時刻から説明する。
- Methods: 前・後synapseの発火時刻に依存する学習をsimulationし、synapse強度と発火の変化を調べる。
- Data and results: 短い遅延や相関した群の入力が強まり、効きにくい入力は弱まる。不規則で入力時刻に敏感な発火を形成する。
- Novelty: Hebbian強化と競争・balancedな発火を、同じ時刻学習ruleから導く。
- Limitations: モデル研究。編者の注意: 生体で観測したSTDPの存在と、この競争機構がそのまま働く証明は別である。
- Publication date note: PubMedと出版社を照合したが、出版社のPublished表記もSeptember 2000までで日単位は未確認。月初を推測で補わない。出典: https://www.nature.com/articles/nn0900_919

### Paper: Small-world brain networks
- Source: PubMed
- Canonical ID: pmid:17079517
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/17079517/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: small-world構造を使い、脳の局所専門化と広域統合を説明するレビュー。
- Objective: 少ない長距離配線で効率と複雑な動態を支える可能性を整理する。
- Methods: graph理論を導入し、macaque・catのtracingと人間のEEG/MEG・fMRI研究へ適用を紹介する。
- Data and results: 高い局所clusterと短い全体経路を持つnetworkの、費用・頑健性・行動への含意を議論する。
- Novelty: 脳networkの情報処理を、配線費用を含む共通のtopologyで比較する。
- Limitations: 編者の注意: small-worldという名称だけでは機構を特定せず、節点の定義・閾値・比較するnull modelに指標が依存する。
- Publication date note: PubMedと出版社を照合したが、出版社のPublished表記もDecember 2006までで日単位は未確認。月初を推測で補わない。出典: https://journals.sagepub.com/doi/10.1177/1073858406293182

### Paper: What Learning Systems do Intelligent Agents Need? Complementary Learning Systems Theory Updated
- Source: PubMed
- Canonical ID: pmid:27315762
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/27315762/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: CLS理論を、replay・一般化・速い皮質学習を含む形へ更新する。
- Objective: 海馬と新皮質の役割分担を最近の証拠とAI設計へつなぐ。
- Methods: replayによる目的依存の経験重み付け、海馬traceの一般化、既知構造と整合する情報の皮質学習を整理する。
- Data and results: 海馬でも一般化、新皮質でも速い学習が可能な条件を論じ、人工agentとの関連を提示する。
- Novelty: 二つの学習系を単純な速い/遅いの固定分類から拡張する。
- Limitations: 理論の更新・統合であり、新しい万能agentの実験ではない。replayの役割は経験統計と目標にも依存する。
- Publication date note: PubMedの巻号情報は2016年7月までで日精度の電子公開日が未記録。出版社版・著者版の追加取得も制限があり、初回公開日の日単位は未確認。索引登録日・会期・月初を代用しない。出典: https://pubmed.ncbi.nlm.nih.gov/27315762/

### Paper: Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory
- Source: PubMed
- Canonical ID: pmid:7624455
- Publication date: 未記載
- URL: https://pubmed.ncbi.nlm.nih.gov/7624455/
- read_level: abstract
- Tags: 基礎文献, 神経科学とAI
- Summary: 速い海馬学習と遅い新皮質学習が記憶を補完するCLS理論。
- Objective: 脳が新しい経験をすばやく記憶できる一方、既存の知識を破壊せず抽象化できる理由を一つの学習器で説明するのは難しい。逐次学習で新しい例が古い例を忘れさせる『干渉』という計算上の問題から、海馬と新皮質の役割分担を説明する。
- Methods: コネクショニストモデルで観測される逐次学習・急速学習・古い知識との干渉を検討し、海馬が特定の経験を速く符号化し、新皮質が繰り返し・交互提示によって共通構造をゆっくり獲得するというComplementary Learning Systems理論を統合した。新しい被験者を無作為に比較した介入実験ではなく、モデルと既存神経生理知見の理論的説明。
- Data and results: 速い学習だけで共通知識へ吸収すると干渉・忘却が起き、経験を海馬へ一時的に蓄え再活性化することで新皮質のゆっくりした統合を支えられる、という計算原理を提示。普遍的な記憶改善率や神経活動の統一スコアを報告した研究ではない。
- Novelty: 海馬と新皮質の違いを単なる解剖学的な区別から、急速な個別記憶と安定した統計的な一般化という相反する最適化要求で説明した。継続学習・経験再生などの機械学習研究にもつながる中心的な理論。
- Limitations: 理論モデルであり、実際の脳が常に完全な二層・二速度で学習することを保証しない。海馬・皮質間の双方向相互作用や追加の学習機構は後続研究を合わせて理解すべき。
- Publication date note: PubMedに日単位の電子公開日・冊子刊行日の記録なし。巻号の刊行年月: 1995 Jul。要約日・索引登録日とは区別。出典: https://pubmed.ncbi.nlm.nih.gov/7624455/

<!-- PAPER_IDS -->
pmid:32880371
pmid:39358518
pmid:23925240
pmid:39358521
pmid:28796202
pmid:33315010
pmid:34696823
pmid:36893230
pmid:34949809
pmid:34032214
pmid:39358527
pmid:39358525
pmid:39261740
pmid:21653723
pmid:12506194
pmid:19188601
pmid:19211893
pmid:26457551
pmid:16201007
pmid:21810475
pmid:22049421
pmid:18403396
pmid:28302591
pmid:21251014
pmid:17079517
pmid:26393868
pmid:29203085
pmid:32989295
pmid:21151783
pmid:27655008
pmid:32139786
pmid:22722855
pmid:31551604
pmid:32640928
pmid:30224673
pmid:25971509
pmid:27067378
pmid:19357332
pmid:30315158
pmid:30877963
pmid:29887338
pmid:34801787
pmid:31320220
pmid:32940606
pmid:30344047
pmid:22096452
pmid:27814352
pmid:24812127
pmid:29681533
pmid:29513219
pmid:30696881
pmid:27039703
pmid:10195184
pmid:7624455
pmid:19528002
pmid:34737231
pmid:27315762
pmid:16001064
pmid:27824044
pmid:27917138
pmid:36864133
pmid:12649484
pmid:16929307
pmid:15996553
pmid:30359611
pmid:10195164
pmid:24462094
pmid:23708143
pmid:10966623
pmid:18275283
pmid:31776490
pmid:11102489
pmid:26941637
pmid:26834568
pmid:17305422
pmid:23668970
pmid:23684880
pmid:24695228
pmid:29116093
pmid:28182017
pmid:23925239
pmid:28292907
pmid:9463459
pmid:26160946
pmid:39358519
pmid:40205214
pmid:38723085
pmid:42691995
pmid:42259917
pmid:40140576
pmid:29743670
pmid:28967910
pmid:33181068
pmid:31942076
pmid:32303713
pmid:32681001
pmid:29205151
pmid:31659335
pmid:32970997
pmid:35173264
pmid:37127759
pmid:37138088
pmid:27791099
pmid:8036517
pmid:9054347
pmid:21502525
<!-- /PAPER_IDS -->
