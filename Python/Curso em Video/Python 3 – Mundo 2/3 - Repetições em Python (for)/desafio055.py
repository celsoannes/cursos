# Desafio:      055
# Enunciado:    Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos


print('====== DESAFIO 055 ======')
maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input('Informe o pesso da pessoa (Kg): '))
    if maior < peso:
        maior = peso
    if menor == 0:
        menor = peso
    elif menor > peso:
        menor = peso
print('{} Kg é o maior peso'.format(maior))
print('{} Kg é o menor peso'.format(menor))