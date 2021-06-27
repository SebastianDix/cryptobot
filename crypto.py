#!python
import os
import csv
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from pprint import pprint as pp
currency_pair = 'BTCUSDT'
api_key=os.environ.get('api_key')
api_secret=os.environ.get('api_secret')
client = Client(api_key, api_secret)
# get market depth
klines = client.get_historical_klines(currency_pair, Client.KLINE_INTERVAL_1MINUTE, "1 year ago UTC")

with open('1_year_klines.csv', 'w', newline='') as csvfile:
    kline_writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])	
    for kline in klines:
        kline_writer.writerow(kline)

# exit()
# depth = client.get_order_book(symbol=currency_pair)
# place a test market buy order, to place an actual order use the create_order function
# order = client.create_test_order(
#         symbol=currency_pair,
#         side=Client.SIDE_SELL,
#         type=Client.ORDER_TYPE_MARKET,
#         quantity=0.01)

# pp(dir(order))
# get all symbol prices
# prices = client.get_all_tickers()
# pp(prices)
