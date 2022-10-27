import joblib


def BuscarUsuarios():

    names = joblib.load('places.sav')
    return names
