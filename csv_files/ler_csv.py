import csv

#lista vazia para guardar os dados do ficheiro
dados = []
with open('ficheiro.csv','r',encoding='utf-8') as f:
    #criaro objeto para ler o ficheiro
    ler = csv.reader(f)
    #percorrer cada linha do ficheiro e adicionar á lista
    for linha in ler:
        dados.append(linha)
print(dados)