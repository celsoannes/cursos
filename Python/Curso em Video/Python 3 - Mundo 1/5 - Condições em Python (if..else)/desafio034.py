# Desafio:      034
# Enunciado:    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#
# Para salários superiores a R$1.250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

print('====== DESAFIO 034 ======')
s = float(input('Informe o salário: R$'))
if (s > 1250):
    print('Seu salário foi reajustado em 10%')
    print('Seu novo salário é de R${:.2f}'.format(((s*10)/100)+s))
else:
    print('Seu salário foi reajustado em 15%')
    print('Seu novo salário é de R${}'.format(((s*15)/100)+s))
