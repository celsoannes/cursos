# Título:       Exercício 18 – Seno, Cosseno e Tangente
# Desafio:      018
# Requisito:    Aula 08
# Enunciado:    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

print('====== EXERCÍCIO 018 ======')
from math import  sin, cos, tan, radians
ângulo = float(input('Digite o Ângulo que você deseja: '))
seno = sin((radians(ângulo)))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))