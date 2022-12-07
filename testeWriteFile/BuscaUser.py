import joblib


def BuscarUsuarios():

    names = joblib.load('names.sav')
    for name in names:
            if (name != names[0]):
                print(name + "\n")
    return 0
