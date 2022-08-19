# Título:       Exercício 83 – Validando expressões matemáticas
# Desafio:      083
# Requisito:    Aula 17
# Enunciado:    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


print('====== EXERCÍCIO 083 ======')
expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == '(':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta válida!')
else:
    print('Sua expressão esta errada!')