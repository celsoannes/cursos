# Título:       Exercício 27 – Primeiro e último nome de uma pessoa
# Desafio:      027
# Requisito:    Aula 09
# Enunciado:    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#
# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

print('====== EXERCÍCIO 027 ======')
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
