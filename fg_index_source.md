Fear and Greed Index API
Rules:

    You may not use our data to impersonate us or to create a service that could be confused with our offering.
    You must properly acknowledge the source of the data and prominently reference it accordingly.
    Commercial use is allowed as long as the attribution is given right next to the display of the data. Please contact us in case of questions.
    This applies to all of our fear and greed data, not just the API.

API: https://api.alternative.me/
Endpoint: /fng/
Method: GET
Description: Get the latest data of the Fear and Greed Index.
Optional Parameters:

    limit, [int]: Limit the number of returned results. The default value is '1', use '0' for all available data. Please note that the field "time_until_update" will only be returned for the latest value ( in other words: when the value '1' is used).
    format, [string]: Choose to either receive the data part formatted as regular JSON or formatted as CSV for easy pasting in spreadsheets, use either 'json' or 'csv' respectively. The default is 'json'.
    date_format, [string]: Choose to either receive the date part formatted for the United States (MM/DD/YYYY), for China and Korea (YYYY/MM/DD) or for the rest of the world (DD/MM/YYYY). Use 'us', 'cn', 'kr' or 'world' respectively. The default is an empty string which will return the date in unixtime, unless format is set to 'csv'. When "format" is set to 'csv' the default "date_format" is 'world'.

Example URL: https://api.alternative.me/fng/
Example URL: https://api.alternative.me/fng/?limit=10
Example URL: https://api.alternative.me/fng/?limit=10&format=csv
Example URL: https://api.alternative.me/fng/?limit=10&format=csv&date_format=us


# source:

https://api.alternative.me/fng/?limit=0&format=csv&date_format=us

