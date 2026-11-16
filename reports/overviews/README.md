# 基礎から現在への全体マップ

レビュー日: 2026-11-16 / 収録 1038件（基礎 774・新着 264）から代表 165件を引用。

収録論文の公開日上限 2026-11-12、レポート日上限 2026-11-16。レビュー日を論文公開日と混同しない。

[ダッシュボードで読む](https://drkamoshika.github.io/papers/?view=map)

## 7分野の到達点

| 分野 | いまできること | 残る境界 |

| --- | --- | --- |

| [言語モデルの学習・推論・効率化](01-language.md) | 少数例での適応、指示に沿う生成、検証器を使う推論、小型化と推論処理の効率化。 | 長く考えれば必ず正しい、量子化しても全用途で同等、という保証はない。 |

| [エージェント・検索・記憶・協調](02-agents.md) | 検索付き回答、コード・Web操作、経験の再利用、複数エージェントによる調査を特定環境で実行。 | 任意の仕事を無監督で最後まで納品し、権限・費用・安全性も守れるとはいえない。 |

| [評価・安全性・解釈可能性](03-trust.md) | ベンチマーク、事実性検査、棄権・不確実性、攻撃試験、説明によって失敗を切り分けられる。 | 高い平均点、もっともらしい説明、安全指示だけで、未知環境の安全性を認定できない。 |

| [医療・生体信号・創薬AI](04-medical.md) | 画像の領域抽出、記録の構造化、生体信号解析、分子・タンパク質の候補探索で有用性を示す。 | 医学試験の高得点や記録の読解から、自律診療・個別予後予測・治療効果までは確定しない。 |

| [表形式・時系列・因果推論](05-structured.md) | 表の分類・回帰、時系列予測、欠損補完、合成データを用途に応じて学習・転移できる。 | 一つのモデルで全表に勝つことや、予測精度から因果効果が分かることは示されていない。 |

| [次イベント予測・点過程](06-events.md) | 不規則なイベントの種類・待ち時間・場所をモデル化し、業務ログや移動履歴で予測できる。 | 次ラベルの正解率だけでは時刻の校正や長期生成、介入の価値、LLMの必要性は判断できない。 |

| [神経科学とAI](07-neuroscience.md) | ハエの回路追跡、マウス局所の構造と活動の対応、人の粗視化ネットワーク解析や条件付きの信号復号。 | 収録研究は、人間全脳の細胞レベル再現や、配線図だけでの感情・意識の説明までは示していない。 |


## 分野をまたいだ変化

### 予測から意思決定へ

言語や系列の予測が良くなることと、仕事を完遂する、介入効果を知る、患者の将来を予測することを分けて評価する。 [DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://arxiv.org/abs/2611.03412) [From Forecasting to World Modeling: Can Temporal Foundation Models Recover Causal Response?](https://arxiv.org/abs/2611.15009) [Performance of a Large Language Model for Predicting Clinical and Radiographic Outcomes in Knee Osteoarthritis: Single-Center Prospective Observational Study](https://pubmed.ncbi.nlm.nih.gov/43019548/)

### 経験・根拠・状態を残す

長い文脈や記憶は量だけでなく、根拠をたどれること、更新できること、使う費用も研究対象になっている。 [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320) [CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation](https://arxiv.org/abs/2611.17316) [SHARP: Semantic Hierarchical Agentic Reasoning for Next POI Prediction with Dynamic Memory](https://arxiv.org/abs/2611.14220)

### 成功した条件を説明する

モデル規模の増加や複雑化だけで結論せず、単純基準、情報量、費用、対象外データ、測定の限界を並べて読む。 [David vs. Goliath in Next Activity Prediction: Argmax vs. LSTM, Transformer, and LLM](https://arxiv.org/abs/2606.15868) [One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation, Imputation, and Prediction](https://arxiv.org/abs/2611.13001) [Your Vision Foundation Model Is Secretly an EEG Foundation Model](https://arxiv.org/abs/2611.17031)

## 読み方と確認範囲

母集団はこのライブラリの収録論文。全論文を同じ重さで引用する系統的レビューではなく、基盤・転換点・直近の検証を選ぶ横断的レビューです。

基礎文献・新着論文は収録先の区別です。基礎文献側にも2026年の研究が含まれるため、古さや新しさは個々の公開日で確認できます。

技術の系譜、分野間の接点、次の課題は編者の整理であり、論文間の直接の引用関係や、商用普及の程度を確定するものではありません。

個別論文の確認範囲は要旨または本文の関連箇所です。今回、代表的な22件の一次資料を追加で照合しました。全件の全文再精読や独立再現を意味しません。

実験の数字は論文の報告値です。異なるデータ・分割・指標の数値を統一順位へ変換していません。

## 更新

この版は上記の収録範囲に基づく手動編集のレビュー。新しい論文や検証結果に応じてMarkdownと公開用overview.jsonを更新する。既存の定期実行や個別論文データの生成処理は変更しない。arXiv・PubMed等の出典選択は論文一覧に保持する。
