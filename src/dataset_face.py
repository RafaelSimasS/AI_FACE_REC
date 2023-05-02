import cv2
import os
import joblib


def CadastrarRosto():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    
    file_path = "./names.txt"
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    names = []

    if not os.path.exists(file_path):
        print('ERROR - Não foi possível encontrar a base de usuários')
        return 0

    names = joblib.load(file_path)
    searchUser = input('\n Informe o nome do Usuário ==>  ')
    try:
        face_id = names.index(searchUser)
    except:
        print("ERROR - Usuário não encontrado")
        return 0

    # face_id = input('\n Entre com o id do Usuário ==>  ')
    print("\n Iniciando Camera...")

    count = 0
    while (True):
        ret, img = cam.read()
        # img = cv2.flip(img, -1) # Inverte a imagem

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1
            # Salva a Imagem capturada na pasta dataset
            cv2.imshow('image', img)
            cv2.imwrite("./dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])
        
        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 100:  # Tira 100 fotos de amostra
            break
    print("\n Coleta de Imagens Finalizada!")
    cam.release()
    cv2.destroyAllWindows()
    # return 0
