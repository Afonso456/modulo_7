"""Programa que grava um dicionario com o modulo pickle"""

import pickle

#ler dados
nome = input('Nome:')
idade = input('Idade:')
email = input('Email:')

#criar dicionario
registo = {'nome':nome,                       
           'idade':idade,
           'email':email
            }

#guardar num ficheiro 
with open('so_um.pkl','ab') as f:
    #serialização
    pickle.dump(registo,f)

print('Dados adicionados')