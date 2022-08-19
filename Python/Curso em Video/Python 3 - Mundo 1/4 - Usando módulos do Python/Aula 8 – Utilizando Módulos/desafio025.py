# Desafio:      024
# Enunciado:    Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

print('====== DESAFIO 024 ======')
nomecompleto = str(input('Informe o seu nome completo: ')).upper()
print('{} possui "SILVA" no nome: {}'.format(nomecompleto, 'SILVA' in nomecompleto))