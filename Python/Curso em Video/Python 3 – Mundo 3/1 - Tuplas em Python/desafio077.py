# Desafio:      077
# Enunciado:    Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


print('====== DESAFIO 077 ======')
lista = ('Todavia', 'desenvolvimento', 'distintas', 'formas', 'estimula', 'diretrizes')
for palavra in lista:
    print(f'Na palavra {palavra.upper()} temos', end='')
    for n in range(0, len(palavra)):
        if 'a' in palavra[n]:
            print(' a', end='')
        elif 'e' in palavra[n]:
            print(' e', end='')
        elif 'i' in palavra[n]:
            print(' i', end='')
        elif 'o' in palavra[n]:
            print(' o', end='')
        elif 'u' in palavra[n]:
            print(' u', end='')
    print('')