# Desafio:      056
# Enunciado:    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos


print('====== DESAFIO 056 ======')
média = 0
nome = ''
mulheres = 0
velho = 0
for i in range(0, 4):
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    sex = str(input('Sexo: M ou F: '))
    média = média + age
    if sex == 'F':
        if age < 20:
            mulheres = mulheres + 1
    else:
        if velho == 0:
            velho = age
            nome = name
        elif velho < age:
            velho = age
            nome = name
print('A média de idade do grupo é: {}'.format(média/4))
if velho == 0:
    print('Não existem homens no grupo')
else:
    print('{} é o Homem mais velho do grupo'.format(nome.title()))

if mulheres == 0:
    print('Não existe mulheres no grupo')
else:
    print('Existem {} mulheres menores de 20 anos'.format(mulheres))
