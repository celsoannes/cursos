# Título:       Exercício 31 – Custo da Viagem
# Desafio:      031
# Requisito:    Aula 10
# Enunciado:    Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


print('====== EXERCÍCIO 031 ======')
distância = float(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}Km.'.format(distância))
'''if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45'''
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
