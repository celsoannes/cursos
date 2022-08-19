# Desafio:      096
# Enunciado:    Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


print('====== DESAFIO 095 ======')
def medida(l, c):
    area = l * c
    print(f'A área de um terreno {l} x {c} é de {area}m².')


print('Controle de Terrenos')
print('-' * 30)
l = float(input('LARGUA (m): '))
c = float(input('Comprimento (m): '))
medida(l, c)
