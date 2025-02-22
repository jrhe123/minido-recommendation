from functools import lru_cache
from os.path import join
from posixpath import join

import pandas as pd
from pyspark.sql.session import SparkSession
from recall.config import config


# python native cache dataset
@lru_cache()
def load_dataset():
    anime_df = pd.read_csv(
        join(config["dataset_path"], "anime.csv"),
        index_col="anime_id",  # use it as index
    )
    rating_df = pd.read_csv(
        join(config["dataset_path"], "rating.csv"),
    )

    return (anime_df, rating_df)


@lru_cache()
def spark_load_ratings(spark: SparkSession):
    return spark.read.csv(
        join(config["dataset_path"], "rating.csv"), header=True, inferSchema=True
    )
