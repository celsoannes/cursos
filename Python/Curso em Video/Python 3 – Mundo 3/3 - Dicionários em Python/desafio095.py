# Desafio:      095
# Enunciado:    Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


print('====== DESAFIO 095 ======')
jogador = dict()
partidas = list()
placar = list()
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    placar.append(jogador.copy())
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'{"cod":<3} {"nome":<10} {"gols":<15} {"total":4}')
for c, v in enumerate(placar):
    print(f'{c:>3} {v["nome"]:<10} {str(v["gols"]):<15} {v["total"]:<4}')
print('-' * 60)
while True:
    j = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if j == 999:
        break
    jogador = placar[j]
    print(f' -- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
    for n, gols in enumerate(jogador['gols']):
        print(f'    No jogo {n} fez {gols} gols.')