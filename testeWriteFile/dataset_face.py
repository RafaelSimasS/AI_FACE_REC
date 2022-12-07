import cv2
import os
import joblib
from namesModuleChecker import find


def CadastrarRosto():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    names = []
    result = find('names.sav', 'C:/Users/Sparq/Documents/Programação/Python/AI_REC/testeWriteFile/')
    if( len(result) == 0 ):
        print('ERROR - Não foi possível encontrar a base de usuários')
        return 0

    names = joblib.load("names.sav")
    searchUser = input('\n Informe o nome do Usuário ==>  ')
    try: 
        face_id = names.index(searchUser)
    except:
        print("ERROR - Usuário não encontrado")
        return 0
        
    # For each person, enter one numeric face id

    # face_id = input('\n Entre com o id do Usuário ==>  ')
    print("\n Iniciando Camera...")
    # Initialize individual sampling face count
    count = 0
    while(True):
        ret, img = cam.read()
        # img = cv2.flip(img, -1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' +  
                        str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 100: # Take 30 face sample and stop video
            break
    # Do a bit of cleanup
    print("\n Coleta de Imagens Finalizada!")
    cam.release()
    cv2.destroyAllWindows()
    return 0