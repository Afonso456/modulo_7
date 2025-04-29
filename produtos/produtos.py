with open('produtos.txt','w',encoding= 'UTF8') as f:
    quantidade = int(input('Quantos produtos pretende adicionar:'))
    for i in range(quantidade):
        nome = input('Nome do produto:')
        preco = float(input('Preço do produto:'))
        preco = str(preco) 
        f.write(nome + '-')
        f.write(preco +  '\n')