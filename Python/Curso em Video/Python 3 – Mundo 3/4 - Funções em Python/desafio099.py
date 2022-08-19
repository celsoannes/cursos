# Desafio:      099
# Enunciado:    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


print('====== DESAFIO 099 ======')
from time import sleep

def maior(* numeros):
    print('Analisando os valores passados...')
    mai = 0
    tot = len(numeros)
    for i in range(0, tot):
        if i == 0:
            mai = numeros[i]
        else:
            if numeros[i] > mai:
                mai = numeros[i]
        print(f'{numeros[i]} ', end='')
        sleep(.25)
    print(f'Foram informados {tot} valores ao todo.')
    print(f'O maior valor foi o {mai}.')



maior(2, 9, 4, 5, 7, 1)
maior(4, 0, 7)
maior(1, 2)
maior(6)
maior()

