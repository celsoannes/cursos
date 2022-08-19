# Desafio:      028
# Enunciado:    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#
# O programa deverá escrever na tela se o usuário venceu ou perdeu

print('====== DESAFIO 028 ======')
from random import randrange
n1 = randrange(1, 5)
print('Consegue descobrir em que número estou pensando?')
n2 = int(input('Digite um número entre 1 e 5: '))
if n1 == n2:
    print('Você adivinhou!')
else:
    print('ERROU! Estava pensando no {}.'.format(n1))
