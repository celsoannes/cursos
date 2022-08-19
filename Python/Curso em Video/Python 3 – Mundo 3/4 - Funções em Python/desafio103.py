# Desafio:      103
# Enunciado:    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


print('====== DESAFIO 103 ======')


def ficha(nome, g):
    print('-' * 20)
    if len(nome) == 0:
        nome = '<desconhecido>'
    if len(g) == 0 or g.isnumeric() == False:
        g = 0
    print(f'O jogador {nome} fez {g} gol(s) no campeonato')

jogador = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
ficha(jogador, gols)
