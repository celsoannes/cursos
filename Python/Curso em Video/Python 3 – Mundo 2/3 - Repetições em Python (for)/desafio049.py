# Desafio:      049
# Enunciado:    Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.


print('====== DESAFIO 049 ======')
n = int(input('Escolha um número para fazer a tabuada: '))
for i in range(1, 11):
    print('{} x {:>2} = {}'.format(n, i, n*i))
