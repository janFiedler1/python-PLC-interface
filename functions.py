import datetime
import json
from pyads import ADSConnection


def send_message(self):
    message = {'text': self.text_input.text(), 'time': str(datetime.datetime.now())}
    plc_connection = ADSConnection('192.168.0.1.1.1', 851)
    plc_connection.open()

def button_clicked(self):
    print("hi")
