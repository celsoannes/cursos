# Título:       Exercício 8 – Conversor de Medidas
# Desafio:      008
# Requisito:    Aula 07
# Enunciado:    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros

print('====== EXERCÍCIO 008 ======')
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
