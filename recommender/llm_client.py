import os
import random
from typing import Dict

# `uv` でインストールした openai パッケージが存在するか試す
try:
    import openai  # type: ignore
except Exception:  # openai が無い場合
    openai = None  # type: ignore

API_KEY = os.getenv("OPENAI_API_KEY")


def _score_with_openai(user: Dict, candidate: Dict) -> float:
    """OpenAI API を利用してスコアを取得する。失敗時は例外を送出。"""
    assert openai and API_KEY  # 呼び出し前にチェック済みのはず
    openai.api_key = API_KEY
    prompt = (
        f"ユーザー{user['id']}と候補{candidate['name']}のマッチ度を"
        "0から10で数値のみ出力してください。"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5,
    )
    text = response.choices[0].message.content.strip()
    return float(text)


def score_candidate(user: Dict, candidate: Dict) -> float:
    """LLMを用いてユーザーと候補者の相性を0-10でスコアリングする。"""
    if openai and API_KEY:
        try:
            return _score_with_openai(user, candidate)
        except Exception:
            # APIエラー時はダミー値にフォールバック
            pass
    random.seed(hash(f"{user['id']}-{candidate['id']}"))
    return random.uniform(0, 10)
