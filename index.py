#!/usr/bin/env python3
#from pprint import pprint
from bitshares.account import Account
from bitshares.market import Market
import time
market = Market("BTS:CNY")
while True:
    print(market.ticker()["latest"])
    time.sleep(5)

