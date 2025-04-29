ficheiro = open('alunos.txt','r',encoding= 'UTF8')

texto = ficheiro.readline() #lê apenas uma linha
texto = ficheiro.readlines() #lê o documento todo
print(texto)

ficheiro.close()

with open('alunos.txt','r',encoding= 'UTF8') as ficheiro: #fechar o ficheiro sem usar o .close()
    texto2 = ficheiro.readlines()
    print(texto2)