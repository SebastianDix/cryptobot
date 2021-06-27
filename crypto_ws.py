#!/usr/bin/env python
kline_url="wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
trade_url="wss://stream.binance.com:9443/ws/btcusdt@trade"
import websocket

def print_ws_message(wsapp, message):
    print(message)

# wsapp = websocket.WebSocketApp(kline_url, on_message=print_ws_message)
wsapp = websocket.WebSocketApp(kline_url, on_message=print_ws_message)
wsapp.run_forever()

