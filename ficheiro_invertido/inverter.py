"""
Programa que cria um ficheiro de texto e depois cria outro que recebeo conteudo do 1º ficheiro
mas em ordem contrario
"""
#criar um ficheiro com com alguma linhas
NOME_F_1 = 'ficheiro1.txt'
NOME_F_2 = 'ficheiro2.txt'

with open(NOME_F_1,'a',encoding='utf-8') as f1:
    for i in range(1,11):
        f1.write(f'linha {i}\n')

with open(NOME_F_2,'w',encoding='utf-8') as f2:
    with open(NOME_F_1,'r',encoding='utf-8') as f1:
        linhas = f1.readlines()
    for i in range(len(linhas)-1,-1,-1):
        f2.write(linhas[i])

print('Copia criada com sucesso')