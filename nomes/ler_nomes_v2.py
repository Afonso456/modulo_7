with open('nomes.txt','r',encoding = 'UTF8') as f:
    while True:
        linha= f.readline()
        if not linha:
            break
        print(linha,end='')