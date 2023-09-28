import cv2
import os
from .utils import load_json, center_text, show_temp_message, get_real_path, is_path_exist, prompt_input_select, format_option

def CadastrarRosto():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    
    file_path = get_real_path("./src/names.json")
    cascade_path = get_real_path("./src/haarcascade_frontalface_alt.xml")
    dataset_path = get_real_path("./src/dataset")
    
    if not is_path_exist(cascade_path):
        show_temp_message("Error - Arquivo Cascade Faltando.")
        return False
    
    if not is_path_exist(file_path):
        show_temp_message('ERROR - Não foi possível encontrar a base de usuários')
        return False
    
    if not is_path_exist(dataset_path):
        os.makedirs(dataset_path)

    names: list = []

    data_dict: dict = load_json(file_path) 
    names = data_dict.get("users", [])

    if not names:
        show_temp_message("Sem Usuários Cadastrados. Voltando para menu...")
        return False
    
    max_user_name_width = max(len(user_name.capitalize()) for user_name in names)

    for number, user_name in enumerate(names, start=1):
        formatted_option = format_option(number, user_name, max_user_name_width)
        print(center_text(formatted_option, max_user_name_width * "#", 3))

    last_option = len(names) + 1
    print(center_text(format_option(last_option, "Retornar para o Menu Principal", max_user_name_width), max_user_name_width * "#", 3))
    choice = prompt_input_select("Selecione o Usuário que deseja cadastrar o Rosto", range(1, last_option + 1))
    if choice == last_option:
        return False
    

    try:
        face_id = choice - 1
    except:
        show_temp_message("ERROR - Usuário não encontrado")
        return False

    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
    show_temp_message("\n Iniciando Camera...")

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
            cv2.imwrite( os.path.join(dataset_path, "User." + str(face_id) + '.' + str(count) + ".jpg"), gray[y:y+h, x:x+w] )
        
        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 3:  # Tira 100 fotos de amostra
            break
    show_temp_message("\n Coleta de Imagens Finalizada!")
    cam.release()
    cv2.destroyAllWindows()
    return True