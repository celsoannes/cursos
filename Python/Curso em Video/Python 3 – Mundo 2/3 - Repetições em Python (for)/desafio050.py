# Desafio:      050
# Enunciado:    Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o


print('====== DESAFIO 050 ======')
s=0
for i in range(0, 6):
    n = int(input('Informe o {}º número: '.format(i+1)))
    if n % 2 == 0:
        s = s + n
print('O total é: {}'.format(s))