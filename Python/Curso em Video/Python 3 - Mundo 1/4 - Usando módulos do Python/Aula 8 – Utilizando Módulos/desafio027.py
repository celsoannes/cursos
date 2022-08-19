# Desafio:      027
# Enunciado:    Faça um programa que leia o nome completo de uma pssoa, mostrando em seguida o primeiro e o último nome separadamente
#
# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

print('====== DESAFIO 027 ======')
nome = str(input('Nome completo: '))
nome = nome.split()
total = int(nome.count())
print('Nome: {}'.format(nome[0]))
print('Sobrenome: {}'.format(total))
