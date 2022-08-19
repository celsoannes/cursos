# Título:       Exercício 49 – Tabuada v.2.0
# Desafio:      049
# Requisito:    Aula 12
# Enunciado:    Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.


print('====== EXERCÍCIO 049 ======')
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))