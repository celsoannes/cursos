# Título:       Exercício 90 – Dicionário em Python
# Desafio:      090
# Requisito:    Aula 19
# Enunciado:    Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.


print('====== EXERCÍCIO 090 ======')
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')