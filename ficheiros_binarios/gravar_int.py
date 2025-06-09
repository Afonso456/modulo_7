"""Programa para guaradr um numrto inteiro num ficheiro binario"""

import struct

numero = 1234

#gaurdar o numero num ficheiro int.dat ou int.bin
with open('int.bin','wb') as f:
    #empacotar o numero no formato inteiro e escrever no ficheiro
    f.write(struct.pack('i',numero))

print('Ficheiro criado')