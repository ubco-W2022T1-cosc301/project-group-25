import pandas as pd
import numpy as np

excluding_positions = ['GK','GKMF','MFFW','FWMF','MFDF','DFMF','FWDF','DFFW']

def load():
    df = pd.read_csv("../data/raw/Stats.csv",encoding="ISO-8859-1", delimiter = ";")
    return df

def remove_excluding_positions(df):
    df = df.drop(df[df.Min < 300].index)
    for each in excluding_positions:
        df = df.drop(df[df.Pos == each].index)
        
    return df

def remove_players(df):    
    df = df.drop(df[df.Min < 300].index)
    df = df.drop(df[df.Pos == 'GK'].index)
    df = df.drop(df[df.Pos == 'GKMF'].index)
    df = df.drop(df[df.Pos == 'MFFW'].index)
    df = df.drop(df[df.Pos == 'FWMF'].index)
    df = df.drop(df[df.Pos == 'MFDF'].index)
    df = df.drop(df[df.Pos == 'DFMF'].index)
    df = df.drop(df[df.Pos == 'FWDF'].index)
    df = df.drop(df[df.Pos == 'DFFW'].index)
    return df

def forwards(df):
    return df[df.Pos == "FW"][["Goals", "Shots", "G/Sh", "Assists", "PasCmp", "Touches", "DriPast", "CarTotDist", "Crs", "GCA", "TklWon", "Press", "Clr", "Int", "Blocks", "Fls", "AerWon"]]

def midfielders(df):
    return df[df.Pos == "MF"][["Goals", "Shots", "G/Sh", "Assists", "PasCmp", "Touches", "DriPast", "CarTotDist", "Crs", "GCA", "TklWon", "Press", "Clr", "Int", "Blocks", "Fls", "AerWon"]]

def defenders(df):
    return df[df.Pos == "DF"][["Goals", "Shots", "G/Sh", "Assists", "PasCmp", "Touches", "DriPast", "CarTotDist", "Crs", "GCA", "TklWon", "Press", "Clr", "Int", "Blocks", "Fls", "AerWon"]]