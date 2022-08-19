# Título:       Exercício 60 – Cálculo do Fatorial
# Desafio:      060
# Requisito:    Aula 14
# Enunciado:    Faça um programa que leia um número qualquer e mostre o seu fatorial.
#
# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120


print('====== EXERCÍCIO 060 ======')
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
