# Desafio:      078
# Enunciado:    Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


print('====== DESAFIO 078 ======')
lista = []
for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
maior = max(lista)
menor = min(lista)
print(f'{maior} foi o maior valor digitado e se enconta na posição ', end='')
for n in range(0, 5):
    if lista[n] == maior:
        print(f'{n}.. ', end='')
print(f'\n{menor} foi o menor valor digitado e se encontra na posição ', end='')
for n in range(0, 5):
    if lista[n] == menor:
        print(f'{n}.. ', end='')


