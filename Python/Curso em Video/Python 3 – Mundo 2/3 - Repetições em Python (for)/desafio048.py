# Desafio:      048
# Enunciado:    Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500


print('====== DESAFIO 048 ======')
soma = 0
for i in range(1, 500):
    impar = i % 2
    multiplo = i * 3
    if impar != 0:
        soma = soma + multiplo
print('A soma dos números múltiplos de 3 é :\033[1:33m{}\033[m'.format(soma))
