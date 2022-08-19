# Desafio:      044
# Enunciado:    Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço noramal e condição de pagamento:
#
# - À vista dinheiro/pix: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros


print('====== DESAFIO 044 ======')
valor = float(input('Qual o valor do produto: R$'))
print('Condição de pagamento:')
condição = int(input('Digite:\n1 - À vista\n2 - Cartão\n'))
if condição == 1:
    print('Você recebeu 10% de desconto.\nTotal a pagar: R$ {:.2f}'.format(valor - ((valor * 10) / 100)))
else:
    parcelas = int(input('Informe um número de parcelas: '))
    if parcelas == 1:
        print('Você recebeu 5% de desconto.\nTotal a pagar: R$ {:.2f}'.format(valor - ((valor * 5) / 100)))
    elif parcelas == 2:
        print('Você não recebeu nenhum desconto.\n Total a pagar R$ {}'.format(valor))
    else:
        print('Acrecimo de 20%\nTotal a pagar R$ {}'.format(valor + ((valor * 20) / 100)))