import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
import datetime as dt 


# df = web.DataReader('GE', 'yahoo', start='2019-09-10', end='2019-10-09')
# print(df.head())

currency = 'USD'
metric   = "Close"

start   = dt.datetime(2020,11,1)
end     = dt.datetime.now()

crypto  = ['BTC', 'ETH', 'ADA', 'CRO', 'BNB', 'SHIB', 'AVAX', 'DOGE', 'SOL']

first = True

for ticker in crypto:
    print(ticker)
    data = web.DataReader(f'{ticker}-{currency}', 'yahoo' , start , end)
    if first:
        combined = data[[metric]].copy()
        combined = combined.rename(columns={metric: ticker})
        first = False
    else:
        combined = combined.join(data[metric])
        combined = combined.rename(columns={metric: ticker})

plt.yscale('log')
for ticker in crypto:
    plt.plot(combined[ticker], label = ticker)

plt.legend(loc = "upper right")
plt.show()