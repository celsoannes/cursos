# Desafio:      064
# Enunciado:    Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)


print('====== DESAFIO 064 ======')
i = 0
quantidade = 0
soma = 0
while i != 999:
    n = int(input('Informe um número: '))
    if n != 999:
        soma += n
        quantidade += 1
    else:
        i = n
print('Quantidade de números inseridos: {}\nTotal: {}'.format(quantidade, soma))
