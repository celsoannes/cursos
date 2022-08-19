# Desafio:      075
# Enunciado:    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares


print('====== DESAFIO 075 ======')
lista = (int(input('Informe o primeiro número: ')),
         int(input('Informe o segundo número: ')),
         int(input('Informe o terceiro número: ')),
         int(input('Informe o quarto número: ')))
vezes = lista.count(9)
posição = lista.index(3)
print(f'O número nove apareceu {vezes} vezes')
print(f'O primeiro valor três foi digitado na {posição+1}ª posição.')
print('Os números pares foram:')
for i in range(0, 4):
    if lista[i] % 2 == 0:
        print(lista[i])


