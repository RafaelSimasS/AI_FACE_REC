import cv2
import numpy as np
from PIL import Image
import os
from .utils import show_temp_message, get_real_path, is_path_exist

# Função que treina a IA para assimilar um rosto com uma das amostras
def FaceTrainer():
# Caminho para diretório de armazenamento de amostras
    path = get_real_path('./src/dataset')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

    # Função que pega as imagens e o endereço das imagens
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L') # grayscale
            img_numpy = np.array(PIL_img,'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        return faceSamples,ids

    print ("\n Treinando Reconhecimento Facial. Espere...")
    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    # Salva o modelo treinado como o arquivo abaixo
    trainer_path = get_real_path('./src/trainer')
    if not is_path_exist(trainer_path):
        os.makedirs(trainer_path)
    recognizer.write(os.path.join(trainer_path, "trainer.yml")) 

    print(ids)
    show_temp_message( "\n {0} Rostos Treinados.".format( len( np.unique(ids) ) ) )
    input("Pressione enter para voltar para o menu:")