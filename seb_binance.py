#!python
import os
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from pprint import pprint as pp
from pprint import pformat as pf
from operator import itemgetter # helps sort list of tuples faster than lambda, see https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
from forex_python.converter import CurrencyRates

import time
start_time = time.time()

def vdir(obj):
    return pf([x for x in dir(obj) if not x.startswith('__')])

def get_Eur_Czk():
    return CurrencyRates().get_rate('EUR','CZK')


class Binance:
    def __repr__(self):
        return "Binance object: " + vdir(self)

    def __init__(self):
        api_key=os.environ.get('api_key')
        api_secret=os.environ.get('api_secret')
        self.client = Client(api_key, api_secret)
        print("After Binance INIT", round(time.time() - start_time,6), "seconds")

    def get_all_balances(self):
        print("After get all balances from binance client ", round(time.time() - start_time,6), "seconds")
        return self.client.get_account()['balances']

    def get_all_tickers(self):
        print("After get all tickers from binance client ", round(time.time() - start_time,6), "seconds")
        return self.client.get_all_tickers()



class Wallet:
    def __init__(self,binance=Binance()):
        self.binance = binance

    def gen_balances(self):
        for balance in self.binance.get_all_balances():
            s_asset = balance['asset']
            f_free = float(balance['free'])
            f_locked = float(balance['locked'])
            if f_free != 0 or f_locked != 0:
                yield (s_asset,f_free+f_locked)

    def get_usdt_values(self):
        values_usdt = []
        balance_dict=dict(self.gen_balances())
        asset_tuple=tuple(a+"USDT" for a in balance_dict.keys())
        # only get prices for assets we actually have
        for ticker in self.binance.get_all_tickers():
            pair_symbol = ticker['symbol']
            symbol = pair_symbol[:-4]
            price = float(ticker['price'])
            if pair_symbol == "EURUSDT":
                self.eurusdt = price
            if pair_symbol in asset_tuple:
                usdt_balance = balance_dict[symbol] * price
                values_usdt.append((symbol,usdt_balance))
        if balance_dict.get('USDT'):
            values_usdt.append(("USDT",balance_dict['USDT']))
        return values_usdt

    def get_eur_values(self):
        to_eur = lambda t: (t[0], t[1] / self.eurusdt)
        return list(map(to_eur,self.get_usdt_values()))
    
    def get_czk_values(self):
        eur_czk = float(get_Eur_Czk())
        to_czk = lambda t: (t[0], t[1] * eur_czk)
        return list(map(to_czk,self.get_eur_values()))
    
    def get_total_czk_value(self):
        return sum(map(lambda x: x[1],self.get_czk_values()))

