from BuscaUser import BuscarUsuarios
from write import AddUser
from removeUser import RemoveUser

print('Escolha uma Opção:\n')
print('1.Adicionar Usuário.\n')
print('2.Remover Usuário.\n')
print('3.Visualizar Usuários Existentes.')
option = input()

if(option == "1"):
    print("Teste    ")
    AddUser()

elif(option == "2"):
    print("Teste 2")
    names = RemoveUser()
    for name in names:
        print(name + "\n")

elif(option == "3"):
    print("Teste 3")
    names = BuscarUsuarios()
    for name in names:
        if( name != name[0]):
            print(name +"\n")
