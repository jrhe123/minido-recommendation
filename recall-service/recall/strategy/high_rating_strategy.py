from random import sample

import recall.dataset.anime as dataset
from recall.config import config
from recall.strategy.recall_strategy import RecallStrategy


class HighRatingStrategy(RecallStrategy):
    def __init__(self):
        super().__init__()
        self.build_pool()

    def name(self):
        return "HighRating"

    def build_pool(self):
        """
        Matthew effect: pool size 500
        """
        # 1. load dataset
        (anime_df, _) = dataset.load_dataset()
        # 2. sort by highest rating animes
        sorted_df = anime_df.sort_values(by=["rating"], ascending=False)
        self.pool = sorted_df.iloc[:500].index.to_list()

        print(f"{self.name()} pool loaded.")

    def recall(self, context, n):
        if config["high_rating"]["shuffle_sample"]:
            # random pick n of items
            return sample(self.pool, n)

        return self.pool[:n]
