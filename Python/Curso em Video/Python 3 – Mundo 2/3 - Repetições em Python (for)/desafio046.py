# Desafio:      046
# Enunciado:    Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.


print('====== DESAFIO 046 ======')
from time import sleep
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('BOOMM!!!')