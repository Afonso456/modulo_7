"""Programa para adicionar,listar,remover e marcar como concluidas as tarefas"""
import os


NOME_F = 'tarefas.txt'

def verifica():
    """Função para verificar se o ficheiro existe"""
    if os.path.exists(NOME_F):
        return True 
    return False

def adicionar():
    """Função para adicionar tarefas"""
    tarefa = input('Descrevaa tarefa que pretende adicionar:')
    data = input('Até quando pretende concluir a tarefa:')
    with open(NOME_F,'a',encoding= 'utf-8') as f:
        f.write(tarefa + '\n')
        f.write(data + '\n')
    print('Tarefa adicionada')

def listar():
    """Função para listar as tarefas enumerandoas"""
    if verifica() == True:
        with open(NOME_F,'r',encoding='utf-8') as f:
            linhas = f.readlines()
            print('---Tarefas---')
        for i in range(len(linhas)):
            linhas = linhas[i]
            print(i,linhas,)
    else:
        print('Ficheiro não existe')

def remover():
    """Função para remover tarefas"""
    if verifica() == False:
        print('Ficheiro não existe')
    else:
        tarefa_remover = input('Tarefa a remover:')
        ler = open(NOME_F,'r',encoding='utf-8')
        escrever = open('temp.txt','w',encoding='utf-8')
        while True:
            linhas = ler.readlines()
            if not linhas:
                break
            escrever.write(linhas)
        escrever.close()
        ler.close()
        os.remove(NOME_F)
        os.remane('temp.txt',NOME_F)
        print('Tarefa removida')

def concluida():
    """Função que recebe uma lista com as tarefas e marca como concluidas as pretendidaa pelo utilizador"""
    with open(NOME_F,'r',encoding='utf-8') as f:
        linhas = f.readlines()
        concluir = input('Tarefa a concluir:')
        for i in range(len(linhas)):
            if concluir in linhas[i]:
                linhas.remove(concluir)   
        f.write(linhas)

def main():
    op = 0
    while op != 5:
        op = input('1.Adicionar tarefa\n2.Listar tarefa\n3.Remover tarefas\n4.Marca concluida\n5.Sair\n')
        if op == '5':
            break
        if op == '1':
            adicionar()
        if op == '2':
            listar()
        if op == '3':
            remover()
        if op == '4':
            concluida()

if __name__ == '__main__':
    main()