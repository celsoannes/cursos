# Título:       Exercício 10 – Conversor de Moedas
# Desafio:      010
# Requisito:    Aula 07
# Enunciado:    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
#               Considere US$ 1.00 = R$ 3,27

print('====== EXERCÍCIO 010 ======')
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))