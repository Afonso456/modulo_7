import os

NOME_F = 'produtos.txt'


def ficheiro_existe():
    if os.path.exists(NOME_F) == False:
        print('O ficheiro não existe')
        return False
    return True

def adicionar_produtos():
    with open(NOME_F,'a',encoding= 'UTF8') as f:
        nome = input('Nome do produto:')
        preco = float(input('Preço do produto:'))
        linha = f'{nome} - {preco}\n'
        f.write(linha)
        
def ler_produtos():
    if ficheiro_existe() == False:
        return
    with open(NOME_F,'r',encoding = 'UTF8') as f:
        while True:
            linha = f.readline()
            #EOF (end of file)
            if not linha:
                break
            partes = linha.split('-')
            nome = partes[0].strip()
            preco = float(partes[1].strip())
            print(f'Produto: {nome} - {preco}€')

def editar_produtos():
    #verificar se o ficheiro existe
    if ficheiro_existe() == False:
        return
    #ler nome do produo a editar
    produto = input('Introduza o nome do produto que deseja editar:')
    #abrir o ficheiro dos produtos para ler
    ficheiro_ler = open(NOME_F,'r',encoding= 'UTF8')
    #abrir o ficheiro temporario para ler
    ficheiro_escrever = open('temp.txt','w',encoding = 'UTF8')
    while True:
        #ler um produto
        linhas = ficheiro_ler.readline()
        if not linhas:
            break
        #verificar se é o produto a editar
        partes = linhas.split('-')
        if produto == partes[0].strip():
            #se sim ler os novos dados
            novo_nome = input('Novo nome do produto:')
            novo_preco = float(input('Novo preço do produto:'))
            linhas = f'{novo_nome} - {novo_preco}\n'
        #gravar no ficheiro temporario
        ficheiro_escrever.write(linhas)
    #fechar ambos os ficheiros 
    ficheiro_escrever.close()
    ficheiro_ler.close()
    #apagar o ficheiro produtos
    os.remove(NOME_F)
    #mudar o nome do ficheiro temporario para produtos
    os.rename('temp.txt',NOME_F)
    print('Produto editado com sucesso')

def apagar_produtos():
        #verificar se o ficheiro existe
    if ficheiro_existe() == False:
        return
    #ler nome do produo a editar
    produto = input('Introduza o nome do produto que deseja editar:')
    #abrir o ficheiro dos produtos para ler
    ficheiro_ler = open(NOME_F,'r',encoding= 'UTF8')
    #abrir o ficheiro temporario para ler
    ficheiro_escrever = open('temp.txt','w',encoding = 'UTF8')
    while True:
        #ler um produto
        linhas = ficheiro_ler.readline()
        if not linhas:
            break
        #verificar se é o produto a editar
        partes = linhas.split('-')
        if produto == partes[0].strip():
            continue
        #gravar no ficheiro temporario
        ficheiro_escrever.write(linhas)
    #fechar ambos os ficheiros 
    ficheiro_escrever.close()
    ficheiro_ler.close()
    #apagar o ficheiro produtos
    os.remove(NOME_F)
    #mudar o nome do ficheiro temporario para produtos
    os.rename('temp.txt',NOME_F)
    print('Produto apagado com sucesso')

def menu():
    op = 0
    while op != 5:
        op= int(input('1.Adicionar Produto\n2.Listar Produtos\n3.Editar Produtos\n4.Apagar Produtos\n5.Sair\n'))
        if op == 5:
            break
        if op == 1:
            adicionar_produtos()
        if op == 2:
            ler_produtos()
        if op == 3:
            editar_produtos()
        if op == 4:
            apagar_produtos()

if __name__ == '__main__':
    menu()