# Título:       Exercício 53 – Detector de Palíndromo
# Desafio:      053
# Requisito:    Aula 12
# Enunciado:    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#
# Ex.:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA


print('====== EXERCÍCIO 053 ======')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
