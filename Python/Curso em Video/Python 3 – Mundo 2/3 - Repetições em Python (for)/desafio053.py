# Desafio:      053
# Enunciado:    Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
#
# Ex.:
# - APOS A SOPA
# - A SACADA DA CASA
# - A TORRE DA DERROTA
# - O LOBO AMA O BOLO
# - ANOTARAM A DATA DA MARATONA


print('====== DESAFIO 053 ======')
frase = str(input('Escreva uma frase: ')).upper()

# separa a frase em um array
frase = frase.split()

# reserva as variaveis para serem usadas no for
palindromo = ''
rfrase = ''
flag = 0

# junta o array
for i in range(0, len(frase)):
    palindromo = str(palindromo + frase[i])
print(palindromo)

# inverte a frase
for i in range(len(palindromo), 0, -1):
    rfrase = rfrase + (palindromo[i-1:i])
print(rfrase)

#testa
for i in range(0, len(palindromo)):
    if palindromo[i:i+1] != rfrase[i:i+1]:
        flag = flag + 1


if flag == 0:
    print('É um palindromo')
else:
    print('Não é um palindromo')