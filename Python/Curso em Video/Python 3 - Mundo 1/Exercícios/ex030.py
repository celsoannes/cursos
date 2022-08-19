# Título:       Exercício 30 – Par ou Ímpar?
# Desafio:      030
# Requisito:    Aula 10
# Enunciado:    Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


print('====== EXERCÍCIO 030 ======')
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))