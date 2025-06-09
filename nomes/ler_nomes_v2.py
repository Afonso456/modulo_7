import os

NOME_F = 'nomes.txt'

if os.path.exists(NOME_F) == False:
    print('O ficheiro não existe')
else:
    with open('nomes.txt','r',encoding = 'UTF8') as f:
        while True:
            linha= f.readline()
            #verifica se encontrou o EOF(end of file)
            if not linha:
                break
            print(linha,end='')

