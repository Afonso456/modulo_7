"""Programa que gurada num ficheiro binario os dados de um cliente: noome, idade, saldo"""

import struct

nome  = input('Nome do cliente:') 
idade = int(input('Idade do cliente:'))
saldo = float(input('Saldo:'))


with open('dados.bin','ab') as f:
    #nome  -> string -> cada letra 1 byte -> 20 bytes
    dados_empacotados = struct.pack('20s',nome.encode('utf-8'))
    f.write(dados_empacotados)
    #idade -> int    -> 4 bytes
    dados_empacotados = struct.pack('i',idade)
    f.write(dados_empacotados)
    #saldo -> float  -> 4 bytes
    dados_empacotados = struct.pack('f',saldo)
    f.write(dados_empacotados)

print('Dados guardados com sucesso')