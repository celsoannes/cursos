# Desafio:      079
# Enunciado:    Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


print('====== DESAFIO 079 ======')
lista = []
opção = 'S'
while True:
    if opção == 'S':
        tmp = (int(input('Digite um valor: ')))
        if tmp not in lista:
            lista.append(tmp)
            print('Valor adicionado com sucesso...')
            opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        else:
            print('Valor duplicado, não será adicionado.')
            opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    elif opção == 'N':
        break
    else:
        print('Opção inválida')
        opção = str(input('Deseja continuar [S/N]')).strip().upper()[0]
lista.sort()
print(f'Você digitou os valores {lista}')

