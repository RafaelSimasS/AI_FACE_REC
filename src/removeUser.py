import joblib
import os
    # Está função remove um nome de usuário já cadastrado
def RemoveUser():

    file_path = "./names.txt"
    if not os.path.exists(file_path):
        print("Error - Não foi possível encontrar a base de dados.")
        return 0
    else:
        names = joblib.load(file_path)
        # print(names)
        nameToExclude = input("Digite o nome de usário que deseja remover: ")
        if nameToExclude in names:
            names.remove(nameToExclude)
            # print(names)
            joblib.dump(names, file_path)
        else:
            print("Este nome não existe na base de dados.")

        return 0
    