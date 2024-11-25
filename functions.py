import datetime
import json

class functions: 

    def send_message(self):
        message = {'text': self.text_input.text(), 'time': str(datetime.datetime.now())}
        self.ws.send(json.dumps(message))

    def on_message(self, ws, message):
        self.label.setText(f"Received message: {message}")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("WebSocket closed")

    def on_open(self, ws):
        print("WebSocket opened")
