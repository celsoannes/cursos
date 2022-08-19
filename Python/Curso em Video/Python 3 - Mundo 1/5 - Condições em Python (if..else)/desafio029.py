# Desafio:      029
# Enunciado:    Escreva um programa que leia a velocidade de um carro.
#
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite

print('====== DESAFIO 029 ======')
v = int(input('Informe a velocidade: '))
if v > 80:
    print('Você foi multado em R$100')
    multa = v - 80
    if multa > 0:
        multa = multa * 7
        print('A multa vai custar R$7.00 por cada Km acima do limite')
        print('A multa é de {}'.format(100+multa))
else:
    print('Dentro do limite de velocidade')
