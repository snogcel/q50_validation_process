
# adjust source data to fit existing QLib methods (1d interval) - Test Import BTCUSDT
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\btcusdt --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA --include_fields Open,High,Low,Close,Volume_BTC,Volume_USDT,tradecount --date_field_name date --freq 'day'

# adjust source data to fit existing QLib methods (60min interval) - Test Import btcusdt
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\h\\btcusdt_adjust --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA --include_fields Open,High,Low,Close,Volume_BTC,Volume_USDT,tradecount --date_field_name Date --freq '60min'


# adjust source data to fit existing QLib methods (1d interval) - Test Import btc_dom
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\btc_dom --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA --include_fields close --date_field_name date --freq 'day'


# adjust source data to fit existing QLib methods (1d interval) - Test Import btc_dom
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\fg_index --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA --include_fields fng_value --date_field_name date --freq 'day'













python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\h\\btcusdt_adjust --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data_crypto\\CRYPTODATA_h --include_fields Open,High,Low,Close,Volume_BTC,Volume_USDT,tradecount --date_field_name Unix --freq '60min' HIGH_FREQ_FORMAT


# TODO - Resample this file using pandas df, to bring into expected format - then proceed.






# adjust source data to fit existing QLib methods (1d interval)
python scripts/dump_bin.py dump_all --csv_path C:\\Projects\\q50_validation_process\\data_csv\\d --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data_crypto\\CRYPTODATA --include_fields open,close,high,low,volume --date_field_name timestamp --freq 'day'

python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data_crypto\\CRYPTODATA --include_fields open,close,high,low,volume --date_field_name timestamp --freq 'day'


# adjust source data to fit existing QLib methods (1h interval)
python scripts/dump_bin.py dump_all --csv_path C:\\Projects\\qlib_trading_v2\\csv_data\\CRYPTODATA_RESAMPLE\60min --qlib_dir C:\\Projects\\qlib_trading_v2\\qlib_data\\CRYPTODATA --include_fields open,close,high,low,volume --date_field_name timestamp --freq '60min'



python scripts/dump_bin.py dump_all --csv_path C:\\Projects\\qlib_trading_v2\\csv_data\\CRYPTODATA_RESAMPLE\240min --qlib_dir C:\\Projects\\qlib_trading_v2\\qlib_data\\CRYPTODATA --include_fields open,close,high,low,volume --date_field_name timestamp --freq '240min'
