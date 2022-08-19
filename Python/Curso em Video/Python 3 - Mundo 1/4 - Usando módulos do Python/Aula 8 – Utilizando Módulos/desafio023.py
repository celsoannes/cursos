# Desafio:      023
# Enunciado:    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#
# Ex:
# Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1


print('====== DESAFIO 023 ======')
n = str(input('Digite um número: '))
un = (len(n)-1)
dz = (len(n)-1)
#cn =
#mi
#tamanho = len(n)
print('unidade: {}'.format(n[un]))
print('dezena: {}'.format(n[0:2]))