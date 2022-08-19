# Desafio:      076
# Enunciado:    Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.


print('====== DESAFIO 076 ======')
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)
fim = len(listagem)
for i in range(0, fim, 2):
    size = int(40 - len(listagem[i]))
    print('{}'.format(listagem[i]), end='')
    print('.' * size, end='')
    print('R$', end='')
    print('{:>8.2f}'.format(listagem[i+1]))
print('-' * 50)
