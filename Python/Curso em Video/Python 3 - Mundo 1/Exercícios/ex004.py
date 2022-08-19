# Título:       Exercício 4 – Dissecando uma Variável
# Desafio:      004
# Requisito:    Aula 06
# Enunciado:    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

print('====== DESAFIO 004 ======')
a = input('Digite algo: ')
print('O tipo primitivo deste valor é: {}'.format(type(a)))
print('Só tem espaços? {}'.format(a.isspace()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumerico? {}'.format(a.isalnum()))
print('Esta em maiuscolas? {}'.format(a.isupper()))
print('Esta em minuscolas? {}'.format(a.islower()))
print('Esta capitalizada? {}'.format(a.istitle()))

