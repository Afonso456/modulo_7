"""Modulo que gerencia os utilizadores guardando os utilizadores num ficheiro binario"""

import utils,pickle,os

utilizadores = {}

def menu():
    op = 0
    os.system("cls")
    while op != 5:
        op = utils.menu(['Adicionar utilizador', 'Remover utilizador','Editar utilizador','Listar utilizadores', 'Sair'],'Menu de utilizadores')
        if op == 5:
            os.system("cls")
            break
        if op == 1:
            adicionar_utilizador()
        if op == 2:
            remover_utilizador()
        if op == 3:
            editar_utilizador()
        if op == 4:
            listar_utilizadores()
    guardar_dados()

def adicionar_utilizador():
    """Função para adicionar utilizadores"""
    nome = utils.ler_string(3,'Nome do utilizador a adicionar:')
    if nome not in utilizadores:
        utilizadores[nome] = {'habitos':{'habito':'',
                                         'total_dias':0,
                                         'dias_consecutivos':0}}
        print(f'Utilizador "{nome}" adicionado com sucesso')
    else:
        print(f'Utilizador "{nome}" já está registado.')

def remover_utilizador():
    """Função para remover utilizadores= {nome:{habitos:{habito}}}"""
    nome = utils.ler_string(3,'Nome do utilizador a remover:')
    if nome in utilizadores:
        del utilizadores[nome]
        print(f'Utilizador "{nome}" removido com sucesso')
    else:
        print(f'Utilizador {nome} não existe')

def editar_utilizador():
    """Função para editar utilizadores[nome] = {'habitos': [{'habito':{}} e guardar no ficheiro binario"""
    nome = utils.ler_string(3,'Nome do utilizador a pesquisar:')
    if nome in utilizadores:
        print(f'Utilizador encontrado')
        nome_editar = utils.ler_string(3,'Novo nome do utilizador:')
        if nome_editar not in utilizadores:
            utilizadores[nome_editar] = utilizadores[nome]
            del utilizadores[nome]
            print(f'Utilizador {nome} editado com sucesso')
            print(f'O novo nome do utilizador é {nome_editar}')
        else:
            print(f'Utilizador {nome_editar} já existe.')
    else:
        print(f'Utilizador {nome} não encontrado')
        guardar_dados()
        return

def listar_utilizadores():
    """Função para listar apenas os utilizadores"""
    print('Utilizadores:')
    if utilizadores:
        for nome in utilizadores:
            print(f' - {nome}')
    else:
        print('Nenhum utilizador registado')

def guardar_dados():
    """Função para guardar os dados dos utilizadores num ficheiro binario"""
    with open('dados.bin','wb') as f:
        pickle.dump(utilizadores,f)

def ler_dados():
    """Função para ler os dados dos utilizadores de um ficheiro binario"""
    if os.path.exists('dados.bin') == False:
        return
    with open('dados.bin','rb') as f:
        global utilizadores
        utilizadores =pickle.load(f)
        return utilizadores