import websocket
import json
import csv
import threading
from datetime import datetime

CSV_FILE = "ticks.csv"

def start_socket(symbol):
    socket_url = f"wss://stream.binance.com:9443/ws/{symbol}@trade"

    def on_message(ws, message):
        data = json.loads(message)
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                symbol.upper(),
                float(data["p"]),
                float(data["q"])
            ])

    def on_error(ws, error):
        print(f"{symbol} ERROR:", error)

    def on_open(ws):
        print(f"{symbol.upper()} socket connected")

    ws = websocket.WebSocketApp(
        socket_url,
        on_message=on_message,
        on_error=on_error,
        on_open=on_open
    )

    ws.run_forever()

# Write header ONCE
with open(CSV_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "symbol", "price", "qty"])

# Start both sockets
threading.Thread(target=start_socket, args=("btcusdt",), daemon=True).start()
threading.Thread(target=start_socket, args=("ethusdt",), daemon=True).start()

# Keep main thread alive
while True:
    pass
