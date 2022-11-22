import pandas as pd
import numpy as np

excluding_positions = ['GK','GKMF','MFFW','FWMF','MFDF','DFMF','FWDF','DFFW']
columns = ["Pos", "Goals", "Shots", "G/Sh", "Assists", "PasCmp", "Touches", "DriPast", "CarTotDist", "Crs", "GCA", "TklWon", "Press", "Clr", "Int", "Blocks", "Fls", "AerWon"]

def load():
    df = pd.read_csv("../data/raw/Stats.csv",encoding="ISO-8859-1", delimiter = ";")
    return df

def remove_players(df):
    df = df.drop(df[df.Min < 300].index)
    for each in excluding_positions:
        df = df.drop(df[df.Pos == each].index)
        
    return df

def forwards(df):
    return df[df.Pos == "FW"][columns]

def midfielders(df):
    return df[df.Pos == "MF"][columns]

def defenders(df):
    return df[df.Pos == "DF"][columns]