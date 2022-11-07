import pandas as pd
import numpy as np

def load():
    df = pd.read_csv("../data/raw/Stats.csv",encoding="ISO-8859-1", delimiter = ";")
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
    forwards = df[df.Pos == "FW"]
    forwards = forwards[["Goals", "Shots", "G/Sh", "Assists", "PasCmp", "Touches", "DriPast", "CarTotDist", "Crs", "GCA", "TklWon", "Press", "Clr", "Int", "Blocks", "Fls", "AerWon"]]
    
    return forwards

def midfielders(df):
    midfielders = df[df.Pos == "MF"]
    midfielders = midfielders[["Goals", "Shots", "G/Sh", "Assists", "PasCmp", "Touches", "DriPast", "CarTotDist", "Crs", "GCA", "TklWon", "Press", "Clr", "Int", "Blocks", "Fls", "AerWon"]]
    
    return midfielders

def defenders(df):
    defenders = df[df.Pos == "DF"]
    defenders = defenders[["Goals", "Shots", "G/Sh", "Assists", "PasCmp", "Touches", "DriPast", "CarTotDist", "Crs", "GCA", "TklWon", "Press", "Clr", "Int", "Blocks", "Fls", "AerWon"]]
    
    return defenders