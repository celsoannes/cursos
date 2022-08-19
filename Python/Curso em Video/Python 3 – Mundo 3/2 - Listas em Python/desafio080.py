# Desafio:      080
# Enunciado:    Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


print('====== DESAFIO 080 ======')
lista = list()
pos = 0
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0:
        lista.append(num)
        print('Adicionado no inicio da lista')
    else:
        if num >= max(lista):
            pos = lista.index(max(lista)) + 1
            lista.insert(pos, num)
            print('Adicionado ao final da lista')
        elif num <= min(lista):
            lista.insert(0, num)
            print('Adicionado no inicio da lista')
        else:
            for p, n in enumerate(lista):
                if num > n and num < lista[p+1]:
                    lista.insert(p+1, num)
                    print(f'Adicionado na posição {p+1} da lista')
print(lista)
