# Desafio:      037
# Enunciado:    Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#
# 1 para binário
# 2 para octal
# 3 para hexadecimal

print('====== DESAFIO 037 ======')
número = int(input('Informe um número: '))
base = int(input('Digite:\n1 para binário\n2 para octal\n3 para hexadecimal'))
if base == 1:
    binário = bin(número)
    print('{} em binário é {}'.format(número, binário))
elif base == 2:
    octal = oct(número)
    print('{} em octal é {}'.format(número, octal))
else:
    hexadecimal = hex(número)
    print('{} em hexadecimal é {}'.format(número, hexadecimal))
