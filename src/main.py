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
