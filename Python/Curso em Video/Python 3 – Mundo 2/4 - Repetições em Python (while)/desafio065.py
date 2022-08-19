# Desafio:      065
# Enunciado:    Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usário se ele quer ou não continuar a digitar valores.


print('====== DESAFIO 065 ======')
c = 'yes'
q = 'n'
soma = 0
loop = 0
maior = 0
menor = 0
while c != 'N':
    n = int(input('Digite um número: '))
    if loop == 0:
        maior = menor = n
    elif maior < n:
        maior = n
    elif menor > n:
        menor = n
    soma += n
    loop += 1
    q = 's'
    while q != 'sn':
        c = str(input('Continuar? [S/N] ')).strip().upper()
        if c == 'S' or c == 'N':
            q = 'sn'
        else:
            q = 'n'
            print('{} não é uma opção válida'.format(c))
print('A média é: {}'.format(soma / loop))
print('{} foi o MAIOR e {} foi o MENOR'.format(maior, menor))
