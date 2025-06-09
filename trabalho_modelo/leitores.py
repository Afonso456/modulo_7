"""
Módulo de gestão dos leitores
"""
import utils,os,pickle

# lista dos leitores
leitores = []

# Campos que nao podem ser editados pelo utilizador
exemplo_leitores = [{"id":1,"nome":"joaquim","idade":13,"email":"joaquim@gmail.com","datanascimento":"12/9/2009","infracoes":""},
                        {"id":2,"nome":"ana","idade":16,"email":"ana@gmail.com","datanascimento":"18/4/2999","infracoes":""},
                        {"id":3,"nome":"maria","idade":14,"email":"maria@gmail.com","datanascimento":"30/02/2026","infracoes":""}]

whitelist_leitores = ["id","infracoes"]


def get_leitor(id):
    """Devolve o leitor com base no id indicado"""
    for leitor in leitores:
        if leitor["id"] == id:
            return leitor
    return None

def configurar():
    """Insere dados de exemplo"""
    leitores.extend(exemplo_leitores)
    # lista de leitores de exemplo

def menu():
    """Submenu para gerir os leitores"""
    op = 0
    while op != 6:
        print("---Menu Leitores---")
        op = utils.menu(["Adicionar","Listar","Editar","Apagar","Pesquisar","Voltar"],"Menu Leitores")
        if op == 6:
            break
        if op == 1:
            adicionar()
        if op == 2:
            listar(leitores)
        if op == 3:
            editar()
        if op == 4:
            apagar()
        if op == 5:
            pesquisar_listar()

def adicionar():
    # Nome
    nome = utils.ler_string(3,"Introduza o seu nome: ")
    # email
    email = utils.ler_string(3,"Introduza o seu email: ")
    # idade
    idade = utils.ler_numero_inteiro_limites(6,80,"Introduza a sua idade: ")
    # data nascimento
    data_nascimento = utils.ler_string(10,"Introduza a sua data de nascimento (dd/mm/aaaa): ")
    # id
    id = 1
    if len(leitores)>0:
        id = leitores[len(leitores)-1]["id"]+1 # Codigo vai gerar o id apartir do id do ultimo leitor
    novo = {
        "id":id,
        "nome": nome,
        "email": email,
        "idade" :idade,
        "datanascimento":data_nascimento,
        "infracoes" :"",
    }
    leitores.append(novo)
    print(f"Leitor novo registrado com sucesso. Tem {len(leitores)} leitores")

def editar():
    # Pesquisar o leitor a editar
    leitores_editar = pesquisar()
    # mostrar os dados de cada leitor encontrado
    if len(leitores_editar) == 0:
        print("Não foram encontrados leitores com esse nome.")
        return
    # mostrar os leitores encontrados
    for leitor in leitores_editar:
        op = input(f"Deseja editar {leitor["nome"]}? (s/n): ")
        if op not in "sS":
            continue
        #mostarr os dados atuais
        print(f"Nome: {leitor["nome"]}  Idade: {leitor["idade"]}  Email: {leitor["email"]} Data de nascimento: {leitor['datanascimento']}")
        #perguntar o campo a alterar
        op = input("Campo a alterar (deixarem barnco para cancelar):")
        if op == "":
            return
        #ler o valor e atualizar 
        op = op.lower()
        if op not in leitor.keys():
            print("Campo não existe")
            break
        valor = input(f"Qual o valor para {op} ?:")
        leitor[op] = valor

def apagar():
    #TODO verificar se o leitor tem livros emprestados
    #pesquisar o leitor a apagar
    leitor_apagar = pesquisar()
    #pesquisar os nomes semelhantes
    if len(leitor_apagar) == 0:
        print("Não existe nenhum leitor para ser removido.")
        return
    #verificar se encontrou pelo menos 1
    if len(leitor_apagar) == 0:
        print("Não foram encontrados leitor.")
        return
    #comfirmar se deseja apagar
    for leitor in leitor_apagar:
        print(f"ID: {leitor["id"]},  Nome:{leitor["nome"]},  Email:{leitor["email"]}")
        op = input(f"Deseja apagar {leitor['nome']} (s/n) ?: ")
        if op not in "sS":
            continue
        else:
            leitores.remove(leitor)
            print(f"Leitor {leitor['nome']} apagado com sucesso")

def listar(lista_a_listar):
    """Função para listar todos os Leitores"""
    print("-"*90)
    print("                                 Lista de Leitores")
    print("-"*90)
    for leitor in lista_a_listar:
        print(f"Id:{leitor["id"]} | Nome: {leitor["nome"]} | email: {leitor["email"]} | data de nascimento: {leitor["datanascimento"]} | infrações: {leitor["infracoes"]} ")
        print("-"*80)

def pesquisar_listar():
    resultado = pesquisar()
    listar(resultado)

def pesquisar():
    """Devolver a lista dos leitores que correspondem a um critério"""
    pesquisa = utils.ler_string(1,f"{"nome"} a pesquisar: ")
    l_resultados = []
    # Adicionar à lista os leitores que correspondem ao resultado da pesquisa
    for leitor in leitores:
        if pesquisa.lower() in leitor["nome"].lower():
            l_resultados.append(leitor)
    return l_resultados

def guardar_dados():
    """Função para guardar os dados dos livros em um ficheiro"""
    with open('leitores.dat','wb') as f:
        pickle.dump(leitores,f)

def ler_dados():
    """Função para ler os dados dos livros de um ficheiro"""
    global leitores
    if os.path.exists('leitores.dat') == False:
        return
    with open('leitores.dat','rb') as f:
        leitores = pickle.load(f)