# Título:       Exercício 99 – Função que descobre o maior
# Desafio:      099
# Requisito:    Aula 20
# Enunciado:    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


print('====== EXERCÍCIO 099 ======')
from time import sleep


def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 0, 7)
maior(1, 2)
maior(6)
maior()