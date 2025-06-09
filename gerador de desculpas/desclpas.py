"""Programa que recebe tres ficheiro de texto com desculpas e escolhe de cada um um desculpa aleatoria"""

import random
import os

F_INTRO   = 'intro.txt'
F_CULPADO = 'culpado.txt'
F_DESC    = 'desculpas.txt'

def escolhe_desculpa(ficheiro):
    if os.path.exists(ficheiro) == False:
        print('O ficheiro não existe')
        return ''
    with open(ficheiro, 'r',encoding= 'utf-8') as f:
        linhas = ficheiro.readlines()
    linha = random.choice(linhas)
    linha = linha.replace('\n','')
    return linha

print(escolhe_desculpa(F_INTRO) + ' ',end = '')
print(escolhe_desculpa(F_CULPADO) + ' ',end = '')
print(escolhe_desculpa(F_DESC) + ' ',end = '')
