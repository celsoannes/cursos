# Desafio:      013
# Enunciado:    Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
print('====== DESAFIO 013 ======')
salario = float(input('Informe o salário do funcionário: '))
aumento = (salario * 15) / 100
print('O salário de {} R$ foi reajustado em 15%, o novo salário é de: {} R$'.format(salario, salario + aumento))
