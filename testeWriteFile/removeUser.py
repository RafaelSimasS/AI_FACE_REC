import joblib


def RemoveUser():
    names = joblib.load('names.sav')
    return names