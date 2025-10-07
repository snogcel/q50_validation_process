
## Identify which data set has the largest scope of data:


<!-- fg_index has a span of data from:

2/1/2018,30,Fear
...
10/6/2025,71,Greed -->

# adjust source data to fit existing QLib methods (1d interval) - Test Import fg_index
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\fg_index --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED --include_fields fng_value --date_field_name date --freq 'day'


<!-- btcusdt_binance has a span of data from:
1.50293E+12,8/17/2017,BTCUSDT,4261.48,4485.39,4200.74,4285.08,795.150377,3454770.051,3427
...
1.75954E+12,10/4/2025,BTCUSDT,122232.21,122800,121510,122391,8208.16678,1002272903,1703590 -->

# adjust source data to fit existing QLib methods (1d interval) - Test Import BTCUSDT
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\btcusdt --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED --include_fields Open,High,Low,Close,Volume_BTC,Volume_USDT,tradecount --date_field_name date --freq 'day'

# TODO - aligning hourly data with daily data is difficult.

# adjust source data to fit existing QLib methods (60min interval) - Test Import btcusdt
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\h\\btcusdt_adjust --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED --include_fields Open,High,Low,Close,Volume_BTC,Volume_USDT,tradecount --date_field_name Date --freq '60min'


<!-- btc_dom has a span of data from:
3/31/2014 18:00,CRYPTOCAP:BTC.D,99.38055076,99.42670354,99.29683247,99.38465167,14938879.04
...
10/5/2025 18:00,CRYPTOCAP:BTC.D,59.31206475,59.36450805,59.08154877,59.08686448,77927102627 -->

# adjust source data to fit existing QLib methods (1d interval) - Test Import btc_dom
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\btc_dom --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED --include_fields close --date_field_name date --freq 'day'





python scripts/check_data_health.py --qlib_dir 'C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA' check_data

# Work, a service provided in exchange for Goods and or Services.
# If you like what you do, you'll never work a day in your life.

# TO DO: Review Data Discrepency against: https://finance.yahoo.com/quote/USDT-BTC/history/?period1=1588809600&period2=1602028800


