from ast import While
import joblib

def AddUser():

    places = []
    places = joblib.load('places.sav')

    inputName = input('Insira um nome: ')
    places.append(inputName)

    joblib.dump(places, 'places.sav')
