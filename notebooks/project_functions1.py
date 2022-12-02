import pandas as pd
import numpy as np

excluding_positions = ['GK','GKMF','MFFW','FWMF','MFDF','DFMF','FWDF','DFFW']
columns = ["Position", "Goals", "Shots", "Goals/Shots", "Assists", "Passes", "Touches", "Dribbles", "Distance", "Crosses", "Goal_creating_actions", "Tackles", "Presses", "Clearances", "Interceptions", "Blocks", "Fouls", "Aerials_Won"]

def load():
    df = pd.read_csv("../data/raw/Stats.csv",encoding="ISO-8859-1", delimiter = ";")
    return df

def remove_players(df):
    df = df.drop(df[df.Min < 300].index)
    for each in excluding_positions:
        df = df.drop(df[df.Pos == each].index)
        
    return df

def rename_columns(df):
    df.rename(columns = {"Pos":"Position", "G/Sh":"Goals/Shots", "PasCmp":"Passes", "DriPast":"Dribbles", "CarTotDist":"Distance", "Crs":"Crosses", "GCA":"Goal_creating_actions", "TklWon":"Tackles", "Press":"Presses", "Clr":"Clearances", "Int":"Interceptions", "Fls":"Fouls", "AerWon":"Aerials_Won"}, inplace = True)
    
    return df
    
    
def forwards(df):
    return df[df.Position == "FW"][columns]

def midfielders(df):
    return df[df.Position == "MF"][columns]

def defenders(df):
    return df[df.Position == "DF"][columns]