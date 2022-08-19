# Título:       Exercício 7 – Média Aritmética
# Desafio:      007
# Requisito:    Aula 07
# Enunciado:    Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média

print('====== EXERCÍCIO 007 ======')
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1+n2)/2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))
