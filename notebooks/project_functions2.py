import pandas as pd
import numpy as np

def unprocessed():
    df = pd.read_csv("../data/raw/Stats.csv",encoding="ISO-8859-1", delimiter = ";")
    return df

def load_and_process(path):
    df2 = (
        pd.read_csv(path,encoding="ISO-8859-1", delimiter = ";")
        .drop(["Carries","CarTotDist", "CarPrgDist", "CarProg", "Car3rd", "CPA", "OG"], axis=1)
        .dropna(axis=0)
        .reset_index()
        .rename(columns={"Comp":"League","CrdR":"RedCards"})
    )
    return df2