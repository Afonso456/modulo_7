import utils,utilizadores,habitos

def main():
    """Função principal do programa"""
    op = 0
    utilizadores.ler_dados()
    habitos.ler_dados()
    while op != 3:
        op = utils.menu(['Menu utilizadores','Menu habitos','Sair'],'Menu principal')
        if op == 1:
            utilizadores.menu()
        if op == 2:
            habitos.menu()
        if op == 3:
            break
    utilizadores.guardar_dados()
    habitos.guardar_dados()
    
if __name__ == '__main__':
    main()