# Thought Process:

I am documenting the data validation process to assemble a Case Study.

> https://github.com/snogcel/q50_validation_process/commits/main/


# Lead Generation Campaign

Start Date: \[October 7th, 2025]\
End Date: \[December 27th, 2025 - 12 weeks from start]

## Campaign Overview

### Goal: Establish Black Circle Technologies, LLC as the technical support provider for an open source data collection platform.

This campaign will establish Black Circle Technologies, LLC as the technical support provider for enterprise-grade DeFi data collection and analysis (see <a href="https://github.com/snogcel/geckoterminal_collector">geckoterminal_collector</a>, an open-source product I have developed). The primary objectives are to increase brand awareness within the blockchain development and institutional finance sectors and to generate qualified leads. By showcasing our platform's technical superiority—including automated market opportunity detection, exceptional system reliability, and seamless multi-network integration—we aim to attract high-value clients looking for a competitive edge in the DeFi space.

## Objectives

1. **Lead Generation:** Generate 150 qualified leads (MQLs) from target organizations by the end of the 12-week campaign.
2. **Brand Awareness:** Increase website traffic by 40% and achieve 500 new followers across LinkedIn and Twitter combined.
3. **Engagement:** Secure 50 registrations for our educational webinar on why Data Collection is incredibly important.

## Target Audience

### Primary Audience: Institutional Trading Firms & Hedge Funds

These organizations require robust, real-time, and highly accurate data analysis tools to execute quantitative trading strategies in the DeFi market.

- **Pain Points:** Manual data collection is slow, error-prone, and resource-intensive. Existing solutions lack enterprise-grade reliability, leading to missed opportunities and significant financial risk. They struggle with effective risk management, including impermanent loss and high drawdowns.
- **Needs:** A platform that automates opportunity detection, provides reliable and accurate data feeds, integrates with existing quantitative models (like QLib), and demonstrates proven backtesting results.

### Secondary Audience: DeFi Protocol Development Teams

These teams build and maintain DeFi protocols and require deep market insights to optimize liquidity, enhance security, and ensure protocol stability.

- **Pain Points:** Difficulty in monitoring liquidity health, assessing risks like impermanent loss proactively, and understanding user behavior (e.g., whale activity) in real time.
- **Needs:** A comprehensive analytics tool that provides insights into liquidity stability, trader diversity, and arbitrage opportunities to improve capital efficiency and strengthen their protocol's market position.

## Key Messages

- **For All Audiences:** <a href="https://github.com/snogcel/geckoterminal_collector">GeckoTerminal Data Collector</a> is the definitive platform for enterprise-grade DeFi data collection and analysis, engineered for institutional-level performance and reliability.
- **Unmatched Speed and Automation:** Automate accurate market opportunity detection in under 30 seconds. Eliminate manual monitoring and reduce system maintenance by 90%.
- **Enterprise-Grade Reliability:** Achieve up to 99%+ availability and a 96% reduction in recovery time with our resilient, self-healing infrastructure.
- **Superior Strategic Insights:** Enhance your DeFi strategy with our multi-network architecture (Solana, Ethereum-ready) and integration-ready design, delivering a verifiable 67% win rate in backtested quantitative models.

## Deliverables

| Channel               | Asset                   | Description                                                                                                                                                                          | Distribution                                                                   |
| --------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| **Content Marketing** | Whitepaper              | A technical deep-dive on "Leveraging AI for Superior DeFi Trading Strategies," detailing our methodology and backtested results (23.7% return, 1.85 Sharpe ratio). | Gated download on a dedicated landing page, promoted via all channels.         |
| **Content Marketing** | Blog Post 1             | "Beyond the Hype: What Enterprise-Grade Reliability Means in DeFi" - focuses on our 99%+ uptime and self-healing infrastructure.                                                     | Company blog, LinkedIn, Twitter, industry forums.                              |
| **Content Marketing** | Blog Post 2             | "The <30-Second Advantage: How Real-Time Analytics Are Redefining DeFi Trading" - showcases our analytics pipeline and speed.                                                        | Company blog, LinkedIn, Twitter, industry forums.                              |
| **Content Marketing** | Case Study              | "How \[Trading Firm Type] Reduced Max Drawdown by 65% with GeckoTerminal Data Collector" - highlights tangible client benefits and ROI.                                                            | Website, email marketing to leads, sales enablement.                           |
| **Webinar**           | Live Webinar            | "Automating DeFi Advantage: A Technical Showcase" - A live demonstration of the platform, showing opportunity detection and QLib integration.                                            | Promoted via email, social media, and paid ads. Registration via landing page. |
| **Email Marketing**   | 4-Part Nurture Sequence | A sequence for new leads, delivering the whitepaper, case study, blog content, and a webinar invitation.                                                                             | Sent to leads who download the whitepaper or register for the webinar.         |
| **Social Media**      | Visual Content          | A series of infographics and short video clips for LinkedIn and Twitter, highlighting key metrics (e.g., <30s detection, 99%+ uptime, 67% win rate).                                 | Posted on LinkedIn and Twitter feeds.                                          |
| **Paid Advertising**  | Ad Campaigns            | Google Ads targeting keywords like "DeFi data API," "quantitative crypto trading." LinkedIn Ads targeting professionals at hedge funds and trading firms.                            | Google Search Network, LinkedIn.                                               |

## Timeline

- **Phase 1: Planning and Setup (Weeks 1-2)**

  - **Week 1:** Finalize campaign KPIs, set up analytics tracking, and define conversion goals.
  - **Week 2:** Develop a detailed content calendar and outline all deliverables.

- **Phase 2: Content Creation (Weeks 3-6)**

  - **Weeks 3-4:** Write and design the whitepaper, case study, and blog posts.
  - **Weeks 5-6:** Develop webinar presentation, create all social media visuals, and build email templates and landing pages.

- **Phase 3: Launch and Promotion (Weeks 7-10)**

  - **Week 7:** Launch paid ad campaigns. Publish first blog post and promote the whitepaper across social channels.
  - **Week 8:** Publish second blog post. Begin promoting webinar registration.
  - **Week 9:** Host the live webinar. Publish the case study and distribute it to attendees and leads.
  - **Week 10:** Distribute the webinar recording. Continue lead nurture sequences and social media promotion.

- **Phase 4: Analysis and Refinement (Weeks 11-12)**

  - **Week 11:** Conduct a mid-campaign analysis of all channel performance against KPIs. Optimize ad spend and targeting based on results.
  - **Week 12:** Compile a final campaign report detailing performance, lead quality, and key learnings. Formulate recommendations for future campaigns.


# Collect Crypto Data

Source 1 (BTCUSDT): https://www.cryptodatadownload.com/data/binance/

Source 2 (fg_index): https://alternative.me/

Source 3 (btc_dom): https://www.tradingview.com/symbols/BTC.D/

> For more information, users can refer to the [related document](https://qlib.readthedocs.io/en/latest/component/data.html#converting-csv-format-into-qlib-format)


### Identify which data set has the largest scope of data:

```bash
fg_index has a span of data from:

2/1/2018,30,Fear
...
10/6/2025,71,Greed
```

```bash
btcusdt_binance has a span of data from:

1.50293E+12,8/17/2017,BTCUSDT,4261.48,4485.39,4200.74,4285.08,795.150377,3454770.051,3427
...
1.75954E+12,10/4/2025,BTCUSDT,122232.21,122800,121510,122391,8208.16678,1002272903,1703590\
```

```bash
btc_dom has a span of data from:

3/31/2014 18:00,CRYPTOCAP:BTC.D,99.38055076,99.42670354,99.29683247,99.38465167,14938879.04
...
10/5/2025 18:00,CRYPTOCAP:BTC.D,59.31206475,59.36450805,59.08154877,59.08686448,77927102627
```

### adjust source data to fit existing QLib methods (1d interval) - Test Import fg_index

```bash
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\fg_index --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED_2 --include_fields fng_value --date_field_name date --freq 'day'
```

### adjust source data to fit existing QLib methods (1d interval) - Test Import BTCUSDT
```bash
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\btcusdt --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED_2 --include_fields Open,High,Low,Close,Volume_BTC,Volume_USDT,tradecount --date_field_name date --freq 'day'
```

### TODO - aligning hourly data with daily data is difficult.

### adjust source data to fit existing QLib methods (60min interval) - Test Import btcusdt
```bash
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\h\\btcusdt_adjust --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED_2 --include_fields Open,High,Low,Close,Volume_BTC,Volume_USDT,tradecount --date_field_name Date --freq '60min'
```

### adjust source data to fit existing QLib methods (1d interval) - Test Import btc_dom
```bash
python scripts/dump_bin.py dump_all --data_path C:\\Projects\\q50_validation_process\\data_csv\\d\\btc_dom --qlib_dir C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA_VALIDATED_2 --include_fields close --date_field_name date --freq 'day'
```

```bash
python scripts/check_data_health.py --qlib_dir 'C:\\Projects\\q50_validation_process\\qlib_data\\CRYPTODATA' check_data
```

### Work, a service provided in exchange for Goods and or Services.
### If you like what you do, you'll never work a day in your life.

### TO DO: Review Data Discrepency against: https://finance.yahoo.com/quote/USDT-BTC/history/?period1=1588809600&period2=1602028800

### next, review against previously completed work:

```bash
train_start_time = "2018-08-02"
train_end_time = "2023-12-31"
valid_start_time = "2024-01-01"
valid_end_time = "2024-09-30"
test_start_time = "2024-10-01"
test_end_time = "2025-04-01"
```

### Result - Validated Data:

```bash
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
```

### next, verify 60min data:

```bash  
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
```

### Then, document the features being created and used as part of this predictive model.

```bash
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
```

### Move Validated Data back to QLib_Trader_v2: https://github.com/snogcel/qlib_trading_v2/commit/71318d231875631352cbe35f55df41ac51ed28ea

### TO-DO: https://github.com/snogcel/qlib_trading_v2/commit/27e6e72db54e08a5c2fcaf63e7dfe0908aca744e

### Input Data Columns:

```bash
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
```

### TODO:


> https://github.com/snogcel/qlib_trading_v2/blob/main/hummingbot_backtest_results/metrics.json

> https://github.com/snogcel/qlib_trading_v2/commit/d17245f1b068a9ef52c2780f78454817cb323e8b

### Decision Trees at 11 depth at Q10, Q50, Q90 should provide the best predictive model.

TODO - validate new dataset

### Case Study Summary - https://www.geeksforgeeks.org/machine-learning/lightgbm-light-gradient-boosting-machine/

```bash
LightGBM Core Parameters

LightGBM’s performance is heavily influenced by the core parameters that control the structure and optimization of the model. Below are some of the key parameters:

    objective: Specifies the loss function to optimize during training. LightGBM supports various objectives such as regression, binary classification and multiclass classification.
    task: It specifies the task we wish to perform which is either train or prediction. The default entry is train.
    num_leaves: Specifies the maximum number of leaves in each tree. Higher values allow the model to capture more complex patterns but may lead to overfitting.
    learning_rate: Determines the step size at each iteration during gradient descent. Lower values result in slower learning but may improve generalization.
    max_depth: Sets the maximum depth of each tree.
    min_data_in_leaf: Specifies the minimum number of data points required to form a leaf node. Higher values help prevent overfitting but may result in underfitting.
    num_iterations: It specifies the number of iterations to be performed. The default value is 100.
    feature_fraction: Controls the fraction of features to consider when building each tree. Randomly selecting a subset of features helps improve model diversity and reduce overfitting.
    bagging_fraction: Specifies the fraction of data to be used for bagging (sampling data points with replacement) during training.
    L1 and L2: Regularization parameters that control L1 and L2 regularization respectively. They penalize large coefficients to prevent overfitting.
    min_split_gain: Specifies the minimum gain required to split a node further. It helps control the tree's growth and prevents unnecessary splits.
    categorical_feature : It specifies the categorical feature used for training model.
```

### How This Open Source Predictive Model Works:

```bash
CORE_LGBM_PARAMS = {
        "objective": "quantile",
        "metric": ["l1", "l2"], # , "l2", "l1" # "rmse"
        "boosting_type": "gbdt",
        "device": "cpu",
        "verbose": 1, # set to verbose for more logs (this is outrageously complex lol)
        "random_state": 141551, # https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
        "early_stopping_rounds": 500,
        "num_boost_round": 2250,         # Let early stopping decide
        "seed": SEED
    }

    GENERIC_LGBM_PARAMS = {       
        # Conservative learning settings for feature exploration
        "learning_rate": 0.1,           # Moderate learning rate
        # "num_leaves": 64,                # Balanced complexity
        # "max_depth": 8,                  # Reasonable depth for GDELT features
        
        # Regularization (moderate to prevent overfitting)
        "lambda_l1": 0.1,
        "lambda_l2": 0.1,
        
        # "min_data_in_leaf": 20, # remove constraint for tuning
        
        "feature_fraction": 0.8,         # Use 80% of features per tree
        "bagging_fraction": 0.8,         # Use 80% of data per iteration
        "bagging_freq": 5,
    }

    # INIT_QLIB_INSTANCE
    # pass multi_quantile_params into QLib architecture

    multi_quantile_params = {
        # 0.1: {'learning_rate': 0.060555113429817814, 'colsample_bytree': 0.7214813020361056, 'subsample': 0.7849919729082881, 'lambda_l1': 8.722794281828277e-05, 'lambda_l2': 3.220667556916701e-05, 'max_depth': 10, 'num_leaves': 224, **GENERIC_LGBM_PARAMS},
        # 0.5: {'learning_rate': 0.02753370821225369, 'max_depth': -1, 'lambda_l1': 0.1, 'lambda_l2': 0.1, **GENERIC_LGBM_PARAMS},
        # 0.9: {'learning_rate': 0.09355380738420341, 'max_depth': 10, 'num_leaves': 249, 'lambda_l1': 0.1, 'lambda_l2': 0.1, **GENERIC_LGBM_PARAMS}

        # 0.1: {**CORE_LGBM_PARAMS},
        # 0.5: {**CORE_LGBM_PARAMS},                
        # 0.9: {**CORE_LGBM_PARAMS} 

        # 11 is a good, even tree depth (see: https://www.geeksforgeeks.org/machine-learning/lightgbm-light-gradient-boosting-machine/)

        0.1: {'max_depth': 11, **CORE_LGBM_PARAMS},
        0.5: {'max_depth': 11, **CORE_LGBM_PARAMS},                
        0.9: {'max_depth': 11, **CORE_LGBM_PARAMS}

    }
```


### Fixed Data Alignment Issue:

```bash
(gecko_env_3_11) C:\Projects\q50_validation_process>conda run --name gecko_env_3_11 python c:/Projects/q50_validation_process/qlib_data_integrity_check.py
                               $btc_dom  $fg_index
instrument        datetime
gdelt_btc_feat_v2 2020-05-01  66.444366       40.0
                  2020-05-02  66.737556       40.0
                  2020-05-03  66.848862       45.0
                  2020-05-04  67.187782       44.0
                  2020-05-05  68.012733       40.0
                  2020-05-06  68.922737       42.0
                  2020-05-07  68.414680       49.0
                  2020-05-08  67.941666       55.0
                  2020-05-09  67.976028       56.0
                  2020-05-10  67.635994       48.0
                  2020-05-11  67.770149       40.0
                  2020-05-12  68.262764       39.0
                  2020-05-13  68.428902       41.0
                  2020-05-14  67.986221       40.0
                  2020-05-15  67.807632       44.0
                  2020-05-16  68.127090       41.0
                  2020-05-17  67.731743       40.0
                  2020-05-18  67.916229       50.0
                  2020-05-19  67.653633       50.0
                  2020-05-20  67.472656       52.0
                  2020-05-21  66.981354       49.0
                  2020-05-22  67.097946       42.0
                  2020-05-23  66.645592       40.0
                  2020-05-24  66.599747       43.0
                  2020-05-25  66.645515       41.0
                  2020-05-26  67.056747       39.0
                  2020-05-27  67.210938       39.0
                  2020-05-28  66.872803       41.0
                  2020-05-29  66.190613       48.0
                  2020-05-30  66.390572       48.0
                  2020-05-31  65.129715       51.0

[3200:MainThread](2025-10-08 08:09:13,779) INFO - qlib.Initialization - [config.py:452] - default_conf: client.
[3200:MainThread](2025-10-08 08:09:14,365) INFO - qlib.Initialization - [__init__.py:75] - qlib successfully initialized based on client settings.
[3200:MainThread](2025-10-08 08:09:14,365) INFO - qlib.Initialization - [__init__.py:77] - data_path={'__DEFAULT_FREQ': WindowsPath('C:/Projects/q50_validation_process/qlib_data/CRYPTODATA_VALIDATED_2')}```

### TO-DO: Debug Data Loaders

```bash
(gecko_env_3_11) C:\Projects\q50_validation_process>conda run --name gecko_env_3_11 python c:/Projects/q50_validation_process/qlib_data_integrity_check.py
                               $btc_dom  $fg_index
instrument        datetime
gdelt_btc_feat_v2 2020-05-01  66.444366       40.0
                  2020-05-02  66.737556       40.0
                  2020-05-03  66.848862       45.0
                  2020-05-04  67.187782       44.0
                  2020-05-05  68.012733       40.0
                  2020-05-06  68.922737       42.0
                  2020-05-07  68.414680       49.0
                  2020-05-08  67.941666       55.0
                  2020-05-09  67.976028       56.0
                  2020-05-10  67.635994       48.0
                  2020-05-11  67.770149       40.0
                  2020-05-12  68.262764       39.0
                  2020-05-13  68.428902       41.0
                  2020-05-14  67.986221       40.0
                  2020-05-15  67.807632       44.0
                  2020-05-16  68.127090       41.0
                  2020-05-17  67.731743       40.0
                  2020-05-18  67.916229       50.0
                  2020-05-19  67.653633       50.0
                  2020-05-20  67.472656       52.0
                  2020-05-21  66.981354       49.0
                  2020-05-22  67.097946       42.0
                  2020-05-23  66.645592       40.0
                  2020-05-24  66.599747       43.0
                  2020-05-25  66.645515       41.0
                  2020-05-26  67.056747       39.0
                  2020-05-27  67.210938       39.0
                  2020-05-28  66.872803       41.0
                  2020-05-29  66.190613       48.0
                  2020-05-30  66.390572       48.0
                  2020-05-31  65.129715       51.0
KeyError: 'label'

[40108:MainThread](2025-10-08 08:16:03,630) INFO - qlib.Initialization - [config.py:452] - default_conf: client.
[40108:MainThread](2025-10-08 08:16:04,320) INFO - qlib.Initialization - [__init__.py:75] - qlib successfully initialized based on client settings.
[40108:MainThread](2025-10-08 08:16:04,320) INFO - qlib.Initialization - [__init__.py:77] - data_path={'__DEFAULT_FREQ': WindowsPath('C:/Projects/q50_validation_process/qlib_data/CRYPTODATA_VALIDATED_2')}
[40108:MainThread](2025-10-08 08:16:04,355) INFO - qlib.timer - [log.py:127] - Time cost: 0.005s | Loading data Done
[40108:MainThread](2025-10-08 08:16:04,355) ERROR - qlib.workflow - [utils.py:41] - An exception has been raised[KeyError: 'label'].
  File "c:\Projects\q50_validation_process\qlib_data_integrity_check.py", line 173, in <module>
    dataset = init_instance_by_config(task_config["dataset"])
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\qlib\utils\mod.py", line 180, in init_instance_by_config
    return klass(**cls_kwargs, **try_kwargs, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\qlib\data\dataset\__init__.py", line 119, in __init__
    self.handler: DataHandler = init_instance_by_config(handler, accept_types=DataHandler)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\qlib\utils\mod.py", line 180, in init_instance_by_config
    return klass(**cls_kwargs, **try_kwargs, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\qlib\data\dataset\handler.py", line 509, in __init__
    super().__init__(instruments, start_time, end_time, data_loader, **kwargs)
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\qlib\data\dataset\handler.py", line 151, in __init__
    self.setup_data()
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\qlib\data\dataset\handler.py", line 660, in setup_data
    self.fit_process_data()
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\qlib\data\dataset\handler.py", line 528, in fit_process_data
    self.process_data(with_fit=True)
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\qlib\data\dataset\handler.py", line 608, in process_data
    _learn_df = self._run_proc_l(_learn_df, self.learn_processors, with_fit=with_fit, check_for_infer=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\qlib\data\dataset\handler.py", line 540, in _run_proc_l
    df = proc(df)
         ^^^^^^^^
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\qlib\data\dataset\processor.py", line 99, in __call__
    return df.dropna(subset=get_group_columns(df, self.fields_group))
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\qlib\data\dataset\processor.py", line 32, in get_group_columns
    return df.columns[df.columns.get_loc(group)]
                      ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\pandas\core\indexes\multi.py", line 3059, in get_loc
    loc = self._get_level_indexer(key, level=0)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\pandas\core\indexes\multi.py", line 3410, in _get_level_indexer
    idx = self._get_loc_single_level_index(level_index, key)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\pandas\core\indexes\multi.py", line 2999, in _get_loc_single_level_index
    return level_index.get_loc(key)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jon Kindel\.conda\envs\gecko_env_3_11\Lib\site-packages\pandas\core\indexes\base.py", line 3819, in get_loc
    raise KeyError(key) from err

ERROR conda.cli.main_run:execute(127): `conda run python c:/Projects/q50_validation_process/qlib_data_integrity_check.py` failed. (See above for error)
```

### Bug Fixed & Data Validated

> https://github.com/snogcel/q50_validation_process/commit/0afb99b8d172ee688f1c62a10b54220f6ad7f56d#diff-5d12afae98d94404e4b3dbbf3e033ffada6a6c0fd86d4c4bef400e1d3cc13861

```bash
    },
    "Volume_USDT": {
        "windows": [1],  # Only VOLUME1 (VOLUME2/3 removed due to high correlation)
    },
```






## Requirements

```bash
pip install -r requirements.txt
```

## Usage of the dataset
> *Crypto dataset only support Data retrieval function but not support backtest function due to the lack of OHLC data.*

## Collector Data


### Crypto Data

#### 1d from Coingecko

```bash

# download from https://api.coingecko.com/api/v3/
python collector.py download_data --source_dir ~/.qlib/crypto_data/source/1d --start 2015-01-01 --end 2021-11-30 --delay 1 --interval 1d

# normalize
python collector.py normalize_data --source_dir ~/.qlib/crypto_data/source/1d --normalize_dir ~/.qlib/crypto_data/source/1d_nor --interval 1d --date_field_name date

# dump data
cd qlib/scripts
python dump_bin.py dump_all --data_path ~/.qlib/crypto_data/source/1d_nor --qlib_dir ~/.qlib/qlib_data/crypto_data --freq day --date_field_name date --include_fields prices,total_volumes,market_caps

```

### using data

```python
import qlib
from qlib.data import D

qlib.init(provider_uri="~/.qlib/qlib_data/crypto_data")
df = D.features(D.instruments(market="all"), ["$prices", "$total_volumes","$market_caps"], freq="day")
```


### Help
```bash
python collector.py collector_data --help
```

## Parameters

- interval: 1d
- delay: 1
