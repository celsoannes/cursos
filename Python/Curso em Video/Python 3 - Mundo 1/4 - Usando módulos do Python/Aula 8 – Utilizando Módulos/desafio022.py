# Desafio:      022
# Enunciado:    Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# O nome com todas as letras em maiúsculas
# O nome com todas minúscolas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

print('====== DESAFIO 021 ======')
nome = str(input('Nome completo: '))
print('O nome com todas as letras em maiúsculas: {}'.format(nome.upper()))
print('O nome com todas minúscolas: {}'.format(nome.lower()))
print('Quantas letras ao todo (sem considerar espaços): {}'.format(len(nome.strip())))
nome = nome.split()
print('Quantas letras tem o primeiro nome: {}'.format(len(nome[0])))
