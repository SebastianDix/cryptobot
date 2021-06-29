#!python
import os
import csv
import numpy
from numpy import genfromtxt
import talib
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from pprint import pprint as pp
from flask import Flask, render_template, url_for
from operator import itemgetter # helps sort list of tuples faster than lambda, see https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index

api_key=os.environ.get('api_key')
api_secret=os.environ.get('api_secret')
client = Client(api_key, api_secret)

app = Flask(__name__)

# tickers = 
# [{'price': '0.05547700', 'symbol': 'ETHBTC'},
#   {'price': '0.00383300', 'symbol': 'LTCBTC'},
#  {'price': '0.00827400', 'symbol': 'BNBBTC'},
tickers = client.get_all_tickers()
def getEurPriceForAsset(assetName,tickers):
    for ticker in tickers:
        if ticker['symbol'] == assetName+"EUR":
            return ticker['price']
        else:
            return None



balances = client.get_account()['balances']
balances = [(b['asset'],float(b['free'])) for b in balances if float(b['free']) != float(0)]
balances.sort(key=itemgetter(2))
print(balances)

exit()

for b in balances:
    # print(type(int(b['free'])))
    print(float(b['free']))

@app.route('/')
def index():
    return render_template("index.html",balances=balances)

if __name__ == '__main__':
    app.run(debug=True)
