# Desafio:      017
# Enunciado:    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

print('====== DESAFIO 016 ======')
from math import hypot, trunc
co = int(input('Cateto Oposto: '))
ca = int(input('Cateto Adjacente: '))
h = hypot(co, ca)
print('O comprimento da hipotenusa é {}'.format(trunc(h)))
