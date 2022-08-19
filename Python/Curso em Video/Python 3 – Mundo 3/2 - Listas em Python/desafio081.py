# Desafio:      081
# Enunciado:    Crie um programa que vai ler vários números e colocar em uma lista.
#
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista


print('====== DESAFIO 081 ======')
resposta = 's'
lista = []
while resposta in 'Ss':
    resposta = 's'
    lista.append(int(input('Digite um valor: ')))
    while resposta not in 'S':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resposta == 'N':
            break
print(f'Quantidade de valores digitados: {len(lista)}')
print(f'Valores em ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')