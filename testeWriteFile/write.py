from ast import While
import joblib

places = []
places = joblib.load('places.sav')
if (type(places) == 'NoneType'):
    print('Teste')
    places = ['None']
inputName = input('Insira um nome: ')
places.append(inputName)

cont = places.count('')
print(f'Teste: {cont}')
# places = places.remove('')
# Dumps into file
joblib.dump(places, 'places.sav')
