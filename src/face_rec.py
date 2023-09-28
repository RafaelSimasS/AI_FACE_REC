import cv2
import os
import paho.mqtt.client as mqtt
import random
import time
import json
import base64
from dotenv import load_dotenv
from utils import show_temp_message, get_real_path, is_path_exist, load_json

def face_rec():
    # IA
    recognizer_path = get_real_path('./trainer/trainer.yml')
    file_path = get_real_path("./names.json")
    dataset_path = get_real_path("./dataset")

    if not is_path_exist(file_path):
        show_temp_message('ERROR - Não foi possível encontrar a base de usuários')
        return False
    
    if not is_path_exist(recognizer_path):
        show_temp_message("Sem Modelo De Reconhecimento Treinado. Voltando para o menu . . .")
        return

    if not is_path_exist(dataset_path):
        os.makedirs(dataset_path)


    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(recognizer_path)

    cascadePath = "haarcascade_frontalface_alt.xml"
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX
    # Inicia contador Ids
    id = 0
    # Nomes Endereçados ao Id: exemplo ==> Rafael: id=1,  etc
    names: list = []

    data_dict: dict = load_json(file_path) 
    names = data_dict.get("users", [])

    if not names:
        show_temp_message("Sem Usuários Cadastrados. Voltando para menu...")
        return False
    
    # Inicializa Camera em modo de Video
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  
    cam.set(4, 480) 
    # Define o tamanho da janela da Camera
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    count = 0
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
                image_Path = os.path.join(dataset_path, "PlainUser." + str(id) + ".jpg")
                cv2.imwrite(image_Path, img)
                with open(image_Path, "rb") as image2bin:
                    encodedImageString = base64.b64encode(image2bin.read())
                    encodedImageString = encodedImageString.decode()
                try:
                    os.remove(image_Path)
                except FileNotFoundError:
                    print(f"File {image_Path} not found.")

                confidence = "  {0}%".format(round(100 - confidence))
                sendMessage = f'{id} esta na porta.'
                data = {
                    'message': sendMessage,
                    'image': encodedImageString,
                    'id': count
                }
                json_data = json.dumps(data, ensure_ascii=False)
                # print(json_data)
                client.publish(topic, json_data)
                count += 1
                time.sleep(5)

                """ 
                ______________________________________________________
                # Caso o rosto seja reconhecido manda uma mensagem via MQTT para o software
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

    show_temp_message("\n Saindo...")
    cam.release()
    cv2.destroyAllWindows()


# PARAMETROS MQTT

# Conectar ao Broker MQTT


env_path = os.path.realpath("../.env")
load_dotenv(env_path)
broker = str(os.getenv("MQTT_HOST"))
port = int(os.getenv("MQTT_PORT"))
topic = str(os.getenv("MQTT_TOPIC"))
client_id = f'python-mqtt-{random.randint(0, 1000)}'
client = mqtt.Client(client_id=client_id,
                    transport="websockets", protocol=mqtt.MQTTv5)

def on_connect(self, client, userdata, flags, rc):
    if rc == 0:
        print("Conexão estabelecida com sucesso")
        client.subscribe(topic)
    else:
        print("Falha na conexão com o código:", rc)
def on_message(client, userdata, message):
    print("mensagem: ",  message.payload.decode())

client.on_connect = on_connect
client.on_message = on_message
client.ws_set_options(path="/mqtt")


client.connect(broker, port)
client.loop_start()

face_rec()