from datetime import datetime
import utils,os,pickle

utilizadores = {} 

def menu():
    op = 0
    os.system("cls")
    while op != 6:
        op = utils.menu(['Adicionar habitos','Remover habitos','Editar habito','Listar habitos','Registar progresso','Sair'],'Menu de habitos')
        if op == 6:
            os.system("cls")
            break
        if op == 1:
            adicionar_habitos()
        if op == 2:
            remover_habitos()
        if op == 3:
            editar_habito()
        if op == 4:
            listar_habitos()
        if op == 5:
            registar_progresso()
    guardar_dados()

def adicionar_habitos():
    """Função para adicionar um novo abito ao dicionario dos utilizadores = {habitos[habito{}]}"""
    nome = utils.ler_string(3,'Insira o nome do utilizador:')
    utilizadores[nome] = {'habitos':{'habito':'',
                                    'total_dias':0,
                                    'dias_consecutivos':0}}
    if nome in utilizadores:
        habito = utils.ler_string(3,'Habito a adicionar:')
        if habito in utilizadores[nome]['habitos']['habito']:
            print('Habtio já existe')
        else:
            utilizadores[nome]['habitos']['habito'] = habito
            print('Habtio adicionado com sucesso')
    else:
        print('Utilizador não encontrado')

def remover_habitos():
    """Função para remover um abito do dicionario dos utilizadores = {habitos[habito{}]}"""
    nome = utils.ler_string(3, 'Nome do utilizador:')
    if nome in utilizadores:
        habito = utils.ler_string(3,'Habito a remover:')
        if habito in utilizadores['nome']['habitos']['habito']:
            utilizadores['nome']['habitos']['habito'].remove(habito)
            print('Habito removido com sucesso')
        else:
            print('Habito não encontrado')
    else:
        print('Utilizador não encontrado')

def editar_habito():
    """Função para editar um habito do dicionario dos utilizadores = {habitos[habito{}]}"""
    nome = utils.ler_string(3, 'Nome do utilizador:')
    if nome in utilizadores:
        habito = utils.ler_string(3,'Habito a editar:')
        if habito in utilizadores['nome']['habitos']['habito']:
            novo_habito = utils.ler_string(3,'Novo habito:')
            utilizadores[nome]['habitos']['habito'].remove(habito)
            utilizadores[nome]['habitos']['habito'].append(novo_habito)
            print('Habito editado com sucesso')
        else:
            print('Habito não encontrado')
    else:
        print('Utilizador não encontrado')

def listar_habitos():
    nome = utils.ler_string(3, 'Nome do utilizador para listar hábitos:')
    if nome in utilizadores:
        habitos = utilizadores[nome]['habitos']
        if not habitos:
            print('Nenhum hábito registrado.')
        else:
            for habito in utilizadores.items():
                print(f'• {habito}')
                print(f'Dias consecutivos - {utilizadores[nome]}')
    else:
        print(f'Utilizador "{nome}" não encontrado.')

def registar_progresso():
    nome = utils.ler_string(3, 'Nome do utilizador:')
    if nome in utilizadores:
        habito = utils.ler_string(3, 'Hábito a registar:')
        if habito in utilizadores[nome]['habitos']:
            hoje = datetime.now().date()
            dados = utilizadores[nome]['habitos'][habito]
            ultimo = dados['ultimo_registro']
            if ultimo == hoje:
                print(f'Hábito "{habito}" já foi registado hoje.')
                return
            dados['dias_totais'] += 1
            if ultimo:
                dias_diferenca = (hoje - ultimo).days
                if dias_diferenca == 1:
                    dados['dias_consecutivos'] += 1
                else:
                    dados['dias_consecutivos'] = 1
            else:
                dados['dias_consecutivos'] = 1
            
            dados['ultimo_registro'] = hoje
            print(f'Progresso de "{habito}" registado com sucesso.')
        else:
            print(f'Hábito "{habito}" não encontrado.')
    else:
        print(f'Utilizador "{nome}" não encontrado.')

def guardar_dados():
    """Função para guardar os habitos de um utilizador num ficheiro binario"""
    with open('habitos.bin','wb') as f:
        pickle.dump(utilizadores,f)

def ler_dados():
    """Função para ler os habitos de um utilizador de um ficheiro binario"""
    if os.path.exists('habitos.bin') == False:
        return
    with open('habitos.bin','rb') as f:
        global utilizadores
        utilizadores = pickle.load(f)
        return utilizadores