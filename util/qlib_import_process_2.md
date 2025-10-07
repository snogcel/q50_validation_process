
# adjust source data to fit existing QLib methods (1d interval) - Test Import BTCUSDT
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\btcusdt --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_BTCUSDT_d --include_fields Open,High,Low,Close,Volume_BTC,Volume_USDT,tradecount --date_field_name date --freq 'day'

# adjust source data to fit existing QLib methods (60min interval) - Test Import btcusdt
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\h\\btcusdt_adjust --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_BTCUSDT_h --include_fields Open,High,Low,Close,Volume_BTC,Volume_USDT,tradecount --date_field_name Date --freq '60min'

# adjust source data to fit existing QLib methods (1d interval) - Test Import btc_dom
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\btc_dom --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_btc_dom_d --include_fields close --date_field_name date --freq 'day'

# adjust source data to fit existing QLib methods (1d interval) - Test Import fg_index
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\fg_index --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_fg_index_h --include_fields fng_value --date_field_name date --freq 'day'


python scripts/check_data_health.py --qlib_dir 'C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA' check_data

# Work, a service provided in exchange for Goods and or Services.
# If you like what you do, you'll never work a day in your life.



