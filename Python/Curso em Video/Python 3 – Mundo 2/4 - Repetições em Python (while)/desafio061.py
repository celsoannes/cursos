# Desafio:      061
# Enunciado:    Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.


print('====== DESAFIO 061 ======')
print('{:=^40}'.format(' PROGRESSAO ARITIMÉTICA '))
pt = int(input('Informe o PRIMEIRO TERMO: '))
r = int(input('Informe a RAZÃO: '))
i = 0
while i < 10:
    an = pt + i * r
    print(an, end=' ')
    i += 1