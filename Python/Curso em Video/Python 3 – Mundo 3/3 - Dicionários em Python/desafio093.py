# Desafio:      093
# Enunciado:    Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


print('====== DESAFIO 093 ======')
jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=' * 40)
print(jogador)
print('-=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for i in range(0, jogador["partidas"]):
    print(f'   => Na partida {i}, fez {jogador["gols"][i]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
