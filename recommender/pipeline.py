import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List

from .database import load_candidates
from .llm_client import score_candidate


DEFAULT_THRESHOLD = 7.5
DEFAULT_TOP_K = 3
INJECTION_PROBABILITY = 0.1


def recommend(user: Dict, top_k: int = DEFAULT_TOP_K, threshold: float = DEFAULT_THRESHOLD) -> List[Dict]:
    """ユーザーに対する候補推薦を返す。"""
    candidates = load_candidates()

    # ランダム挿入: スコア下位の候補を一部前方へ挿入
    low_ranked = candidates[int(len(candidates) / 2) :]
    for candidate in low_ranked:
        if random.random() < INJECTION_PROBABILITY:
            index = random.randint(0, len(candidates) - 1)
            candidates.insert(index, candidate)

    results: List[Dict] = []
    with ThreadPoolExecutor() as executor:
        future_map = {executor.submit(score_candidate, user, c): c for c in candidates}
        for future in as_completed(future_map):
            candidate = future_map[future]
            score = future.result()
            if score >= threshold:
                results.append({"candidate": candidate, "score": score})
            if len(results) >= top_k:
                break
    # スコア順で返却
    results.sort(key=lambda x: x['score'], reverse=True)
    return results
