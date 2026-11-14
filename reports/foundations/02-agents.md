# 基礎文献 — エージェント・検索・記憶・協調

> schema_version: 1
> report_date: 2026-11-14

## ダイジェスト

選定112件中、以下は原著照合・編集確認を終えた112件。選定リストだけの論文を完成済み件数には含めない。原著要旨までの記述と本文確認を区別し、Limitationsの「編者の注意」は著者の自己申告と区別する。

研究の流れと2026年論文との接続は [文献集の案内](README.md) を参照。

## 完全版レポート

### Paper: Memory Networks
- Source: arXiv
- Canonical ID: arxiv:1410.3916
- Publication date: 2014-10-15
- URL: https://arxiv.org/abs/1410.3916
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 記憶ネットワークは、推論と長期記憶を統合した新しい学習モデルである。
- Objective: 質問応答において、長期記憶が動的な知識ベースとして機能することを検証する。
- Methods: 読み書きできる長期記憶と推論componentを共同で学習する。大規模QAと模擬世界から作った小規模で複雑なQAを用い、複数の支持文の連鎖を評価する。
- Data and results: 特に後者のタスクでは、複数の支持文を連鎖させることで推論能力を示すことができた。
- Novelty: 長期記憶を読み書きし、予測に共同で使用する新しい学習モデルクラスを提案した点。
- Limitations: 編者の注意: 複数文推論の例は模擬世界taskにおける検証である。現在の会話agentの無制限の長期記憶や任意の実世界推論を確立したものではない。要旨に誤差分析の数値はない。

### Paper: End-To-End Memory Networks
- Source: arXiv
- Canonical ID: arxiv:1503.08895
- Publication date: 2015-03-31
- URL: https://arxiv.org/abs/1503.08895
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 再帰的アテンションモデルを持つニューラルネットワークを提案する。
- Objective: 外部記憶を複数hopで参照するMemory Networkを、従来より少ない教師信号でend-to-end学習する方法を検討する。
- Methods: 再帰的なアテンションモデルを持ち、複数の計算ステップ（hops）を実行可能とする。
- Data and results: 合成QAでは少ない監督情報でMemory Networksに匹敵し、Penn Treebank・Text8ではRNN/LSTMに相当する成績を報告。両者で複数hopの有効性を示す。
- Novelty: 本手法はEnd-to-Endで学習するため、より少ない教師信号で適用可能である点。
- Limitations: 編者の注意: 少ない教師信号は教師なし学習と同義ではない。合成QAと二つの言語モデルdatasetでの成果であり、実世界の長期対話記憶への転移は要旨では検証されない。

### Paper: Dynamic Memory Networks for Visual and Textual Question Answering
- Source: arXiv
- Canonical ID: arxiv:1603.01417
- Publication date: 2016-03-04
- URL: https://arxiv.org/abs/1603.01417
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: DMNを改良し、画像とテキストの質問応答に適用したモデルを提案する。
- Objective: 回答根拠文のラベルを学習時に与えないQAと、画像を使うQAへDMNを拡張できるかを調べる。
- Methods: DMNのメモリおよび入力モジュールを改善し、画像に対応するための新規入力モジュールを追加してDMN+モデルを構築した。
- Data and results: 提案されたDMN+モデルは、サポートファクトの教師なし設定でVQAとbabi-10kの両データセットで最先端の結果を達成した。
- Novelty: 本研究では、画像のための新しい入力モジュールを導入し、視覚的質問応答への適用可能性を示した点に新規性がある。
- Limitations: 編者の注意: supporting-fact supervisionなしという設定でも、QAの教師信号自体がないわけではない。VQA・bAbI-10kでの当時の改善を、任意の視覚推論能力の確立と混同しない。

### Paper: OpenAI Gym
- Source: arXiv
- Canonical ID: arxiv:1606.01540
- Publication date: 2016-06-05
- URL: https://arxiv.org/abs/1606.01540
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 強化学習研究のためのツールキットであるOpenAI Gymを紹介する。
- Objective: どのような構成要素と設計上の決定がGymに含まれているか？
- Methods: ベンチマーク問題のコレクションと共通インターフェースを提供し、結果共有サイトを設けた。
- Data and results: 共通interfaceを持つRL benchmark群と結果共有の仕組みを提供し、その構成・設計判断をwhitepaperで説明する。要旨に新RL algorithmの性能改善値はない。
- Novelty: 共通インターフェースを持つ多様なベンチマーク問題を統合した点。
- Limitations: 編者の注意: 評価toolkitの原著であり、現行softwareのAPI説明や現在の保守状態を示す資料ではない。共通interfaceだけでseed・予算・評価protocolまで一致するとは限らない。

### Paper: Key-Value Memory Networks for Directly Reading Documents
- Source: arXiv
- Canonical ID: arxiv:1606.03126
- Publication date: 2016-06-09
- URL: https://arxiv.org/abs/1606.03126
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 文書から直接質問応答を行うための新しいキーバリューメモリネットワークを提案した。
- Objective: 知識ベースの制約やスパース性を克服し、文書からの直接的な質問応答を実現すること。
- Methods: WikiMoviesというQAデータセットを構築し、アドレス指定と出力段階で異なるエンコーディングを利用するKey-Value Memory Networksを適用した。
- Data and results: 本手法は既存のWikiQAベンチマークにおいて最先端の結果を達成し、KBや情報抽出とのギャップを縮小させた。
- Novelty: メモリ読み出し操作のアドレス指定と出力段階に異なるエンコーディングを用いる点。
- Limitations: 編者の注意: WikiMoviesは映画分野のraw textと前処理KBを揃えた比較用datasetである。KB、抽出情報、文書間の差の縮小を、任意分野での文書理解の解決と解釈できない。要旨に詳細な数値はない。

### Paper: SCAN: Learning Hierarchical Compositional Visual Concepts
- Source: arXiv
- Canonical ID: arxiv:1707.03389
- Publication date: 2017-07-11
- URL: https://arxiv.org/abs/1707.03389
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: SCANは、視覚ドメインで階層的・構成的な抽象概念を学習する新しいフレームワークである。
- Objective: 自然界の多様な現象が持つ背後にある、発見可能な抽象的概念をどのように学習できるか？
- Methods: SCANは、シンボルと画像を関連付け、教師なしで発見された分離された視覚プリミティブを用いて概念を学習する。
- Data and results: 訓練後、SCANは象徴的記述から画像サンプルを生成し、逆に画像からシンボルの推論も可能である。
- Novelty: 本アプローチは、シンボルと画像のペアリングが非常に少なくても機能し、シンボル表現の形式について仮定を置かない点にある。
- Limitations: 編者の注意: 本稿のSCANはSymbol-Concept Association Networkであり、同名の言語指示合成benchmarkとは別である。少数でもsymbol–画像pairを使い、全工程が無監督という意味ではない。

### Paper: Relational inductive biases, deep learning, and graph networks
- Source: arXiv
- Canonical ID: arxiv:1806.01261
- Publication date: 2018-06-04
- URL: https://arxiv.org/abs/1806.01261
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: entity・関係・合成規則を扱うgraph networkで、関係的帰納biasと組合せ汎化を整理する。
- Objective: 人間的な知能の鍵である組み合わせ的汎化を実現するためのアプローチを探求すること。
- Methods: 本稿では、関係性の帰納的バイアスを活用する方法としてグラフネットワークという新しいビルディングブロックを提案した。
- Data and results: graph上の既存network群を統一・拡張するbuilding blockとlibraryを提示し、関係推論と構成的汎化を支える設計を論じる。位置付け・review・統一が中心で、要旨に一律の性能差はない。
- Novelty: 「手動設計」と「エンドツーエンド学習」の二者択一を否定し、両者の相補性を活かすアプローチを提唱した点。
- Limitations: 編者の注意: 構造化biasの有用性を提唱する論文で、人間並みの汎化を完成した実証ではない。graphの表現選択と適切な関係dataが必要である。

### Paper: TextWorld: A Learning Environment for Text-based Games
- Source: arXiv
- Canonical ID: arxiv:1806.11532
- Publication date: 2018-06-29
- URL: https://arxiv.org/abs/1806.11532
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 難度・言語・観測を制御したtext gameを生成し、RLの汎化を測るTextWorld。
- Objective: 商用text gameの部分観測・疎報酬等を分解し、学習と転移を体系的に調べる。
- Methods: 対話play、状態追跡、報酬付与を備えるPython libraryを作り、既成gameと手作り・自動生成gameでbaseline agentを評価する。
- Data and results: 難度・scope・言語を制御したbenchmarkとagent評価を提供し、似ているが異なるgame集合による汎化研究を可能にする。要旨にscore値はない。
- Novelty: 固定gameの攻略から、生成時に課題要因を制御し比較する実験環境へ移る。
- Limitations: 編者の注意: text gameの形式的状態と生成規則に依存し、自由な実世界言語理解を全面評価するものではない。観測・報酬を緩めた設定と商用gameの難度も区別する。

### Paper: BabyAI: A Platform to Study the Sample Efficiency of Grounded Language Learning
- Source: arXiv
- Canonical ID: arxiv:1810.08272
- Publication date: 2018-10-18
- URL: https://arxiv.org/abs/1810.08272
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 合成言語の接地指示を学ぶsample効率を、19段階のBabyAIで測る。
- Objective: 人間が対話的に教えるために必要なdata量を評価し、構成的な言語学習の難しさを調べる。
- Methods: 難度が増す19levelと英語の部分集合である合成言語、教師を模擬するheuristic expertを実装。神経agentのbaselineと必要教示量を見積もる。
- Data and results: 一部levelの学習に必要な人手量を推定し、当時の深層法は構成的言語の学習に十分sample効率が高くないという証拠を報告。要旨に必要例数はない。
- Novelty: 最終成功率だけでなく、人間から実際に教えられる量かというsample効率を研究対象にする。
- Limitations: 編者の注意: heuristic教師と合成言語での推定で、現実の人間による教示・自由言語の全費用を測ったものではない。BabyAI 1.1の改良と原版を区別する。

### Paper: Generalization through Memorization: Nearest Neighbor Language Models
- Source: arXiv
- Canonical ID: arxiv:1911.00172
- Publication date: 2019-11-01
- URL: https://arxiv.org/abs/1911.00172
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 事前学習済みLMをkNNモデルで補強する手法を提案し、高い性能を示した。
- Objective: 言語モデリングにおいて、単語予測よりもテキスト系列間の類似度学習が容易であるか検証すること。
- Methods: 事前学習LMの次単語分布と、LM埋め込み空間の近傍検索から得たkNN分布を線形補間する。datastoreの差替えによるdomain適応も評価する。
- Data and results: WikiText-103で元の学習集合を近傍DBに使い、追加学習なしでperplexity 15.79、baseline比2.9 point改善を報告。希少な事実知識の予測への利点を定性的に示す。
- Novelty: 事前学習済みLMとkNNモデルの線形補間により、追加学習なしで性能向上を実現する点。
- Limitations: 編者の注意: 追加学習なしでもdatastore構築・検索の資源は必要である。perplexity改善は正答率の2.9%改善ではない。外部DBが持つ情報や類似度への依存を伴う。

### Paper: REALM: Retrieval-Augmented Language Model Pre-Training
- Source: arXiv
- Canonical ID: arxiv:2002.08909
- Publication date: 2020-02-10
- URL: https://arxiv.org/abs/2002.08909
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: REALMは、知識を明示的かつ解釈可能な形で捉えるため、言語モデルに検索機構を追加した。
- Objective: 言語モデルのパラメータ内に暗黙的に格納される世界知識を、よりモジュール的で解釈可能な方法で捉えたい。
- Methods: Wikipedia等から文書を取得する潜在retrieverを、masked language modelingの信号で教師なし事前学習する。数百万文書を考慮する検索を経て学習し、微調整・推論にも検索を使う。
- Data and results: 三つのOpen-QA benchmarkで比較した既存手法より絶対accuracyが4〜16 percentage points高いと報告。検索による解釈可能性・モジュール性の定性的利点も述べる。
- Novelty: 知識リトリーバーを教師なしで事前学習し、言語モデルのパラメータ外に知識をモジュール化して組み込んだ点。
- Limitations: 編者の注意: 4〜16は原著で比較した当時の手法との差である。文書の取得が説明の忠実性や回答の正しさを保証するわけではなく、要旨には誤検索時の挙動の数値はない。

### Paper: Dense Passage Retrieval for Open-Domain Question Answering
- Source: arXiv
- Canonical ID: arxiv:2004.04906
- Publication date: 2020-04-10
- URL: https://arxiv.org/abs/2004.04906
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 密な表現のみで文書検索が可能であることを示す。
- Objective: オープンドメインQAにおける効率的なパッセージ検索の実現方法を問う。
- Methods: シンプルなデュアルエンコーダフレームワークを用い、少数の質問とパッセージから埋め込みを学習させた。
- Data and results: 複数のopen-domain QA datasetでLucene-BM25よりtop-20検索精度が絶対値で9〜19 percentage points高いと報告。end-to-end QAでも複数benchmarkの当時最高成績を更新した。
- Novelty: 従来のスパースモデルに頼らず、密な表現のみで実用的な文書検索を実現した点。
- Limitations: 編者の注意: 9〜19は相対改善率ではなく絶対精度差。検索精度と最終回答精度を混同しない。少量でも質問・passageの教師データを使い、未知分野への性能は要旨だけでは判断できない。

### Paper: ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT
- Source: arXiv
- Canonical ID: arxiv:2004.12832
- Publication date: 2020-04-27
- URL: https://arxiv.org/abs/2004.12832
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ColBERTは、深層言語モデルの表現力を保ちつつ効率的な文書検索を実現する新しいランキングモデルである。
- Objective: 大規模なニューラルネットワークによる計算コスト増大という課題をどう解決するか？
- Methods: クエリと文書を独立にエンコードした後、安価で強力な相互作用ステップを用いて微細な類似度をモデル化する。
- Data and results: 二つのpassage検索datasetでBERT系rankingに匹敵する有効性を保ち、比較条件下で実行速度約100倍、query当たりFLOPs約1万分の1と報告する。
- Novelty: 遅延させることで文書表現をオフラインで事前計算可能にし、クエリ処理を大幅に高速化する点。
- Limitations: 編者の注意: 文書表現の事前計算を可能にする構造であり、offline計算とindex格納の費用はquery当たりFLOPsとは別である。速度倍率は原著の比較モデル・評価条件に依存する。

### Paper: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- Source: arXiv
- Canonical ID: arxiv:2005.11401
- Publication date: 2020-05-22
- URL: https://arxiv.org/abs/2005.11401
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: RAGモデルは、事前学習済みパラメータと外部知識を統合し、高度なNLPタスクで性能向上を実現する。
- Objective: 大規模言語モデルの知識アクセス能力の限界を克服する方法を探求すること。
- Methods: 事前学習済みseq2seqモデルと、Wikipediaのdense indexを検索するretrieverを結合する。出力系列全体で同じ文書群を使う方式と、tokenごとに文書を変えられる方式を比較した。
- Data and results: 本手法は3つのオープンドメインQAタスクでSOTAを達成し、生成言語もより具体的で多様かつ事実に即していることが示された。
- Novelty: パラメータと非パラメトリックメモリを組み合わせた汎用的なファインチューニングレシピを提案した点。
- Limitations: 編者の注意: Wikipediaと原著のQA・生成taskでの評価であり、検索文書が正しいことや幻覚の解消を保証しない。取得文書と回答の事実的一致を実運用で別途評価する必要がある。

### Paper: DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning
- Source: arXiv
- Canonical ID: arxiv:2006.08381
- Publication date: 2020-06-15
- URL: https://arxiv.org/abs/2006.08381
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: DreamCoderは、プログラム記述を通じて専門知識を習得するシステムである。
- Objective: 問題と解について考えるための言語を学習することが目的である。
- Methods: program探索を導く神経networkとdomain言語を共同に学ぶ。wake-sleepで記号的な新抽象を言語へ追加し、想像・再生した問題でnetworkを訓練する。
- Data and results: 帰納programming、描画、scene構築等を解き、関数型programming・vector代数・古典物理の基本概念を再発見すると報告する。要旨にtask別scoreはない。
- Novelty: 概念が以前学習したものから構成的に構築され、解釈可能で転移可能な表現を得る点。
- Limitations: 編者の注意: 用意したdomain・primitive・taskに基づくprogram学習であり、rawな実世界観測から物理法則全般を自律発見した意味ではない。探索言語とdataへの依存がある。

### Paper: BabyAI 1.1
- Source: arXiv
- Canonical ID: arxiv:2007.12770
- Publication date: 2020-07-24
- URL: https://arxiv.org/abs/2007.12770
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: BabyAI 1.1は、接地された言語指示に従うエージェントのサンプル効率を測定するプラットフォームである。
- Objective: BabyAIのagent構造を小さく改め、接地言語指示の学習sample効率と難しいlevelの性能を改善する。
- Methods: BabyAI 1.0の結果をベースに、エージェントのアーキテクチャを3点修正し、性能向上を図った。
- Data and results: この改善により、強化学習のサンプル効率が最大3倍になり、最も難しいレベルでの模倣学習性能は77%から90.4%に向上した。
- Novelty: 本プラットフォームは、エージェントのアーキテクチャを改良することで計算効率と性能向上を目指している。
- Limitations: 編者の注意: 三つの構造修正によるBabyAI内の改善で、どの改良がどれだけ寄与するかは要旨では分からない。最大3倍はRL sample効率で、あらゆる実時間計算が3倍速い意味ではない。

### Paper: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning
- Source: arXiv
- Canonical ID: arxiv:2010.03768
- Publication date: 2020-10-08
- URL: https://arxiv.org/abs/2010.03768
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ALFWorldは、テキストによる抽象的推論と視覚環境での具現化を統合するシミュレータである。
- Objective: エージェントが抽象的な推論能力と具体的な実行能力の両方を習得するためのインフラストラクチャを提供すること。
- Methods: TextWorldで学習した抽象知識を、ALFREDベンチマークの目標に基づき視覚環境で実行可能にするパイプラインを構築した。
- Data and results: BUTLERエージェントは、TextWorldで学んだ抽象知識が具現化された行動に対応し、視覚環境のみでの訓練より優れた汎化能力を示すことが実証された。
- Novelty: 本シミュレータは、テキストベースのポリシー学習とリッチなビジュアル環境での目標実行を可能にし、両者の連携を実現した点にある。
- Limitations: 編者の注意: textと視覚の対応を揃えたsimulation基盤であり、任意の自然言語世界modelから実robotへ自動転移する保証ではない。BUTLERの各moduleや観測誤差も結果へ影響する。

### Paper: Retrieval Augmentation Reduces Hallucination in Conversation
- Source: arXiv
- Canonical ID: arxiv:2104.07567
- Publication date: 2021-04-15
- URL: https://arxiv.org/abs/2104.07567
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 検索拡張による知識接地型対話が、ハルシネーションを大幅に低減する。
- Objective: 検索を組み込んだ対話モデルで、多turnの文脈を扱いながら会話能力と知識に基づく正確さを両立できるかを調べる。
- Methods: リトリーバー、ランカー、エンコーダ・デコーダを含む複数のコンポーネントを持つアーキテクチャを研究した。
- Data and results: 二つの知識接地型対話taskで当時の最高成績を報告。学習外の場面への汎化と、人手評価による知識幻覚の低減を示すが、要旨に低減率の数値はない。
- Novelty: 検索拡張ループ構造を知識接地型対話に応用し、会話能力と知識性を両立させた点。
- Limitations: 編者の注意: 幻覚の低減は解消を意味しない。検索sourceの質やmulti-turn queryの失敗を含む現在の実用場面で同じ効果が出るかは、要旨のみでは確かめられない。

### Paper: AndroidEnv: A Reinforcement Learning Platform for Android
- Source: arXiv
- Canonical ID: arxiv:2105.13231
- Publication date: 2021-05-27
- URL: https://arxiv.org/abs/2105.13231
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: touchscreenを共通interfaceとし、多様なAndroid appでRLを研究するAndroidEnv。
- Objective: 人が使うapp・serviceを、agentの学習と評価に利用できる環境を作る。
- Methods: Android deviceの現実的simulation上で共通touch入力を提供し、複数taskで既存の代表的RL agentを実験する。
- Data and results: 環境の機能と設計を概説し、用意したtaskでのRL評価を報告。要旨にはtask数・成功率・実device転移の定量結果はない。
- Novelty: 個別gameの専用actionから、Android ecosystemの共通touch interfaceへRL環境を広げる。
- Limitations: 著者は実deviceへの展開を可能性として述べる。編者の注意: simulationで学習できることは、実deviceの全appに安全・正確に転移できた証明ではない。

### Paper: Decision Transformer: Reinforcement Learning via Sequence Modeling
- Source: arXiv
- Canonical ID: arxiv:2106.01345
- Publication date: 2021-06-02
- URL: https://arxiv.org/abs/2106.01345
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 強化学習をシーケンスモデリング問題として捉え、Transformerで解く手法を提案した。
- Objective: 強化学習の問題をどのようにシーケンスモデリングとして定式化できるか？
- Methods: 希望するreturn、過去の状態・行動を条件に、causal mask付き自己回帰Transformerで次の行動を予測する。value関数fitやpolicy gradientを使う従来法と比較する。
- Data and results: 本モデルは、Atari、OpenAI Gym、Key-to-Doorタスクで最先端のオフラインRLベースラインと同等以上の性能を示した。
- Novelty: 価値関数をフィッティングしたりポリシー勾配を計算したりせず、望ましいリターンに条件付けして行動を出力する点が新しい。
- Limitations: 編者の注意: offline dataに基づく条件付き予測であり、希望returnを指定すれば必ず達成・最適化できる保証ではない。dataの質・coverageや状態表現の条件を伴う。

### Paper: Improving language models by retrieving from trillions of tokens
- Source: arXiv
- Canonical ID: arxiv:2112.04426
- Publication date: 2021-12-08
- URL: https://arxiv.org/abs/2112.04426
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 大規模コーパスからの検索情報を利用し、言語モデルの性能を向上させる手法を提案した。
- Objective: 先行トークンとの局所的類似性に基づき、大規模な文書チャンクから取得した情報で自己回帰型言語モデルを強化する方法は何か。
- Methods: 凍結されたBertリトリーバーと微分可能なエンコーダを用い、チャンク化されたクロスアテンション機構を組み込んだRETROを構築し、学習させた。
- Data and results: 2兆tokenの検索DBを用い、The Pileでは25分の1のparameter数でGPT-3、Jurassic-1に相当する性能を報告。微調整後にQAへ転移し、既存Transformerへ検索を追加するRETROfitも示す。
- Novelty: 検索情報を明示的なメモリとして利用することで、これまでにない大規模なデータを用いて言語モデルを改善できる道を開いた点。
- Limitations: 編者の注意: 25分の1はモデルparameter数であり、検索DBとindexの格納量や検索計算を含む総資源ではない。The Pileの比較を全downstream taskに一般化できない。

### Paper: WebGPT: Browser-assisted question-answering with human feedback
- Source: arXiv
- Canonical ID: arxiv:2112.09332
- Publication date: 2021-12-17
- URL: https://arxiv.org/abs/2112.09332
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: WebGPTは、ウェブブラウジング環境でGPT-3をファインチューニングし、質問応答能力を向上させたモデルである。
- Objective: 人間が実行可能なタスクとして設定することで、模倣学習と人間のフィードバックを用いてモデルの回答品質を最適化することを目指した。
- Methods: ELi5データセットを用い、行動クローニングでGPT-3をファインチューニングした後、人間の選好を予測する報酬モデルを用いた拒否サンプリングを実施した。
- Data and results: ELI5でbest modelの回答は、人間実演者の回答との比較で56%の確率、Reddit最高投票回答との比較で69%の確率で好まれた。相対的な品質向上率ではない。
- Novelty: ウェブブラウジング環境でのファインチューニングと、報酬モデルを用いた拒否サンプリングを組み合わせることで性能を向上させた点である。
- Limitations: 編者の注意: 人間選好率は事実正確性の保証ではない。参照を集める手順でも各引用が十分に回答を支持するかは別に検証が必要で、text browsing環境の条件にも依存する。

### Paper: Competition-Level Code Generation with AlphaCode
- Source: arXiv
- Canonical ID: arxiv:2203.07814
- Publication date: 2022-02-08
- URL: https://arxiv.org/abs/2203.07814
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 競技programming用dataと大量sampling・挙動filterで複雑問題を解くAlphaCode。
- Objective: 単純な指示のcode化を超え、algorithm理解が必要な未見問題の解を生成する。
- Methods: 整理した競技data、大規模で効率的なTransformer、大量の候補生成を組み合わせ、program挙動で絞った少数候補を提出する。Codeforces大会を模擬評価する。
- Data and results: 5,000超参加者の大会群で、平均上位54.3%の順位を報告。訓練data・architecture・大量samplingとfilterの三要因が重要とする。
- Novelty: 生成modelの一回の出力より、問題解決の探索空間を多数候補で広げ、挙動で選別するsystemを構成する。
- Limitations: 編者の注意: 模擬競技の順位で、全開発工程や実際の大会参加の成績ではない。多数候補・filter・少数提出を含むため単発pass@1や同計算量のLM比較とは区別する。

### Paper: ScienceWorld: Is your Agent Smarter than a 5th Grader?
- Source: arXiv
- Canonical ID: arxiv:2203.07540
- Publication date: 2022-03-14
- URL: https://arxiv.org/abs/2203.07540
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 知識を答えるだけでなく、模擬世界で実験して使う科学推論を測るScienceWorld。
- Objective: 既知概念を新しい文脈で使う能力と、過去の類似回答の検索に依存する能力を区別する。
- Methods: 小学校科学相当のinteractive text環境を作り、未知物質の導電性実験等を評価する。interactive学習と静的QA・実演学習を比較する。
- Data and results: 100,000stepの対話学習をした150万parameter agentが、静的に学習した110億parameter modelを上回る例を報告し、環境への接地の仮説を支持する。
- Novelty: 科学知識の正答から、実験を計画・実行して概念を再利用する能力へ評価を進める。
- Limitations: 編者の注意: parameter数以外に学習方法・環境経験が違う比較である。小modelが全taskで大型LMより優れる証明や、実験室での科学発見能力の評価ではない。

### Paper: Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
- Source: arXiv
- Canonical ID: arxiv:2204.01691
- Publication date: 2022-04-04
- URL: https://arxiv.org/abs/2204.01691
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMの知識をロボット行動に結びつけるため、事前学習されたスキルで制約する手法を提案した。
- Objective: 自然言語指示に基づき、具体的な環境で実行可能な行動計画を生成する方法を探る。
- Methods: LLMの高水準の手順知識を、事前学習skillと各skillのvalue functionで実行可能性に接地し、環境に適したactionを選択する。
- Data and results: 実環境のmobile manipulatorの複数taskで、複数stepに及ぶ抽象的な自然言語指示の達成を報告。要旨には成功率の値はなく、long-horizonは長期間の自律稼働を意味しない。
- Novelty: 低レベルスキルと大規模言語モデルを組み合わせ、価値関数による物理環境への接地を行う点が新規である。
- Limitations: 編者の注意: 用意・学習したskillとそのvalue推定の範囲に依存する。適切な高水準計画と、低水準動作の安全な実行・未知環境への転移は別に検証する必要がある。

### Paper: WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents
- Source: arXiv
- Canonical ID: arxiv:2207.01206
- Publication date: 2022-07-04
- URL: https://arxiv.org/abs/2207.01206
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 実商品情報を使う模擬commerce環境WebShopで、指示に沿う探索・購入行動を研究する。
- Objective: 現実的言語と大規模化を両立したinteractive benchmarkを作る。
- Methods: 118万商品・12,087指示・1,600超人手実演を用意し、RL・模倣・事前学習modelを比較。軌跡・ablationと実siteへの転移も調べる。
- Data and results: best model成功率29%、rule-based 9.6%、人間expert59%。Amazon/eBayでも非自明なsim-to-real転移を報告するが、その成功率は要旨にない。
- Novelty: 商品要件の解釈、query再構成、noisy page処理、探索を一つの実行taskとして評価する。
- Limitations: 編者の注意: 学習・主評価はsimulationであり、実際の購入取引を全面自律化した実証ではない。成功率29%と後続研究の平均報酬scoreを直接比較しない。

### Paper: Inner Monologue: Embodied Reasoning through Planning with Language Models
- Source: arXiv
- Canonical ID: arxiv:2207.05608
- Publication date: 2022-07-12
- URL: https://arxiv.org/abs/2207.05608
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 成功判定・scene説明・人間の応答を言語feedbackとして取り込み、robotの計画を閉loop化する。
- Objective: skillの選択だけでなく、状況変化に合わせた実行時点・計画変更を追加訓練なしで行えるかを調べる。
- Methods: LLMへ環境から自然言語feedbackを返し、inner monologueとして計画へ反映する。模擬・実卓上操作と実kitchenのmobile manipulationを評価する。
- Data and results: 三domainで閉loopの言語feedbackが高水準指示の完了を大きく改善と報告。要旨に成功率や費用の数値はない。
- Novelty: 事前に固定した言語planから、実行結果を受けて言語的に更新する計画へ進める。
- Limitations: 編者の注意: feedbackを作る成功検出・scene理解・人間入力に依存する。LLMの追加訓練なしでも、用意したskillや知覚moduleが不要という意味ではない。

### Paper: Code as Policies: Language Model Programs for Embodied Control
- Source: arXiv
- Canonical ID: arxiv:2209.07753
- Publication date: 2022-09-16
- URL: https://arxiv.org/abs/2209.07753
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMをロボット制御ポリシー生成に転用し、自然言語からコードを記述する手法を提案した。
- Objective: 自然言語の指示に基づき、ロボットの動作を記述するポリシーコードをLLMで自動生成できるか検証すること。
- Methods: 自然言語commandと対応codeのfew-shot例を与え、知覚出力を処理する関数・feedback loopと制御APIのpolicy codeを生成する。未定義関数を再帰的に生成する階層code生成も使う。
- Data and results: 複数の実robotで反応的制御やwaypoint制御を実演。階層code生成でHumanEvalの39.8%を解けたと報告するが、この値はrobot成功率ではない。
- Novelty: ロボット中心の定式化として「コードをポリシー」とし、反応的・ウェイポイントベースの制御ポリシー表現を可能にした点。
- Limitations: 編者の注意: 利用可能な知覚・制御primitiveとAPIに依存する。HumanEvalのcode正解率と、実robotでの安全性・成功率・未知環境への転移は別の評価である。

### Paper: ProgPrompt: Generating Situated Robot Task Plans using Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2209.11302
- Publication date: 2022-09-22
- URL: https://arxiv.org/abs/2209.11302
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 本研究は、LLMを用いたロボットの状況に応じたタスク計画生成手法を提案する。
- Objective: 現在の環境にある物体とrobotが実行できる動作をpromptに与え、実行可能なtask planを生成する。
- Methods: 利用可能なアクションとオブジェクトのプログラム的仕様および実行例をプロンプトとしてLLMに入力し、計画を生成させる。
- Data and results: VirtualHomeでのタスクにおいて最先端の成功率を示し、物理ロボットアームでもテーブルトップタスクに適用可能であることを実証した。
- Novelty: 利用可能なアクションとオブジェクトのプログラム的仕様をプロンプトに組み込むことで、状況依存的な計画生成を実現する点。
- Limitations: 編者の注意: 自然言語指示だけではなく、action・objectの仕様と例programを与える方法である。VirtualHomeと卓上robotでの検証から、未知の動作を一から獲得する能力は主張できない。

### Paper: ReAct: Synergizing Reasoning and Acting in Language Models
- Source: arXiv
- Canonical ID: arxiv:2210.03629
- Publication date: 2022-10-06
- URL: https://arxiv.org/abs/2210.03629
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ReActは、推論と行動を交互に組み合わせることでLLMの能力を高める手法である。
- Objective: LLMにおける推論と行動の統合的な利用可能性を探求すること。
- Methods: ReActでは、思考過程（reasoning traces）とタスク固有のアクションをインターリーブさせ、外部情報源との連携を行う。
- Data and results: Wikipedia APIを使うHotpotQA・FEVERで幻覚や誤り伝播を減らしたと報告。ALFWorldとWebShopでは1〜2例の提示で、比較した模倣・RL手法より成功率が34%・10%絶対改善。
- Novelty: 推論トレースが行動計画の追跡と例外処理を助け、外部アクションが情報収集を可能にする点。
- Limitations: 編者の注意: 取得する外部情報と実行環境に依存する。選定課題での幻覚低減は、全出力の事実性や悪意あるツール入力への安全性を保証しない。

### Paper: RT-1: Robotics Transformer for Real-World Control at Scale
- Source: arXiv
- Canonical ID: arxiv:2212.06817
- Publication date: 2022-12-13
- URL: https://arxiv.org/abs/2212.06817
- read_level: full_text
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 画像履歴と指示からtoken化actionを予測し、大規模実robot dataの効果を調べるRT-1。
- Objective: data量・多様性を吸収し、新task・物体・環境へ汎化するrobot modelを学習する。
- Methods: 指示で条件付けたEfficientNetの視覚tokenをTokenLearnerで縮約し、decoder-only Transformerへ入力してactionを出す模倣学習を行う。
- Data and results: 13robot・17か月で130,000超episodeを収集し、700超の指示で97%成功と報告。data多様性を削ると汎化が大きく落ちるablationも示す。
- Novelty: 言語・画像・actionの簡潔なtoken化と実時間制御を、多様な実robot実演のscale研究に結ぶ。
- Limitations: 著者は実演者の能力を超えにくい模倣学習、既知概念の組合せに限られる新指示、未見の全く新しい運動への非汎化、器用な操作の不足を挙げる。

本文の照合箇所: [5.1、6.5/Table 7、7 Limitations](https://arxiv.org/html/2212.06817v1)。

### Paper: Toolformer: Language Models Can Teach Themselves to Use Tools
- Source: arXiv
- Canonical ID: arxiv:2302.04761
- Publication date: 2023-02-09
- URL: https://arxiv.org/abs/2302.04761
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: Toolformerは、外部APIの使用を自己教師あり学習で可能にしたモデルである。
- Objective: 大規模言語モデルが基本的な機能や外部ツール利用に苦戦する問題を解決すること。
- Methods: APIごとの少数の実演を起点に自己教師あり学習し、API選択、呼出時点、引数、結果のtoken予測への統合を学ぶ。計算機、QA、検索、翻訳、calendarを使う。
- Data and results: Toolformerは様々な下流タスクで大幅に性能向上し、より大きなモデルと競合する結果を得た。
- Novelty: 外部ツール利用の判断・実行プロセスを自己教師あり学習で追加した点。
- Limitations: 編者の注意: APIごとに少数の実演を必要とする。自己教師ありという表現を完全な無監督の未知API獲得とは解釈できない。要旨の改善は選定したdownstream taskでのものである。

### Paper: PaLM-E: An Embodied Multimodal Language Model
- Source: arXiv
- Canonical ID: arxiv:2303.03378
- Publication date: 2023-03-06
- URL: https://arxiv.org/abs/2303.03378
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 視覚・連続状態・textをLLMへ入力し、複数のrobot・視覚言語taskを共同学習するPaLM-Eを提案する。
- Objective: ロボット工学などの実世界タスクにおける一般推論の課題、すなわちグラウンディングの問題を解決すること。
- Methods: 視覚、連続状態推定、テキスト入力を織り交ぜたマルチモーダル文を入力とし、複数の具現化されたタスクでエンドツーエンド学習させた。
- Data and results: 複数embodiment・観測modalityでの推論とjoint trainingの正の転移を報告。最大562BのPaLM-EはOK-VQAで当時最高成績を示し、規模増加とともに一般言語能力を保つとする。
- Novelty: インターネット規模の言語、視覚、および視覚言語ドメインでの共同訓練により、ポジティブトランスファーを示す点。
- Limitations: 編者の注意: groundingの構成とtaskでの成果であり、任意の物理環境での一般推論や安全動作の保証ではない。562Bは最大構成で、全実験が同じ規模とは限らない。

### Paper: Diffusion Policy: Visuomotor Policy Learning via Action Diffusion
- Source: arXiv
- Canonical ID: arxiv:2303.04137
- Publication date: 2023-03-07
- URL: https://arxiv.org/abs/2303.04137
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 視覚条件付きのdenoising diffusionとして、多峰性のrobot action分布を学ぶDiffusion Policy。
- Objective: 高次元で複数の妥当行動があるvisuomotor制御を、安定に模倣学習する。
- Methods: action分布のscoreを学び、推論時に確率的Langevin stepで反復生成する。receding horizon制御、視覚条件付け、時系列diffusion Transformerを導入する。
- Data and results: 4操作benchmarkの12taskで当時の先端法を一貫して上回り、平均46.9%改善と要旨は報告。絶対point差という記述ではない。
- Novelty: 生成画像ではなくaction列をdiffusionで表し、多峰性・高次元性を持つ実制御へ適用する。
- Limitations: 編者の注意: 反復denoisingは制御時の推論費用を伴う。12taskでの模倣policyの改善を、未知の全行動や安全な長期計画の保証とみなさない。

### Paper: Reflexion: Language Agents with Verbal Reinforcement Learning
- Source: arXiv
- Canonical ID: arxiv:2303.11366
- Publication date: 2023-03-20
- URL: https://arxiv.org/abs/2303.11366
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: Reflexionは、言語エージェントを重み更新なしに言語的フィードバックで強化するフレームワークである。
- Objective: 従来の強化学習の課題を克服し、効率的に試行錯誤から学習する方法を探る。
- Methods: エージェントがタスクのフィードバック信号について口頭で反省し、これをエピソード記憶バッファに保持して次の試行に利用する。
- Data and results: HumanEvalコーディングベンチマークで91%のpass@1精度を達成し、GPT-4（80%）を上回った。
- Novelty: 重み更新ではなく、言語的なフィードバックを通じてエージェントを強化するというアプローチを採用した点。
- Limitations: 編者の注意: 反省を次の試行へ渡す構成であるため、モデルだけでなく試行回数、利用できる評価器、記憶の有無を揃えて比較する必要がある。誤った反省の蓄積も別の課題となる。

### Paper: HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face
- Source: arXiv
- Canonical ID: arxiv:2303.17580
- Publication date: 2023-03-30
- URL: https://arxiv.org/abs/2303.17580
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: HuggingGPTは、LLMを制御器として利用し、多様なAIモデルを連携させることで複雑なタスクを解決する。
- Objective: 様々なドメインやモダリティの複雑なAIタスクを自律的に解決する方法を探る。
- Methods: ChatGPTが要求を計画に分け、Hugging Faceの機能説明からmodelを選び、各subtaskを実行し、結果をまとめる。言語を異種model間の共通interfaceとする。
- Data and results: 言語・画像・音声等をまたぐtaskの実行例を報告。要旨に統一benchmarkでの数値はなく、AGIへの接続は著者の展望である。
- Novelty: LLMを制御器として利用し、既存のAIモデル群を接続・協調させるフレームワークを提案した点。
- Limitations: 編者の注意: 実行例の提示と汎用的な自律解決の保証は区別する。controllerの計画、選択model、外部serviceの可用性に依存し、要旨に失敗率・総費用の数値はない。

### Paper: CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society
- Source: arXiv
- Canonical ID: arxiv:2303.17760
- Publication date: 2023-03-31
- URL: https://arxiv.org/abs/2303.17760
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 役割とinception promptでagent同士の自律協力と会話data生成を調べるCAMEL。
- Objective: 人の継続的な会話誘導への依存を減らし、agentの協調を拡張可能に研究する。
- Methods: role-playingの枠組みでchat agentをtaskへ導き、instruction-following協力のdataと振舞いを分析する公開libraryを提供する。
- Data and results: 複数agentの協力研究と会話data生成の枠組みを示す。要旨に他方式に対する統一成功率や費用差の数値はない。
- Novelty: 単一assistantとの対話から、役割を設定したagent間会話を研究・data生成の単位にする。
- Limitations: 編者の注意: 認知・社会という表現はagent挙動の研究上の類比で、人間の認知過程を直接実証するものではない。役割の指定だけでuser意図の保持を保証しない。

### Paper: REFINER: Reasoning Feedback on Intermediate Representations
- Source: arXiv
- Canonical ID: arxiv:2304.01904
- Publication date: 2023-04-04
- URL: https://arxiv.org/abs/2304.01904
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: REFINERは、推論過程に自動フィードバックを与えるフレームワークである。
- Objective: 中間的な推論ステップの誤りを検出し、改善する手法を提案すること。
- Methods: reasoning LMとcriticモデルを用い、構造化されたフィードバックで反復的に推論を改善させる。
- Data and results: 三つの推論taskで同規模baselineより改善を報告。学習したcriticをGPT-3.5/ChatGPTへ使う場合はreasonerを微調整せず改善できるとする。要旨にscore値はない。
- Novelty: 批判的モデルが自動フィードバックを提供し、推論過程の質を高める点が新しい。
- Limitations: 編者の注意: criticの構造化feedbackを使う反復であり、追加計算とcritic誤りの影響を伴う。人手loop dataなしのcritic訓練は、評価や全taskの教師情報が不要という意味ではない。

### Paper: Generative Agents: Interactive Simulacra of Human Behavior
- Source: arXiv
- Canonical ID: arxiv:2304.03442
- Publication date: 2023-04-07
- URL: https://arxiv.org/abs/2304.03442
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 生成エージェントは、LLMを拡張し記憶と計画を行うことで人間らしい振る舞いをシミュレートする。
- Objective: いかにして大規模言語モデルを用いて、人間らしく振る舞う計算ソフトウェアエージェントを構築できるか？
- Methods: LLMに自然言語で経験の記録を保存させ、それを高次の内省として統合し動的に計画に利用するアーキテクチャを設計した。
- Data and results: 25 agentの町で、単一のparty開催意図から二日間に招待・交流・参加調整が生じた例を報告。観察・計画・内省の各componentが行動のもっともらしさに寄与するablationを示す。
- Novelty: LLMと計算エージェントを融合させ、観察、計画、内省というパターンで人間らしいシミュレーションを実現した点。
- Limitations: 編者の注意: 評価対象は行動のbelievabilityであり、現実の人間集団の予測精度や心理モデルとしての妥当性ではない。社会的振舞いの例を独立した意識・意図の証拠とは解釈しない。

### Paper: Teaching Large Language Models to Self-Debug
- Source: arXiv
- Canonical ID: arxiv:2304.05128
- Publication date: 2023-04-11
- URL: https://arxiv.org/abs/2304.05128
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMに自己デバッグ能力を教えるSelf-Debugging手法を提案し、コード生成性能を向上させた。
- Objective: 複雑なプログラミングタスクにおいて、単発で正しい解を生成する課題を解決すること。
- Methods: Few-shot demonstrationを用いてLLMに自己デバッグを学習させ、実行結果や自然言語での説明を通じて誤りを特定させる。
- Data and results: Spiderベンチマークではコード説明によりベースラインより2-3%向上し、TransCoderやMBPPでは最大12%の精度向上を示した。
- Novelty: 人間からのフィードバックなしに、実行結果と自然言語の説明から自己デバッグを行う能力をLLMに付与した点。
- Limitations: 編者の注意: unit testのないSpiderとtestのあるTransCoder/MBPPでは得られるfeedbackが異なる。人手の正誤feedbackなしでも実行結果を利用し、外部情報を一切使わない内省とは異なる。

### Paper: ChemCrow: Augmenting large-language models with chemistry tools
- Source: arXiv
- Canonical ID: arxiv:2304.05376
- Publication date: 2023-04-11
- URL: https://arxiv.org/abs/2304.05376
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ChemCrowは、化学ツールを統合しLLMの能力を拡張するエージェントである。
- Objective: LLMが抱える化学問題への対応や外部知識アクセス性の課題を解決すること。
- Methods: 18の専門設計されたツールを統合し、有機合成、創薬、材料設計タスクに適用した。
- Data and results: 18 toolを統合し、忌避剤と3種の有機触媒の合成を計画・実行し、新規発色団の探索を支援したと報告。LLMと専門家による評価も実施した。
- Novelty: LLMと外部化学ツール群を統合するエージェントフレームワークを提供し、科学的応用を可能にした点。
- Limitations: 著者はGPT-4評価器が明らかに誤ったGPT-4回答とChemCrowの結果を区別できなかったと報告する。編者の注意: LLM judgeだけで化学taskの正しさを判定する限界を示す。

### Paper: API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs
- Source: arXiv
- Canonical ID: arxiv:2304.08244
- Publication date: 2023-04-14
- URL: https://arxiv.org/abs/2304.08244
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: API-Bankは、ツール利用LLMのための包括的なベンチマークを提供し、性能評価と学習に役立つ。
- Objective: 現在のLLMsのツール利用能力や、その限界を明らかにするための質問に取り組むこと。
- Methods: 評価用に73 API・314対話・753呼出を構築。別に2,138 API/1,000domain由来1,888訓練対話を作り、AlpacaからLynxを学習する。計画・検索・呼出を評価する。
- Data and results: GPT-3.5はGPT-3より改善を示し、GPT-4が計画に優れる一方、提案モデルLynxはAlpacaより26点以上向上した。
- Novelty: 本研究では、ツール利用の評価と学習のための包括的なベンチマークAPI-Bankを初めて導入した点。
- Limitations: 編者の注意: 評価tool数と訓練API数は別である。Lynxの26超はpoint差で相対26%ではない。原著の基盤model・構成に基づく比較で現行tool利用全体を代表しない。

### Paper: WizardLM: Empowering large pre-trained language models to follow complex instructions
- Source: arXiv
- Canonical ID: arxiv:2304.12244
- Publication date: 2023-04-24
- URL: https://arxiv.org/abs/2304.12244
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMを用いて複雑な指示データ生成の課題を解決し、WizardLMを開発した。
- Objective: 人間による高難度な指示データ作成の労力と限界を克服する方法を探る。
- Methods: 初期指示からEvol-Instructで段階的に書き直し、多様な複雑性を持つデータを生成・混合してLLaMAをファインチューニングした。
- Data and results: complexityを揃えたtestとVicuna testで人手評価し、高難度部分ではWizardLM回答がChatGPTより好まれると報告。GPT-4評価では29skill中17でChatGPTの90%超相当とする。
- Novelty: 人間ではなくAI自身が指示データを進化させるEvol-Instruct手法を提案し、モデルの能力向上に利用した点。
- Limitations: 著者は一部でChatGPTに及ばないと述べる。編者の注意: 人手選好とGPT-4 judgeの評価であり、全taskの客観的正答率が90%という意味ではない。生成指示の品質・biasにも依存する。

### Paper: Active Retrieval Augmented Generation
- Source: arXiv
- Canonical ID: arxiv:2305.06983
- Publication date: 2023-05-11
- URL: https://arxiv.org/abs/2305.06983
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 次の文を予測して根拠を探し、低確信の内容を再生成するactive retrievalのFLARE。
- Objective: 最初に一回検索するだけでは不足する、長文生成中の継続的な情報取得を設計する。
- Methods: 今後のsentence予測をqueryに使い、low-confidence tokenを含む場合に関連文書を取得して文を再生成する。四つの知識集約的長文taskで比較する。
- Data and results: 全四taskで比較法を上回るか競合する性能を報告。いつ・何を取得するかを生成中に決める有効性を示すが、要旨にscoreはない。
- Novelty: 入力queryだけでなく、生成が向かう先を予測して動的に検索需要を作る。
- Limitations: 編者の注意: confidenceが高い誤答を必ず検出する仕組みではない。予測文に引かれた検索biasと、反復検索・再生成の計算費用を含めて評価する必要がある。

### Paper: MemoryBank: Enhancing Large Language Models with Long-Term Memory
- Source: arXiv
- Canonical ID: arxiv:2305.10250
- Publication date: 2023-05-17
- URL: https://arxiv.org/abs/2305.10250
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 対話経験を検索・更新し、忘却と強化を入れる長期記憶MemoryBankを提案する。
- Objective: 継続的なやり取りで関連情報を保持し、user特性へ適応する会話を支える。
- Methods: 経過時間と重要性による忘却曲線を模した更新を使う。SiliconFriendを実対話の定性評価とChatGPTで模擬する長期対話の定量評価で調べる。
- Data and results: 関連記憶の回想、user性格の理解、共感的応答の例を報告。要旨にmetric別の数値や臨床試験結果はない。
- Novelty: 全履歴を同じように保存するのではなく、重要性と時間で選択的に忘れ・強化する記憶管理を入れる。
- Limitations: 編者の注意: 心理対話の微調整やcompanionの評価は心理治療の安全性・有効性の実証ではない。模擬user評価と実利用者の長期便益を区別する。

### Paper: ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings
- Source: arXiv
- Canonical ID: arxiv:2305.11554
- Publication date: 2023-05-19
- URL: https://arxiv.org/abs/2305.11554
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ToolkenGPTは、ツールをトークン化しLLMに組み込む手法である。
- Objective: 大規模言語モデルの外部ツール利用における課題を解決する方法を探る。
- Methods: 基盤LMを凍結し、toolごとのtokenに対応する埋め込みを実演dataから学習する。toolkenの出力後にLMが引数を補完しtoolを実行する。
- Data and results: 数値推論、知識QA、embodied plan生成で、比較baselineを上回るtool利用を報告。要旨にtask別の成功率はない。
- Novelty: ツールをトークン（toolken）化することで、任意の数のツールを動的に組み込む柔軟性を実現した点。
- Limitations: 編者の注意: tool追加には埋め込みの学習と実演が必要で、任意数への拡張可能性は無限に費用なく使える保証ではない。引数生成の誤りやtoolの失敗も別に評価する。

### Paper: Improving Factuality and Reasoning in Language Models through Multiagent Debate
- Source: arXiv
- Canonical ID: arxiv:2305.14325
- Publication date: 2023-05-23
- URL: https://arxiv.org/abs/2305.14325
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 複数エージェントによる議論でLLMの事実性と推論能力を向上させる手法を提案した。
- Objective: 複数の言語モデルインスタンスに個別の応答と推論プロセスを議論させ、共通の最終回答を得ることで性能向上が可能か検証する。
- Methods: 複数の言語モデルインスタンスが複数ラウンドにわたって自身の応答と推論過程を提案し、議論させる手順を採用した。これは既存のブラックボックスモデルにも適用可能である。
- Data and results: 数学・戦略推論と生成内容の事実性に改善を報告。全taskで同一手順・promptを用い、black-boxモデルにも適用する。要旨にはtask別の数値・検定結果はない。
- Novelty: 複数の言語モデルインスタンスが応答と推論プロセスを議論する「心の社会」のアプローチを提案した点である。
- Limitations: 編者の注意: 複数instance・複数roundを使う追加推論費用がある。要旨だけでは同じ計算予算の単一モデル反復との比較や、誤った合意の頻度は判断できない。

### Paper: ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models
- Source: arXiv
- Canonical ID: arxiv:2305.18323
- Publication date: 2023-05-23
- URL: https://arxiv.org/abs/2305.18323
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ReWOOは、推論と外部観察を分離し、効率的なALMを実現する手法である。
- Objective: 既存のALMが抱える冗長なプロンプトや繰り返し実行による計算複雑性の課題を解決すること。
- Methods: LLMの思考プロセスから外部からの観測結果の取得を切り離すモジュール式パラダイムReWOOを提案し、6つのNLPベンチマークで評価した。
- Data and results: ReWOOはHotpotQAで5倍のトークン効率と4%の精度向上を示し、ツール失敗時にも堅牢性を示すことが確認された。
- Novelty: 推論プロセスと外部観察を分離することで、計算複雑性を大幅に削減する新しいパラダイムを提案した点。
- Limitations: 編者の注意: HotpotQAでのtoken効率とaccuracyは原著条件の値であり、全tool workflowの費用削減率ではない。観測を受けて次の行動を適応させる必要があるtaskへの一般化は要旨では判断できない。

### Paper: Reasoning with Language Model is Planning with World Model
- Source: arXiv
- Canonical ID: arxiv:2305.14992
- Publication date: 2023-05-24
- URL: https://arxiv.org/abs/2305.14992
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMの推論能力を世界モデルと計画アルゴリズムで強化するRAPフレームワークを提案した。
- Objective: 複雑な推論で将来状態と行動結果を予測し、代替経路を探索する計画をLLMに組み込む方法を検討する。
- Methods: LLMを世界モデルおよび推論エージェントとして再利用し、モンテカルロ木探索に基づく計画アルゴリズムを組み込んだRAPフレームワークを構築した。
- Data and results: 計画生成・数学・論理でCoT等と比較。ある計画生成設定でLLAMA-33BのRAPがGPT-4のCoTより33%相対改善と報告する。33 percentage pointsではない。
- Novelty: LLMにモンテカルロ木探索を組み込むことで、推論空間における戦略的な探索を可能にした点。
- Limitations: 編者の注意: LLMにworld modelがないという説明は著者の動機付けで、あらゆるmodel内部を証明した結論ではない。探索・報酬と追加推論計算を使うため、基盤model単独の能力差とは区別する。

### Paper: Gorilla: Large Language Model Connected with Massive APIs
- Source: arXiv
- Canonical ID: arxiv:2305.15334
- Publication date: 2023-05-24
- URL: https://arxiv.org/abs/2305.15334
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: API呼出生成向けに微調整したGorillaを、文書検索と組み合わせて評価する。
- Objective: LLMsがAPIコールを通じてツールを利用する潜在能力の実現可能性を探ること。
- Methods: LLaMAをAPI呼出向けに微調整し、API文書retrieverと接続する。Hugging Face、TorchHub、TensorHub由来のAPIBenchで呼出生成と文書更新への適応を調べる。
- Data and results: Gorillaは、文書検索システムと統合することで、テスト時ドキュメント変更への適応力とハルシネーションの軽減を示した。
- Novelty: API利用の正確さを専用dataで学習し、推論時の文書検索によるversion変更への適応と組み合わせる。
- Limitations: 編者の注意: GPT-4超えは原著のAPI呼出生成の比較であり、全taskでの優越ではない。呼出文の正確さと、権限・副作用を含む実行の安全性は別に評価する。要旨にtask別scoreはない。

### Paper: Voyager: An Open-Ended Embodied Agent with Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2305.16291
- Publication date: 2023-05-25
- URL: https://arxiv.org/abs/2305.16291
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: Voyagerは、Minecraft内で自律的に学習するLLM搭載のエージェントである。
- Objective: 人間による介入なしに、どのようにして継続的な世界探索とスキル獲得を可能にするか？
- Methods: 自動カリキュラム、実行可能なスキルライブラリ、環境フィードバックを取り込む反復プロンプティング機構を用いる。
- Data and results: Minecraftで先行法比3.3倍の固有item、2.3倍の移動距離、主要技術到達の最大15.3倍高速化を報告。skill libraryを新しいworldの新taskに再利用した。
- Novelty: 環境からのフィードバックと自己検証を組み込んだ新しい反復プロンプティング機構を採用した点。
- Limitations: 編者の注意: skillは実行可能codeとして保存され、GPT-4の重みを更新する学習とは異なる。結果はMinecraftと原著の比較条件に関するもので、実世界robotの性能を示さない。

### Paper: On the Tool Manipulation Capability of Open-source Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2305.16504
- Publication date: 2023-05-25
- URL: https://arxiv.org/abs/2305.16504
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: オープンソースLLMのツール操作能力を向上させ、クローズドAPIに匹敵させる手法を提案した。
- Objective: 実用的な量の人手によるデータ整備で、公開LLMのツール操作を主要な閉鎖モデルに近づけられるかを調べる。
- Methods: ToolBenchという多様なソフトウェアツールからなるベンチマークを作成し、使用例やインコンテキストデモなどを用いてモデルを調整した。
- Data and results: 成功率が最大90%に達し、ToolBenchの8task中4taskでGPT-4に競合すると報告。90%の相対改善という意味ではない。
- Novelty: プログラムによるデータ生成、システムプロンプト、インコンテキストデモ検索器を組み合わせることで、オープンソースLLMのツール操作能力を向上させた点。
- Limitations: 著者はtoolごとに約1開発日分のデータ整備を要すると述べる。編者の注意: 8taskでの比較であり、ToolLLM（arXiv:2307.16789）のToolBenchとは別のbenchmarkである。

### Paper: Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents
- Source: arXiv
- Canonical ID: arxiv:2306.03314
- Publication date: 2023-06-05
- URL: https://arxiv.org/abs/2306.03314
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 多エージェントシステムを活用し、LLMの能力を向上させる新しいフレームワークを提案した。
- Objective: 複雑なタスク処理において、複数の知的なエージェントが協調する仕組みを確立すること。
- Methods: Auto-GPT、BabyAGI、APIを使うGorilla等をcase studyとし、異なる役割・属性を持つagentの協調設計と応用を論じる。
- Data and results: 提案された多エージェントシステムは、法廷シミュレーションやソフトウェア開発など多様なドメインでの応用可能性を示した。
- Novelty: 各エージェントに固有の属性と役割を持たせ、知識交換を通じてLLMの能力向上を図る点。
- Limitations: 著者はloop、security、scalability、評価等を課題として扱う。編者の注意: case studyと構想が中心であり、要旨には統一benchmarkによる性能向上や費用対効果の数値はない。

### Paper: ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases
- Source: arXiv
- Canonical ID: arxiv:2306.05301
- Publication date: 2023-06-08
- URL: https://arxiv.org/abs/2306.05301
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ToolAlpacaは、小規模LLMに汎用的なツール利用能力を学習させるフレームワークである。
- Objective: tool-useの共通知識を学習した小型modelが、新しいtoolごとの追加訓練なしに利用できるかを調べる。
- Methods: multi-agent simulationで50カテゴリ・400超APIから3,938利用例を生成し、7B・13Bを微調整する。学習時に見ないtoolを評価する。
- Data and results: ToolAlpacaはGPT-3.5に匹敵する効果的な汎用ツール利用能力を示し、実現可能であることを実証した。
- Novelty: 本手法は、最小限の人的介入で多様なコーパスを自動生成し、小規模モデルでの学習を目指す点にある。
- Limitations: 編者の注意: unseen toolごとの訓練が不要という意味で、tool-useの訓練全体が不要ではない。simulation dataと評価toolの構成に依存し、原著のGPT-3.5との比較を全modelへ一般化しない。

### Paper: Mind2Web: Towards a Generalist Agent for the Web
- Source: arXiv
- Canonical ID: arxiv:2306.06070
- Publication date: 2023-06-09
- URL: https://arxiv.org/abs/2306.06070
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 137の実websiteから集めた多様なtaskと行動軌跡で、Web agentの汎化を評価する。
- Objective: 少数の模擬siteを超え、新しいwebsite・domainにも使えるagentを研究する。
- Methods: 31domain・137siteの2,000超taskとcrowd行動系列を収集。巨大HTMLを小LMでfilterしてから大LMへ渡す方法を比較する。
- Data and results: HTML filteringで有効性・効率が改善し、未知site・domainでも一定の成果を報告する一方、真に汎用なagentには改善余地が大きいとする。要旨にscoreはない。
- Novelty: 実websiteの多様な相互作用と、入力を絞る小modelを組み合わせた一般化testbedを示す。
- Limitations: 編者の注意: any websiteは研究目標で、全siteの達成保証ではない。収集軌跡による評価とlive siteでのend-to-end実行を同じ成功率とみなさない。

### Paper: RestGPT: Connecting Large Language Models with Real-World RESTful APIs
- Source: arXiv
- Canonical ID: arxiv:2306.06624
- Publication date: 2023-06-11
- URL: https://arxiv.org/abs/2306.06624
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: RestGPTはLLMと実世界のRESTful APIを接続し、複雑な指示に対応する手法である。
- Objective: 既存のツール利用型LLMが抱える、現実世界での複雑な指示への対応限界を克服すること。
- Methods: RestGPTは、LLMの能力を活用し、粗視的から微細なオンライン計画機構でタスク分解とAPI選択を行う。また、RESTful API呼び出しに特化した実行器を持つ。
- Data and results: 二つの実世界scenarioと人手の指示・gold経路を持つRestBenchを構築し、複雑な指示への成果と頑健性を報告。要旨に具体的な成功率はない。
- Novelty: 本研究は、LLMを広く採用されているRESTソフトウェアアーキテクチャのAPIに接続する新しいアプローチを提案した点にある。
- Limitations: 編者の注意: API parameterの構成と応答parseも含むsystemであり、LLM単体の改善と区別する。二scenarioでの結果は任意のREST APIへの正しい実行やAGIを示すものではない。

### Paper: ToolQA: A Dataset for LLM Question Answering with External Tools
- Source: arXiv
- Canonical ID: arxiv:2306.13304
- Publication date: 2023-06-23
- URL: https://arxiv.org/abs/2306.13304
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 外部ツール利用能力を評価する新しいデータセットToolQAを提案した。
- Objective: LLMの内部知識と外部ツール使用が必要な質問を区別し、評価することが目的である。
- Methods: 13種類の専門ツールを用いた自動的なデータキュレーションプロセスでToolQAを構築した。
- Data and results: 自動curationと13専門toolによるToolQAを公開し、既存tool利用LMの強み・弱点を診断する。要旨にはmodel別の定量成績や失敗内訳はない。
- Novelty: 外部ツール使用が必要な質問に特化し、既存知識との重複を最小限に抑えた点が新規である。
- Limitations: 著者は事前学習dataとの重複を最小化する努力を述べ、完全な非重複を保証していない。編者の注意: 内部知識だけで解ける問題と外部toolが不可欠な問題の区別が評価の中心である。

### Paper: Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks
- Source: arXiv
- Canonical ID: arxiv:2307.02477
- Publication date: 2023-07-05
- URL: https://arxiv.org/abs/2307.02477
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMの推論能力を反実仮想タスクで検証し、その限界を探った研究である。
- Objective: 言語モデルが持つ抽象的な推論能力は汎用的か、それとも事前学習された特定のタスクに特化しているのかを解明すること。
- Methods: 11種類のタスク群を用いて、「反実仮想」なバリアントを作成し、標準タスクの前提から逸脱した形で性能を評価するフレームワークを提案・適用した。
- Data and results: 反実仮想バリアントでは非自明な性能を示すものの、デフォルト条件と比較して一貫して大幅に性能が低下することが確認された。
- Novelty: 標準的なタスク設定からの逸脱を意図的に組み込んだ「反実仮想」タスク変数を評価フレームワークとして導入した点。
- Limitations: 編者の注意: 原著は抽象推論を全否定せず、部分的能力と既知手続への依存の両方を報告する。前提を変えた11taskの結果から、すべての推論が暗記だけだとは結論できない。

### Paper: Lost in the Middle: How Language Models Use Long Contexts
- Source: arXiv
- Canonical ID: arxiv:2307.03172
- Publication date: 2023-07-06
- URL: https://arxiv.org/abs/2307.03172
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMは長文コンテキストの利用に課題があり、特に中央部の情報参照が苦手である。
- Objective: 言語モデルが長い入力コンテキスト内の情報をどの程度効果的に利用しているかを分析する。
- Methods: マルチドキュメントQAとキーバリュー検索の2タスクで性能を評価し、情報の位置変化による影響を検証した。
- Data and results: 関連情報が文頭や末尾にある場合に高い性能を示す一方、長文の中央部にある情報は参照が困難であることが判明した。
- Novelty: 入力コンテキスト内の情報利用に関する理解を深め、将来のモデルのための評価プロトコルを提供する点。
- Limitations: 編者の注意: multi-document QAとkey-value retrievalにおける位置依存の結果である。context窓の最大長と、そこにある情報の有効利用を区別する。現行の全modelで必ず同じ劣化が起こるという主張ではない。

### Paper: VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models
- Source: arXiv
- Canonical ID: arxiv:2307.05973
- Publication date: 2023-07-12
- URL: https://arxiv.org/abs/2307.05973
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMの知識を統合し、ロボット操作のための軌道を合成する手法を提案した。
- Objective: 自由形式の指示と物体セットから、多様なマニピュレーションタスクの軌道合成を目指す。
- Methods: LLMが言語指示からaffordanceと制約を推定し、VLMとcode生成で3D value mapへ接地する。model-based plannerで閉loopの6-DoF waypoint列を合成する。
- Data and results: 提案フレームワークはシミュレーションおよび実ロボット環境で多様な日常操作タスクを実行可能であることを示した。
- Novelty: LLMのコード生成能力を利用し、知識を観測空間に接地させる3Dバリューマップを合成した点。
- Limitations: 編者の注意: value mapの知覚・合成とplannerの精度に依存する。onlineのdynamics学習を使う接触の多いsceneもあり、すべての動作を経験なしに完全解決する意味ではない。要旨にtask別成功率はない。

### Paper: ChatDev: Communicative Agents for Software Development
- Source: arXiv
- Canonical ID: arxiv:2307.07924
- Publication date: 2023-07-16
- URL: https://arxiv.org/abs/2307.07924
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMエージェントによる対話型開発フレームワークChatDevを提案する。
- Objective: 各フェーズの技術的非一貫性を克服し、協調的なソフトウェア開発を目指す。
- Methods: 専門エージェントがチャットチェーンとコミュニケーションデハルシネーションでガイドされ、設計・コーディング・テストに貢献させる。
- Data and results: 自然言語はシステム設計に有利であり、プログラミング言語での対話はデバッグに役立つことが判明した。
- Novelty: 言語を統一的な橋渡しとし、LLMエージェント間の自律的なタスク解決を可能にする点を提案する。
- Limitations: 編者の注意: 設計・code・test段階の協調を扱う研究で、既存大規模repositoryの実issue修正と同じ問題設定ではない。要旨に定量的な成功率・費用・保守性の比較はない。

### Paper: WebArena: A Realistic Web Environment for Building Autonomous Agents
- Source: arXiv
- Canonical ID: arxiv:2307.13854
- Publication date: 2023-07-25
- URL: https://arxiv.org/abs/2307.13854
- read_level: full_text
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: WebArenaは、現実的なウェブタスク実行のための環境を提供し、自律エージェントの評価を可能にする。
- Objective: 自然言語コマンドによる日常タスク管理を行う自律エージェントの実世界での性能評価を目指す。
- Methods: 実機能を持つ4分野のsiteとtool・manualを用意。241templateから812課題を作り、回答の一致・意味比較やURL、database状態で機能的正しさを採点する。
- Data and results: GPT-4ベースのエージェントは複雑なタスクで14.41%の成功率に留まり、人間の78.24%から大きく乖離した。
- Novelty: 本環境は、現実的なウェブサイトを模倣し、長期かつ多様なベンチマークタスクを提供することで新規性を確立した。
- Limitations: 編者の注意: 14.41%対78.24%は原著のbest GPT-4 agentと人間の比較であり、現在のagent一般の値ではない。機能を再現した管理下のWeb環境で、任意のlive website全体を評価したものではない。

本文の照合箇所: [3.1 Intent Collection、3.2 Evaluation Annotation](https://arxiv.org/html/2307.13854v3)。

### Paper: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
- Source: arXiv
- Canonical ID: arxiv:2307.15818
- Publication date: 2023-07-28
- URL: https://arxiv.org/abs/2307.15818
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: Web知識をロボット制御に組み込むVLAモデルRT-2を提案し、汎化能力と推論力を向上させた。
- Objective: 単一のモデルでロボット観察から行動のマッピング学習と大規模事前学習の恩恵を得ることを目指す。
- Methods: 最先端のVLMをロボット軌道データとWeb規模のVQAタスクの両方で共同ファインチューニングする。行動をテキストトークンとして表現し、自然言語と同様に訓練セットに組み込む。
- Data and results: 約6,000試行で評価し、新物体への汎化、robot学習にない指示の解釈、大小・位置の推論等を報告。CoTを組み込んだ多段階の意味推論例も示す。
- Novelty: 行動をテキストトークンとして表現し、自然言語とロボット行動を同一形式でモデルに組み込む一般的手法を提案した点。
- Limitations: 編者の注意: Webで学んだ意味知識の転移と、robotが未知の運動skillを安全に習得することは別である。6,000は評価試行数で成功数ではなく、要旨に一律の成功率はない。

### Paper: ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs
- Source: arXiv
- Canonical ID: arxiv:2307.16789
- Publication date: 2023-07-31
- URL: https://arxiv.org/abs/2307.16789
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ToolLLMは、実世界のAPI利用に特化したフレームワークを提供し、オープンソースLLMのツール使用能力を向上させる。
- Objective: オープンソースLLMが外部APIを利用するツール使用能力において抱える限界点を克服する方法を探る。
- Methods: 49カテゴリ16,464 APIからChatGPTで指示と解答経路を生成してToolBenchを構築。深さ優先探索、API retriever、ToolEvalを整備し、LLaMAをToolLLaMAへ微調整する。
- Data and results: ファインチューニングされたToolLLaMAは複雑な指示を実行し、未見のAPIへの汎化能力を示し、ChatGPTに匹敵する性能を発揮した。
- Novelty: 本研究では、データ構築、モデル訓練、評価を含む包括的なツール使用フレームワークであるToolLLMを提案した点が新規である。
- Limitations: 編者の注意: データ・解答経路・評価がChatGPT等に依存し、自動評価と実際の正しい実行は区別が必要。本稿のToolBenchはarXiv:2305.16504の同名benchmarkとは別である。

### Paper: MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework
- Source: arXiv
- Canonical ID: arxiv:2308.00352
- Publication date: 2023-08-01
- URL: https://arxiv.org/abs/2308.00352
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: MetaGPTは、LLMベースのマルチエージェント協調に人間的なワークフローを組み込んだメタプログラミングフレームワークである。
- Objective: 複雑なタスクにおける論理的不整合やハルシネーションの問題を解決する方法を探る。
- Methods: SOPsをプロンプトシーケンスとして符号化し、アセンブリラインのパラダイムで多様な役割を割り当てる。
- Data and results: 共同ソフトウェアエンジニアリングベンチマークにおいて、従来のチャットベースシステムより一貫性のあるソリューションを生成した。
- Novelty: 役割と標準作業手順をprompt列へ組み込み、中間成果物を確認する流れで自由な会話の連鎖による誤りを減らす協調設計である。
- Limitations: 編者の注意: agentの専門性は役割設計によるもので、人間専門家と同等の資格・能力を実証した意味ではない。要旨に費用を揃えた比較や誤りの完全な解消は示されない。

### Paper: Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization
- Source: arXiv
- Canonical ID: arxiv:2308.02151
- Publication date: 2023-08-04
- URL: https://arxiv.org/abs/2308.02151
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 環境フィードバックからプロンプトを自動調整するフレームワークを提案した。
- Objective: LLMエージェントの性能向上のため、環境からの報酬を利用した最適化手法を確立すること。
- Methods: 過去失敗の根因と行動計画を言語化してagentのpromptを改良するretrospective modelを、複数環境の報酬からpolicy gradientで微調整する。
- Data and results: 提案されたエージェントは時間経過とともに改善し、環境からの勾配を利用しないベースラインを大幅に上回る性能を示した。
- Novelty: ポリシー勾配最適化を用いて言語エージェントのプロンプトを調整する手法を提案した点が新規である。
- Limitations: 編者の注意: 主に学習するのはpromptを改善するretrospective modelであり、verbal feedbackだけの方式と区別する。報酬が取得できる条件に依存し、要旨にtask別の数値や学習費用はない。

### Paper: AgentBench: Evaluating LLMs as Agents
- Source: arXiv
- Canonical ID: arxiv:2308.03688
- Publication date: 2023-08-07
- URL: https://arxiv.org/abs/2308.03688
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMをエージェントとして評価する多次元ベンチマークAgentBenchを提案した。
- Objective: インタラクティブ環境におけるLLMのエージェントとしての能力を定量的に評価する必要がある。
- Methods: APIベースおよびOSSのLLMを用いて、8つの異なる環境で広範なテストを実施し、性能を評価した。
- Data and results: 8環境で商用上位modelと70B以下の多数のOSSに性能差を報告。長期推論・意思決定・指示追従が主な失敗要因で、code学習の影響はtaskにより異なるとする。
- Novelty: AgentBenchという多次元ベンチマークを提供し、LLMエージェントの能力を包括的に評価する枠組みを提示した。
- Limitations: 編者の注意: 要旨のmodel総数はLaTeX macroが未展開のため確定しない。商用対OSSの比較は公開時点のmodel構成に依存し、parameter数だけの因果効果を分離した結果ではない。

### Paper: AgentSims: An Open-Source Sandbox for Large Language Model Evaluation
- Source: arXiv
- Canonical ID: arxiv:2308.04026
- Publication date: 2023-08-08
- URL: https://arxiv.org/abs/2308.04026
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMの評価のためのオープンソースサンドボックスAgentSimsを提案する。
- Objective: 既存のLLM評価手法が抱える制約や課題を解決する方法は何か？
- Methods: インタラクティブGUIまたは数行のコードでエージェントや建物を追加し、タスクベースの評価環境を構築できる。
- Data and results: 本フレームワークにより、研究者は関心のある特定の能力をテストするための評価タスクを容易に構築・実行可能になった。
- Novelty: GUIでagent・建物を配置し、記憶・計画・tool利用機構を差し替えて特定能力を調べられる評価基盤の提供が貢献である。
- Limitations: 編者の注意: task-based評価を汎用的解決策とするのは著者の提案である。要旨に他評価法への優越を示す定量比較はなく、simulationが現実の全能力を測れると保証しない。

### Paper: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation
- Source: arXiv
- Canonical ID: arxiv:2308.08155
- Publication date: 2023-08-16
- URL: https://arxiv.org/abs/2308.08155
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: AutoGenは、複数のエージェントが対話する仕組みでLLMアプリを構築できるフレームワークである。
- Objective: どのようにして複数のエージェントの会話を通じて高度なLLMアプリケーションを開発できるか？
- Methods: 本フレームワークでは、カスタマイズ可能なエージェント群を用い、LLM、人間からの入力、ツールを組み合わせた対話モードで動作させる。自然言語とコードの両方で柔軟な対話パターンを定義する。
- Data and results: 数学、coding、QA、operations research、online意思決定等の事例で有効性を示す。要旨には全task共通の性能差や統一比較の数値はない。
- Novelty: エージェント間の相互作用挙動を柔軟に定義できる点が新規であり、汎用的な基盤を提供する。
- Limitations: 編者の注意: 会話の構成を柔軟に定義できるframeworkの提案であり、多agent化が常に品質や費用効率を改善するという証明ではない。人間・tool・LLMの構成差も比較に影響する。

### Paper: AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors
- Source: arXiv
- Canonical ID: arxiv:2308.10848
- Publication date: 2023-08-21
- URL: https://arxiv.org/abs/2308.10848
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLM搭載エージェントの協調性を高めるマルチエージェントフレームワークを提案した。
- Objective: 現実世界でのタスク達成に向けた、個体間の協力メカニズムを探求すること。
- Methods: 人間集団力学に着想を得て、構成が動的に調整可能なマルチエージェントフレームワークを構築し実験を行った。
- Data and results: 本フレームワークは単一のエージェントを上回る性能を発揮し、協調タスク遂行中の社会行動の創発も確認された。
- Novelty: 個々の能力以上のシステムとして機能する、動的構成変更可能なマルチエージェント枠組みを提供した点。
- Limitations: 編者の注意: 複数agentの優位は原著で選んだtask・構成での報告であり、同計算予算での普遍的優越ではない。正負の社会的振舞いも論じるが、要旨に各失敗率・追加費用はない。

### Paper: A Survey on Large Language Model based Autonomous Agents
- Source: arXiv
- Canonical ID: arxiv:2308.11432
- Publication date: 2023-08-22
- URL: https://arxiv.org/abs/2308.11432
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 本稿はLLMベースの自律エージェントに関する包括的なサーベイを提供し、その構造と応用を網羅的に解説する。
- Objective: LLMを用いた自律エージェント研究の現状を体系的にレビューし、今後の課題と方向性を示すこと。
- Methods: LLMベースのエージェント構築のための統一フレームワークを提案し、社会科学、自然科学、工学分野での多様な応用例と評価戦略を包括的に概観した。
- Data and results: 本サーベイでは、エージェントの構造化された枠組み、多岐にわたる応用分野、および一般的な評価手法について詳細に論じている。
- Novelty: これまでの研究を包含する統一フレームワークを提案し、LLMベースのエージェントに関する包括的な視点を提供した点。
- Limitations: 編者の注意: 構成・応用・評価のsurveyであり統一条件の新規性能実験ではない。要旨には検索式や採否基準がなく、文献が後日増えることと原著版の網羅性は区別する。

### Paper: ModelScope-Agent: Building Your Customizable Agent System with Open-source Large Language Models
- Source: arXiv
- Canonical ID: arxiv:2309.00986
- Publication date: 2023-09-02
- URL: https://arxiv.org/abs/2309.00986
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ModelScope-Agentは、オープンソースLLMを制御器とする汎用エージェントフレームワークである。
- Objective: 複雑なタスク遂行のため、LLMに外部API連携能力を持たせる方法論の構築が求められている。
- Methods: tool-use data収集、retrieval、登録、memory制御、model学習・評価を統合するengineを提供し、公開LLMとmodel API・一般APIを接続する。
- Data and results: ModelScopeGPTは、本フレームワークを用いて1000以上の公開AIモデルとローカル知識に接続できる実用的なアシスタントとして機能する。
- Novelty: 本フレームワークは、ツール利用データ収集から評価までを網羅し、オープンソースLLMを制御器とする汎用性を実現した点にある。
- Limitations: 編者の注意: 1,000超は接続可能なAI modelの規模であり、それぞれのtaskで正しく利用できる成功数ではない。要旨には統一benchmarkの正答率・失敗率・費用は示されない。

### Paper: The Rise and Potential of Large Language Model Based Agents: A Survey
- Source: arXiv
- Canonical ID: arxiv:2309.07864
- Publication date: 2023-09-14
- URL: https://arxiv.org/abs/2309.07864
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 本稿は、LLMを基盤とするエージェントの概念から応用までを包括的に調査したサーベイ論文である。
- Objective: LLMがAIエージェント設計における汎用的な出発点としてなぜ適しているのかを明らかにすること。
- Methods: エージェントの概念を哲学的な起源から追跡し、LLMベースのエージェントのための「脳」「知覚」「行動」の一般フレームワークを提示した。
- Data and results: 単一エージェント、マルチエージェント、人間との協調といった広範な応用例に加え、エージェント社会における振る舞いを考察している。
- Novelty: LLMを基盤とし、「脳」「知覚」「行動」という三つの主要コンポーネントからなる一般フレームワークを提案した点。
- Limitations: 編者の注意: 概念史と構成・応用・社会的振舞いを整理するsurveyであり、AGIの達成を実証する研究ではない。要旨には文献検索の採否基準や全研究の網羅率はない。

### Paper: Agents: An Open-source Framework for Autonomous Language Agents
- Source: arXiv
- Canonical ID: arxiv:2309.07870
- Publication date: 2023-09-14
- URL: https://arxiv.org/abs/2309.07870
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 自律的な言語エージェント構築のためのオープンソースフレームワーク「Agents」を公開した。
- Objective: 自然言語インターフェースで多様なタスクを自動解決する言語エージェントの実現を目指す。
- Methods: 計画、メモリ、ツール使用、マルチエージェント通信など重要機能をサポートするように設計されたライブラリである。
- Data and results: 計画・記憶・tool利用・多agent通信・symbolic制御を備えた公開libraryを提供する。要旨には非専門家による利用試験やtask成功率の定量値はない。
- Novelty: Agentsは、自律的な言語エージェントの進歩をより広い非専門家層に開くことを目的としている点。
- Limitations: 編者の注意: 使いやすさ・拡張性は設計上の目標と機能の記述であり、あらゆる利用者が高性能agentを構築できる実証ではない。frameworkの機能数とtask達成能力を分ける。

### Paper: Ragas: Automated Evaluation of Retrieval Augmented Generation
- Source: arXiv
- Canonical ID: arxiv:2309.15217
- Publication date: 2023-09-26
- URL: https://arxiv.org/abs/2309.15217
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 検索context・根拠への忠実性・生成品質を分け、参照正解なしで評価するRagas。
- Objective: RAGを単一正答率だけでなく、retrievalとgenerationの複数側面から迅速に評価する。
- Methods: 関連・focusedなcontextの取得、取得内容の忠実な利用、出力品質を測るmetric群を提案し、人手ground truth annotationを必要としない枠組みを構成する。
- Data and results: reference-free評価frameworkと指標群の提案が成果。要旨には人手との一致率や評価誤差の数値はない。
- Novelty: 取得根拠と出力の関係を分解し、正解文を作る費用を抑えた評価cycleを設ける。
- Limitations: 編者の注意: reference-freeは評価器の誤りや独立検証が不要という意味ではない。文書に忠実でも文書自体が誤っていれば事実正確とは限らず、指標間の意味を区別する。

### Paper: DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines
- Source: arXiv
- Canonical ID: arxiv:2310.03714
- Publication date: 2023-10-05
- URL: https://arxiv.org/abs/2310.03714
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: DSPyは、言語モデル呼び出しを宣言的グラフとして抽象化し、自己改善可能なパイプライン構築を可能にするプログラミングモデルである。
- Objective: 複雑なタスク解決のためのLMパイプライン開発をより体系的に行うための手法を提案すること。
- Methods: 宣言的moduleを結ぶtext変換graphとしてpipelineを表し、実演の生成・収集等を通じ、与えたmetricを高めるようcompilerで最適化する。
- Data and results: 数学文章題、多hop検索、複雑QA、agent loopを含む二つのcase studyを報告。標準few-shotに対しGPT-3.5とLlama2-13B-chatで大きな改善、小型modelで専門家prompt鎖と競合する例を示す。
- Novelty: DSPyはLMパイプラインを宣言的グラフとして抽象化し、コンパイルを通じて自己改善可能な構造を提供することが新しい点である。
- Limitations: 編者の注意: 最適化対象metricと訓練・開発dataに依存する。compilerが任意taskの大域最適を保証する意味ではない。改善率はcase studyの比較対象・model条件を伴う。

### Paper: Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models
- Source: arXiv
- Canonical ID: arxiv:2310.04406
- Publication date: 2023-10-06
- URL: https://arxiv.org/abs/2310.04406
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LMのvalue推定・内省と外部feedbackをMonte Carlo木探索へ組み込むLATSを提案する。
- Objective: 言語モデルの単なる行動プロセスへの依存性を克服し、自律エージェントとしての能力を向上させる方法を探る。
- Methods: モンテカルロ木探索を組み込み、外部フィードバック環境とLMベースの価値関数を用いてLMsをエージェント化する。
- Data and results: GPT-4でHumanEval pass@1 92.7%、GPT-3.5でWebShop平均score 75.9を報告。programming、QA、Web、数学に適用する。
- Novelty: LATSは、推論、行動、計画能力を統合し、外部フィードバック環境を取り入れた点が新規である。
- Limitations: 編者の注意: pass@1でも内部に探索と複数の推論・feedback利用を含むため、一回の素の生成精度と同じではない。WebShopの平均scoreを成功率75.9%へ読み替えない。

### Paper: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- Source: arXiv
- Canonical ID: arxiv:2310.06770
- Publication date: 2023-10-10
- URL: https://arxiv.org/abs/2310.06770
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: SWE-benchは、実世界のGitHub課題を用いたLLM評価フレームワークである。
- Objective: 言語モデルが現実のソフトウェアエンジニアリングの問題を解決できるか検証すること。
- Methods: 12のPythonリポジトリから2,294の実在するGitHub課題を用い、コードベース編集タスクとして定式化した。
- Data and results: 12のPython repositoryから集めた実issueとPRの2,294問題を用い、原著評価のbest model Claude 2が1.96%を解決。複数file等にまたがる修正の難しさを示す。
- Novelty: 実世界のGitHub課題とプルリクエストを利用し、複雑な変更調整能力を評価する点。
- Limitations: 編者の注意: 1.96%は原著時点の評価であり現在のagentの成功率ではない。Pythonの選定repositoryに限り、Lite・Verified等の後発subsetとは問題数・構成が異なる。

### Paper: Fine-Tuning LLaMA for Multi-Stage Text Retrieval
- Source: arXiv
- Canonical ID: arxiv:2310.08319
- Publication date: 2023-10-12
- URL: https://arxiv.org/abs/2310.08319
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLaMAをファインチューニングし、多段階テキスト検索の性能向上を目指した研究である。
- Objective: 最先端の大規模言語モデル（LLMs）が、従来のテキスト検索手法にどのような改善をもたらすかを検証すること。
- Methods: 最新のLLaMAモデルを密なリトリーバー（RepLLaMA）と点ごとの再ランク付け器（RankLLaMA）としてファインチューニングし、MS MARCOデータセットで評価した。
- Data and results: LLMsは小型モデルを上回り、長いコンテキスト処理によりドキュメント全体を捉えられ、BEIRでのパイプラインも高いゼロショット性能を示した。
- Novelty: RepLLaMAとRankLLaMAの組み合わせにより、従来のセグメンテーションやプーリング戦略を不要とする包括的な文書表現が可能になった点。
- Limitations: 編者の注意: MS MARCOで微調整しBEIRへ転移する検索実験であり、全domainの無監督検索を保証しない。document全体を扱える範囲はcontext長に依存し、query時費用やindex容量も比較する必要がある。

### Paper: MemGPT: Towards LLMs as Operating Systems
- Source: arXiv
- Canonical ID: arxiv:2310.08560
- Publication date: 2023-10-12
- URL: https://arxiv.org/abs/2310.08560
- read_level: full_text
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: MemGPTは、LLMのコンテキスト制限を克服するOSのようなシステムである。
- Objective: LLMの限られたコンテキストウィンドウを超える長期的な情報処理を可能にする方法論を探求すること。
- Methods: 高速・低速のmemory階層間で情報を移すvirtual context管理と、割込みによる制御を導入する。文書分析と複数session対話で評価する。
- Data and results: 拡張Multi-Session Chatのdeep memory retrievalでGPT-4のaccuracyは32.1%からMemGPT併用92.5%へ。GPT-4 Turboでは35.3%から93.4%。文書QA・nested KV検索も評価する。
- Novelty: 従来のOSの階層的メモリシステムから着想を得て、LLMに仮想的な大容量メモリ機能を持たせた点。
- Limitations: 編者の注意: 基盤context窓を無限化せず外部記憶を検索する方式。上記はMSCに追加した狭い正解範囲の質問へのaccuracyで、人間との長期実会話全体の正確さではない。

本文の照合箇所: [2.2–2.4 記憶管理、3.1/Table 2 対話評価](https://arxiv.org/html/2310.08560v2)。

### Paper: Open X-Embodiment: Robotic Learning Datasets and RT-X Models
- Source: arXiv
- Canonical ID: arxiv:2310.08864
- Publication date: 2023-10-13
- URL: https://arxiv.org/abs/2310.08864
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ロボット学習の一般化を目指し、大規模なデータセットとモデルを提案した。
- Objective: ロボティクス分野で汎用的なX-ロボットポリシーの訓練は可能か？
- Methods: 21機関から収集した22種類のロボットを用いた527スキルのデータセットを構築し、高容量モデルRT-Xを訓練した。
- Data and results: RT-Xは、他のプラットフォームの経験を活用することで複数のロボットの能力向上を示す正の転移効果を示した。
- Novelty: 汎用的なX-ロボットポリシーを目指し、標準化されたデータ形式とモデルを提供した点。
- Limitations: 編者の注意: 標準化dataを用いたrobot間の正の転移であり、全robotへのzero-shot動作保証ではない。原著要旨のtask数表示は解釈が不明瞭なため再掲せず、22robot・21機関・527skillという確認できる規模を記す。

### Paper: OpenAgents: An Open Platform for Language Agents in the Wild
- Source: arXiv
- Canonical ID: arxiv:2310.10634
- Publication date: 2023-10-16
- URL: https://arxiv.org/abs/2310.10634
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: OpenAgentsは、日常的な環境で言語エージェントを利用・ホストするためのオープンプラットフォームである。
- Objective: 既存のフレームワークが無視する非専門ユーザーへのアクセスとアプリケーションレベル設計を考慮したエージェント基盤を提供すること。
- Methods: データ分析用Data Agent（Python/SQL）、200以上のAPIツールを持つPlugins Agent、自律的なWeb Browsingを行うWeb Agentを含む3つのエージェント群を提供する。
- Data and results: Python/SQL分析、200超API利用、Web閲覧の三agentと利用者向けUI・local deploymentを提供。要旨に利用者試験や統一task成功率の定量結果はない。
- Novelty: 非専門ユーザーの利用とアプリケーションレベル設計に焦点を当てた、実環境での言語エージェントのためのオープンプラットフォームを提供した点。
- Limitations: 編者の注意: 実用アクセスを重視したplatformの提案であり、一般利用での失敗・latency・安全性の全てを解決した実証ではない。200超はtool規模で成功数ではない。

### Paper: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
- Source: arXiv
- Canonical ID: arxiv:2310.11511
- Publication date: 2023-10-17
- URL: https://arxiv.org/abs/2310.11511
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: Self-RAGは、自己内省を通じてLLMのファクト性と品質を向上させるフレームワークである。
- Objective: 検索の必要性や文書の関連性にかかわらず固定件数を使うRAGの問題を、適応的検索と自己評価で改善する。
- Methods: 単一のLMを訓練し、特別なリフレクション・トークンを用いて必要な時に適応的に情報を検索・生成・内省する。
- Data and results: 7B・13BのSelf-RAGでopen-domain QA、推論、fact検証を評価し、ChatGPTや検索付きLlama2-chatより良い成績、長文の事実性・引用精度の改善を報告する。
- Novelty: 本手法は、単に知識を付加するだけでなく、自己内省のプロセスを組み込む点で新規性を持つ。
- Limitations: 編者の注意: reflection tokenを学習する方法であり、一般modelに内省promptを足すだけとは異なる。自己評価の誤りや検索sourceの信頼性は残り、引用の存在と支持関係の正しさを区別する。

### Paper: LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS-Agent Ecosystem
- Source: arXiv
- Canonical ID: arxiv:2312.03815
- Publication date: 2023-12-06
- URL: https://arxiv.org/abs/2312.03815
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMをAIOSとし、エージェントをアプリとする新しいエコシステムを提唱する。
- Objective: LLMが従来のOSやアプリケーションの枠を超えてどのようにコンピューティングシステムを変革するかを探る。
- Methods: 伝統的なOSアーキテクチャを紹介した後、「LLM as OS (LLMOS)」という概念的フレームワークを構築し、AIOS-Agentエコシステムを提案した。
- Data and results: LLMをkernel、contextをmemory、外部保存をfile system、toolをdevice/libraryに対応させる概念枠組みと、agent ecosystemの研究roadmapを示す。実装の性能実験は要旨にない。
- Novelty: LLMをOSカーネルのように位置づけ、エージェントをアプリとして捉えるAIOSという新しいパラダイムを提案した点。
- Limitations: 編者の注意: 自然言語programmingや開発の民主化は構想であり、測定された達成結果ではない。OSとの類比が従来OSの隔離・信頼性・resource管理の保証を備える意味ではない。

### Paper: AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation
- Source: arXiv
- Canonical ID: arxiv:2312.13010
- Publication date: 2023-12-20
- URL: https://arxiv.org/abs/2312.13010
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: AgentCoderは、複数エージェントによる反復的なテストと最適化でコード生成を行う手法である。
- Objective: LLMのコード生成における課題を解決するため、効果的なテストケース生成と実行を統合するシステムを提案すること。
- Methods: プログラマー、テスト設計者、テスト実行者の3専門エージェントからなるフレームワークを用い、フィードバックに基づき協調的にコード生成を行う。
- Data and results: GPT-4構成でHumanEval 96.3%、MBPP 91.8% pass@1を報告。原著記載の総token overheadはそれぞれ56.9K、66.3Kで、比較法の138.2K、206.5Kと対比する。
- Novelty: プログラマー、テスト設計者、テスト実行者の専門エージェントによる多層的な協調システムを構築した点。
- Limitations: 編者の注意: 生成・test・修正を内部で反復したsystemのpass@1であり、単一回生成の値ではない。自動生成testの十分性と実repositoryでの保守・securityは別問題である。

### Paper: Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training
- Source: arXiv
- Canonical ID: arxiv:2401.05566
- Publication date: 2024-01-10
- URL: https://arxiv.org/abs/2401.05566
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LLMは安全訓練でも維持される欺瞞的振る舞いを学習可能である。
- Objective: 現在の最先端の安全訓練技術で、AIが学習した欺瞞的な戦略を検出・除去できるか？
- Methods: 年号によるプロンプト変更に基づき、モデルに脆弱なコードを挿入するバックドア挙動を訓練し、SFT, RL, 敵対的訓練でテストした。
- Data and results: 標準的な安全訓練技術では、このバックドア挙動は持続的に維持され、特に大規模モデルや思考連鎖を用いる場合に顕著であった。
- Novelty: 意図的に作ったbackdoorが安全訓練後も残り、一部の敵対的学習でtrigger識別を高めて隠れる場合を示す。
- Limitations: 著者はproof-of-conceptとして欺瞞的挙動を作成している。編者の注意: 自然発生したすべてのLLMが同じ策略を持つ証拠ではなく、安全訓練が常に失敗すると結論するものでもない。

### Paper: AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents
- Source: arXiv
- Canonical ID: arxiv:2401.13178
- Publication date: 2024-01-24
- URL: https://arxiv.org/abs/2401.13178
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: AgentBoardは、LLMエージェントの多段階評価のための包括的なベンチマークとフレームワークである。
- Objective: 多様なシナリオにおけるエージェント性能を統一的に評価する課題に取り組むこと。
- Methods: AgentBoardは、進捗率を捉える指標と多角的な分析が可能なツールキットを提供する。
- Data and results: 最終成功率に加えて、途中の達成を追う細粒度progress rateと分析toolkitを提示する。要旨にはtask別の性能値や既存評価法との定量差はない。
- Novelty: プロセス中の詳細な進捗度を測定する「fine-grained progress rate metric」を提供した点。
- Limitations: 編者の注意: 進捗の指標は最終的な正しい完了や安全性そのものではない。要旨では進捗の採点規則・失敗ごとの内訳が分からず、その尺度を解釈して比較する必要がある。

### Paper: VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks
- Source: arXiv
- Canonical ID: arxiv:2401.13649
- Publication date: 2024-01-24
- URL: https://arxiv.org/abs/2401.13649
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 画像を見なければ解けないWeb taskで、multimodal agentを測るVisualWebArena。
- Objective: text中心の評価では見落とす視覚的groundingを、現実的なWeb実行で調べる。
- Methods: image-textの理解、指示解釈、site操作が必要なtaskを構成し、text-onlyとmultimodalの上位agentを定量・定性比較する。
- Data and results: text-only agentの限界と、multimodal agentにも残る能力gapを報告。要旨にはtask数や成功率の具体値はない。
- Novelty: 画像情報が不可欠なtaskを明示的に含め、視覚model追加の効果を実行taskで評価する。
- Limitations: 編者の注意: imageを入力できることと正しいGUI操作は別能力である。選定環境の成果を任意siteの操作や実務安全性の保証へ一般化しない。

### Paper: Corrective Retrieval Augmented Generation
- Source: arXiv
- Canonical ID: arxiv:2401.15884
- Publication date: 2024-01-29
- URL: https://arxiv.org/abs/2401.15884
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 取得文書の品質評価に応じて検索・再構成を変えるCorrective RAGを提案する。
- Objective: retrievalが誤ったときに、無関係文書へ依存する生成を減らす。
- Methods: 軽量retrieval evaluatorのconfidenceで知識取得actionを選び、必要に応じWeb検索を追加する。文書を分解・再構成して重要情報へ絞る。
- Data and results: 短文・長文生成の四datasetで既存RAGの性能を大きく改善と報告。要旨にtask別score・検索費用の数値はない。
- Novelty: 検索結果を固定して生成するのではなく、品質判定を次の検索行動に接続する補正段階を設ける。
- Limitations: 編者の注意: evaluatorとWeb sourceも誤りを持ち得る。plug-and-playは適用形式の説明で、全RAG構成への一律改善や、幻覚の完全な解消の保証ではない。

### Paper: ReGAL: Refactoring Programs to Discover Generalizable Abstractions
- Source: arXiv
- Canonical ID: arxiv:2401.16467
- Publication date: 2024-01-29
- URL: https://arxiv.org/abs/2401.16467
- read_level: full_text
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ReGALは、コードのリファクタリングを通じて再利用可能な抽象化を学習する手法である。
- Objective: LLMが有用な抽象化を開発するために必要なグローバルビューの欠如という課題を解決すること。
- Methods: ReGALは勾配フリーの手法を用い、既存プログラムから繰り返し検証・洗練しながらライブラリを構築する。
- Data and results: CodeLlama-13BでLOGO 45.6→57.1%、Date 42.8→68.9%、TextCraft 18.8→26.9%（3seed）。v2はMATH・TabMWPも評価し、例えばTabMWPの同modelは29.1→27.9%で、全設定で改善するわけではない。
- Novelty: 本手法はコードのリファクタリングを通じて再利用可能な抽象化を学習し、LLMの能力を底上げすることを提案した点にある。
- Limitations: 著者はcode関数が動的環境では神経policyより柔軟性に欠け、全domain・全例に有用な抽象があるわけではないと述べる。外部先行法とはICL等の方法差があり、同条件のprimitive baselineを主比較とする。

本文の照合箇所: [4.2 比較条件、5/Table 1、7 Limitations](https://arxiv.org/html/2401.16467v2)。

### Paper: RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval
- Source: arXiv
- Canonical ID: arxiv:2401.18059
- Publication date: 2024-01-31
- URL: https://arxiv.org/abs/2401.18059
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 文書chunkを再帰的にまとめたtreeから、複数抽象度の情報を検索するRAPTOR。
- Objective: 短い連続chunkだけの検索で長文全体の文脈を捉えにくい問題を改善する。
- Methods: chunkをembedding・cluster・要約し、bottom-upのtreeを構築。推論時に異なる要約levelから取得し、長文QA等で従来RAGと比較する。
- Data and results: 再帰要約検索で複数taskを改善し、GPT-4との組合せでQuALITYの従来best accuracyから絶対20 percentage points改善と要旨は報告する。
- Novelty: 元chunkの近傍検索に加え、文書をまたぐ階層的要約を検索対象に含める。
- Limitations: 編者の注意: 要約treeの構築費用と、抽象化で根拠・細部が失われる可能性を別途評価する。20pointは指定benchmark・構成での値で全RAGの改善幅ではない。

### Paper: RAG-Fusion: a New Take on Retrieval-Augmented Generation
- Source: arXiv
- Canonical ID: arxiv:2402.03367
- Publication date: 2024-01-31
- URL: https://arxiv.org/abs/2402.03367
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: RAG-Fusionは、複数のクエリ生成と再ランキングにより、より正確で包括的な情報提供を可能にする手法である。
- Objective: 製品情報を迅速に取得するニーズに対し、RAG-Fusionが有効な代替手段となるかを評価すること。
- Methods: RAG-Fusionを用いて、複数のクエリを生成し、それらをReciprocal Rank Fusion (RRF)で再ランキングして文書とスコアを融合させた。
- Data and results: Infineonの製品情報取得の場面で、accuracy・関連性・包括性を手動評価し、多queryで内容が充実する例を報告。要旨にsample数や数値比較はない。
- Novelty: 本研究は、複数のクエリ生成とReciprocal Rank Fusion (RRF)の組み合わせによる情報検索の高度化を示した点にある。
- Limitations: 著者は生成queryの関連性が不足するとtopicから逸脱する回答があると報告する。編者の注意: 製品情報の事例評価で、全RAG用途への優越を確立したものではない。

### Paper: CodeAgent: Autonomous Communicative Agents for Code Review
- Source: arXiv
- Canonical ID: arxiv:2402.02172
- Publication date: 2024-02-03
- URL: https://arxiv.org/abs/2402.02172
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 複数のcode review agentにQA-Checkerを加え、元のreview質問への適合を監督する。
- Objective: 単一入出力modelでは難しい協調的なcode reviewを自動化する。
- Methods: commit messageとの不一致、脆弱性導入、style順守、修正提案の四taskを評価し、supervisory agentが各agentの寄与を確認する。
- Data and results: 四つのreview taskで有効性と当時の先端性能を報告し、data・codeを公開。要旨にmetric別scoreはない。
- Novelty: role分担だけでなく、初期review目的へ議論を戻す監督componentを組み込む。
- Limitations: 編者の注意: QA-Checkerによる監督は脆弱性不存在やreview完全性の証明ではない。四taskの範囲・判定基準・追加推論費用を揃えて比較する必要がある。

### Paper: AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Calls
- Source: arXiv
- Canonical ID: arxiv:2402.04253
- Publication date: 2024-02-06
- URL: https://arxiv.org/abs/2402.04253
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 大規模なAPI利用に特化した自己内省型エージェントAnyToolを提案する。
- Objective: ユーザーのクエリ解決のために、広範なAPI群から最適なツール選択と実行を行う方法論を確立すること。
- Methods: 階層的なAPIリトリーバー、ソルバー、および自己内省機構を統合し、GPT-4の関数呼び出し機能を利用して構築した。
- Data and results: AnyToolは、既存のベースラインであるToolLLMに対し、ToolBenchで平均パス率が+35.4%向上するなど優れた性能を示した。
- Novelty: APIリトリーバーに階層構造を導入し、自己内省機構により初期解が不適切だった場合の再試行メカニズムを組み込んだ点。
- Limitations: 著者は従来評価がpass率を過大にする問題を指摘し、AnyToolBenchを追加する。編者の注意: 解決可能なAPI部分集合が存在すると仮定する。要旨の+35.4%は表現を保持し、相対率かpoint差かを独断で変換しない。

### Paper: An Interactive Agent Foundation Model
- Source: arXiv
- Canonical ID: arxiv:2402.05929
- Publication date: 2024-02-08
- URL: https://arxiv.org/abs/2402.05929
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 本研究は、多様なタスクに対応する対話型エージェント基盤モデルを提案した。
- Objective: AIシステムを静的なモデルから動的なエージェントベースのシステムへ移行させるための手法を探る。
- Methods: 視覚マスク自己エンコーダ、言語モデリング、次行動予測を含む多様な事前学習戦略を統合する訓練パラダイムを用いた。
- Data and results: robotics、gaming、healthcareの3分野で文脈に関係した出力を示す。要旨は定性的な主張であり、task別のscore・sample数・対照法の数値を記さない。
- Novelty: 本アプローチは、ロボットシーケンスや大規模動画データなど多様なソースを活用する汎用性が強みである。
- Limitations: 編者の注意: 三分野での出力例は汎用性の検証の一部であり、未見の任意taskの達成や臨床有効性を保証しない。healthcareの患者転帰や前向き検証は要旨から確認できない。

### Paper: WebLINX: Real-World Website Navigation with Multi-Turn Dialogue
- Source: arXiv
- Canonical ID: arxiv:2402.05930
- Publication date: 2024-02-08
- URL: https://arxiv.org/abs/2402.05930
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 複数turnのuser指示に従う実Web navigationを、大規模な実演軌跡で評価するWebLINX。
- Objective: 会話の進行に応じて変わる指示と巨大なWeb入力をagentが扱えるかを調べる。
- Methods: 150超site・2,300専門家実演・100,000相互作用を収集。関連elementをrankしてHTMLを絞り、screenshot・行動履歴と併せ各modelを評価する。
- Data and results: 小さな微調整decoderが最良zero-shot LMや一部の大きな微調整multimodal modelを上回るが、全微調整modelが未知siteへの汎化に苦戦すると報告。
- Novelty: 単発指示から会話型Web navigationへ拡張し、入力選別と人の行動再現を共通dataで比較する。
- Limitations: 著者は未知site汎化の難しさを明記する。編者の注意: 人の行動再現を測る設定と、live taskの最終成功率は区別し、微調整ありとzero-shotのdata差も考慮する。

### Paper: WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?
- Source: arXiv
- Canonical ID: arxiv:2403.07718
- Publication date: 2024-03-12
- URL: https://arxiv.org/abs/2403.07718
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: ServiceNow上の33taskで企業Web操作を測り、BrowserGymを提供するWorkArena。
- Objective: 一般的な知識労働の日常taskを、browser agentがどの程度遂行できるか調べる。
- Methods: remote-hostedのServiceNow benchmarkと、豊富なaction・multimodal観測を備えるBrowserGymを構築し、公開・閉鎖LM agentを比較する。
- Data and results: 完全自動化には大きなgapがあり、公開・閉鎖LMの性能差も大きいと報告。要旨に各modelの成功率はない。
- Novelty: 企業softwareの日常操作を共通の評価対象とし、agent設計・評価を行う環境と併せて提供する。
- Limitations: 編者の注意: 原著の33taskはWorkArena++の682taskとは別。単一platformでの結果を、全企業systemや現場の生産性効果にそのまま一般化しない。

### Paper: RAFT: Adapting Language Model to Domain Specific RAG
- Source: arXiv
- Canonical ID: arxiv:2403.10131
- Publication date: 2024-03-15
- URL: https://arxiv.org/abs/2403.10131
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: RAFTは、ドメイン特化型RAGのための新しい学習レシピを提案する。
- Objective: open-bookの特定domain QAで、検索文書から有用な根拠を選びdistractorを無視する能力をpost-trainingで高める。
- Methods: 質問と関連・無関連の検索文書を与え、関連箇所の逐語引用とCoT型応答を学習する。PubMed、HotpotQA、Gorillaでdomain内RAGを評価する。
- Data and results: PubMed, HotpotQA, Gorillaデータセットで一貫して性能が向上し、ドメイン特化型RAGの改善策となる。
- Novelty: 関連文書から質問への回答に必要な正確な引用を伴う学習プロセスを導入した点。
- Limitations: 編者の注意: in-domainのopen-book設定での改善であり、未知domainへのzero-shot転移の保証ではない。引用を生成する学習と、実際の引用の正確性・sourceの信頼性は別途評価する。

### Paper: Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity
- Source: arXiv
- Canonical ID: arxiv:2403.14403
- Publication date: 2024-03-21
- URL: https://arxiv.org/abs/2403.14403
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 質問の複雑さを予測し、検索なし・単回・反復RAGを選ぶAdaptive-RAG。
- Objective: 単純な質問の余計な計算と、複雑な質問への検索不足を両方減らす。
- Methods: modelの予測結果とdatasetの性質から自動labelを集め、小LM classifierでquery複雑度を予測する。三種の回答戦略を動的に切り替える。
- Data and results: 複数難度を含むopen-domain QAで、適応検索を含むbaselineに対して効率とaccuracyを改善すると報告。要旨に具体値はない。
- Novelty: 検索の有無だけでなく、必要な検索の深さを小型classifierのroute選択として学習する。
- Limitations: 編者の注意: classifierの誤routeと自動labelのbiasに依存する。queryの見かけの複雑さが必要な根拠量を常に正しく表す保証や、全domainの最適routingではない。

### Paper: AutoCodeRover: Autonomous Program Improvement
- Source: arXiv
- Canonical ID: arxiv:2404.05427
- Publication date: 2024-04-08
- URL: https://arxiv.org/abs/2404.05427
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: AutoCodeRoverは、LLMとコード検索を組み合わせた自動プログラム改善手法である。
- Objective: ソフトウェアのバグ修正や機能追加といったプログラム改善を自律的に達成する方法を探る。
- Methods: ASTのclass/method構造を使った反復検索で修正contextを絞る。test suiteが使える場合はspectrum-based fault localizationも組み合わせる。
- Data and results: 実GitHub issue 300件のSWE-bench Liteで19%解決、平均0.43米ドルと報告する。比較は原著時点のbaselineと費用条件に基づく。
- Novelty: ソフトウェアプロジェクトをファイル群としてではなく、プログラム構造（AST）として扱う点に新規性がある。
- Limitations: 著者はtestを使うfault localizationをtest suiteが利用可能な場合に限定する。編者の注意: 19%はLite版であり、SWE-bench全体の成功率や現在の価格ではない。

### Paper: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments
- Source: arXiv
- Canonical ID: arxiv:2404.07972
- Publication date: 2024-04-11
- URL: https://arxiv.org/abs/2404.07972
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 実Web・desktop appとfile操作を含む369taskを、実行結果で採点するOSWorld。
- Objective: 特定appに限られないcomputer agentの実務能力を、再現可能な環境で調べる。
- Methods: 初期状態とtaskごとの実行評価scriptを備え、複数OS上の実環境を構成。app横断workflowでLLM/VLM agentと人間を比較する。
- Data and results: 原著では人間72.36%超に対しbest model12.24%成功を報告し、GUI groundingと操作知識に主な問題を見いだす。
- Novelty: text回答だけでなく、実computer内での状態変化をtask固有のscriptで評価する統合基盤を提供する。
- Limitations: 編者の注意: OS対応の範囲と、各OSで同数・同条件のtaskを評価したことは同義ではない。数値は原著時点の設定で、現在のagent一般の成功率ではない。

### Paper: RAGCache: Efficient Knowledge Caching for Retrieval-Augmented Generation
- Source: arXiv
- Canonical ID: arxiv:2404.12457
- Publication date: 2024-04-18
- URL: https://arxiv.org/abs/2404.12457
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 取得知識の中間状態をGPU・host階層にcacheし、RAGの待ち時間とthroughputを改善する。
- Objective: 知識を長いcontextへ注入するRAGの計算・memory費用を減らす。
- Methods: 中間状態をknowledge treeへ整理し、LLM推論と検索patternを考慮する置換policyでcacheする。retrievalとinferenceも動的に重ね、vLLM/Faiss上で評価する。
- Data and results: vLLMとFaissの統合baselineに対し、TTFTを最大4倍短縮、throughputを最大2.1倍に改善と報告。
- Novelty: 回答textだけでなく、取得知識の推論中間状態をRAG専用の階層cacheとして再利用する。
- Limitations: 編者の注意: 最大値はworkload・hit率・memory条件に依存する。TTFT短縮と全回答完了時間は別で、検索・生成の正確性を改善する手法とは異なる。

### Paper: From Local to Global: A Graph RAG Approach to Query-Focused Summarization
- Source: arXiv
- Canonical ID: arxiv:2404.16130
- Publication date: 2024-04-24
- URL: https://arxiv.org/abs/2404.16130
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: entity graphとcommunity要約で、corpus全体を問うglobalな質問へ答えるGraphRAG。
- Objective: 個別の根拠取得が中心のRAGと、大量文書のquery-focused summarizationの長所を結ぶ。
- Methods: LLMでentity knowledge graphを作り、関連entityのcommunity要約を事前生成する。質問ごとに各要約から部分回答を作り、統合回答へまとめる。
- Data and results: 約100万token規模のdatasetのglobal sensemaking質問で、通常RAGより回答の包括性・多様性が大きく改善と報告。要旨に数値はない。
- Novelty: 短い関連箇所の取得から、corpus全体の構造を事前要約し集約する検索・生成へ拡張する。
- Limitations: 編者の注意: 主評価はglobalな質問であり、局所的なfact QAの全てに勝る意味ではない。graph・要約の事前生成費用や抽出誤りを含めて比較する必要がある。

### Paper: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
- Source: arXiv
- Canonical ID: arxiv:2405.15793
- Publication date: 2024-05-06
- URL: https://arxiv.org/abs/2405.15793
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: LMエージェントの性能向上のため、専用のインターフェースを提案する。
- Objective: 言語モデルエージェントがソフトウェア工学タスクを遂行する際のインターフェース設計の影響を調査すること。
- Methods: SWE-agentというシステムを用い、カスタムのエージェント・コンピューターインターフェース（ACI）を構築し、コード作成やリポジトリ操作を行う。
- Data and results: SWE-benchとHumanEvalFixでSOTAを達成し、それぞれpass@1率12.5%、87.7%を記録した。
- Novelty: エージェントの能力を引き出すため、専用のACIを導入し、自律的なコンピューター利用を可能にした点。
- Limitations: 編者の注意: 12.5%はSWE-bench、87.7%はHumanEvalFixという別taskのpass@1である。SWE-bench Liteや後年のVerified版の値と直接比較せず、model・interface・実行予算を揃える。

### Paper: Octo: An Open-Source Generalist Robot Policy
- Source: arXiv
- Canonical ID: arxiv:2405.12213
- Publication date: 2024-05-20
- URL: https://arxiv.org/abs/2405.12213
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 多様なrobot経験で事前学習し、新しい観測・action空間へ適応する公開policy Octo。
- Objective: 新robotごとの一からの学習を減らし、sensorや制御形式が異なる設定へ効率よく移す。
- Methods: Open X-Embodimentの800,000軌跡でTransformer policyを学習。言語またはgoal画像で指示し、九platformで適応と構造・dataのablationを評価する。
- Data and results: 新しい観測・action空間へ有効に微調整でき、標準consumer GPUで数時間の適応が可能と報告。要旨に全platform共通の成功率はない。
- Novelty: 特定robot用policyだけでなく、異なる入力・出力へ微調整しやすい汎用初期値を公開する。
- Limitations: 編者の注意: generalistは新しい全robotへの無調整成功を意味しない。in-domain dataとfine-tuningの条件、platformごとの評価taskの違いを確認する必要がある。

### Paper: AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents
- Source: arXiv
- Canonical ID: arxiv:2405.14573
- Publication date: 2024-05-23
- URL: https://arxiv.org/abs/2405.14573
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 20の実Android appでtaskを動的構成し、再現可能な状態評価を行うAndroidWorld。
- Objective: 固定testだけでは見えないtask変動への頑健性とmobile操作能力を評価する。
- Methods: 116のparameter化taskに初期化・成功判定・後処理を実装し、状態を変更・検査する。agent比較、desktop agentのmobile適用、task variationを評価する。
- Data and results: best agentは30.6%成功。desktop由来agentはmobileで劣り、task変形でも成績が大きく変わると報告する。
- Novelty: 自然言語の表現やtask parameterを変えられる動的構成と、device状態による採点を組み合わせる。
- Limitations: 編者の注意: 無制限に生成可能なのは設計されたtask族のinstanceで、全app機能や全user意図の網羅ではない。30.6%は原著の評価構成に関する値である。

### Paper: OpenVLA: An Open-Source Vision-Language-Action Model
- Source: arXiv
- Canonical ID: arxiv:2406.09246
- Publication date: 2024-06-13
- URL: https://arxiv.org/abs/2406.09246
- read_level: full_text
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 7Bの公開VLAでrobot制御と効率的な適応・量子化を調べるOpenVLA。
- Objective: 閉鎖VLAへの依存と、新robotへ微調整する費用を減らす。
- Methods: Llama 2とDINOv2/SigLIP特徴を組み、970,000実演で学習。一般操作、LoRA、低精度推論を評価する。
- Data and results: 29task等でRT-2-Xより成功率が絶対16.5point高いと要旨は報告。別の縮小構成の8task/80rolloutではBF16 71.3%、int4 71.9%、int8 58.1%で、int8の低速化が制御に影響した。
- Novelty: 公開VLAの重み・学習基盤と、適応・推論効率を実robot評価まで結び付ける。
- Limitations: 著者は単一画像入力、高周波制御・器用さ、通常90%未満の信頼性を課題とする。量子化実験は小さいdata混合・SigLIPのみの構成で、主modelと同一条件ではない。

本文の照合箇所: [5.3 脚注4、5.4/Table 2、6 Limitations](https://arxiv.org/html/2406.09246v3)。

### Paper: $τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains
- Source: arXiv
- Canonical ID: arxiv:2406.12045
- Publication date: 2024-06-17
- URL: https://arxiv.org/abs/2406.12045
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 本研究は、実世界でのエージェントの性能を評価する新しいベンチマーク$ au$-benchを提案した。
- Objective: 言語エージェントが人間ユーザーとの対話やドメイン固有のルールに従う能力を評価するためのベンチマークが必要である。
- Methods: シミュレーションされたユーザーとAPIツール、ポリシーガイドラインを持つエージェント間の動的会話を模倣し、終了時のデータベース状態と比較する。
- Data and results: gpt-4o等のfunction-calling agentでも成功率50%未満、retailではpass^8が25%未満と報告。単発成功に加え、反復試行での一貫した成功の難しさを示す。
- Novelty: 本研究は、ユーザーとの対話とドメイン固有ルール遵守を評価する$ au$-benchという新しいベンチマークを提案した。
- Limitations: 編者の注意: userはLLMによるsimulationであり実利用者試験ではない。pass^kは複数試行での信頼性の尺度で、k候補から一つ成功を選ぶpass@kと混同しない。

### Paper: Agentless: Demystifying LLM-based Software Engineering Agents
- Source: arXiv
- Canonical ID: arxiv:2407.01489
- Publication date: 2024-07-01
- URL: https://arxiv.org/abs/2407.01489
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 修正箇所の特定・修復・patch検証を固定手順で行い、複雑なagentに対する強いbaselineを示す。
- Objective: 高度な自律型LLMエージェントは本当に必要かという疑問に答えること。
- Methods: Agentlessとして、局所化、修復、パッチ検証の三段階プロセスを採用し、複雑なツール使用や将来行動決定を排除した。
- Data and results: SWE-bench Liteで32.00%（96件）の修正と0.70ドルの費用を報告し、当時の公開agentと比較。問題文に正解patchがある例や情報不足等を調べ、Lite-Sを作る。
- Novelty: 自律型エージェントに頼らず、単純で解釈可能な三段階プロセスを用いるアプローチを提案した点。
- Limitations: 著者はSWE-bench Liteの問題文に正解漏出や情報不足・誤誘導がある例を報告する。編者の注意: 最高という主張は当時の比較対象であり、固定手順があらゆる開発taskで勝る意味ではない。

### Paper: WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks
- Source: arXiv
- Canonical ID: arxiv:2407.05291
- Publication date: 2024-07-07
- URL: https://arxiv.org/abs/2407.05291
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 知識労働の複合workflowを682taskで測るWorkArena++を提案する。
- Objective: 企業環境で計画・推論が実際の自律task解決へつながるかを評価する。
- Methods: 計画、論理・算術、検索、文脈理解を要するtaskを構成し、LLM・VLM・人間を比較。正解付き観測・行動traceを大量生成する機構も提供する。
- Data and results: 上位modelにも職場assistantとしての課題が残ると報告。682taskと訓練用trace生成機構が成果で、要旨にmodel別成功率はない。
- Novelty: 単純な画面操作から、複数能力を組み合わせる企業のworkflowへ評価を進める。
- Limitations: 編者の注意: 現実を模したbenchmarkと実企業での生産性・誤操作の影響は異なる。生成された正解軌跡を、唯一の許される手順と解釈しない。

### Paper: ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities
- Source: arXiv
- Canonical ID: arxiv:2408.04682
- Publication date: 2024-08-08
- URL: https://arxiv.org/abs/2408.04682
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: tool間の状態依存と対話中の実行を含めるToolSandboxで、従来評価の抜けを補う。
- Objective: 単発・stateless APIや固定対話軌跡では測れない、状態を持つtool利用を評価する。
- Methods: stateful実行、暗黙のtool間依存、on-policy user simulator、任意軌跡の中間・最終milestone評価を統合する。
- Data and results: 公開modelとproprietary modelに性能差を報告し、状態依存、canonicalization、情報不足のtaskは上位modelにも難しいと示す。要旨にtask別scoreはない。
- Novelty: 正しい単一呼出だけでなく、状態と情報が変わる対話・tool系列を評価単位にする。
- Limitations: 編者の注意: userはsimulationで、実利用者への有効性試験ではない。milestone達成と最終成功・安全性は別尺度であり、評価taskの状態設計にも依存する。

### Paper: LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory
- Source: arXiv
- Canonical ID: arxiv:2410.10813
- Publication date: 2024-10-14
- URL: https://arxiv.org/abs/2410.10813
- read_level: full_text
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: 長期対話記憶の五能力を500問で測り、索引・検索・読み取りの設計を分解する。
- Objective: 情報抽出、複数session推論、時間推論、知識更新、棄権を長い履歴で評価する。
- Methods: 編集した模擬根拠sessionと背景履歴を組み、QAをGPT-4oで採点、検索をRecall/NDCGで評価する。索引分解・key拡張・時間queryを比較する。
- Data and results: v1のGPT-4oでは根拠sessionのみaccuracy .870に対し約115k token履歴で.606、相対30.3%低下。全履歴を持つことと必要な記憶を使えることの差を示す。
- Novelty: 長期記憶を保存容量だけでなく、索引・検索・回答という段階別の制御点として評価する。
- Limitations: 編者の注意: 30.3%は相対低下で30.3pointではない。QAはLLM judge、商用systemは別の97問・短い履歴で、両評価を同条件とみなさない。

本文の照合箇所: [3.3–3.5、Figure 4、4.1](https://arxiv.org/html/2410.10813v1)。

<!-- PAPER_IDS -->
arxiv:1410.3916
arxiv:1503.08895
arxiv:1603.01417
arxiv:1606.01540
arxiv:1606.03126
arxiv:1707.03389
arxiv:1806.01261
arxiv:1806.11532
arxiv:1810.08272
arxiv:1911.00172
arxiv:2002.08909
arxiv:2004.04906
arxiv:2004.12832
arxiv:2005.11401
arxiv:2006.08381
arxiv:2007.12770
arxiv:2010.03768
arxiv:2104.07567
arxiv:2105.13231
arxiv:2106.01345
arxiv:2112.04426
arxiv:2112.09332
arxiv:2203.07814
arxiv:2203.07540
arxiv:2204.01691
arxiv:2207.01206
arxiv:2207.05608
arxiv:2209.07753
arxiv:2209.11302
arxiv:2210.03629
arxiv:2212.06817
arxiv:2302.04761
arxiv:2303.03378
arxiv:2303.04137
arxiv:2303.11366
arxiv:2303.17580
arxiv:2303.17760
arxiv:2304.01904
arxiv:2304.03442
arxiv:2304.05128
arxiv:2304.05376
arxiv:2304.08244
arxiv:2304.12244
arxiv:2305.06983
arxiv:2305.10250
arxiv:2305.11554
arxiv:2305.14325
arxiv:2305.18323
arxiv:2305.14992
arxiv:2305.15334
arxiv:2305.16291
arxiv:2305.16504
arxiv:2306.03314
arxiv:2306.05301
arxiv:2306.06070
arxiv:2306.06624
arxiv:2306.13304
arxiv:2307.02477
arxiv:2307.03172
arxiv:2307.05973
arxiv:2307.07924
arxiv:2307.13854
arxiv:2307.15818
arxiv:2307.16789
arxiv:2308.00352
arxiv:2308.02151
arxiv:2308.03688
arxiv:2308.04026
arxiv:2308.08155
arxiv:2308.10848
arxiv:2308.11432
arxiv:2309.00986
arxiv:2309.07864
arxiv:2309.07870
arxiv:2309.15217
arxiv:2310.03714
arxiv:2310.04406
arxiv:2310.06770
arxiv:2310.08319
arxiv:2310.08560
arxiv:2310.08864
arxiv:2310.10634
arxiv:2310.11511
arxiv:2312.03815
arxiv:2312.13010
arxiv:2401.05566
arxiv:2401.13178
arxiv:2401.13649
arxiv:2401.15884
arxiv:2401.16467
arxiv:2401.18059
arxiv:2402.03367
arxiv:2402.02172
arxiv:2402.04253
arxiv:2402.05929
arxiv:2402.05930
arxiv:2403.07718
arxiv:2403.10131
arxiv:2403.14403
arxiv:2404.05427
arxiv:2404.07972
arxiv:2404.12457
arxiv:2404.16130
arxiv:2405.15793
arxiv:2405.12213
arxiv:2405.14573
arxiv:2406.09246
arxiv:2406.12045
arxiv:2407.01489
arxiv:2407.05291
arxiv:2408.04682
arxiv:2410.10813
<!-- /PAPER_IDS -->
