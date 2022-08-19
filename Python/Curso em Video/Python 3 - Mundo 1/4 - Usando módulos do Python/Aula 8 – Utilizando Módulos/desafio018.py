# Desafio:      018
# Enunciado:    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

print('====== DESAFIO 018 ======')
from math import sin, cos, tan
angulo = int(input("Informe um ângulo: "))
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print("O seno do ângulo é: {}".format(seno))
print("O cosseno do ângulo é: {}".format(cosseno))
print("A tangente do ângulo é: {}".format(tangente))
