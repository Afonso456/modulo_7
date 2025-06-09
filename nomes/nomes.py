with open('nomes.txt','w',encoding= 'UTF8') as ficheiro:
    for i in range (10):
        nome = input("Insira um nome:")
        ficheiro.write(nome + '\n')