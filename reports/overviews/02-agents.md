# エージェント・検索・記憶・協調：基礎から現在へのレビュー

レビュー日: 2026-11-16。収録論文の公開日上限: 2026-11-12。

外部知識を検索する仕組みから、道具を使って環境を変え、経験を保存し、複数の役割を調整する仕組みへ進んだ。現在の境界は、局所的な成功を長い仕事全体の整合性へつなげられるかにある。

収録基礎文献 112件／本レビューで引用する基礎文献 18件・新着論文 7件。分野横断の文献を含み、件数は引用IDの集合から計算。

## いま何ができるか

検索付き回答、コード・Web操作、経験の再利用、複数エージェントによる調査を特定環境で実行。

任意の仕事を無監督で最後まで納品し、権限・費用・安全性も守れるとはいえない。 [1](https://arxiv.org/abs/2210.03629) [2](https://arxiv.org/abs/2611.17041) [3](https://arxiv.org/abs/2611.03412)

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

## 直近研究の位置づけ

### LEAD-RL：調査の貢献を評価する

5ベンチマーク・2モデル系列で評価。BrowseCompで共有チーム報酬方式より正答率2.49ポイント増、実行のクリティカルパスに沿った費用24.5%減。実組織の調査全体の効率を直接測った結果ではない。 [2](https://arxiv.org/abs/2611.17041)

### WikiTrace：教訓に原記録を結び付ける

5エージェントベンチマークで、同じ教訓だけを与える対照より良く、記憶による性能悪化も減らしたと報告。要旨に統一した改善率は示されていない。根拠を確認できる記憶という設計が中心である。 [17](https://arxiv.org/abs/2611.14320)

### DeliverBench：仕事全体で見ると限界が残る

11の実務由来プロジェクト・150の下位課題で、7構成の最高成績は最終納品65.0/100、90点を合格条件にした下位課題の合格率50.0%。成果物の誤りが後工程へ持ち越される点を評価に入れている。 [3](https://arxiv.org/abs/2611.03412)

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

## 参考文献と確認範囲

1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — 2022-10-06 / arxiv:2210.03629 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2210.03629)

2. [From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research](https://arxiv.org/abs/2611.17041) — 2026-11-12 / arxiv:2611.17041 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17041) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.17041v1)

3. [DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://arxiv.org/abs/2611.03412) — 2026-11-02 / arxiv:2611.03412 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.03412) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.03412v3)

4. [Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906) — 2020-04-10 / arxiv:2004.04906 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2004.04906)

5. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — 2020-05-22 / arxiv:2005.11401 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2005.11401)

6. [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511) — 2023-10-17 / arxiv:2310.11511 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2310.11511)

7. [Corrective Retrieval Augmented Generation](https://arxiv.org/abs/2401.15884) — 2024-01-29 / arxiv:2401.15884 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2401.15884)

8. [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — 2023-02-09 / arxiv:2302.04761 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2302.04761)

9. [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — 2023-10-10 / arxiv:2310.06770 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2310.06770)

10. [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) — 2023-07-25 / arxiv:2307.13854 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.13854)

11. [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — 2023-03-20 / arxiv:2303.11366 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2303.11366)

12. [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — 2023-05-25 / arxiv:2305.16291 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.16291)

13. [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — 2023-10-12 / arxiv:2310.08560 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2310.08560)

14. [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — 2023-07-06 / arxiv:2307.03172 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.03172)

15. [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) — 2023-08-16 / arxiv:2308.08155 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2308.08155)

16. [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — 2023-02-23 / arxiv:2302.12173 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2302.12173)

17. [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320) — 2026-11-10 / arxiv:2611.14320 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14320) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.14320v1)

18. [CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation](https://arxiv.org/abs/2611.17316) — 2026-11-12 / arxiv:2611.17316 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17316)

19. [Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753) — 2022-09-16 / arxiv:2209.07753 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2209.07753)

20. [ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience](https://arxiv.org/abs/2611.16872) — 2026-11-12 / arxiv:2611.16872 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.16872)

21. [VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](https://arxiv.org/abs/2611.03575) — 2026-11-02 / arxiv:2611.03575 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.03575)

22. [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352) — 2024-06-19 / arxiv:2406.13352 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2406.13352)

23. [Counterfactual Temporal Point Processes](https://arxiv.org/abs/2111.07603) — 2021-11-15 / arxiv:2111.07603 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2111.07603)

24. [Knowing When to Intervene: Causal Evaluation of AI Agents](https://arxiv.org/abs/2611.09792) — 2026-11-06 / arxiv:2611.09792 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.09792)

25. [Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory](https://pubmed.ncbi.nlm.nih.gov/7624455/) — 公開日未確認 / pmid:7624455 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=pmid%3A7624455)

## このレビューの範囲

母集団はこのライブラリの収録論文。全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断的レビューです。

基礎文献・新着論文は収録先の区別です。基礎文献側にも2026年の研究が含まれるため、古さや新しさは個々の公開日で確認できます。

技術の系譜、分野間の接点、次の課題は編者の整理であり、論文間の直接の引用関係や、商用普及の程度を確定するものではありません。

個別論文の確認範囲は要旨または本文の関連箇所です。今回、代表的な22件の一次資料を追加で照合しました。全件の全文再精読や独立再現を意味しません。

実験の数字は論文の報告値です。異なるデータ・分割・指標の数値を統一順位へ変換していません。

[7分野の全体マップ](https://drkamoshika.github.io/papers/?view=map)
