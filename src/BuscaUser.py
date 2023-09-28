from .utils import load_json, update_json, center_text, show_temp_message, clear_prompt, is_path_exist
import os
def buscar_usuarios():  
    file_path = os.path.realpath("./src/names.json")
    if not is_path_exist(file_path):
        show_temp_message("Base de nomes não existente.")
        return
    
    data_dict: dict = load_json(file_path)

    names = data_dict.get('users', [])
    if not names:
        show_temp_message("Lista de Usuários Vazia")
        return
    for name in names:
        print(name)
    input("Pressione enter para voltar: ")
