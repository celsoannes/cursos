# Título:       Exercício 13 – Reajuste Salarial
# Desafio:      013
# Requisito:    Aula 07
# Enunciado:    Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

print('====== EXERCÍCIO 013 ======')
salário = float(input('Qual é o salário do Funcionário? R$ '))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}'.format(salário, novo))