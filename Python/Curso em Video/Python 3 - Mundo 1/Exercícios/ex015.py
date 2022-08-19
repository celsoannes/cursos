# Título:       Exercício 15 – Aluguel de Carros
# Desafio:      015
# Requisito:    Aula 07
# Enunciado:    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('====== EXERCÍCIO 015 ======')
km = float(input('Quantidade de Km percorridos: '))
kmrodados = km * 0.15
dias = int(input('Quantidade de dias alugado: '))
diarias = dias * 60
print('{} km rodados custam R$ {:.2f}'.format(km, kmrodados))
print('{} dias custam R$ {}'.format(dias, diarias))
print('O total a ser pago é: {:.2f}'.format(kmrodados+diarias))
