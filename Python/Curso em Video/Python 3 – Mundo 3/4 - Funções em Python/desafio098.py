# Desafio:      098
# Enunciado:    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


print('====== DESAFIO 097 ======')


def contagem(n1, n2, passo):
    print('-=' * 20)
    print(f'Contagem de {n1} até {n2} de {passo} em {passo}')
    if n2 < n1:
        if passo > 0:
            passo = -passo
    for i in range(n1, n2, passo):
        print(f'{i} ', end='')
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
n1 = int(input('Início: '))
n2 = int(input('Fim: '))
p = int(input('Passo: '))
contagem(n1, n2, p)