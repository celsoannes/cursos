# Desafio:      072
# Enunciado:    Crie um programa que tenha uma tupla totalmente preencida com uma contagem por extenso, de zero até vinte.
#
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrál-lo por extenso.


print('====== DESAFIO 072 ======')
numero = 21
numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorzer', 'quinze', 'desseseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero >= 0 and numero <= 20:
        print(f'Você digitou o número {numeros[numero]}')
        break
