# 言語モデルの学習・推論・効率化：基礎から現在へのレビュー

レビュー日: 2026-11-16。収録論文の公開日上限: 2026-11-12。

汎用の言語表現を、指示に従う生成器へ、さらに計算量を配分して解く推論器へ発展させてきた。現在は、能力だけでなく学習・推論・運用コストを含めて設計する段階にある。

収録基礎文献 101件／本レビューで引用する基礎文献 21件・新着論文 4件。分野横断の文献を含み、件数は引用IDの集合から計算。

## いま何ができるか

少数例での適応、指示に沿う生成、検証器を使う推論、小型化と推論処理の効率化。

長く考えれば必ず正しい、量子化しても全用途で同等、という保証はない。 [1](https://arxiv.org/abs/2005.14165) [2](https://arxiv.org/abs/2611.17320) [3](https://arxiv.org/abs/2611.13410)

## 基礎からの積み上げ

### 分散表現から文脈表現へ

単語の近さをベクトルで扱う段階から、attentionで入力間の関係を計算し、文脈ごとの表現を作る段階へ進んだ。Transformerは現在の多くのモデルの構成上の出発点になる。 [4](https://arxiv.org/abs/1301.3781) [5](https://arxiv.org/abs/1409.0473) [6](https://arxiv.org/abs/1706.03762) [7](https://arxiv.org/abs/1810.04805)

### 事前学習と規模の設計

GPT-3は少数例を文脈に置く適応を示し、スケーリング則とChinchillaはモデル規模だけでなくデータ量・計算量の配分を設計対象にした。これは性能の増加傾向を扱う知見で、個々の回答の正しさを保証する法則ではない。 [1](https://arxiv.org/abs/2005.14165) [8](https://arxiv.org/abs/2001.08361) [9](https://arxiv.org/abs/2203.15556)

### 人間の指示・選好へ合わせる

指示学習と人間のフィードバック、DPOによる選好最適化が、事前学習モデルを利用目的へ合わせる道筋を整えた。選好への適合と、事実性・安全性の達成は別の評価が必要になる。 [10](https://arxiv.org/abs/2109.01652) [11](https://arxiv.org/abs/2203.02155) [12](https://arxiv.org/abs/2305.18290)

### 推論時の探索と実装の最適化

Chain-of-Thought、自己整合性、過程の検証が推論時の計算配分へつながる。一方、LoRA・量子化・FlashAttention・PagedAttentionは、更新パラメータ、メモリ、入出力、バッチ実行の別々のボトルネックを扱う。 [13](https://arxiv.org/abs/2201.11903) [14](https://arxiv.org/abs/2203.11171) [15](https://arxiv.org/abs/2305.20050) [16](https://arxiv.org/abs/2106.09685) [17](https://arxiv.org/abs/2210.17323) [18](https://arxiv.org/abs/2205.14135) [19](https://arxiv.org/abs/2309.06180)

## 到達点・適用条件・残る境界

### 指示に沿う生成と用途適応 — 比較が蓄積

できていること: 共通の事前学習モデルを、少数例や追加学習で要約・質問応答などの用途へ適応できる。

条件: 対象言語・入力長・専門領域を合わせて評価し、検索や外部ツールで不足する知識を補う。

残る境界: 流暢さや指示遵守から、未知事実の正確性や分布外への一般化までは導けない。 [1](https://arxiv.org/abs/2005.14165) [11](https://arxiv.org/abs/2203.02155) [16](https://arxiv.org/abs/2106.09685)

### 計算を追加して推論を改善する — 限定条件で実証

できていること: 複数解候補の探索・再生成と検証により、対象の数学・推論課題の成績を改善できる。

条件: 候補を区別できる検証器と、正答率の増加に見合う追加計算の予算が要る。

残る境界: 検証器が誤れば誤答を選び直す。推論ベンチマークでの改善を、長期業務の完遂能力へそのまま移せない。 [14](https://arxiv.org/abs/2203.11171) [20](https://arxiv.org/abs/2408.03314) [2](https://arxiv.org/abs/2611.17320)

### 小型化してエージェントを動かす — 限定条件で実証

できていること: 重みの低ビット化と教師からの行動修正を組み合わせ、対象エージェント課題で精度低下を抑えられる。

条件: 圧縮後のモデルを実際の行動系列で評価する。単発テキストの誤差だけでは環境との相互作用の失敗を捕まえにくい。

残る境界: 対象のモデル・量子化方式・課題以外で同じ性能差になるとは限らず、学習用教師の費用も残る。 [17](https://arxiv.org/abs/2210.17323) [21](https://arxiv.org/abs/2305.14314) [3](https://arxiv.org/abs/2611.13410)

### 長文・複数利用者の推論を効率化する — 限定条件で実証

できていること: attentionの入出力削減、KVメモリの管理、繰り返し部分の分散再利用で処理時間や収容効率を改善できる。

条件: GPU構成、バッチサイズ、文脈の共有率、通信量を含めたワークロードで測る。

残る境界: 最初のトークンが速くなることと、回答全体の完了時間や正答率が改善することは同じ指標ではない。 [18](https://arxiv.org/abs/2205.14135) [19](https://arxiv.org/abs/2309.06180) [22](https://arxiv.org/abs/2611.09474)

## 直近研究の位置づけ

### DiVR：どこを再生成するかを学ぶ

微調整済みLLaDA-8B-Baseの5推論ベンチマークで、平均正答率35.3%から43.4%。greedyの1.9〜3.5倍の計算を使う。生成器を変えずに検証器を改善する方向だが、対象課題内の結果として読む。 [2](https://arxiv.org/abs/2611.17320)

### SteerDistill：圧縮後の行動を修正する

5エージェントベンチマーク・3モデルで、W4A16の最良比較法より平均1.67〜2.18ポイント改善し、BF16との差を1ポイント以内にしたと報告。圧縮誤差を行動上の失敗から修復する。 [3](https://arxiv.org/abs/2611.13410)

### Nebula：再利用をクラスタ全体で管理する

4モデル・4種のRAG／エージェント負荷で、最良比較法に対する最初のトークンまでの待ち時間の中央値を平均61.4%削減。長い文脈の共有パターンを実装の設計へ取り込む研究である。 [22](https://arxiv.org/abs/2611.09474)

## 次の課題（編者の整理）

### 能力・計算量・費用を同時に比べる

モデル単体の成績に加え、検証器、生成回数、教師、キャッシュを含む総費用と遅延を揃えた比較が次の焦点になる。 [20](https://arxiv.org/abs/2408.03314) [3](https://arxiv.org/abs/2611.13410) [22](https://arxiv.org/abs/2611.09474)

### 推論手順を能力の説明に使えるか

途中の説明がもっともらしくても、実際の判断理由と一致するかは別に検証する必要がある。 [23](https://arxiv.org/abs/2307.13702)

## 分野間の接点（編者の整理）

- [エージェント・検索・記憶・協調](https://drkamoshika.github.io/papers/?view=map&topic=agents): 言語生成を外部ツールと組み合わせると、評価単位が一回答から行動系列へ変わる。 [24](https://arxiv.org/abs/2210.03629) [3](https://arxiv.org/abs/2611.13410)

- [評価・安全性・解釈可能性](https://drkamoshika.github.io/papers/?view=map&topic=trust): 選好最適化・長い推論・高い自信のどれも、事実性や校正の代わりにはならない。 [12](https://arxiv.org/abs/2305.18290) [25](https://arxiv.org/abs/2611.14661)

## 読む順番

1. [Attention Is All You Need](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1706.03762)

2. [Language Models are Few-Shot Learners](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2005.14165)

3. [Training Compute-Optimal Large Language Models](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2203.15556)

4. [Training language models to follow instructions with human feedback](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2203.02155)

5. [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2201.11903)

6. [Learning When Diffusion Language Models Should Regenerate](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17320)

7. [SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.13410)

## 参考文献と確認範囲

1. [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — 2020-05-28 / arxiv:2005.14165 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2005.14165)

2. [Learning When Diffusion Language Models Should Regenerate](https://arxiv.org/abs/2611.17320) — 2026-11-12 / arxiv:2611.17320 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.17320) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.17320v1)

3. [SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering](https://arxiv.org/abs/2611.13410) — 2026-11-10 / arxiv:2611.13410 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.13410) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.13410v1)

4. [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) — 2013-01-16 / arxiv:1301.3781 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1301.3781)

5. [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) — 2014-09-01 / arxiv:1409.0473 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1409.0473)

6. [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — 2017-06-12 / arxiv:1706.03762 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1706.03762)

7. [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) — 2018-10-11 / arxiv:1810.04805 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A1810.04805)

8. [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — 2020-01-23 / arxiv:2001.08361 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2001.08361)

9. [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) — 2022-03-29 / arxiv:2203.15556 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2203.15556)

10. [Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652) — 2021-09-03 / arxiv:2109.01652 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2109.01652)

11. [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — 2022-03-04 / arxiv:2203.02155 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2203.02155)

12. [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) — 2023-05-29 / arxiv:2305.18290 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.18290)

13. [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) — 2022-01-28 / arxiv:2201.11903 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2201.11903)

14. [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) — 2022-03-21 / arxiv:2203.11171 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2203.11171)

15. [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) — 2023-05-31 / arxiv:2305.20050 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.20050)

16. [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) — 2021-06-17 / arxiv:2106.09685 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2106.09685)

17. [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323) — 2022-10-31 / arxiv:2210.17323 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2210.17323)

18. [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135) — 2022-05-27 / arxiv:2205.14135 / 本文の関連箇所確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2205.14135)

19. [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — 2023-09-12 / arxiv:2309.06180 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2309.06180)

20. [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) — 2024-08-06 / arxiv:2408.03314 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2408.03314)

21. [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) — 2023-05-23 / arxiv:2305.14314 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2305.14314)

22. [Nebula: Distributed Position-Independent Caching for LLM Serving](https://arxiv.org/abs/2611.09474) — 2026-11-06 / arxiv:2611.09474 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.09474) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.09474v1)

23. [Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702) — 2023-07-17 / arxiv:2307.13702 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2307.13702)

24. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — 2022-10-06 / arxiv:2210.03629 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=foundations&paper=arxiv%3A2210.03629)

25. [Abstention Is Not Threshold Compliance: Stated Scoring Rules in Open Language Models](https://arxiv.org/abs/2611.14661) — 2026-11-10 / arxiv:2611.14661 / 要旨確認 / [ライブラリ内要約](https://drkamoshika.github.io/papers/?collection=daily&paper=arxiv%3A2611.14661) / 今回の再確認: 2026-11-16、一次資料の要旨・該当記述、[一次資料](https://arxiv.org/abs/2611.14661v1)

## このレビューの範囲

母集団はこのライブラリの収録論文。全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断的レビューです。

基礎文献・新着論文は収録先の区別です。基礎文献側にも2026年の研究が含まれるため、古さや新しさは個々の公開日で確認できます。

技術の系譜、分野間の接点、次の課題は編者の整理であり、論文間の直接の引用関係や、商用普及の程度を確定するものではありません。

個別論文の確認範囲は要旨または本文の関連箇所です。今回、代表的な22件の一次資料を追加で照合しました。全件の全文再精読や独立再現を意味しません。

実験の数字は論文の報告値です。異なるデータ・分割・指標の数値を統一順位へ変換していません。

[7分野の全体マップ](https://drkamoshika.github.io/papers/?view=map)
