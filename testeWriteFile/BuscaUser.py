import joblib


def BuscarUsuarios():

    names = joblib.load('names.sav')
    return names
