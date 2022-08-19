# Desafio:      088
# Enunciado:    Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


print('====== DESAFIO 088 ======')
from random import randint
from time import sleep
jogos = int(input('Você deseja fazer quantos jogos? '))
palpite = list()
sugestões = list()
for i in range(0, jogos):
    for p in range(0, 6):
        numeroaleatório = randint(1, 6)
        if palpite.count(numeroaleatório) == 0:
            palpite.append(numeroaleatório)
        else:
            while palpite.count(numeroaleatório) > 0:
                numeroaleatório = randint(1, 60)
            palpite.append(numeroaleatório)

    sugestões.insert(i, palpite[:])
    palpite.clear()
for jogo in range(0, len(sugestões)):
    jogodasorte = sugestões[jogo]
    jogodasorte.sort()
    print(f'Jogo {jogo+1}: {jogodasorte}')
    jogodasorte.clear()
    sleep(.5)
