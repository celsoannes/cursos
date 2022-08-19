# Desafio:      036
# Enunciado:    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#
# Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário ou então o emprestimo será negado


print('====== DESAFIO 036 ======')
casa = float(input('Qual o valor da casa R$'))
salário = float(input('Qual o seu salário R$'))
anos = float(input('Vai pagar em quantos anos? '))
prestação = (casa / anos) / 12
margem = ((salário * 30) / 100)
if prestação > margem:
    print('Emprestimo negado!')
    print('Prestação de {:.2f} excede 30% do salário {:.2f}'.format(prestação, margem))
else:
    print('Parabéns! Seu empréstimo foi aprovado.')