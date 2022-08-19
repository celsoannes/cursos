# Desafio:      070
# Enunciado:    Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
#
# A) qual é o total gasto na compra
# B) quantos produtos custam mais de R$ 1000
# C) qual é o nome do poduto mais barato


print('====== DESAFIO 070 ======')
continuar = '-'
barato = ''
total = mil = menor = 0
while True:
    produto = str(input('Nome do Produto: '))
    preço = int(input('Preço: R$'))
    total += preço
    if preço > 1000:
        mil += 1
    if continuar == '-':
        barato = produto
        menor = preço
    elif menor > preço:
        barato = produto
        menor = preço
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    continuar = 's'
print(f'Total: {total}')
print(f'{mil} produtos custaram mais de 1000')
print(f'{barato} foi o produto mais barato')
