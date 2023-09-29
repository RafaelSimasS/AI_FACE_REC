from src.BuscaUser import buscar_usuarios
from src.add_urser import AddUser
from src.removeUser import RemoveUser
from src.dataset_face import CadastrarRosto
from src.face_trainer import FaceTrainer
from src.face_rec import *
from src.utils import *

def menu():
    while True:
        clear_prompt()
        print(center_title("MENU"))
        print(center_text('1. Adicionar Usuário.'))
        print(center_text('2. Remover Usuário.'))
        print(center_text('3. Visualizar Usuários Existentes.'))
        print(center_text('4. Cadastrar Rosto de Usuário.'))
        print(center_text('5. Sair.'))
        option = prompt_input_select("Escolha uma Opção", range(1, 6))
        if (option == 1):
            # Função para adicionar nome de usuário
            AddUser()
            clear_prompt()
        elif (option == 2):
            # Função para remover nome de usuário
            RemoveUser()
            clear_prompt()
        elif (option == 3):
            # Função para buscar nome de usuários existentes
            buscar_usuarios()
            clear_prompt()
        elif (option == 4):
            # Função para cadastrar
            if CadastrarRosto():
                FaceTrainer()
            else:
                continue
            clear_prompt()
        elif (option == 5):
            clear_prompt()
            break

if __name__ == "__main__":
    menu()