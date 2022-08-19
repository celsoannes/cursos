# Desafio:      091
# Enunciado:    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.


print('====== DESAFIO 091 ======')
from random import randint
from operator import itemgetter
jogo = dict()
jogos = list()
print('Valores sorteados:')
for i in range(0, 4):
    jogo[f'jogador"{i+1}"'] = randint(1, 6)
    jogos.append(jogo.copy())
    #jogo.clear()
print(jogo)
for i, v in enumerate(jogos):
    print(f'{i} - {v}')
#ranking = sorted()
