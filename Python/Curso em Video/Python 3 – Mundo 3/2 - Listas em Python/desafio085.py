# Desafio:      085
# Enunciado:    Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


print('====== DESAFIO 085 ======')
lista = [[], []]
for i in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        lista[0].insert(0, n)
    else:
        lista[1].insert(0, n)
lista[0].sort()
lista[1].sort()
print(f'Pares: {lista[0]}')
print(f'Impares: {lista[1]}')

