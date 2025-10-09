# Leverage Existing QLib Research


# recreate custom QLib bin structure, and continuing validating approach.

# python scripts/dump_bin.py dump_all ... --symbol_field_name symbol

python scripts/dump_bin.py dump_all ... --symbol_field_name symbol

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



# python scripts/get_data.py qlib_data --target_dir ./qlib_data/us_data --region us


# test using yfinance to pull USDT and figure out what schema the CSV files should be in

# https://github.com/ranaroussi/yfinance

