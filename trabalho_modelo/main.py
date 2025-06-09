"""
Trabalho Modelo - Modulo 7
--------------------------
Um programa para gerir livros e emprestimos de uma biblioteca.
    -Gestão de livros (CRUD)
    -Gestão de leitores (CRUD)
    -Emprestimos e devoluções 
    -Estatisticas (emprestimos em atraso, top livros, top mes, top leitores)
Para o modulo 7 foi adicionado a materialização dos dados
"""
import utils,livros,leitores,emprestimos,estatisticas,os

#Deve estar True quando em testes e False quando concluido
DEBUG = False

def menu():
    if DEBUG:
        livros.configurar()
        leitores.configurar()
        emprestimos.ler_dados()
    op = 0
    #ler dados dos ficheiros
    livros.ler_dados()
    leitores.ler_dados()
    while op != 5:
        os.system("cls")
        op = utils.menu(["Livros","Leitores","Emprestimos/Devoluções","Estatisticas","Sair"],"Menu principal")
        if op == 5:
            break
        if op == 1:
            livros.menu()  
        if op == 2:
            leitores.menu()
        if op == 3:
            emprestimos.menu()
        if op == 4:
            estatisticas.menu()
    #guardar od dados
    livros.guardar_dados()
    leitores.guardar_dados()
    emprestimos.guardar_dados()

if __name__ == "__main__":
    menu()