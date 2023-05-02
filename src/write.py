import joblib
from namesModuleChecker import find
from time import sleep
import os
    # Esta função adiciona um nome de usário informado pelo pelo usuário ao arquivo names.sav
def AddUser():
    names = []
    path_atual = os.path.dirname(__file__)
    path_atual = path_atual + "\\"
    result = find('names.sav', path_atual)
    # Busca se há algum arquivo chamado names.sav
    
    if( len(result) == 0 ):
        # Caso não encontre o arquivo, será criado um com o mesmo nome
        open("./names.sav", "x")
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