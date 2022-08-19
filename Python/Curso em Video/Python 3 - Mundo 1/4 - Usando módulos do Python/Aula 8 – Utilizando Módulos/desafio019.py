# Desafio:      019
# Enunciado:    Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

print('====== DESAFIO 019 ======')
import random
sorteio = random.choice(['Pateta', 'Mickey', 'Margarida', 'Pato Donald'])
print('O escolhido é o aluno numero: {}'.format(sorteio))