import concurrent.futures
import time
from typing import List

import recall.strategy as strategy
from recall import util
from recall.context import Context
from recall.dataset.embedding import get_one_item_embedding
from recall.model.lsh import get_item_lsh

strategies: List[strategy.RecallStrategy] = [
    # testing
    # strategy.SimpleRecallStrategy(),
    strategy.HighRatingStrategy(),
    strategy.MostRatingStrategy(),
    # embedding
    strategy.UserEmbeddingStrategy(),
]


def anime_recall(context: Context, n=20) -> List[int]:
    """
    returns a list of anime ids
    """

    # multi-thread
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 1. iterate all the strategies we init above
        outputs = executor.map(lambda s: run_strategy(s, context, n), strategies)

        """
        outputs: [
            [1,2,3], # simple strategy
            [3,4,5], # high rating strategy
            [2,3,4], # most rating strategy
        ]
        =>
        [1,2,3,3,4,5,2,3,4]
        =>
        [1,2,3,4,5]
        """
        # 2.1 format outputs
        outputs = [id for sub_list in outputs for id in sub_list]
        # 2.2 remove duplicates
        outputs = list(dict.fromkeys(outputs))
        print(f"Got {len(outputs)} uniq recall results")

        return outputs


# def similar_animes(context: Context, n=20) -> List[int]:
#     """
#     returns a list of anime ids
#     """
#     stra = strategy.SimilarAnimeStrategy()
#     return stra.recall(context, n)


def similar_animes(context: Context, n=20) -> List[int]:
    lsh = get_item_lsh()
    target_item_emb = get_one_item_embedding(context.anime_id)
    outputs = lsh.search(target_item_emb, n=n)
    return outputs


def run_strategy(strategy: strategy.RecallStrategy, context: Context, n):
    start_time = time.time()
    res = strategy.recall(context, n=n)
    elapse_time = time.time() - start_time
    print("Strategy %s took %.2fms" % (strategy.name(), elapse_time * 1000))
    return res
