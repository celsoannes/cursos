# Desafio:      057
# Enunciado:    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja erradom peça a digitação novamente até ter um valor correto.


print('====== DESAFIO 057 ======')

sexo = 'm'
while sexo not in ('F', 'M'):
    sexo = str(input('Digite o sexo [M/F]: ')).strip()
    print(sexo)
