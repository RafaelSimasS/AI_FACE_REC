import joblib
from namesModuleChecker import find
from time import sleep
    # Esta função adiciona um nome de usário informado pelo pelo usuário ao arquivo names.sav
def AddUser():
    names = []
    result = find('names.sav', 'C:/Users/Sparq/Documents/Programação/Python/AI_REC/testeWriteFile/')
    # Busca se há algum arquivo chamado names.sav
    
    if( len(result) == 0 ):
        # Caso não encontre o arquivo, será criado um com o mesmo nome
        open("names.sav", "x")
        sleep(2.00)
        print("A base de nomes não foi encontrada...")
        print("Criando Uma Nova...\n")
        names.append("None")
        joblib.dump(names, 'names.sav')
        names = joblib.load("names.sav")
        inputName = input("Digite o nome da pessoa: ")
        names.append(inputName)

        joblib.dump(names, "names.sav")
    else:
        
        names = joblib.load('names.sav')
        
        inputName = input('Insira um nome: ')
        names.append(inputName)

        joblib.dump(names, 'names.sav')