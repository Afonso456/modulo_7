"""
Programa que lê uma frase do utilizador em ingles e verifica se existe no dicionario
"""

import os

NOME_F = 'words_alpha.txt'

def existe_ficheiro():
    if os.path.exists(NOME_F):
        return True
    return False

def ler_frase():
    texto = input('Insira uma frase em ingles:')
    texto = texto.strip().lower()
    return texto.split(' ')

def ler_ficheiro():
    with open(NOME_F,'r',encoding='UTF8') as ficheiro:
        #remover o \n no final das linhas
        linhas = ficheiro.readlines()
        return linhas

def verificar_palavras(palavras,dicionario):
    erro = False
    for palavra in palavras:
        if palavra+'\n' not in dicionario:
            #adicionar \n pq exite naspalavra do dicionario
            print(f'A palavra {palavra} não existe no dicionario')
            erro = True
    if erro == False:
        print('A frase não contem erros')

def main():
    if existe_ficheiro() == False:
        print('O ficheiro não existe')
        return
    frase = ler_frase()
    dicionario = ler_ficheiro()
    verificar_palavras(frase,dicionario)
if __name__ == '__main__':
    main()