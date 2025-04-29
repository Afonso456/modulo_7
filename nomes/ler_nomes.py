with open('nomes.txt','r',encoding = 'UTF8') as f:
    textos = f.readlines()
    for linha in textos:
        print(linha,end = '')