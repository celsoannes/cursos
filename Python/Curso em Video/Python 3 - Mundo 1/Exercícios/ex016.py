# Título:       Exercício 16 – Quebrando um número
# Desafio:      016
# Requisito:    Aula 08
# Enunciado:    Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#
# Ex.: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

print('====== EXERCÍCIO 016 ======')
'''import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))