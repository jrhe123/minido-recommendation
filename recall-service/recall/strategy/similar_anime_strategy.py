from recall.strategy.recall_strategy import RecallStrategy
import recall.dataset.anime as dataset

(anime_df, _) = dataset.load_dataset()
# sort by id
sorted_df = anime_df.sort_index()

class SimilarAnimeStrategy(RecallStrategy):
    def name(self):
        return 'Similar Anime'

    def recall(self, context, n=20):
        """
        DUMMY: based on the id value => similarity
        """
        anime_id = context.anime_id
        # location of id (index)
        anime_iloc = sorted_df.index.get_loc(anime_id)

        # check if it exceed the range, e.g., it's the last one element
        from_index = anime_iloc
        if from_index + n > len(sorted_df):
            from_index = len(sorted_df) - n

        return sorted_df.iloc[from_index: from_index + n].index.to_list()