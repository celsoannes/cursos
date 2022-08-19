# Desafio:      024
# Enunciado:    Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

print('====== DESAFIO 024 ======')
cidade = str(input('Digite o nome da cidade: '))
print('A cidade possui "SANTO" no nome: {}'.format('SANTO' in cidade.upper()))