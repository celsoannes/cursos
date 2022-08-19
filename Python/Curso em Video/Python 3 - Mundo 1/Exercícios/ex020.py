# Título:       Exercício 20 – Sorteando uma ordem na lista
# Desafio:      020
# Requisito:    Aula 08
# Enunciado:    O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

print('====== EXERCÍCIO 020 ======')
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('O aluno escolhido foi {}'.format(lista))