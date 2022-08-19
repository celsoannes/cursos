# Desafio:      035
# Enunciado:    Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triângulo.
#
# Condição de existência do triângulo
# Dados três segmentos de reta, nem sempre eles podem formar um triângulo. Para que os três segmentos formem um triângulo, existe o que conhecemos como condição de existência, que é a seguinte: a soma de dois lados é sempre menor que o terceiro lado.
#
# Em um triângulo, segundo a condição de existência, temos que:
# a + b > c
# b + c > a
# a + c > b

print('====== DESAFIO 035 ======')
r1 = int(input('Informe o tamanho da primeira reta: '))
r2 = int(input('Informe o tamanho da segunda reta: '))
r3 = int(input('Informe o tamanho da terceura reta: '))
if (r1 + r2) > r3:
    if (r2 + r3) > r1:
        if (r1 + r3) > r2:
            print('Podemos formar um triângulo')
        else:
            print('Não podemos formar um triângulo')
    else:
        print('Não podemos formar um triângulo')
else:
    print('Não podemos formar um triângulo')