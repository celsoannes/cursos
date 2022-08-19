# Desafio:      063
# Enunciado:    Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#
# Ex:
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8


print('====== DESAFIO 063 ======')
n = int(input('Digite um número: '))
s = int(input('Deseja mostrar quantos elementos? '))
ultimo = 0
penultio = 0
atual = 0
i = 0
while i != s:
    if i == 0:
        atual = n
        ultimo = atual
    elif i == 1:
        atual = ultimo + 1
        penultio = ultimo
        ultimo = atual
    else:
        atual = ultimo + penultio
        penultio = ultimo
        ultimo = atual
    print(atual)
    i += 1
