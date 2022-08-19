# Desafio:      090
# Enunciado:    Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.


print('====== DESAFIO 090 ======')
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
elif aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Aprovado'
print('-=' * 50)
for n, m in aluno.items():
    print(f"- {n} é igual a {m}")
