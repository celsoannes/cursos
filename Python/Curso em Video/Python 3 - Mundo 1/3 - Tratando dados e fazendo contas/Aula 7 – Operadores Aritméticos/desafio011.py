# Desafio:      011
# Enunciado:    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma àewa de 2m quadrados
print('====== DESAFIO 011 ======')

altura = int(input('Informe a Altura da parede: '))
largura = int(input('Informe a Largura da parede: '))
area = altura * largura
litros = area / 2
print('A parede possui {} metros quadrados e será necessário {} litros de tinta'.format(area, litros))
