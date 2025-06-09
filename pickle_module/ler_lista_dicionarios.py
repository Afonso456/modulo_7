"""Leitura de um ficheiro pickle com uma lista"""

import pickle

#lista vazia
lista = []

with open('lista.pkl','rb')as f:
    lista = pickle.load(f)

print(lista)