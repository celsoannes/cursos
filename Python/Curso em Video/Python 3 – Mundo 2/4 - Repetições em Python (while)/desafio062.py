# Desafio:      062
# Enunciado:    Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.


print('====== DESAFIO 062 ======')
print('{:=^40}'.format(' PROGRESSAO ARITIMÉTICA '))
pt = int(input('Informe o PRIMEIRO TERMO: '))
r = int(input('Informe a RAZÃO: '))
i = 0
t = 10
while i != t:
    an = pt + i * r
    print(an, end=' ')
    i += 1
    if i == t:
        n = int(input('\nMostrar mais quantos termos? '))
        if t == 0:
            i == t
        else:
            t += n