# Desafio:      012
# Enunciado:    Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
print('====== DESAFIO 012 ======')

preco = float(input('Informe o preço do produto: '))
desconto = (preco * 5) / 100
print('O valor do produto com desconto é {}'.format(preco - desconto))
