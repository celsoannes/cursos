# Desafio:      016
# Enunciado:    Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#
# Ex.: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

print('====== DESAFIO 016 ======')
from math import trunc
real = float(input('Digite um número: '))
inteiro = trunc(real)
print('O número {} tem a parte inteira {}'.format(real, inteiro))