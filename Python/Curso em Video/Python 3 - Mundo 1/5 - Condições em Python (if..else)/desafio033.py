# Desafio:      033
# Enunciado:    Faça um programa que leia três números e mostre qual é o maior e qual é o menor

print('====== DESAFIO 032 ======')
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
if n1 > n2:
    if n1 > n3:
        print('{} é o Maior.'.format(n1))
if n2 > n1:
    if n2 > n3:
        print('{} é o Maior'.format(n2))
if n3 > n1:
    if n3 > n2:
        print('{} é o Maior'.format(n3))

if n1 < n2:
    if n1 < n3:
        print('{} é o Menor.'.format(n1))
if n2 < n1:
    if n2 < n3:
        print('{} é o Menor'.format(n2))
if n3 < n1:
    if n3 < n2:
        print('{} é o Menor'.format(n3))