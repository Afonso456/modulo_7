"""Programa para ler varios dados de um ficheiro binario
Cada registo tem 28 bytes:
        nome  -> string -> cada letra 1 byte -> 20 bytes
        idade -> int    -> 4 bytes
        saldo -> float  -> 4 bytes
"""

import struct

with open('dados.bin','rb') as f:
    while True:
        try:
            #ler os dados todos de uma vez
            dados_bin = f.read(28)
            if not dados_bin:
                break
            dados = struct.unpack('20sif', dados_bin)
            #converter a string binario para string
            nome = dados[0].decode('utf-8').strip('\x00')
            print(f'Nome: {nome}')
            print(f'Idade: {dados[1]}')
            print(f'Saldo: {dados[2]}')
        except EOFError:
            break