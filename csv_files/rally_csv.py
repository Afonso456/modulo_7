"""
Um programa que deixa adicionar pilotos e carros,litar os pilotos e carros e pesquisar os piloto\\carro ou carro\\piloto
"""
import csv
import os

F_PILOTOS = 'pilotos.csv'
F_CARROS  = 'carros.csv'

lista_carros = []
lista_pilotos = []

def escrever(lista,nome):
    chaves = lista[0].keys()

    with open(nome, 'w', encoding='utf-8',newline='') as f:
        #varavel para guardar no ficheiro indicando o nome do ficheiro e as chaves
        escrever = csv.DictWriter(f,fieldnames=chaves)
        #gravar o cabeçalho
        escrever.writeheader()
        #gravar os dados
        for i in range(len(lista)):
            #grava os dados correspondentes as chaves
            escrever.writerow(lista[i])
    return 

def ler(nome_ficheiro):
    #lista vazia para guardar os dados do ficheiro
    dados = []
    #verificar se o ficheiro existe
    if os.path.exists(nome_ficheiro) == False:
        print('Ficheiro não existe')
        return dados
    with open(nome_ficheiro,'r',encoding='utf-8') as f:
        #criaro objeto para ler o ficheiro
        ler = csv.DictReader(f)
        #percorrer cada linha do ficheiro e adicionar á lista
        for linha in ler:
            dados.append(linha)
    return dados

def verifica(matricula):
    """Função que rcebe a matricula do carro e devolve true se a matricula existe e false se não existir"""
    for i in range(len(lista_carros)):
        if lista_carros[i]['matricula'] == matricula:
            return True
        return False

def verifica_n_matricula(matricula):
    """Função que devolve o numero de pilotos de um carro"""
    contar = 0
    for p in lista_pilotos:
        if p['matricula'] == matricula:
            contar += 1
    return contar
        
def adicionar():
    """Função para adicionar um carro ou um piloto"""
    op = input('Adicionar [P]iloto ou [C]arro:')
    if not op:
        return
    if op in 'Cc':
        marca = input('Marca do carro:')
        modelo= input('Modelo do carro:')
        matricula = input('Matriula:')
        if verifica(matricula) == False:
            return
        carro ={'marca':marca,
                'modelo':modelo,
                'matricula':matricula}
        lista_carros.append(carro)
        escrever(lista_carros,F_CARROS)
        print('Carro adicionado com sucesso')
    if op in 'Pp':
        matricula = input('Matricula:')
        #verificar se a matricula existe
        if verifica(matricula) == False:
            print('Matricula não existe')
            return
        if verifica_n_matricula(matricula) >=2:
            print('O carro ja possui 2 pilotos')
            return
        nome= input('Nome do piloto:')
        idade = input('Idade:')
        pais = input('País:')
        piloto = {'nome':nome,
                  'idade':idade,
                  'pais':pais,
                  'matricula':matricula}
        lista_pilotos.append(piloto)
        escrever(lista_pilotos,F_PILOTOS)
        print('Piloto adicionado com sucesso')

def listar():
    """Função para listar os carros e pilotos"""
    op = input('Adicionar [P]iloto ou [C]arro:')
    if op in 'Cc':
        print(lista_carros)
    if op in 'Pp':
        print(lista_pilotos)

def pesquisar():
    """Função para pesquisar carros e pilotos"""
    matricula = input('Matricula do carro a pesquisar:')
    if matricula:
        #mostrar os pilotos do carro
        for p in range(len(lista_pilotos)):
            if lista_pilotos[p]['matricula'] == matricula:
                print(lista_pilotos[p])
    piloto = input('Nome do piloto a pesquisar:')
    if piloto:
        #mostrar os carros do piloto
        for p in lista_pilotos:
            if p['nome'] == piloto:
                for c in range(len(lista_carros)):
                    if lista_carros[c]['matricula']:
                        print(lista_carros[c])

def main():
    op = 0
    global lista_carros,lista_pilotos
    lista_carros = ler(F_CARROS)
    lista_pilotos = ler(F_PILOTOS)
    while op != 4:
        op= int(input('1.Adicionar\n2.Listar\n3.Pesquisar\n4.Sair\n'))
        if op == 1:
            adicionar()
        if op == 2:
            listar()
        if op == 3:
            pesquisar()
        if op == 4:
            break

if __name__ == "__main__":
    main()