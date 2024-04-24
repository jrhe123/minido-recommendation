import recall.dataset.anime as dataset
from recall.strategy.recall_strategy import RecallStrategy


class SimpleRecallStrategy(RecallStrategy):
    def __init__(self):
        super().__init__()

    def name(self):
        return "Simple"

    def recall(self, context, n):
        (anime_df, _) = dataset.load_dataset()

        # DUMMY: just return first n items in the list (ids only)
        return anime_df.iloc[:n].index.to_list()
