# Desafio:      074
# Enunciado:    Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


print('====== DESAFIO 074 ======')
from random import randrange
menor = 0
maior = 0
a = randrange(100)
b = randrange(100)
c = randrange(100)
d = randrange(100)
e = randrange(100)
números = (a, b, c, d, e)
for i in range(0, 5):
    if i == 0:
        menor = maior = números[0]
    elif números[i] < menor:
        menor = números[i]
    elif números[i] > maior:
        maior = números[i]
print(f'Lista com números aleatórios:\n{números}')
print(f'{menor} é o menor número da lista')
print(f'{maior} é o maior número da lista')