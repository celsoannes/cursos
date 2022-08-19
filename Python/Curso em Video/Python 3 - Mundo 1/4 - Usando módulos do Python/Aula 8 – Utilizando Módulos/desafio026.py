# Desafio:      026
# Enunciado:    Faça um programa que leia uma frase pelo teclado e mostre:
#
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

print('====== DESAFIO 026 ======')
frase = str(input('Digite uma frase: '))
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('{} é a posição onde a letra "A" aparece a primeira vez.'.format(frase.find('A')))
#print('A letra "A" aparece a última vez na posição {}.'.format())