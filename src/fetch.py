from datetime import datetime, timedelta
import entsoe
import pandas as pd
import config

API_KEY = config.api_key
CLIENT = entsoe.EntsoePandasClient(API_KEY)

def get_todays_prices():
    today = datetime.now()
    tmrrw = today + timedelta(days=1)

    today = today.strftime("%Y%m%d")
    tmrrw = tmrrw.strftime("%Y%m%d")

    start = pd.Timestamp(today, tz='Europe/Helsinki')
    end = pd.Timestamp(tmrrw, tz='Europe/Helsinki')
    country_code = "FI"

    prices = CLIENT.query_day_ahead_prices(country_code, start, end)
    return prices.to_dict()
