import cv2           #Import opencv
import NameFind      # importe as cascatas de Haar para obter a detecção de rosto e olho
import paho.mqtt.client as mqtt
import time
import random
import mysql.connector
from datetime import date, datetime, timedelta
import requests
import sys
#import base64
import numpy as np
from time import sleep
#from t_enc import encode_64
#import json

####################################

# Mosquitto MQTT
username    = ""
password    = ""
broker_address  = "localhost"
port        = 1883

# Banco de dados MySql
user_mysql  = "root"
pwd_mysql   = "MYSECRET"
db_mysql    = "campainha"
port_mysql        = "3306"


Connected = False   #global variable 

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")
 
def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload) )


    cnx = mysql.connector.connect(user=user_mysql, password=pwd_mysql, database=db_mysql, port = port_mysql)
    cursor = cnx.cursor()
    
    query = ("INSERT INTO usuario "
           "(id, nome, timestamp) "
           "VALUES (%s, %s, %s, %s)")

    #query = ("INSERT INTO campainha "
    #        "(nome) "
    #        "VALUES (%s)")

    dados_recebidos = (msg.topic, msg.payload, str(int(time.time())))
    
    # Carrega e executa a query.
    cursor.execute(query, dados_recebidos)
    cnx.commit()
    
    # Encerra a conexÃ£o com o banco de dados.
    cursor.close()
    cnx.close()

    
def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

#------------------------------------------------

mqttc = mqtt.Client("clientidUnico")

# Assina as funções de callback
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

mqttc.username_pw_set(username=username, password=password)
mqttc.connect(broker_address, port=port)

mqttc.subscribe("nome", 0)

mqttc.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

######################################
face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')  # Classificador "face frontal" Haar Cascade
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml') # Classificador "olho" Haar Cascade

recognise = cv2.face.EigenFaceRecognizer_create(15,4000)  # creating EIGEN FACE RECOGNISER
recognise.read("Recogniser/trainingDataEigan.xml")                              # Carregar os dados de treinamento

Count = 0

# -------------------------     START THE VIDEO FEED ------------------------------------------
cap = cv2.VideoCapture(0)                                                       # Camera object
# cap = cv2.VideoCapture('TestVid.wmv')   # Video object
ID = 0
while True:
    ret, img = cap.read()                                                       # Read the camera object
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converta a câmera em cinza
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                         #Detecte os rostos e armazene as posições
    for (x, y, w, h) in faces:                                                  # Frames  LOCATION X, Y  WIDTH, HEIGHT
        # ------------ CONFIRMANDO QUE OS OLHOS ESTÃO DENTRO DO ROSTO MELHOR RECONHECIMENTO DE ROSTO É GANHO ------------------
        gray_face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))               # O rosto é isolado e cortado
        eyes = eye_cascade.detectMultiScale(gray_face)




            #img_jp = cv2.read("saved_faces/User." + str('face') + "." + str(Count) + ".jpg")
            
        
        for (ex, ey, ew, eh) in eyes:
            ID, conf = recognise.predict(gray_face)                              # Determine o ID da foto
            NAME = NameFind.ID2Name(ID, conf)
            NameFind.DispID(x, y, w, h, NAME, gray)


            value = "{} tocando a campainha".format(NAME)
            mqttc.publish("nome",value)
            time.sleep(1)


      #      if (x != 0):
       #         Count = np.random.randint(0, 999999)
        #        cv2.imwrite("saved_faces/User." + str('face') + "." + str(Count) + ".jpg", gray_face)
         #       caminho = "saved_faces/User." + str('face') + "." + str(Count) + ".jpg"
          #      img64 = encode_64(caminho)
           #     encoded_utf8 = str(img64)
            #    encoded_utf8 = f'data:image/jpeg;base64,{encoded_utf8[2:-1]}'
#
                 
 #               payload = json.dumps({"name": f"{NAME}", "screenshot": f"{encoded_utf8}"})

  #              newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
         
   #             res = requests.post("https://campainha-inclusiva-production.up.railway.app/feedbacks", data=payload, headers=newHeaders)
    #            print(res.text)
                
        

    cv2.imshow('EigenFace Face Recognition System', gray)                       # Show the video
    if cv2.waitKey(1) & 0xFF == ord('q'):                                       # Quit if the key is Q
        break
cap.release()
cv2.destroyAllWindows()
