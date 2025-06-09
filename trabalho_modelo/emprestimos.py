"""
Modulo de gestão de emprestimos e devoluções
"""
from datetime import datetime, timedelta
import utils,livros,leitores
import os,pickle

#livro({}), leitor({}), data_emprestimo, data_devolução, estado
emprestimos = []


def menu():
    """Submenu para gerir os emprestimos"""
    op = 0
    while op != 4:
        op = utils.menu(["Emprestimo","Devolução","Listar emprestimos","Voltar"],"Menu de emprestios/devoluções")
        if op == 4:
            break
        if op == 1:
            emprestimo()
        if op == 2:
            devolucao()
        if op == 3:
            listar_emprestimos()

def emprestimo():
    """Função responsavel por registar os emprestimos de cada livro"""
    novo_emp = {}
    #ler o livro a emprestar
    print("Indique o livro a emprestar")
    livro_emprestar = livros.pesquisar()
    if len(livro_emprestar) == 0:
       print("Nenhum livro encontrado. Tente novamente")
       return
    elif len(livro_emprestar) > 1:
        #mostrar os livros encontrados
        livros.listar(livro_emprestar)
        #pedir o id do livro a emprestar
        print("Indique o id do livro a emprestar:")
        id = int(input())
        for livro in livro_emprestar:
            if livro["id"] == id:
                #verificar se o livro pode ser emprestado
                if livro["estado"] != "disponivel":
                    print("Livro emprestado")
                    return
                novo_emp["livro"] = livro
                break
        if "livro" not in novo_emp:
            print("O id indicado não existe")
            return
    else:
        #so encontrou um livro
        if livro_emprestar[0]["estado"] != "disponivel":
            print("Livro emprestado")
            return
        novo_emp["livro"] = livro_emprestar[0]
    
    #ler o leitor que leva o livro
    leitores_emprestimo = leitores.pesquisar()
    if len(leitores_emprestimo) == 0:
        print("Leitor não encontrado")
        return
    elif len(leitores_emprestimo) > 1:
        print("Leitor encontrado")
        leitores.listar(leitores_emprestimo)
        id = utils.ler_numero_inteiro("Indique o id do leitor:")
        for leitor in leitores_emprestimo:
            if leitor["id"] == id:
                novo_emp["leitor"] = leitor
                break
        if "leitor" not in novo_emp:
            print("O id indicado não existe")
            return
    else:
        novo_emp["leitor"] = leitores_emprestimo[0]
    #TODO verificar se o leitor pode levar o livro
    #registar o emprestimo com data de devolução
    data_atual = datetime.now()
    data_entrega = data_atual + timedelta(days=30)
    str_atual = data_atual.strftime("%Y-%m-%d")
    str_entega = data_entrega.strftime("%Y-%m-%d")
    novo_emp["data_emprestimo"] = str_atual
    novo_emp["data_devolucao"] = str_entega
    novo_emp["estado"] = True #emprestimo a decorrer
    emprestimos.append(novo_emp)
    #atualizar o estado do livro
    novo_emp["livro"]["estado"] = "emprestado"
    novo_emp["livro"]["leitor"] = novo_emp["leitor"]
    print("Emprestimo registado com sucesso")
    print(f"Livro emprestado: {novo_emp["livro"]["titulo"]}")
    print(f"Leitor: {novo_emp["leitor"]["nome"]}")

def devolucao():
    """Função responsavel po registar as devoluções dos livros"""
    #ler o id do livro a devolver
    id_livro = utils.ler_numero_inteiro("Id do livro a devolver:")
    #verificar se o livro esta emprestada
    livro = livros.get_livro(id_livro)
    if livro == None:
        print("Não existe nenhum livro com id indicado")
    if livro["estado"] != "emprestado":
        print("Livro não emprestado")
    #verificar se a devolução esta dentro do pazos
    emprestimo_devolver = None
    for emprestimo in emprestimos:
        if emprestimo["livro"] == livro and emprestimo["estado"] == True:
            emprestimo_devolver = emprestimo
            
    if emprestimo_devolver == None:
        print("Emprestimo não encontrado")
        return
    data_devolucao = emprestimo_devolver["data_devolucao"]
    data_atual = datetime.now() 
    idata_atual = int(data_atual.strftime("%Y%m%d"))
    idata_devolucao = int(datetime.strptime(data_devolucao, "%Y-%m-%d").strftime("%Y%m%d"))
    if idata_atual > idata_devolucao:
        print("Devolução atrasada")
        #registar se houve infração do leitor
        emprestimo_devolver["leitor"]["infracoes"] += "Entrega fora de prazo"

    #atualizar o nr de emprestimos do livro
    livro["nr_emprestimos"] += 1

    #muda o estdo do livro
    livro["estado"] = "disponivel"
    livro["leitor"] = None

    #mudar o estado do emprestimo
    emprestimo_devolver["estado"] = False
    print("Devolução concluida com sucesso")

def listar_emprestimos():
    #perguntar se pretendever todos os emprestimos ou
    #ou so os emprestimos por concluir
    op = utils.ler_string(1,"Listar [T]odos ou so por [C]ocluir:")
    for emp in emprestimos:
        if op in "tT" or (op in "cC" and emp["estado"] == True):
            print(f"Livro-{emp["livro"]["titulo"]} Leitor-{emp["leitor"]["nome"]} Estado-{emp["estado"]}")

def guardar_dados():
    """Ficheiro para guardar os dados dos emprestimos num ficheiro"""
    #criar uma lista sem referencias pra dicionaios de outras listas
    lista_ficheiro = []
    for e in emprestimos:
        novo = {
                #substituir a referencia para lista leitores pelo id
                "livro"          :e["livro"]["titulo"],
                'id_leitor'      :e['leitor']['id'],
                #substituir a referencia para lista livros pelo id
                'id_livro'       :e['livro']['id'],
                'data_emprestimo':e['data_emprestimo'],
                'data_devolucao' :e['data_devolucao'],
                'estado'         :e['estado'],}
        lista_ficheiro.append(novo)
    with open('emprestimos.data','wb') as f:
        pickle.dump(lista_ficheiro,f)

def ler_dados():
    """Função para ler os emprestimos de um ficheiro"""
    global emprestimos
    emprestimos = []
    lista_ficheiro = []
    if os.path.exists('emrpestimos.data') == False:
        return
    with open('emprestimos.data','rb') as f:
        lista_ficheiro =pickle.load(f)
    #criar a lista emprestimos com as referencias
    for e in lista_ficheiro:
        novo = {
                'data_emprestimo':e['data_emprestimo'],
                'data_devolucao' :e['data_devolucao'],
                'estado'         :e['estado'],
                'leitor'         :leitores.get_leitor(e['id_leitor']),
                'livro'          :livros.get_livro(e['id_livro'])}
    emprestimos.append(novo)