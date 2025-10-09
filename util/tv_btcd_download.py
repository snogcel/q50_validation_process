
# Fetch Data from: https://www.tradingview.com/symbols/BTC.D/
# using this existing library:

# pip install --upgrade --no-cache-dir git+https://github.com/rongardF/tvdatafeed.git


""" For usage instructions, watch these videos-

v1.2 tutorial with installation and backtrader usage

https://youtu.be/f76dOZW2gwI

Full tutorial

https://youtu.be/qDrXmb2ZRjo


 """

from tvDatafeed import TvDatafeed, Interval
tv = TvDatafeed()
BTCD = tv.get_hist(symbol='BTC.D',exchange='CRYPTOCAP',interval=Interval.in_daily,n_bars=5000)

BTCD.to_csv('BTCD.csv')

