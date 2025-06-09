"""Programa para ler um numero inteiro de um ficheiro binario"""

import struct

#abrir o ficheiro int.dat em modo leitura binaria
with open('int.dat','rb') as f:
    #ler o numero do ficheiro
    numero = struct.unpack('i',f.read(4))
    print(numero[0])