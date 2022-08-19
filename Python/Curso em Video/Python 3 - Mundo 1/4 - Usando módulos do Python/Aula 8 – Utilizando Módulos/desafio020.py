# Desafio:      020
# Enunciado:    O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random

print('====== DESAFIO 020 ======')
from random import shuffle
alunos = 'Pateta Mickey Margarida Donald'.split()
ordem = random.shuffle(alunos)
print('Ordem de apresentação dos trabalhos será: {}'.format(alunos))
