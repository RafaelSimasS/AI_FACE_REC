import joblib


def buscar_usuarios():

    names = joblib.load('./names.txt')
    for name in names:
            if (name != names[0]):
                print(name)
    return 0
