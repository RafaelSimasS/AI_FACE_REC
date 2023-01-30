from paho.mqtt import client as mqtt_client
import random
import time


# PARAMETROS MQTT
broker = 'borker.emqx.io'
port = 8083
topic = "/oi"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(
        client_id=client_id, transport="websockets", protocol=mqtt_client.MQTTv5)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.ws_set_options(path="/mqtt")

    def on_message(message):
        print("mensagem: " + message)

    client.on_message = on_message
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(5)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
# def subscribe(client):
#     while(True):
#         time.sleep(5)


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


run()
