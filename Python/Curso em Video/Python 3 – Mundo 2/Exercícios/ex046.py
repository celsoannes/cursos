# Título:       Exercício 46 – Contagem regressiva
# Desafio:      046
# Requisito:    Aula 12
# Enunciado:    Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.


print('====== EXERCÍCIO 046 ======')
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BOM! BUM! POOW!')