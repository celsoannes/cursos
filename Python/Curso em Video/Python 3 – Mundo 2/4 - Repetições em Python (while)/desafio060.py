# Desafio:      060
# Enunciado:    Faça um programa que leia um número qualquer e mostre o seu fatorial.
#
# Ex.:
# 5! = 5x4x3x2x1 = 120


print('====== DESAFIO 060 ======')
n = int(input('Informe um número: '))
print('Fatorial de {} é '.format(n), end='')
total = n
fatorial = 0
while n != 1:
    total = total * (n - 1)
    n -= 1
print('{}'.format(total))
