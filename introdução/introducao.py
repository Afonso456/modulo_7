"""
r -leitura(cria o ficheiro caso n exista)
w - escrever(destroi tudo do ficheiro caso ele exista)
a - escrever no final do ficheiro
r+ -leitura/escrita
w+ - leitura/escrita (cria o ficheiro caso n exista ou destroi o ficheiro caso ja exista)
a+ - leitura/escrita (adiciona texto no final do documento)
"""

#abrir um ficheiro
ficheiro = open("alunos.txt",'w',encoding= 'UTF8')

ficheiro.write("Olá mundo\n")
ficheiro.write("Inicio\n")
ficheiro.write("Fim\n")
ficheiro.writelines("Olá pessoal") #escrever em varias linhas de uma vez

ficheiro.close()