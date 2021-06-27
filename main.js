let kline_url = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m";
let binanceSocket = new WebSocket(kline_url);

binanceSocket.onmessage = function (event) {
	console.log(event.data)
}

