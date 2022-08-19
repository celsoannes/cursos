# Desafio:      068
# Enunciado:    Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


print('====== DESAFIO 068 ======')
from random import randint
vitórias = 0
while True:
    cpu = randint(1, 2)
    v1 = int(input('Digite um valor: '))
    p1 = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    jogada = (cpu + v1) % 2
    if jogada == 0 and p1 == 'P':
        print('Você VENCEU!')
        vitórias += 1
    elif jogada == 1 and p1 == 'I':
        print('Você VENCEU!')
        vitórias += 1
    else:
        print('Você Perdeu!')
        print(f'Você venceu {vitórias} vezes')
        break
    print('Vamos jogar novamente...')

