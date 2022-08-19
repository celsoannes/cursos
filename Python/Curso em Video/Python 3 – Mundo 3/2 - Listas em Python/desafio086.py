# Desafio:      086
# Enunciado:    Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.


print('====== DESAFIO 086 ======')
matriz = [[[]], [[]], [[]]]
for x in range(0, 3):
    for y in range(0, 3):
        matriz[x].insert(y, int(input(f'Digite um valor para [{x}, {y}]: ')))
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matriz[x][y]}]', end='')
    print()
