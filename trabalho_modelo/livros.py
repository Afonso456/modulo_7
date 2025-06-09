"""
Modulo de gestão dos livros
"""

import utils,os,pickle

#lista dos livros
livros = []
#lista de livros de exemplo

whitelist = ["id","estado","leitor","nr_emprestimos"] #campos inalteraveis

def get_livro(id):
    for livro in livros:
        if livro["id"] == id:
            return livro
    return None


def configurar():
    """Insere dados de exemplo"""
    livros_exemplo = [
        {"id":1,"titulo":"livro1","autor":"autor1","tema":"tema1","editora":"editora1","ano":2020,
        "estado":"disponivel","leitor":None,"nr_emprestimos":10},
        {"id":2,"titulo":"livro2","autor":"autor2","tema":"tema2","editora":"editora2","ano":2000,
        "estado":"disponivel","leitor":None,"nr_emprestimos":5},
        {"id":3,"titulo":"livro3","autor":"autor1","tema":"tema3","editora":"editora3","ano":1670,
        "estado":"disponivel","leitor":None,"nr_emprestimos":20}
        ]
    livros.extend(livros_exemplo)

def menu():
    """Submenu para gerir os livros"""
    op = 0
    while  op != 6:
        #os.system("cls")
        print("---Menu Livros---")
        op = utils.menu(["Adicionar","Listar","Editar","Apagar","Pesquisar","Voltar"],"Menu livros")
        if op == 6:
            break
        if op == 1:
            adicionar()
        if op == 2:
            listar(livros)
        if op == 3:
            editar()
        if op == 4:
            apagar()
        if op == 5:
            listar_pesquisa() 

def adicionar():
    """Função para adicionar novos livros"""
    #titulo
    titulo = utils.ler_string(3,"Titulo do livro:")
    #autor
    autor = utils.ler_string(3,"Autor(a) do livro:")
    #tema
    tema = utils.ler_string(3,"Tema do livro:")
    #editora
    editora = utils.ler_string(3,"Editora do livro:")
    #ano de edição
    ano = utils.ler_numero_inteiro_limites(1500,2030,"Introduza  o ano de edição:")
    #id
    id = 1
    if len(livros) > 0:
        id = livros[len(livros)-1]["id"] + 1 #gera o id a partir do id do ultimo livro
    novo = {
        "id":id,
        "titulo":titulo,
        "autor":autor,
        "tema":tema,
        "editora":editora,
        "ano":ano,
        "estado":"disponivel",
        "leitor":None,
        "nr_emprestimos":0
    }

    livros.append(novo)
    print(f"Livro adicionado com sucesso. Possui {len(livros)} livros")

def listar(lista_a_listar):
    """Função para listar todos os livros"""
    print("-" * 80)
    print("                           Lista de livros")
    print("-" * 80)
    for livro in lista_a_listar:
        print(f"ID:{livro['id']}  Titulo:{livro['titulo']}  Tema:{livro['tema']}  Autor:{livro['autor']}  Estado:{livro['estado']}")
        print("-" * 80)

def editar():
    """Função para editar livros"""
    #pesquisar o livro a editar
    livros_editar = pesquisar() 
    #mosrar os dados de cada livro encontrado
    if len(livros_editar) == 0:
        print("Não foi encontado nenhum livro")
        return
    #mostrar todos os livros
    listar(livros_editar)
    #perguntar o id do livro a editaar
    id = utils.ler_numero_inteiro("Introduza o id do livro a editar ou 0(zero) para cancelar:")
    if id == 0:
        return
    #livro com o id indicado
    livro = None
    for l in livros_editar:
        if l["id"] == id:
            livro = l
            break
        if livro is None:
            print("ID não existe")
            return
    #permitir alterar os dados
    lista_campos = list(livro.keys())
    #remover os campos que não podem ser alterados
    for c in whitelist:
        lista_campos.remove(c)
    op = utils.menu(lista_campos,"Campo a editar:")
    #mostrar o valor atual do campo a editar
    campo = lista_campos[op-1]
    print(f"O campo {campo} tem o valor {livro[campo]}")
    #perguntar o novo valor
    novo_valor = utils.ler_string(3,"Novo valor:")
    #atualizar o valor do campo
    livro[campo] = novo_valor
    #mostrar os dados do livro atualizados
    print(f"O livro {livro['titulo']} foi atualizado com sucesso")

def apagar():
    if len(livros) == 0:
        print("Não existem livros")
        return
    #pesquisar os livros com titulo semelhante
    livro_apagar = pesquisar()
    #comfirmar para cada um dos livros se deseja apagar
    for livro in livro_apagar:
        print(f"ID: {livro['id']}, Titulo: {livro['titulo']}, Autor: {livro['autor']}")
        op = input("Deseja remover o livro (s/n):")
        if op in "ss":
            #TODO verificar se o livro esta ou não emprestado
            livros.remove(livro)
            print(f"O livro {livro['titulo']} foi removido com sucesso. Tem {len(livros)} livros")

def listar_pesquisa():
    resultado = pesquisar()
    listar(resultado)

def pesquisar():
    """Devolver a lista dos livros que correspondem a um criterio"""
    #deixar o utilizador escolher o campo de pesquisa
    op = utils.menu(["Autor","Titulo"],"Esolha o campo de pesquisa:")
    #criar uma lista para os resultados
    resultados = []
    if op == 1:
        campo = "autor"
    else:
        campo = "titulo"
    pesquisa = utils.ler_string(3,f"{campo} a procurar:")
    #adicionar a lista os resultados que correspodem a pesquisa
    for livro in livros:
        if pesquisa.lower() in livro[campo].lower():
            resultados.append(livro)
    #mostrar os resultados
    return resultados

def guardar_dados():
    """Função para guardar os dados dos livros em um ficheiro"""
    with open('livros.dat','wb') as f:
        pickle.dump(livros,f)

def ler_dados():
    """Função para ler os dados dos livros de um ficheiro"""
    global livros
    if os.path.exists('livros.dat') == False:
        return
    with open('livros.dat','rb') as f:
        livros = pickle.load(f)