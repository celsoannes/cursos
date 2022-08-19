# Título:       Exercício 25 – Procurando uma string dentro de outra
# Desafio:      025
# Requisito:    Aula 09
# Enunciado:    Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

print('====== EXERCÍCIO 025 ======')
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))