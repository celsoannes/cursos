# Desafio:      100
# Enunciado:    Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.


print('====== DESAFIO 100 ======')
from random import randint
from time import sleep
números = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = randint(1, 10)
        print(f'{n} ', end='')
        números.append(n)
        sleep(.3)
    print('PRONTO!')


def somaPar():
    soma = 0
    for n in números:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {números}, temos {soma}')


sorteia()
somaPar()
