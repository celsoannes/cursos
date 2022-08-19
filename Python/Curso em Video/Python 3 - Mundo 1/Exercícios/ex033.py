# Título:       Exercício 33 – Maior e menor valores
# Desafio:      033
# Requisito:    Aula 10
# Enunciado:    Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


print('====== EXERCÍCIO 033 ======')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))