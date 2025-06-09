lista = [
    {'nome':'antonio',
     'morada':'viseu',
     'idade': 30
     },
    {'nome':'marco',
     'morada':'lisboa',
     'idade': 25
     },
]

#ler e escrever em ficheiro de texto com o formato csv
import csv

#cabeçalho do ficheiro csv
chaves = lista[0].keys()
with open('ficheiro.csv', 'w', encoding='utf-8',newline='') as f:
    #varavel para guardar no ficheiro indicando o nome do ficheiro e as chaves
    escrever = csv.DictWriter(f,fieldnames=chaves)
    #gravar o cabeçalho
    escrever.writeheader()
    #gravar os dados
    for i in range(len(lista)):
        #grava os dados correspondentes as chaves
        escrever.writerow(lista[i])


print('Ficheiro criado com sucesso')