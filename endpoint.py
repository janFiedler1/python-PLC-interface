import websocket
import json
import datetime

def on_message(ws, message):
    data = json.loads(message)
    print(f"Received message: {data}")
    print(f"Text: {data['text']}")
    print(f"Time: {data['time']}")

ws = websocket.WebSocketApp("ws://localhost:8765", on_message=on_message)
ws.run_forever()