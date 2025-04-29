with open('alunos.txt','r',encoding= 'UTF8') as ficheiro:
    texto = ficheiro.readline()
    print(texto)
    ficheiro.seek(0) #andar para um posição escolhida no ficheiro
    texto = ficheiro.readline()
    print(texto)
