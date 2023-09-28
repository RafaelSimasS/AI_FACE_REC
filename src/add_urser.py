from .utils import load_json, update_json, center_text, show_temp_message, clear_prompt

import os
    # Esta função adiciona um nome de usário informado pelo pelo usuário ao arquivo names.json
def AddUser():
    clear_prompt()
    names: list = []
    data_dict: dict = {}
    # Busca se há algum arquivo chamado names.json
    file_path = os.path.realpath("./src/names.json")

    if not os.path.exists(file_path):
        # Caso não encontre o arquivo, será criado um com o mesmo nome
        print("A base de nomes não foi encontrada...")
        print("Criando Uma Nova...\n")

        input_name = input("Digite o nome da pessoa a ser adicionada (Pressione Enter com valor vazio para Voltar): ")
        if not input_name:
            show_temp_message("Voltando para o Menu Principal")
            return
        names.append(input_name)
        data_dict["users"] = names

        try:
            update_json(file_path, data_dict)
            show_temp_message(f"Usuário {input_name} inserido com sucesso")
        except Exception as e:
            show_temp_message(f"Ocorreu um erro ao tentar adicionar o usuário {input_name}. Error: {e}", 3)

    else:
        data_dict = load_json(file_path)
        names = data_dict.get('users', [])
        
        input_name = input('Digite o nome da pessoa a ser adicionada (Pressione Enter com valor vazio para Voltar): ')

        if not input_name:
            show_temp_message("Voltando para o Menu Principal")
            return
        
        names.append(input_name)
        data_dict["users"] = names
        try:
            update_json(file_path, data_dict)
            show_temp_message(f"Usuário {input_name} inserido com sucesso")
        except Exception as e:
            show_temp_message(f"Ocorreu um erro ao tentar adicionar o usuário {input_name}. Error: {e}", 3)
