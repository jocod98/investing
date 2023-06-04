import backtrader as bt
import pandas as pd
from datetime import datetime

cerebro = bt.Cerebro()

# Create a data feeddf
df =pd.read_csv("amc_ohlcv.csv")
print(df.head())



