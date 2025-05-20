# prompt-based-recommmend

## README（日本語）

### 概要

このリポジトリは、**LLM（大規模言語モデル）を用いた軽量なレコメンドエンジンのアーキテクチャ**を実装するためのPoC設計です。

従来の推薦システムが必要とした「特徴量の設計」「教師データの蓄積」「モデル学習」を一切不要とし、  
代わりにLLMを使って **ユーザーと候補者の相性を直接評価（スコアリング）** し、そのスコアに基づいて推薦を行います。

また、コストと応答速度の最適化のため、**「一定スコアを超えた候補がk人見つかった時点で処理を打ち切る」早期停止（early stopping）戦略**を採用。  
公平性確保のために、ソート下位の候補者をランダムで一部混入させる探索戦略も備えています。

---

### 主な特徴

- **ゼロ学習・ゼロ特徴量設計で使えるLLMレコメンド**
- **スコア閾値 × k件ヒットで評価処理を即時打ち切り**
- **任意のソート軸に加えて、ランダム挿入による露出機会の担保**
- **並列処理による高速化 & APIコスト最適化**
- **プロンプトの変更で評価軸を自在に切り替え可能**

---
### 使い方


`notebooks/recommender_demo.ipynb` では、同じ処理をJupyter Notebook形式で実装しています。
手元の環境にJupyterがあれば、ブラウザ上で処理の流れを確認できます。
1. [uv](https://docs.astral.sh/uv/) をインストール
2. 仮想環境を作成し依存関係をインストール
3. `OPENAI_API_KEY` を設定してAPIサーバを起動

```bash
# uv のインストール例
curl -Ls https://astral.sh/uv/install.sh | sh

# 依存関係のインストール
uv venv
uv pip install -r requirements.txt

# サーバ起動
OPENAI_API_KEY=sk-... python -m recommender.api
# 別ターミナルで
curl "http://localhost:8000/recommend?user_id=1"
```
---

### 今後の拡張

- LLMスコアと実際のユーザー選択結果のログを収集し、教師データとして活用  
- 公平性指標（露出率、選択率）を計測し、挿入アルゴリズムを動的に最適化  

---

## README (English)

### Overview

This repository contains a proof-of-concept (PoC) implementation of a **lightweight recommendation engine powered by Large Language Models (LLMs)**.

Unlike traditional systems that require extensive feature engineering or training, this architecture **relies on LLMs to score user-candidate pairs via prompts**, removing the need for prior training or labeled data.

To optimize latency and API cost, we implement an **early stopping strategy**—as soon as `k` candidates exceed a given score threshold, the evaluation stops.  
Additionally, to avoid ranking bias and long-tail suppression, we randomly inject lower-ranked candidates into the evaluation queue.

---

### Key Features

- **Zero training / zero feature engineering – LLMs handle scoring directly**
- **Early stopping once `k` candidates exceed a threshold**
- **Fairness-aware injection of low-ranked candidates**
- **Parallel processing to minimize latency and cost**
- **Flexible evaluation logic via prompt tuning**

---

### Future Extensions

- Logging LLM scores and user selection outcomes to create feedback-based optimization  
- Integrating fairness metrics (e.g., exposure rate) to dynamically balance ranking and randomness

---

### 開発ガイドライン

Python コードの静的解析には [Ruff](https://github.com/astral-sh/ruff) を使用しています。
GitHub Actions のワークフロー `.github/workflows/ruff.yml` では、
`ruff check . --output-format=github` を実行して自動的に検査を行います。
