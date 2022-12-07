import joblib
from namesModuleChecker import find

def RemoveUser():
    searchResult = find("names.sav", "C:/Users/Sparq/Documents/Programação/Python/AI_REC/testeWriteFile/")
    if  (len(searchResult) == 0):
        print("Error - Não foi possível encontrar a base de dados.")
        return 0
    else:
        names = joblib.load('names.sav')

        nameToExclude = input("Digite o nome de usário que deseja remover: ")
        names = names.remove(nameToExclude)

        joblib.dump(names, "names.sav")

        return 0
    