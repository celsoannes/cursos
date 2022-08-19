# Desafio:      031
# Enunciado:    Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

print('====== DESAFIO 031 ======')
km = int(input('Qual é a distância da viagem Km: '))
if km <= 200:
    print('Sua viagem custará R${:.2f}'.format(km*0.50))
else:
    print('Sua viagem custará R${}'.format(km*0.45))