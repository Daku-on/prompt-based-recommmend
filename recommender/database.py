import json
from pathlib import Path
from typing import List, Dict

DATA_PATH = Path(__file__).resolve().parent.parent / 'data' / 'candidates.json'


def load_candidates() -> List[Dict]:
    """候補者データをスコア降順で取得する。"""
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # score降順でソート
    return sorted(data, key=lambda x: x['score'], reverse=True)
