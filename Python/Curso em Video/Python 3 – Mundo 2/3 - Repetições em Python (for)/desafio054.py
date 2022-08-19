# Desafio:      054
# Enunciado:    Crie um programa que leia o ano de nascimento de sete pessoas. No Final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


print('====== DESAFIO 054 ======')
from datetime import datetime

maior = 0
menor = 0
ano = datetime.today().year
for i in range(0, 7):
    nascimento = int(input('Informe o ano de nascimento: '))
    if ano - nascimento >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Existem {} pessoas de maior e {} pessoas de menor'.format(maior, menor))

