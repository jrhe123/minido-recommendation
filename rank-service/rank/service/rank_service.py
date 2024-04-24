from random import sample

import rank.util.recall_service_client as recall_client


def anime_rank(context, n=20):
    recall_res = recall_client.get_recall(context.user_id)

    # sample 20 of them
    return sample(recall_res, n)
