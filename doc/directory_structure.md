# ディレクトリ構成

```
recommender/
    __init__.py
    api.py          # 簡易HTTPサーバ
    database.py     # 候補者データ読み込み
    llm_client.py   # LLMスコアリング（ダミー実装）
    pipeline.py     # 推薦処理本体
```

`notebooks/` には、上記実装を実際に動かせる Jupyter Notebook (`recommender_demo.ipynb`) を配置しています。

`data/candidates.json` には候補者のサンプルデータが格納されています。
APIサーバは `python -m recommender.api` で起動し、`/recommend?user_id=1` の
形式で推薦結果を取得できます。
