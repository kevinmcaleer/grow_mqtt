from datetime import datetime

import paho.mqtt.client as mqtt
import json
from time import sleep

now = datetime.now()

# date_string =  now.strftime("%m/%d/%Y, %H:%M:%S")

enviro_stub = {
    "temperature": 21.1,
    "humidity": 90.1,
    "pressure": 1111,
    "luminance": 1000,
    "moisture_a": 50,
    "moisture_b": 60,
    "moisture_c": 60
  }

def update_payload():
    now = datetime.now()
    date_string =  now.strftime("%m/%d/%Y, %H:%M:%S")
    payload = {
        "nickname": "Enviro Stub",
        "timestamp": date_string,
        "readings": enviro_stub,
        "model": "grow",
        "uid": "enviro-stub123465432"
    }
    return payload

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("grow/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.152", 1883, 60)

# publish(topic, payload=None, qos=0, retain=False)

while True:
    payload = update_payload()
    client.publish("enviro/envirogrow01", json.dumps(payload))
    print('published: ' + json.dumps(payload))
    sleep(2)

