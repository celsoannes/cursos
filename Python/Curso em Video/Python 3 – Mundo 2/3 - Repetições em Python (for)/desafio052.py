# Desafio:      052
# Enunciado:    Faça um programa que leia um número inteiro e diga se ele é ou não um número primo


print('====== DESAFIO 052 ======')
n = int(input('Digite um número: '))
c = 0
for i in range(0, n):
    if n % 2 == 0:
        c = c + 1
if c > 2:
    print('{} não é um número primo'.format(n))
else:
    print('{} é um número primo'.format(n))
