# ディレクトリ構成

```
recommender/
    __init__.py
    api.py          # 簡易HTTPサーバ
    database.py     # 候補者データ読み込み
    llm_client.py   # LLMスコアリング（ダミー実装）
    pipeline.py     # 推薦処理本体
```

`data/candidates.json` には候補者のサンプルデータが格納されています。
依存関係は `requirements.txt` に記載しており、uv を用いて以下のように
インストールします。

```bash
uv venv
uv pip install -r requirements.txt
```

APIサーバは `python -m recommender.api` で起動し、`/recommend?user_id=1` の
形式で推薦結果を取得できます。
