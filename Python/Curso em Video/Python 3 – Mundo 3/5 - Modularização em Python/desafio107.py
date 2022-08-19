# Desafio:      107
# Enunciado:    Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.


print('====== DESAFIO 107 ======')
import moeda107
num = float(input('Digite o preço: R$'))
print(f'A metade de R${num} é R${moeda107.metade(num)}')
print(f'O dobro de R${num} é {moeda107.dobro(num)}')
print(f'Aumentando 10%, temos R${moeda107.aumentar(num)}')
