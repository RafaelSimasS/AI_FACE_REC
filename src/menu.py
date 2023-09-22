from BuscaUser import buscar_usuarios
from add_urser import AddUser
from removeUser import RemoveUser
from dataset_face import CadastrarRosto
from face_trainer import FaceTrainer
from face_rec import main
import os
import time

def menu():
    while True:
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
            buscar_usuarios()
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear") 
        elif (option == "4"):
            # Função para cadastrar
            CadastrarRosto()
            FaceTrainer()
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear") 
        elif (option == "5"):
            main()
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear") 
        elif (option == "0"):
            break
        else:
            print("Opção inválida!")
            time.sleep(1) 
            os.system("cls") if os.name == "nt" else os.system("clear")


menu()
