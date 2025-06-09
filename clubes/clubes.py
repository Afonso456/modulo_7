"""
Programa que cria dois ficheiros com os socios de dois clubes e encontra socios que estejam nos dois clubes
"""
import os

NOME1 = 'tondela.txt'
NOME2 = 'academico.txt'

def socios_repetidos():
    if os.path.exists(NOME1) == False and os.path.exists(NOME2):
        with open(NOME1,'r',encoding='UTF8') as ficheiro:
            socios1 = ficheiro.readlines()
        with open(NOME2,'r',encoding= 'UTF8') as ficheiro:
            socios2 = ficheiro.readlines()
        
        #remover \n
        for i in range(len(socios1)):
            socios1[i] = socios1[i].replace('\n',',')
        for i in range(len(socios2)):
            socios2[i] = socios2[i].replace('\n',',')
        encontra = False
        for socio in socios1:
            if socio in socios2:
                print(f'{socio} É socio dos dois clubes')
                encontra = True
        if encontra == False:
            print('Não existem socios em ambos os clubes')

socios_repetidos()