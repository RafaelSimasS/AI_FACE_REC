import joblib
import namesModuleChecker as nc

def AddUser():
    names = []
    result = nc.find('names.sav', 'C:/Users/Sparq/Documents/Programação/Python/AI_REC/testeWriteFile/')
    isNameExist = len(result)
    if( isNameExist == 0 ):
        open("names.sav", "x")
        print("A base de nomes não foi encontrada...")
        print("Criando Uma Nova...")
        names.append("None")
        joblib.dump(names, 'names.sav')
    else:
        
        names = joblib.load('names.sav')

        inputName = input('Insira um nome: ')
        names.append(inputName)

        joblib.dump(names, 'names.sav')