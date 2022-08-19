# Desafio:      084
# Enunciado:    Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


print('====== DESAFIO 084 ======')
pessoas = list()
pesada = list()
leve = list()
maior = menor = 0
while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    pessoa = [nome, peso]
    pessoas.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
for i in range(len(pessoas)):
    if i == 0:
        maior = menor = pessoas[i][1]
    elif pessoas[i][1] > maior:
        maior = pessoas[i][1]
    elif pessoas[i][1] < menor:
        menor = pessoas[i][1]

for i in range(0, len(pessoas)):
    if pessoas[i][1] == maior:
        pesada.append(pessoas[i][0])
    elif pessoas[i][1] == menor:
        leve.append(pessoas[i][0])


print(f'O maior peso foi de {maior}Kg. Peso de {pesada}')
print(f'O menor peso foi de {menor}Kg. Peso de {leve}')
