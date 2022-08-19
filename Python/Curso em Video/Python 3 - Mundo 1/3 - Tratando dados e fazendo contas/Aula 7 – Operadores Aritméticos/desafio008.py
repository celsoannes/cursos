# Desafio:      008
# Enunciado:    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros

print('====== DESAFIO 008 ======')
m = int(input('Digite uma medida em metros: '))
cm = m * 100
mm = m * 1000
print('{} metros equivalem a {} centimetros.\n {} metros equivalem a {} milimetros'.format(m, cm, m, mm))
