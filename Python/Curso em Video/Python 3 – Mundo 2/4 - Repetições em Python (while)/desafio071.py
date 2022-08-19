# Desafio:      071
# Enunciado:    Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1


print('====== DESAFIO 071 ======')
valor = int(input('Que valor você quer sacar? R$'))
cinquenta = 50
vinte = 20
dez = 10
um = 1
onça = mico = arara = beijaflor = 0

while cinquenta <= valor:
    cinquenta += 50
    onça += 1
valor = valor - 50 * onça
while vinte <= valor:
    vinte += 20
    mico += 1
valor = valor - 20 * mico
while dez <= valor:
    dez += 10
    arara += 1
valor = valor - 10 * arara
while um <= valor:
    um += 1
    beijaflor += 1
print(f'Total de {onça} cédulas de R$50')
print(f'Total de {mico} cédulas de R$20')
print(f'Total de {arara} cedulas de R$10')
print(f'Total de {beijaflor} cedulas de R$1')
