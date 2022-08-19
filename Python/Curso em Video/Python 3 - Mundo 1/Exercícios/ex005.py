# Título:       Exercício 5 – Antecessor e Sucessor
# Desafio:      005
# Requisito:    Aula 07
# Enunciado:    Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

print('====== EXERCÍCIO 005 ======')
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))