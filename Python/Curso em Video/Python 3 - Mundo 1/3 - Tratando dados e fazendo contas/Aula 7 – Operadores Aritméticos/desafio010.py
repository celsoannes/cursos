# Desafio:      010
# Enunciado:    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

print('====== DESAFIO 010 ======')
reais = float(input('Quantos reais você tem? '))
dolar = 3.27
compra = reais / dolar
print('Você pode comprar {} dolares!'.format(compra))