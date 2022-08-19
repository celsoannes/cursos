# Título:       Exercício 17 – Catetos e Hipotenusa
# Desafio:      017
# Requisito:    Aula 08
# Enunciado:    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

print('====== EXERCÍCIO 017 ======')
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
