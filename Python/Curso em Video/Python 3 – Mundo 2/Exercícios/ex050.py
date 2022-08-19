# Título:       Exercício 50 – Soma dos pares
# Desafio:      050
# Requisito:    Aula 12
# Enunciado:    Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.


print('====== EXERCÍCIO 050 ======')
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))