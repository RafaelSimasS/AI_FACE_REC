import cv2
import numpy as np
import os
import joblib
import paho.mqtt.client as mqtt
import random
import time

# PARAMETROS MQTT
broker = '192.168.137.65'
port = 1883
topic = "isValid"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


""" 
_______________________________________________
# Conectar ao Broker MQTT
client = mqtt.Client("rasp-cam")
client.connect(broker)
time.sleep(2) 
_______________________________________________

"""


# IA
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
# iniciate id counter
id = 0
# Nomes Endereçados ao Id: example ==> Rafael: id=1,  etc
names = []
names = joblib.load("names.sav")
# Inicializa Camera em modo de Video
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video widht
cam.set(4, 480)  # set video height
# Define o tamanho da janela da Camera
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))

            """ 
            ______________________________________________________
            # Caso o rosto seja reconhecido manda uma mensagem via MQTT para o software
            client.publish(topic, f'{id} está na porta.')
            time.sleep(5) 
            _____________________________________________________
            """
        else:
            id = "Desconhecido"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(
            img,
            str(id),
            (x+5, y-5),
            font,
            1,
            (255, 255, 255),
            2
        )
        cv2.putText(
            img,
            str(confidence),
            (x+5, y+h-5),
            font,
            1,
            (255, 255, 0),
            1
        )

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # Pressionar "ESC" Para Sair do Video
    if k == 27:
        break

print("\n Saindo...")
cam.release()
cv2.destroyAllWindows()
