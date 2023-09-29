import os
from .utils import load_json, update_json, center_text, format_option, prompt_input_select, show_temp_message

    # Está função remove um nome de usuário já cadastrado
def RemoveUser():

    file_path = os.path.realpath("./src/names.json")
    if not os.path.exists(file_path):
        show_temp_message("Error - Não foi possível encontrar a base de dados.")
        return

    data_dict: dict = load_json(file_path)
    names: list = data_dict.get('users',[])
    
    if not names:
        show_temp_message("A lista de usuários está vazia.")
        return

    max_user_name_width = max(len(dataset_name.capitalize()) for dataset_name in names)

    for number, user_name in enumerate(names, start=1):
        formatted_option = format_option(number, user_name, max_user_name_width)
        print(center_text(formatted_option, max_user_name_width * "#", 3))

    last_option = len(names) + 1
    print(center_text(format_option(last_option, "Retornar para o Menu Principal", max_user_name_width), max_user_name_width * "#", 3))
    choice = prompt_input_select("Selecione o Usuário que deseja remover: ", range(1, last_option + 1))

    if choice == last_option:
        return
    else:
        removed_user = names.pop(choice - 1)

        data_dict['users'] = names
        update_json(file_path, data_dict)
        show_temp_message(f"O usuário '{removed_user}' foi removido com sucesso.")
    