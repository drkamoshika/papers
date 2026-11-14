# 基礎文献 — エージェント・検索・記憶・協調

> schema_version: 1
> report_date: 2026-11-14

## ダイジェスト

選定112件中、以下は原著照合・編集確認を終えた38件。選定リストだけの論文を完成済み件数には含めない。原著要旨までの記述と本文確認を区別し、Limitationsの「編者の注意」は著者の自己申告と区別する。

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
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: WebArenaは、現実的なウェブタスク実行のための環境を提供し、自律エージェントの評価を可能にする。
- Objective: 自然言語コマンドによる日常タスク管理を行う自律エージェントの実世界での性能評価を目指す。
- Methods: Eコマース、ソーシャルフォーラムなど4分野の機能的ウェブサイトを持つ環境を構築し、ツールや外部知識ベースで強化した。
- Data and results: GPT-4ベースのエージェントは複雑なタスクで14.41%の成功率に留まり、人間の78.24%から大きく乖離した。
- Novelty: 本環境は、現実的なウェブサイトを模倣し、長期かつ多様なベンチマークタスクを提供することで新規性を確立した。
- Limitations: 編者の注意: 14.41%対78.24%は原著のbest GPT-4 agentと人間の比較であり、現在のagent一般の値ではない。機能を再現した管理下のWeb環境で、任意のlive website全体を評価したものではない。

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

### Paper: MemGPT: Towards LLMs as Operating Systems
- Source: arXiv
- Canonical ID: arxiv:2310.08560
- Publication date: 2023-10-12
- URL: https://arxiv.org/abs/2310.08560
- read_level: abstract
- Tags: 基礎文献, エージェント・検索・記憶・協調
- Summary: MemGPTは、LLMのコンテキスト制限を克服するOSのようなシステムである。
- Objective: LLMの限られたコンテキストウィンドウを超える長期的な情報処理を可能にする方法論を探求すること。
- Methods: 高速・低速のmemory階層間で情報を移すvirtual context管理と、割込みによる制御を導入する。文書分析と複数session対話で評価する。
- Data and results: MemGPTは、基盤となるLLMのコンテキストウィンドウを超える大規模文書分析や多セッションチャットでの利用が可能であることを示した。
- Novelty: 従来のOSの階層的メモリシステムから着想を得て、LLMに仮想的な大容量メモリ機能を持たせた点。
- Limitations: 編者の注意: 基盤LLMのcontext窓そのものを無限化する方法ではなく、情報の移動・保存・検索で補う。検索されない細部の保持や無限長会話での完全記憶を保証しない。

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

<!-- PAPER_IDS -->
arxiv:1410.3916
arxiv:1503.08895
arxiv:1603.01417
arxiv:1606.03126
arxiv:1911.00172
arxiv:2002.08909
arxiv:2004.04906
arxiv:2004.12832
arxiv:2005.11401
arxiv:2104.07567
arxiv:2112.04426
arxiv:2210.03629
arxiv:2302.04761
arxiv:2303.11366
arxiv:2303.17580
arxiv:2304.03442
arxiv:2304.05376
arxiv:2305.14325
arxiv:2305.18323
arxiv:2305.14992
arxiv:2305.16291
arxiv:2305.16504
arxiv:2307.02477
arxiv:2307.03172
arxiv:2307.07924
arxiv:2307.13854
arxiv:2307.16789
arxiv:2308.00352
arxiv:2308.03688
arxiv:2308.04026
arxiv:2308.08155
arxiv:2308.11432
arxiv:2310.08560
arxiv:2312.03815
arxiv:2401.13178
arxiv:2404.05427
arxiv:2405.15793
arxiv:2407.01489
<!-- /PAPER_IDS -->
