# Desafio:      089
# Enunciado:    Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


print('====== DESAFIO 089 ======')
continuar = ' '
no = 0
alunos = []
while continuar not in 'N':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno = [nome, nota1,  nota2]
    alunos.insert(no, aluno)
    no += 1
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
print('-=' * 50)
print(f'{"No.":<4}{"NOME":<20}{"MÉDIA":>6}')
print('-' * 30)
for i, l in enumerate(alunos):
    média = (l[1] + l[2]) / 2
    print(f'{i:<4}{l[0]:<20}{média:>6}')
print('-' * 30)
while True:
    matricula = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if matricula == 999:
        break
    print(f'Notas de {alunos[matricula][0]} são Nota 1: {alunos[matricula][1]}, Nota 2: {alunos[matricula][2]}')
    print('-' * 30)

#print(alunos)
