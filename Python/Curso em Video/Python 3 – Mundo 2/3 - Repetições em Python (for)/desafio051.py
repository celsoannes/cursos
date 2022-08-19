# Desafio:      051
# Enunciado:    Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.


print('====== DESAFIO 051 ======')
print('{:=^40}'.format(' PROGRESSAO ARITIMÉTICA '))
pt = int(input('Informe o PRIMEIRO TERMO: '))
r = int(input('Informe a RAZÃO: '))
for a in range(1, 11):
    an = pt + (a - 1) * r
    print(an)
