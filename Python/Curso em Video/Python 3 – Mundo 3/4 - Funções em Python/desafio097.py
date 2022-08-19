# Desafio:      097
# Enunciado:    Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~


print('====== DESAFIO 097 ======')
def escreva(txt):
    tamanho = len(txt) + 6
    print('~' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('~' * tamanho)

escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')