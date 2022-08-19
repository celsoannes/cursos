# Desafio:      067
# Enunciado:    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicidado for negativo.


print('====== DESAFIO 067 ======')
tábuada = 0
while True:
    tábuada = int(input('Quer ver a tabuada de qual valor? '))
    if tábuada < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    i = 0
    while i < 10:
        i += 1
        print(f'{tábuada} x {i} = {i*tábuada}')