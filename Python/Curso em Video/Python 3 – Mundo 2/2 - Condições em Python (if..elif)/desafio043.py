# Desafio:      043
# Enunciado:    Desenvolva uma lógica que leia o peso e a altura de uma pessoa e calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida


print('====== DESAFIO 043 ======')
peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))
imc = int(peso / (altura ** 2))
if imc < 18.5:
    print('IMC: {}\nPeso: \033[1:33mAbaixo do Peso\033[m'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('IMC: {}\nPeso: \033[1:32mIdeal\033[m'.format(imc))
elif imc >= 25 and imc <= 30:
    print('IMC: {}\nPeso: \033[1:33mSobrepeso\033[m'.format(imc))
elif imc >= 30 and imc <= 40:
    print('IMC: {}\nPeso: \033[1:31mObesidade\033[m'.format(imc))
else:
    print('IMC: {}\nPeso: \033[1:33:41mObesidade Mórbida\033[m'.format(imc))
