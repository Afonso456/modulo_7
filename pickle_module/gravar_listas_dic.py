"""Programa que utiliza o modulo pickle para guardar uma lista num ficheiro binario"""

import pickle

#lista de dados a guardar
lista = [1,2,3,
         'quatro',
         {'nome':'cinco','email':'cinco@gmail.com'},
         6]

#guardar a lista no ficheiro
with open('lista.pkl','wb') as f:
    pickle.dump(lista,f)

print('Dados guardados com sucesso')