import pandas as pd
import numpy as np

def load_data(path):    
    return pd.read_csv("../data/raw/Stats.csv",encoding="ISO-8859-1", delimiter = ";")

def process_data(df, dataset_type):
# The dataset_type varible of type boolean refers to whether the dataset is the main dataset(true) or a subset of the main dataset(false)

    if (dataset_type):

        temp_df = (
              df
              .rename(columns={"Rk": "Rank","Min":"min_played","SoT":"shots_target","SoT%":"shots_target%"})
              .dropna(axis=0)
              .index_col("Rank")
          )
    else:

        temp_df = (
              df
              .rename(columns={"Born": "age_group"})
# Age_group is a column where we catorgorise age into groups increasing by 5
            .assign(age_group=lambda x: (int)(2022-x)/5)
          )


    return temp_df