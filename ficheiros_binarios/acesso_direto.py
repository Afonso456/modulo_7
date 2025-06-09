"""Programa para ler os dados de um registro com base no nr do registo
Cada registo ocupa 28 byes
"""

import os
import struct

TAMANHO_REGISTO = 28 

#calcular o tamnho do ficheiro
tamanho = os.path.getsize('dados.bin')

#calcular nr de registos
nr_registos = tamanho / TAMANHO_REGISTO

n_ler = int(input(f'Tem {nr_registos} registos qual pretende ler:'))

if n_ler >  nr_registos:
    print('O registo não existe')

else:
    with open('dados.bin','rb') as f:
        #posicionar o cursor no byte correspondente ao registo a ler
        byte_ler = (n_ler -1) * TAMANHO_REGISTO
        f.seek(byte_ler)
        #ler o registo
        dados_bin = f.read(28)
        #desempacotar os dados
        dados = struct.unpack('20sif', dados_bin)
        #converter a string binaria para string
        print(f'Nome:  {dados[0].decode('utf-8').strip('\x00')}')
        print(f'Idade: {dados[1]}')
        print(f'Saldo: {dados[2]}')