# python scripts/dump_bin.py dump_all ... --symbol_field_name symbol


# Refreshing my memory on what I already did a few months ago...

import pandas as pd
import numpy as np

# Create a sample DataFrame with a DatetimeIndex
dates = pd.date_range('2023-01-01', periods=100, freq='H')
data = np.random.rand(100)
df = pd.DataFrame({'value': data}, index=dates)

# Downsample from hourly to daily, taking the mean
daily_mean = df.resample('D').mean()
print("Daily Mean:\n", daily_mean.head())

# Upsample from hourly to 30-minute intervals, forward filling missing values
half_hourly_ffill = df.resample('30T').ffill()
print("\nHalf-Hourly (forward-filled):\n", half_hourly_ffill.head())


python scripts/dump_bin.py dump_all --csv_path C:\\Projects\\qlib_trading_v2\\csv_data\\CRYPTODATA_RESAMPLE\1d --qlib_dir C:\\Projects\\qlib_trading_v2\\qlib_data\\CRYPTODATA --include_fields open,close,high,low,volume --date_field_name timestamp --freq 'day'
python scripts/dump_bin.py dump_all --csv_path C:\\Projects\\qlib_trading_v2\\csv_data\\CRYPTODATA_RESAMPLE\60min --qlib_dir C:\\Projects\\qlib_trading_v2\\qlib_data\\CRYPTODATA --include_fields open,close,high,low,volume --date_field_name timestamp --freq '60min'
python scripts/dump_bin.py dump_all --csv_path C:\\Projects\\qlib_trading_v2\\csv_data\\CRYPTODATA_RESAMPLE\240min --qlib_dir C:\\Projects\\qlib_trading_v2\\qlib_data\\CRYPTODATA --include_fields open,close,high,low,volume --date_field_name timestamp --freq '240min'



""" 
python scripts/dump_bin.py dump_all --csv_path C:\\Projects\\qlib_trading_v2\\csv_data\\CRYPTODATA --qlib_dir C:\\Projects\\qlib_trading_v2\\qlib_data\\CRYPTODATA --include_fields open,close,high,low,volume --date_field_name timestamp --freq '1min'

python scripts/dump_bin.py dump_all --csv_path C:\\Projects\\qlib_trading_v2\\csv_data\\CRYPTODATA_RESAMPLE\1d --qlib_dir C:\\Projects\\qlib_trading_v2\\qlib_data\\CRYPTODATA --include_fields open,close,high,low,volume --date_field_name timestamp --freq 'day'

python scripts/dump_bin.py dump_all --csv_path C:\\Projects\\qlib_trading_v2\\csv_data\\CRYPTODATA_RESAMPLE\60min --qlib_dir C:\\Projects\\qlib_trading_v2\\qlib_data\\CRYPTODATA --include_fields open,close,high,low,volume --date_field_name timestamp --freq '60min'

python scripts/dump_bin.py dump_all --csv_path C:\\Projects\\qlib_trading_v2\\csv_data\\CRYPTODATA_RESAMPLE\240min --qlib_dir C:\\Projects\\qlib_trading_v2\\qlib_data\\CRYPTODATA --include_fields open,close,high,low,volume --date_field_name timestamp --freq '240min'


python scripts/dump_bin.py dump_all --csv_path C:\\Projects\\qlib_trading_v2\\csv_data\\GDELT_BTC_MERGED --qlib_dir C:\\Projects\\qlib_trading_v2\\qlib_data\\CRYPTODATA2 --include_fields RawVol_Back_To_The_70s,RawVol_Environment,RawVol_Geopolitical_Risk,RawVol_Monetary,RawVol_Roaring_20s,RawVol_Secular_Stagnation,RawVol_Social,CWT_Back_To_The_70s,CWT_Environment,CWT_Geopolitical_Risk,CWT_Monetary,CWT_Roaring_20s,CWT_Secular_Stagnation,CWT_Social,btc_dom,fg_index --date_field_name date --freq 'day'



c:\Projects\qlib_trading\csv_data\GDELT_MERGED


GDELT_FEAT	2017-01-31	2025-04-08 """

#    BTC pairs (BCH, ETH, LTC, UNI)
#    USDT pairs (AAVE, BCH, BTC, DOGE, ETH, LINK, LTC, SUSHI, UNI, YFI)
#    USDC pairs (AAVE, AVAX, BAT, BCH, BTC, CRV, DOGE, DOT, ETH, GRT, LINK, LTC, MKR, SHIB, SUSHI, UNI, XTZ, YFI)
#    USD pairs (AAVE, AVAX, BAT, BCH, BTC, CRV, DOGE, DOT, ETH, GRT, LINK, LTC, MKR, SHIB, SUSHI, UNI, USDC, USDT, XTZ, YFI)

""" (gecko_env_3_11) C:\Projects\q50_validation_process\scripts>python dump_bin.py dump_all --help
INFO: Showing help with the command 'dump_bin.py dump_all -- --help'.

NAME
    dump_bin.py dump_all

SYNOPSIS
    dump_bin.py dump_all COMMAND | VALUE | --data_path=DATA_PATH --qlib_dir=QLIB_DIR <flags>

ARGUMENTS
    DATA_PATH
        Type: str
    QLIB_DIR
        Type: str

FLAGS
    -b, --backup_dir=BACKUP_DIR
        Type: Optional[str]
        Default: None
    --freq=FREQ
        Type: str
        Default: 'day'
    -m, --max_workers=MAX_WORKERS
        Type: int
        Default: 16
    -d, --date_field_name=DATE_FIELD_NAME
        Type: str
        Default: 'date'
    --file_suffix=FILE_SUFFIX
        Type: str
        Default: '.csv'
    -s, --symbol_field_name=SYMBOL_FIELD_NAME
        Type: str
        Default: 'symbol'
    -e, --exclude_fields=EXCLUDE_FIELDS
        Type: str
        Default: ''
    -i, --include_fields=INCLUDE_FIELDS
        Type: str
        Default: ''
    -l, --limit_nums=LIMIT_NUMS
        Type: Optional[int]
        Default: None

COMMANDS
    COMMAND is one of the following:

     get_datetime_index

VALUES
    VALUE is one of the following:

     ALL_MODE

     CALENDARS_DIR_NAME

     DAILY_FORMAT

     DUMP_FILE_SUFFIX

     FEATURES_DIR_NAME

     HIGH_FREQ_FORMAT

     INSTRUMENTS_DIR_NAME

     INSTRUMENTS_END_FIELD

     INSTRUMENTS_FILE_NAME

     INSTRUMENTS_SEP

     INSTRUMENTS_START_FIELD

     UPDATE_MODE

 """
