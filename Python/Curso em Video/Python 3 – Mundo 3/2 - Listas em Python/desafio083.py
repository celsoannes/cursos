# Desafio:      083
# Enunciado:    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


print('====== DESAFIO 083 ======')
expressão = str(input('Digite uma expressão: '))
tamanho = len(expressão)
lista = []
for i in range(0, tamanho):
    lista.append(expressão[i])
abre = lista.count('(')
fecha = lista.count(')')
if abre == fecha:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão esta errada!')