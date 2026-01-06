# Market price electricity watch

## Overview
This project uses [ENTSO-E Transparency Platform](https://transparency.entsoe.eu/) API to fetch European market price data for electricity.
A Flask app uses this data to control "traffic lights" to make electricity consumption management easier.

<img src="/assets/prices_22-10-2025.png" alt="Day prices" width="700" height="400">

**The market prices for electricity in Finland on the day of the creation of this project fetched with the program.**

## Instuctions
```bash
$ git clone git@github.com:vainiovesa/market-price-electricity-watch.git
$ cd market-price-electricity-watch
```
Get a personal API key from entso-e and put it in [this file](https://github.com/vainiovesa/market-price-electricity-watch/blob/1421b95e84684d6a98ebd0356050a95f58e060fa/src/config.py). Run the project

### With Docker
```bash
$ docker compose up
```

### Without Docker
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cd src
$ python3 app.py
```
