import cv2
import numpy as np
from PIL import Image
import os

# Caminho para diretório de armazenamento de amostras
def FaceTrainer():
    path = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml");

    # Função que pega as imagens e o endereço dos dados
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
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
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    # Salva o modelo treinado como o arquivo abaixo
    recognizer.write('trainer/trainer.yml') 

    print("\n {0} Rostos Treinados. Saindo...".format(len(np.unique(ids))))