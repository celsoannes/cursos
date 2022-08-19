# Desafio:      059
# Enunciado:    Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso


print('====== DESAFIO 059 ======')
n1 = int(input('Informe o primeiro Valor: '))
n2 = int(input('Informe o segundo Valor: '))
menu = 0
while menu != 5:
    menu = int(input('''MENU
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    Escolha uma opção: '''))
    if menu == 1:
        print('{}+{}= {}\n'.format(n1, n2, n1+n2))
    elif menu == 2:
        print('{}*{}= {}\n'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print('{} é o maior'.format(n1))
        else:
            print('{} é o maior'.format(n2))
    elif menu == 4:
        n1 = int(input('Informe o primeiro Valor: '))
        n2 = int(input('Informe o segundo Valor: '))
    elif menu == 5:
        print('Tchau!')
    else:
        print('Você digitou uma opção inválida!')