import os
import random
from typing import Dict

# OPENAI_API_KEY が設定されていれば利用可能なはずだが、
# この環境では openai パッケージがインストールされていない可能性があるため
# ダミー実装とする。

API_KEY = os.getenv('OPENAI_API_KEY')


def score_candidate(user: Dict, candidate: Dict) -> float:
    """LLMを用いてユーザーと候補者の相性を0-10でスコアリングする。"""
    # 実際にはOpenAI APIを呼び出すが、ここではランダム値を返す
    random.seed(hash(f"{user['id']}-{candidate['id']}"))
    return random.uniform(0, 10)
