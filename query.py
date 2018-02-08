#!/usr/bin/env python3
from bitshares.market import Market

from bitshares.asset import Asset

market = Market("BTS:CNY")

bts = Asset("BTS")
cny = Asset("CNY")

def query_market():
    print(market.ticker()["latest"])

def query_asset():
    print(bts, cny)

query_asset()
