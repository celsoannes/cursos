# Desafio:      047
# Enunciado:    Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50


print('====== DESAFIO 047 ======')
for i in range(1, 50):
    if i % 2 == 0:
        print('{} é PAR'.format(i))