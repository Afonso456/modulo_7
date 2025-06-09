"""Modulo de gestão das estatisticas"""

import utils
from datetime import datetime 
import emprestimos



def menu():
    op = 0
    while op != 5:
        op = utils.menu(["Livro mais requisitado ultimo mês","Leitor com mais requisições","Emprestimos em atraso","Top mês","Voltar"],"Menu de Estatisticas")
        if op == 5:
            break
        if op == 1:
            livro_mais_requisitado()
        if op == 2:
            leitor_mais_requisitado()
        if op  == 3:
            emprestimos_atraso()
        if op == 4:
            top_mes()

def livro_mais_requisitado():
    """Função para encontrar o livro mais requisitado no último mês (mês anterior ao mês atual)"""
    if len(emprestimos.emprestimos) == 0:
        print("Não tem empréstimos")
        return
    #mês e ano a pesquisar
    data_atual = datetime.now()
    data_atual = data_atual.strftime("%Y-%m-%d")
    partes = data_atual.split("-")
    ano = int(partes[0])
    mes = int(partes[1])
    mes = mes - 1
    if mes == 0:
        mes = 12
        ano = ano - 1
   
    #criar um dicionário { titulo: contagem}
    dicionario_livros={}
    #percorrer empréstimos
    for emprestimo in emprestimos.emprestimos:
        #verificar se é do mês anterior (comparar mês e ano)
        data_emprestimo = emprestimo['data_emprestimo'].split("-")
        ano_emprestimo = int(data_emprestimo[0])
        mes_emprestimo = int(data_emprestimo[1])
        if ano_emprestimo == ano and mes_emprestimo == mes:
            #contar se sim
            if emprestimo['livro']['titulo'] in dicionario_livros:
                dicionario_livros[emprestimo['livro']['titulo']] += 1
            else:
                dicionario_livros[emprestimo['livro']['titulo']] = 1
    #percorrer o dicionário e encontrar o maior
    maior = 0
    titulo_maior =""
    for livro in dicionario_livros:
        if dicionario_livros[livro]>maior:
            titulo_maior = livro
            maior = dicionario_livros[livro]
    print(f"O livro mais emprestado no mês anterior ({mes}/{ano}) foi {titulo_maior} com {maior} empréstimos.")

def leitor_mais_requisitado():
    """Função para mostrar o leitor com mais emprestimos"""
    if len(emprestimos.emprestimos) == 0:
        print("Não existem emprestimos registado")
        return
    dicionario_leitores = {}
    for emprestimo in emprestimos.emprestimos:
        nome = emprestimo["leitor"]["nome"]
        if nome in dicionario_leitores:
            dicionario_leitores[nome] += 1
        else:
            dicionario_leitores[nome] = 1
    nome_maior =""
    maior = 0
    for leitor in dicionario_leitores:
        if dicionario_leitores[leitor] > maior:
            maior = dicionario_leitores[leitor]
            nome_maior = leitor
    print(f"O leitor com maior numero de emprestimos é {nome_maior} com {maior} emprestimos")

def emprestimos_atraso():
    """Mostra os emprestimos em atraso"""
    if len(emprestimos.emprestimos) == 0:
        print("Não existem emprestimos registados")
        return
    #criar uma variavel para a data atual
    data_atual = datetime.now()
    #converter para inteiro
    idata_atual = int(data_atual.strftime("%Y%m%d"))
    #percorrer a lista do emprestimos
    contar = 0
    for emprestimo in emprestimos.emprestimos:
        data_devolucao = emprestimo["data_devolucao"]
        #converter a data dos emprestimos em inteiro
        idata_devolucao = int(datetime.strptime(data_devolucao, "%Y-%m-%d").strftime("%Y%m%d"))
        #comparar com a data atual
        if idata_devolucao > idata_atual and emprestimo["estado"] == True:
            print(f"O leitor {emprestimo["leitor"]["nome"]} tem o livro {emprestimo["livro"]["titulo"]} por entragar em atraso a {idata_devolucao - idata_atual}")
            contar += 1

def top_mes():
    """Mostra o mes em que existiram mais emprestimos"""
    if len(emprestimos.emprestimos) == 0:
        print("Não existem emprestimos registados")
        return
    #percorrer a lista dos emprestimos
    meses = []
    for i in range(12):
        meses.append(0)
    #extrair os meses com data de emprestimo
    for emprestimo in emprestimos.emprestimos:
        partes = emprestimo["data_emprestimo"].split("-")
        mes_emprestimo = int(partes[1])
        #somar 1 na lista dos meses na posicao no mes de emprestim
        meses[mes_emprestimo -1] += 1
    #percorrer a lista dos messes e encontrar o maior
    maior = 0
    for i in range(len(meses)):
        if meses[i] > meses[maior]:
            maior = i
    #mostrar a posicao d maior +1
    print(f"O mes com maior numero de emprestimos foi o {maior + 1} com {maior} emprestimos")