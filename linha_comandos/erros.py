"""
Programa que recebe uma frase\\palavra e guarda num ficheiro terminado caso eteja em branco
Programa para gravar e ler ficheiro de texto
Utilização:
    py erros.py -l [NOME_FICHEIRO] - o prograam deve abrir o ficheiro indicado ou o ficheiro predefenido
    py erros.py -a [NOME_FICHEIRO] - o programa deve adicionar ao ficheiro indicado ou ao ficheiro predefenido todas as linhas 
    que o utilizador que escreve até introduzir um linha em branco
"""

import os
import sys #fornece acesso aos parametros da linha de comandoa

NOME_F = 'frase.txt'

def adicionar():
    while True:
        frase = input('>>')
        if frase == '':
            break
        else:
            with open(NOME_F,'a',encoding='UTF8') as f:
                f.write(frase + '\n')
                print('Frase guardada com sucesso')

def ler():
    if os.path.exists(NOME_F) == False:
        print(f'Ficheiro {NOME_F} não existe')
        return
    with open(NOME_F,'r',encoding= 'UTF8' ) as f:
        linhas = f.readlines()
    for linha in linhas:
        print(linha,end= '')
    
def main():
    global NOME_F
    #ler os argumentos da linha de comandos
    if len(sys.argv) <= 1:
        print('Utilização: py erros.py -l | -a [NOME_FICHEIRO]')
        return
    if len(sys.argv) == 3:
        NOME_F = sys.argv[2]
    op = sys.argv[1]
    if op.lower() == '-a':
        adicionar()
    elif op.lower() == '-l':
        ler()
    else:
        print('Opção inválida')

if __name__ == '__main__':
    main()