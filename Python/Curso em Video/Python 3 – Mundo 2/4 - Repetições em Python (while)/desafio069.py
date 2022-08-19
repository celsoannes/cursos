# Desafio:      069
# Enunciado:    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário que ou nãp continuar.
# No final mostre:
#
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos


print('====== DESAFIO 069 ======')
continuar = 'S'
homens = mulheres = maior = 0
while True:
    sexo = 'a'
    if continuar == 'N':
        break
    elif continuar == 'S':
        idade = int(input('Idade: '))
        while sexo not in 'MF':
            sexo = str(input('Sexo [M/F] ')).strip().upper()[0]
        if idade > 18:
            maior += 1
        if sexo == 'H':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres += 1
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    else:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print(f'{maior} pessoas tem mais de 18')
print(f'Foram cadastrados {homens} homens')
print(f'{mulheres} mulheres tem menos de 20 anos')
