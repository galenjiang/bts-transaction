#!/usr/bin/env python3
from pprint import pprint
from bitsharesapi.websocket import BitSharesWebsocket
# from bitshares.account import Account
# import time
# while True:
#     time.sleep(5)
# from bitshares import BitShares
# print(bitshares.info())

ws = BitSharesWebsocket(
    "wss://openledger.hk/ws",
    markets=[["1.3.0", "1.3.113"]],
    on_market=pprint,
)
ws.run_forever()