import yfinance as yf

# dat = yf.Ticker("USDT-BTC")
# dat.info

df = yf.download(["USDT-BTC"], interval="1d")
df.to_csv('./yfinance_usdt_btc_1d.csv')

# yfinance.download(tickers, start=None, end=None, actions=False, threads=True, ignore_tz=None, group_by='column', auto_adjust=None, back_adjust=False, repair=False, keepna=False, progress=True, period=None, interval='1d', prepost=False, proxy=<object object>, rounding=False, timeout=10, session=None, multi_level_index=True) → DataFrame | None

""" 

    tickersstr, list

        List of tickers to download
    periodstr

        Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max Default: 1mo Either Use period parameter or use start and end
    intervalstr

        Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo Intraday data cannot extend last 60 days
    start: str

        Download start date string (YYYY-MM-DD) or _datetime, inclusive. Default is 99 years ago E.g. for start=”2020-01-01”, the first data point will be on “2020-01-01”
    end: str

        Download end date string (YYYY-MM-DD) or _datetime, exclusive. Default is now E.g. for end=”2023-01-01”, the last data point will be on “2022-12-31”
    group_bystr

        Group by ‘ticker’ or ‘column’ (default)
    prepostbool

        Include Pre and Post market data in results? Default is False
    auto_adjust: bool

        Adjust all OHLC automatically? Default is True
    repair: bool

        Detect currency unit 100x mixups and attempt repair Default is False
    keepna: bool

        Keep NaN rows returned by Yahoo? Default is False
    actions: bool

        Download dividend + stock splits data. Default is False
    threads: bool / int

        How many threads to use for mass downloading. Default is True
    ignore_tz: bool

        When combining from different timezones, ignore that part of datetime. Default depends on interval. Intraday = False. Day+ = True.
    rounding: bool

        Optional. Round values to 2 decimal places?
    timeout: None or float

        If not None stops waiting for a response after given number of seconds. (Can also be a fraction of a second e.g. 0.01)
    session: None or Session

        Optional. Pass your own session object to be used for all requests
    multi_level_index: bool

        Optional. Always return a MultiIndex DataFrame? Default is True

 """
