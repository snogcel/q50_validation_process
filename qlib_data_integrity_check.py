import qlib
from qlib.constant import REG_US, REG_CN 
from qlib.utils import init_instance_by_config, flatten_dict

# Fixed imports using new src structure
from src.data.nested_data_loader import CustomNestedDataLoader
from src.data.crypto_loader import crypto_dataloader_optimized as crypto_dataloader
from src.data.gdelt_loader import gdelt_dataloader_optimized as gdelt_dataloader

from qlib.data.dataset.processor import Processor
from qlib.utils import get_callable_kwargs
from qlib.data.dataset import processor as processor_module
from inspect import getfullargspec
from qlib.data.dataset.handler import DataHandlerLP
from qlib.data import D

train_start_time = "2018-08-02"
train_end_time = "2023-12-31"
valid_start_time = "2024-01-01"
valid_end_time = "2024-09-30"
test_start_time = "2024-10-01"
test_end_time = "2025-04-01"

fit_start_time = None
fit_end_time = None

provider_uri = "/Projects/q50_validation_process/qlib_data/CRYPTODATA_VALIDATED_2"

SEED = 42 # RANDOM SEED for Entropy Purposes
MARKET = "all"
BENCHMARK = "BTCUSDT"
EXP_NAME = "crypto_exp_101"
FREQ = "day"

qlib.init(provider_uri=provider_uri, region=REG_US)

def check_transform_proc(proc_l, fit_start_time, fit_end_time):
        new_l = []
        for p in proc_l:
            if not isinstance(p, Processor):
                klass, pkwargs = get_callable_kwargs(p, processor_module)
                args = getfullargspec(klass).args
                if "fit_start_time" in args and "fit_end_time" in args:
                    assert (
                        fit_start_time is not None and fit_end_time is not None
                    ), "Make sure `fit_start_time` and `fit_end_time` are not None."
                    pkwargs.update(
                        {
                            "fit_start_time": fit_start_time,
                            "fit_end_time": fit_end_time,
                        }
                    )
                proc_config = {"class": klass.__name__, "kwargs": pkwargs}
                if isinstance(p, dict) and "module_path" in p:
                    proc_config["module_path"] = p["module_path"]
                new_l.append(proc_config)
            else:
                new_l.append(p)
        return new_l


if __name__ == '__main__': 


    # IGNORE
    
    df = D.features(
        ["gdelt_btc_feat_v2"],
        ["$btc_dom","$fg_index"],
        start_time="2020-05-01",
        end_time="2020-05-31"
    )

    print(df)

    raise SystemExit()

    # Case Study Research
    # see: https://www.geeksforgeeks.org/machine-learning/lightgbm-light-gradient-boosting-machine/


    # null data is being offset against the calendar.txt file

    # if a data loader is used, it can be preprocessed to eliminate null data.

    # now that we know that the data exists, we can use an existing data loader I wrote personally.

    # this is a perfect way to complete the task I planned to work on previously.


    freq_config = {
        "feature": "60min", 
        "label": "day"
    }

    inst_processors = [
        {
            "class": "TimeRangeFlt",
            "module_path": "qlib.data.dataset.processor",
            "kwargs": {
                "start_time": train_start_time,
                "end_time": test_end_time,
                "freq": freq_config["feature"]
            }
        }
    ]

    crypto_data_loader = {
        "class": "crypto_dataloader_optimized",
        "module_path": "src.data.crypto_loader",
        "kwargs": {
            "config": {
                "feature": crypto_dataloader.get_feature_config(),
                "label": crypto_dataloader.get_label_config(),                                                
            },                                            
            "freq": freq_config["feature"],  # "60min"
            "inst_processors": inst_processors
        }
    }

    gdelt_data_loader = {
        "class": "gdelt_dataloader_optimized",
        "module_path": "src.data.gdelt_loader",
        "kwargs": {
            "config": {
                "feature": gdelt_dataloader.get_feature_config()
            },
            "freq": freq_config["label"],  # "day"
            "inst_processors": inst_processors
        }
    }

    _learn_processors = [{"class": "DropnaLabel"},]
    _infer_processors = []

    infer_processors = check_transform_proc(_infer_processors, fit_start_time, fit_end_time)
    learn_processors = check_transform_proc(_learn_processors, fit_start_time, fit_end_time)

    handler_config = {
        "instruments": ["BTCUSDT"],
        "start_time": train_start_time,
        "end_time": test_end_time,                
        "data_loader": gdelt_data_loader,        
        "infer_processors": infer_processors,
        "learn_processors": learn_processors,
        "shared_processors": [],
        "process_type": DataHandlerLP.PTYPE_A,
        "drop_raw": False 
    }

    dataset_handler_config = {
        "class": "DataHandlerLP",
        "module_path": "qlib.data.dataset.handler",
        "kwargs": handler_config,
    }

    # finalized model after tuning
    task_config = {
        "dataset": {
            "class": "DatasetH",
            "module_path": "qlib.data.dataset",                        
            "kwargs": {
                "handler": dataset_handler_config,
                "segments": {
                    "train": (train_start_time, train_end_time),
                    "valid": (valid_start_time, valid_end_time),
                    "test": (test_start_time, test_end_time),
                },
            }
        }
    }

    dataset = init_instance_by_config(task_config["dataset"])

    # prepare segments
    df_train, df_valid, df_test = dataset.prepare(
        segments=["train", "valid", "test"], col_set=["feature", "label"], data_key=DataHandlerLP.DK_L
    )

    print(df_train)

    # df_train.to_csv('df_train_validate.csv')



