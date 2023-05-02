import joblib
from time import sleep
import os
    # Esta função adiciona um nome de usário informado pelo pelo usuário ao arquivo names.txt
def AddUser():
    names = []
    # Busca se há algum arquivo chamado names.txt
    file_path = "./names.txt"
    if not os.path.exists(file_path):
        # Caso não encontre o arquivo, será criado um com o mesmo nome
        open("./names.txt", "x")
        sleep(2.00)
        print("A base de nomes não foi encontrada...")
        print("Criando Uma Nova...\n")
        names.append("None")
        inputName = input("Digite o nome da pessoa: ")
        names.append(inputName)
        # print(names)

        joblib.dump(names, "./names.txt")
    else:
        
        names = joblib.load('./names.txt')
        
        inputName = input('Insira um nome: ')
        names.append(inputName)

        joblib.dump(names, 'names.txt')