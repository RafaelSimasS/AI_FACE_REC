import paho.mqtt.client as mqtt
import random
import time

topic = "teste"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# Conectar ao Broker MQTT


def on_connect(client, userdata, flags, rc, self):
    print("Conexão estabelecida com código: ", rc)
    client.subscribe(topic)


def on_message(client_, userdata, message):
    print("mensagem: ",  message.payload.decode())


client = mqtt.Client(client_id=client_id,
                     transport="websockets", protocol=mqtt.MQTTv5)

client.on_connect = on_connect
client.on_message = on_message  
client.ws_set_options(path="/mqtt")


client.connect("broker.emqx.io", 8083)