from BuscaUser import BuscarUsuarios
from write import AddUser
from removeUser import RemoveUser
from dataset_face import CadastrarRosto
from face_trainer import FaceTrainer
import os
import time

def menu():
    print('\n1.Adicionar Usuário.\n')
    print('2.Remover Usuário.\n')
    print('3.Visualizar Usuários Existentes.\n')
    print('4.Cadastrar Rosto de Usuário.\n')
    print('0.Sair.\n')
    option = input("Escolha uma Opção: ")

    if (option == "1"):
        # Função para adicionar nome de usuário
        AddUser()
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear") 
    elif (option == "2"):
        # Função para remover nome de usuário
        RemoveUser()
        time.sleep(1) 
        os.system("cls") if os.name == "nt" else os.system("clear")
    elif (option == "3"):

        # Função para buscar nome de usuários existentes
        BuscarUsuarios()
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear") 
    elif (option == "4"):
        # Função para cadastrar
        CadastrarRosto()
        FaceTrainer()
    elif (option == "0"):
        return 0
    menu()


menu()