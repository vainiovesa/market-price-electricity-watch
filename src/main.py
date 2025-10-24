from datetime import datetime
from fetch import get_todays_prices

def write(prices:dict):
    with open("todays_prices.csv", "w") as file:
        for timestamp, price in prices.items():
            row = f"{timestamp};{price}"
            file.write(row + "\n")

def read():
    data = {}
    with open("todays_prices.csv", "r") as file:
        for row in file:
            timestamp, price = row.replace("\n", "").split(";")
            data[timestamp] = price
    return data

def get_price_now():
    current_time = datetime.now()
    date = current_time.strftime("%Y-%m-%d")
    check = date + " 00:15:00+03:00"
    data = read()

    if check not in data:
        # Data file contains old data
        todays_prices = get_todays_prices()
        write(todays_prices)
        data = read()

    quart_intervals = ["00", "15", "30", "45"]
    last_quart = "00"
    for interval in quart_intervals:
        if int(interval) <= int(current_time.minute):
            last_quart = interval

    fetchtime = f"{date} {current_time.hour}:{last_quart}:00+03:00"
    current_price = float(data[fetchtime])

    return current_price
