# Desafio:      094
# Enunciado:    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média


print('====== DESAFIO 094 ======')
pessoa = dict()
pessoas = list()
acimadamedia = list()
totalidade = mediaidade = 0
totalpessoas = 0
mulheres = ''
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    totalidade += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    totalpessoas += 1
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {totalpessoas} pessoas cadastradas.')
mediaidade = totalidade / totalpessoas
print(f'B) A média de idade é {mediaidade:.2f}')
for c in range(0, totalpessoas):
    pessoa = pessoas[c]
    if pessoa['sexo'] == 'F':
        mulheres += pessoa["nome"] + ' '
    if pessoa['idade'] > mediaidade:
        acimadamedia.append(pessoa)
print(f'C) As mulheres cadastradas foram {mulheres}')
for c in range(0, len(acimadamedia)):
    if c == 0:
        print('D) Lista das pessoas que estão acima da média:')
    print('   ', end='')
    for k, v in acimadamedia[c].items():
        print(f'{k} = {v};', end=' ')
    print()
print('<< ENCERRADO >>')


