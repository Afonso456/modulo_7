"""Programa para gerir uma petshop:
raça   - string  -> 30 bytes
peso   - float   -> 4 bytes
genero - string  -> 1 byte
preço  - float   -> 4 bytes
"""

import struct
import os
import utils

NOME_F = 'animais.bin'

def adicionar():
    """Função para adicionar animais"""
    raca = str(input('Raça do animal:'))
    peso = float(input('Peso do animal:'))
    genero = str(input('Genero do animal (M/F):'))
    preco = float(input('Preço do animal:'))
    with open(NOME_F,'ab') as f:
        f.write(struct.pack('30s',raca.encode('utf-8')))
        f.write(struct.pack('f',peso))
        f.write(struct.pack('1s',genero.encode('utf-8')))
        f.write(struct.pack('f',preco))
    print('Dados registados com sucesso')

def listar():
    """Função para listar os animais"""
    if os.path.exists(NOME_F) == False:
        print('Ficheiro não existe')
    else:
        with open(NOME_F,'rb') as f:
            while True:
                #raça
                dados_bin = f.read(30)
                if not dados_bin:
                    break
                dados = struct.unpack('30s',dados_bin)
                print(f'Raça - {dados[0].decode('utf-8').strip('\x00')}')
                #peso
                dados_bin = f.read(4)
                dados = struct.unpack('f',dados_bin)
                print(f'Peso - {dados[0]}')
                #genero
                dados_bin = f.read(1)
                dados = struct.unpack('1s',dados_bin)
                print(f'Genero - {dados[0].decode('utf-8').strip('\x00')}')
                #preco
                dados_bin = f.read(4)
                dados = struct.unpack('f',dados_bin)
                print(f'Preço - {dados[0]}')

def apagar():
    """Função para remover um animal"""
    with open(NOME_F,'rb') as f_ler:
        with open('temp.bin','wb') as f_escrever:
            while True:
                raca_bin = f_ler.read(30)
                if not raca_bin:
                    break
                #ler um registo
                peso_bin    = f_ler.read(4) 
                genero_bin  = f_ler.read(1)
                preco_bin   =  f_ler.read(4)
                raca        = struct.unpack('30s',raca_bin)
                #mostrar ao utilizador
                print(f'Raça {raca[0].decode('utf-8'.rstrip('\x00'))}')
                #se não for para apagar gravar no ficheiro temp
                op = input('Pretende apagar este animal:')
                if op not in 'Ss':
                    f_escrever.write(raca_bin)
                    f_escrever.write(peso_bin)
                    f_escrever.write(genero_bin)
                    f_escrever.write(preco_bin)
    #apagar o ficheiro original
    os.remove(NOME_F)
    #mudar o nome do ficheiro temporario
    os.rename('temp.bin',NOME_F)
    print('Animal removido com sucesso')

def editar():
    """Função para editar o cadastro de um animal"""
    #abrir o ficheiro para leitura e escrita
    with open(NOME_F,'rb+') as f:
        while True:
            raca_bin = f.read(30)
            if not raca_bin:
                break
            #ler um registo
            peso_bin    = f.read(4) 
            genero_bin  = f.read(1)
            preco_bin   = f.read(4)
            #mostrar os animais
            raca   = struct.unpack('30s',raca_bin)[0].decode('utf-8').rstrip('\x00')
            peso   = struct.unpack('f',peso_bin)[0]
            genero = struct.unpack('1s',genero_bin)[0].decode('utf-8').rstrip('\x00')
            preco  =  struct.unpack('f',preco_bin)[0]
            print(f'Raça - {raca} Peso - {peso} Genero - {genero} Preço - {preco}')
            op = utils.ler_string(1,'Pretende editar este animal (s/n)')
            #perguntar se pretende alterar algum
            if op in 'Ss':
                raca   = str(input('Nova raça:')) 
                peso   =  float(input('Novo peso:'))
                genero = str(input('Novo genero:'))
                preco  = float(input('Novo preço:'))
                #se alterar gravar novamente o mesmo registo
                f.seek(-39,os.SEEK_CUR)
                f.write(struct.pack('30s',raca.encode('utf-8')))
                f.write(struct.pack('f',peso))
                f.write(struct.pack('1s',genero.encode('utf-8')))
                f.write(struct.pack('f',preco))

def mais_caro():
    """Função que mostra o animal mais caro"""
    with open(NOME_F,'rb') as f:


def main():
    op = 0
    while op != 5:
        op = utils.menu(['Adicionar','Listar','Remover','Editar','Sair'],'Pet Shop')
        if op == 5:
            break
        if op == 1:
            adicionar()
        if op == 2:
            listar()
        if op == 3:
            apagar()
        if op == 4:
            editar()
        
if __name__ == '__main__':
    main()