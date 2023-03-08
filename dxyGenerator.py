import pandas as pd
from datetime import datetime
import datetime as dt
import numpy as np


# Load the data into a pandas DataFrame
df_UCAD = pd.read_csv("USDCAD5.csv")
df_GU = pd.read_csv("GBPUSD5.csv")
df_EU = pd.read_csv("EURUSD5.csv")
df_UCHF = pd.read_csv("USDCHF5.csv")
df_USEK = pd.read_csv("USDSEK5.csv")
df_UJ = pd.read_csv("USDJPY5.csv")

"""
Forumula for dxy:
USDX = 50.14348112  EURUSD^-0.576  USDJPY^0.136  GBPUSD^-0.119  USDCAD^0.091  USDSEK^0.042  USDCHF^0.036
"""


def exportDate(df, start_date, end_date=None):
    if end_date == None:
        datesDf = df["date"] == start_date
    else:
        datesDf = (df["date"] >= start_date) & (df["date"] <= end_date)
    structuredDf = df[datesDf]

    return structuredDf


def structureMT4Data(df):  # df cleaning and formatting
    df.columns = ["date", "time", "open", "high", "low", "close", "volume"]

    df["date"] = pd.to_datetime(df["date"])
    df["date"] = pd.to_datetime(df["date"], format="%Y%m/%d")
    df["time"] = pd.to_datetime(df["time"], format="%H:%M").dt.time
    return df


dfUCAD = structureMT4Data(df_UCAD)
dfGU = structureMT4Data(df_GU)
dfEU = structureMT4Data(df_EU)
dfCHF = structureMT4Data(df_UCHF)
dfSEK = structureMT4Data(df_USEK)
dfUJ = structureMT4Data(df_UJ)

dfUCAD = exportDate(dfUCAD, "2022-02-01", "2023-02-28")
dfGU = exportDate(dfGU, "2021-02-01", "2023-02-28")
dfEU = exportDate(dfEU, "2021-02-01", "2023-02-28")
dfCHF = exportDate(dfCHF, "2021-02-01", "2023-02-28")
dfSEK = exportDate(dfSEK, "2021-02-01", "2023-02-28")
dfUJ = exportDate(dfUJ, "2021-02-01", "2023-02-28")

# Merge the data frames based on the date and time column
df = pd.merge(dfUCAD, dfGU, on=["date", "time"])
df = pd.merge(df, dfEU, on=["date", "time"])
df = pd.merge(df, dfCHF, on=["date", "time"])
df = pd.merge(df, dfSEK, on=["date", "time"])
df = pd.merge(df, dfUJ, on=["date", "time"])
df.columns = [
    "date",
    "time",
    "UCAD_open",
    "UCAD_high",
    "UCAD_low",
    "UCAD_close",
    "UCAD_volume",
    "GU_open",
    "GU_high",
    "GU_low",
    "GU_close",
    "GU_volume",
    "EU_open",
    "EU_high",
    "EU_low",
    "EU_close",
    "EU_volume",
    "UCHF_open",
    "UCHF_high",
    "UCHF_low",
    "UCHF_close",
    "UCHF_volume",
    "USEK_open",
    "USEK_high",
    "USEK_low",
    "USEK_close",
    "USEK_volume",
    "UJ_open",
    "UJ_high",
    "UJ_low",
    "UJ_close",
    "UJ_volume",
]

print(df)

dxy = pd.DataFrame()
dxy["date"] = df["date"]
dxy["time"] = df["time"]
dxy["open"] = (
    50.14348112
    * df["UCAD_open"] ** 0.091
    * df["GU_open"] ** (-0.119)
    * df["EU_open"] ** (-0.576)
    * df["UJ_open"] ** 0.136
    * df["USEK_open"] ** 0.042
    * df["UCHF_open"] ** 0.036
)
dxy["high"] = (
    50.14348112
    * df["UCAD_high"] ** 0.091
    * df["GU_high"] ** (-0.119)
    * df["EU_high"] ** (-0.576)
    * df["UJ_high"] ** 0.136
    * df["USEK_high"] ** 0.042
    * df["UCHF_high"] ** 0.036
)
dxy["low"] = (
    50.14348112
    * df["UCAD_low"] ** 0.091
    * df["GU_low"] ** (-0.119)
    * df["EU_low"] ** (-0.576)
    * df["UJ_low"] ** 0.136
    * df["USEK_low"] ** 0.042
    * df["UCHF_low"] ** 0.036
)
dxy["close"] = (
    50.14348112
    * df["UCAD_close"] ** 0.091
    * df["GU_close"] ** (-0.119)
    * df["EU_close"] ** (-0.576)
    * df["UJ_close"] ** 0.136
    * df["USEK_close"] ** 0.042
    * df["UCHF_close"] ** 0.036
)
print(dxy)
dxy.to_csv("dxy5.csv", index=False)
