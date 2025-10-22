from datetime import datetime, timedelta
import entsoe
import pandas as pd
import config

api_key = config.api_key
client = entsoe.EntsoePandasClient(api_key)

today = datetime.now()
tmrrw = today + timedelta(days=1)

today = today.strftime("%Y%m%d")
tmrrw = tmrrw.strftime("%Y%m%d")

start = pd.Timestamp(today, tz='Europe/Helsinki')
end = pd.Timestamp(tmrrw, tz='Europe/Helsinki')
country_code = "FI"

prices = client.query_day_ahead_prices(country_code, start, end)
prices = prices.to_dict()
