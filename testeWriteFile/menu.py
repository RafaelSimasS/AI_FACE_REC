from BuscaUser import BuscarUsuarios
from write import AddUser
from removeUser import RemoveUser
from dataset_face import CadastrarRosto
from face_trainer import FaceTrainer
def menu():
    print('\n1.Adicionar Usuário.\n')
    print('2.Remover Usuário.\n')
    print('3.Visualizar Usuários Existentes.\n')
    print('4.Cadastrar Rosto de Usuário.\n')
    option = input("Escolha uma Opção: ")

    if (option == "1"):
        AddUser()

    elif (option == "2"):
        RemoveUser()


    elif (option == "3"):

        BuscarUsuarios()

    elif (option == "4"):
        CadastrarRosto()
        FaceTrainer()

    

menu()