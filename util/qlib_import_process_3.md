
## Identify which data set has the largest scope of data:


<!-- fg_index has a span of data from:

2/1/2018,30,Fear
...
10/6/2025,71,Greed -->

# adjust source data to fit existing QLib methods (1d interval) - Test Import fg_index
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\fg_index --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED_2 --include_fields fng_value --date_field_name date --freq 'day'


<!-- btcusdt_binance has a span of data from:
1.50293E+12,8/17/2017,BTCUSDT,4261.48,4485.39,4200.74,4285.08,795.150377,3454770.051,3427
...
1.75954E+12,10/4/2025,BTCUSDT,122232.21,122800,121510,122391,8208.16678,1002272903,1703590 -->

# adjust source data to fit existing QLib methods (1d interval) - Test Import BTCUSDT
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\btcusdt --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED_2 --include_fields Open,High,Low,Close,Volume_BTC,Volume_USDT,tradecount --date_field_name date --freq 'day'

# TODO - aligning hourly data with daily data is difficult.

# adjust source data to fit existing QLib methods (60min interval) - Test Import btcusdt
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\h\\btcusdt_adjust --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED_2 --include_fields Open,High,Low,Close,Volume_BTC,Volume_USDT,tradecount --date_field_name Date --freq '60min'


<!-- btc_dom has a span of data from:
3/31/2014 18:00,CRYPTOCAP:BTC.D,99.38055076,99.42670354,99.29683247,99.38465167,14938879.04
...
10/5/2025 18:00,CRYPTOCAP:BTC.D,59.31206475,59.36450805,59.08154877,59.08686448,77927102627 -->

# adjust source data to fit existing QLib methods (1d interval) - Test Import btc_dom
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\btc_dom --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED_2 --include_fields close --date_field_name date --freq 'day'





python scripts/check_data_health.py --qlib_dir 'C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA' check_data

# Work, a service provided in exchange for Goods and or Services.
# If you like what you do, you'll never work a day in your life.

# TO DO: Review Data Discrepency against: https://finance.yahoo.com/quote/USDT-BTC/history/?period1=1588809600&period2=1602028800


# next, review against previously completed work:

train_start_time = "2018-08-02"
train_end_time = "2023-12-31"
valid_start_time = "2024-01-01"
valid_end_time = "2024-09-30"
test_start_time = "2024-10-01"
test_end_time = "2025-04-01"

# Result - Validated Data:

instrument datetime
btcusdt    2020-05-01  8620.000000   9059.179688  8613.559570  8826.959961
           2020-05-02  8825.669922   9010.000000  8753.000000  8972.049805
           2020-05-03  8972.580078   9200.000000  8712.000000  8894.160156
           2020-05-04  8894.150391   8950.000000  8522.000000  8871.959961
           2020-05-05  8871.919922   9118.580078  8760.000000  9021.830078
           2020-05-06  9021.360352   9395.000000  8906.209961  9142.919922
           2020-05-07  9143.400391  10067.000000  9021.000000  9986.400391
           2020-05-08  9986.299805  10035.959961  9705.000000  9800.009766
           2020-05-09  9800.019531   9914.250000  9520.000000  9539.400391
           2020-05-10  9539.099609   9574.830078  8117.000000  8722.769531
           2020-05-11  8722.769531   9168.000000  8200.000000  8561.519531
           2020-05-12  8562.040039   8978.259766  8528.780273  8810.790039
           2020-05-13  8810.990234   9398.000000  8792.990234  9309.370117
           2020-05-14  9309.349609   9939.000000  9256.759766  9791.980469
           2020-05-15  9791.969727   9845.620117  9150.000000  9316.419922
           2020-05-16  9315.959961   9588.000000  9220.000000  9381.269531
           2020-05-17  9380.809570   9888.000000  9322.099609  9680.040039
           2020-05-18  9681.110352   9950.000000  9464.230469  9733.929688
           2020-05-19  9733.929688   9897.209961  9474.000000  9775.530273
           2020-05-20  9775.129883   9842.000000  9326.000000  9511.429688
           2020-05-21  9511.429688   9578.469727  8815.000000  9068.650391
           2020-05-22  9067.509766   9271.000000  8933.519531  9170.000000
           2020-05-23  9170.000000   9307.849609  9070.000000  9179.150391
           2020-05-24  9179.009766   9298.000000  8700.000000  8720.339844
           2020-05-25  8718.139648   8979.660156  8642.719727  8900.349609
           2020-05-26  8900.349609   9017.669922  8700.000000  8841.179688
           2020-05-27  8841.000000   9225.000000  8811.730469  9204.070312
           2020-05-28  9204.070312   9625.469727  9110.000000  9575.889648
           2020-05-29  9575.870117   9605.259766  9330.000000  9427.070312
           2020-05-30  9426.599609   9740.000000  9331.230469  9697.719727
           2020-05-31  9697.719727   9700.000000  9381.410156  9448.269531

# next, verify 60min data:
                                      $open  ...       $close
instrument datetime                          ...
btcusdt    2020-05-01 00:00:00  8620.000000  ...  8707.509766
           2020-05-01 01:00:00  8707.500000  ...  8662.610352
           2020-05-01 02:00:00  8663.070312  ...  8726.360352
           2020-05-01 03:00:00  8725.500000  ...  8675.349609
           2020-05-01 04:00:00  8675.099609  ...  8791.589844
...                                     ...  ...          ...
           2020-05-30 20:00:00  9535.129883  ...  9440.610352
           2020-05-30 21:00:00  9440.459961  ...  9491.410156
           2020-05-30 22:00:00  9492.440430  ...  9729.000000
           2020-05-30 23:00:00  9729.000000  ...  9697.719727
           2020-05-31 00:00:00  9697.719727  ...  9656.669922

# Then, document the features being created and used as part of this predictive model.

config={
    "kbar": {},  # Use optimized kbar features
    "price": {
        "windows": [1],  # Only OPEN1 (OPEN2/3 removed due to high correlation)
        "feature": ['OPEN'],
    },
    "volume": {
        "windows": [1],  # Only VOLUME1 (VOLUME2/3 removed due to high correlation)
    },
    "rolling": {
        "windows": [1, 2, 3],  # Reduced window set
        "include": ['RSV'],  # Keep only most valuable rolling features
    },
}

# Optimized kbar features (removed redundant volatility measures)
fields += [
    
    # realized_vol_6
    'Std(Log($close / Ref($close, 1)), 6)',
    
    # ── Relative volatility (short/long)
    'Std(Log($close / Ref($close, 1)), 5) / Std(Log($close / Ref($close, 1)), 20)', 

    # ── Rolling price momentum for directional context
    '$close / Ref($close, 5) - 1', # 5 hours
    '$close / Ref($close, 10) - 1', # 10 hours
    '$close / Ref($close, 25) - 1', # 25 hours

    # ── High-volatility regime flag
    "If(Std(Log($close / Ref($close, 1)), 5) / Std(Log($close / Ref($close, 1)), 20) > 1.25, 1, 0)", 
    
    #'If(Std(Log($close / Ref($close, 1)), 6) > Quantile(Std(Log($close / Ref($close, 1)), 6), 180, 0.9), 1, 0)', 
    #'If(Std(Log($close / Ref($close, 1)), 6) > Quantile(Std(Log($close / Ref($close, 1)), 6), 180, 0.7), 1, 0)', 
    #'If(Std(Log($close / Ref($close, 1)), 6) < Quantile(Std(Log($close / Ref($close, 1)), 6), 180, 0.3), 1, 0)', 
    #'If(Std(Log($close / Ref($close, 1)), 6) < Quantile(Std(Log($close / Ref($close, 1)), 6), 180, 0.1), 1, 0)', 
    
    'Std(Log($close / Ref($close, 1)), 6)',
    'Rank(Std(Log($close / Ref($close, 1)), 6), 180) / 180 * 10',
    'Std(Log($close / Ref($close, 1)), 6) * Std(Log($close / Ref($close, 1)), 6)',
    '(Std(Log($close / Ref($close, 1)), 6) - Quantile(Std(Log($close / Ref($close, 1)), 6), 30, 0.01)) / (Quantile(Std(Log($close / Ref($close, 1)), 6), 30, 0.99) - Quantile(Std(Log($close / Ref($close, 1)), 6), 30, 0.01))',
    'Std(Log($close / Ref($close, 1)), 6) - Ref(Std(Log($close / Ref($close, 1)), 6), 1)',
    '(Std(Log($close / Ref($close, 1)), 6) - Ref(Std(Log($close / Ref($close, 1)), 6), 1)) * 2000'
]


# Move Validated Data back to QLib_Trader_v2: https://github.com/snogcel/qlib_trading_v2/commit/71318d231875631352cbe35f55df41ac51ed28ea

# TO-DO: https://github.com/snogcel/qlib_trading_v2/commit/27e6e72db54e08a5c2fcaf63e7dfe0908aca744e

# Input Data Columns:

$close
$high
$low
$open
$tradecount
$volume_btc
$volume_usdt

# TO-DO: align these against qlib_trader_v2

$close
$high
$low
$open
$volume

# Fix QLib_Trader_V2 to utilize these column names, and then perform a backtest to validate results.


# Features (outlined above):

$realized_vol_6
$relative_volatility_index
$momentum_5
$momentum_10
$momentum_25
$high_vol_flag
vol_raw
vol_raw_decile
vol_risk
vol_scaled
vol_raw_momentum
vol_momentum_scaled
OPEN1
VOLUME1
RSV1
RSV2
RSV3
LABEL0

# Data Validated! https://github.com/snogcel/qlib_trading_v2/commit/e9a789bd664354c1c588c5537e9375ec71ad6981

# Backtester still needs some work:

(my_env_3_11) C:\Projects\qlib_trading_v2>conda run --name my_env_3_11 python c:/Projects/qlib_trading_v2/src/backtesting/backtester.py
No price file specified, will simulate from returns
Starting Hummingbot backtest with 0 observations...
Trading pair: BTCUSDT
Long threshold: 0.6, Short threshold: 0.6
No price data provided, simulating from returns...
Simulating prices from returns

Traceback (most recent call last):
  File "c:\Projects\qlib_trading_v2\src\backtesting\backtester.py", line 1367, in <module>
    backtester, results = run_hummingbot_backtest()
                          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Projects\qlib_trading_v2\src\backtesting\backtester.py", line 1356, in run_hummingbot_backtest
    results = backtester.run_backtest(df, price_data=price_data, price_col='close', return_col='truth')
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Projects\qlib_trading_v2\src\backtesting\backtester.py", line 829, in run_backtest
    final_portfolio_value = self.balance + self.position * current_price
                                                           ^^^^^^^^^^^^^
UnboundLocalError: cannot access local variable 'current_price' where it is not associated with a value

ERROR conda.cli.main_run:execute(127): `conda run python c:/Projects/qlib_trading_v2/src/backtesting/backtester.py` failed. (See above for error)

# Backtesting Prior to Data Validation:

No price file specified, will simulate from returns
Starting Hummingbot backtest with 10000 observations...
Trading pair: BTCUSDT
Long threshold: 0.6, Short threshold: 0.6
No price data provided, simulating from returns...
Simulating prices from returns
Processed 0/10000 observations, Price: $100.00, Portfolio: $99,997.85
Processed 1000/10000 observations, Price: $90.39, Portfolio: $96,621.24
Processed 2000/10000 observations, Price: $118.56, Portfolio: $101,710.27
Processed 3000/10000 observations, Price: $146.15, Portfolio: $112,236.97
Processed 4000/10000 observations, Price: $135.88, Portfolio: $114,873.05
Processed 5000/10000 observations, Price: $228.23, Portfolio: $116,356.59
Processed 6000/10000 observations, Price: $213.99, Portfolio: $114,445.37
Processed 7000/10000 observations, Price: $233.68, Portfolio: $121,115.38
Processed 8000/10000 observations, Price: $197.01, Portfolio: $118,774.25
Processed 9000/10000 observations, Price: $206.57, Portfolio: $125,414.04
Backtest completed. Final portfolio value: $126,698.82

=== HUMMINGBOT QUANTILE BACKTEST REPORT ===

CONFIGURATION:
- Trading Pair: BTCUSDT
- Initial Balance: $100,000.00
- Long Threshold: 0.60
- Short Threshold: 0.60
- Max Position: 30.0%
- Fee Rate: 0.100%

POSITION MANAGEMENT:
- Neutral Close Threshold: 0.70
- Min Confidence to Hold: 1.0
- Opposing Signal Threshold: 0.40

PERFORMANCE SUMMARY:
- Total Return: 26.71%
- Annualized Return: 23.04%
- Volatility: 12.86%
- Sharpe Ratio: 1.68
- Max Drawdown: -6.51%

TRADING STATISTICS:
- Total Trades: 3,522
- Total Holds: 6,306
- Trade Frequency: 35.22%
- Hold Frequency: 63.06%
- Win Rate: 8.83%

HOLD ANALYSIS:
- HOLD_POSITION: 6,306 periods

FINAL STATE:
- Final Balance: $126,698.82
- Final Position: 0.0000
- Final Portfolio Value: $126,709.94

OBSERVATIONS: 10,000

  - signal_summary_stats.json (quick signal analysis statistics)

Hummingbot backtest results saved to hummingbot_backtest_results
  - portfolio_history.csv (portfolio evolution with hold/trade actions)
  - trades.csv (individual trades)
  - holds_analysis.csv (detailed hold state analysis)
  - signal_analysis_pivot.csv (pivot-ready signal vs trade analysis)
  - metrics.json (performance metrics)
  - report.txt (summary report)



# Backtesting Parameters:

rain_start_time = "2018-08-02"
train_end_time = "2023-12-31"
valid_start_time = "2024-01-01"
valid_end_time = "2024-09-30"
test_start_time = "2024-10-01"
test_end_time = "2025-04-01"

fit_start_time = None
fit_end_time = None

provider_uri = "/Projects/qlib_trading_v2/qlib_data/CRYPTO_DATA"

SEED = 23020 # RANDOM SEED for Entropy Purposes, see: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
MARKET = "all"
BENCHMARK = "BTCUSDT"
EXP_NAME = "crypto_exp_101"
FREQ = "day"

qlib.init(provider_uri=provider_uri, region=REG_US)
