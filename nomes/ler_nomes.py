import os

NOME_F = 'nomes.txt'

if os.path.exists(NOME_F) == False:
    print('O ficheiro não existe')
else:
    with open('nomes.txt','r',encoding = 'UTF8') as f:
        textos = f.readlines()

    for linha in textos:
        print(linha,end = '')