# Desafio:      101
# Enunciado:    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


print('====== DESAFIO 101 ======')
from datetime import datetime
def voto(nsc):
    idade = datetime.today().year - nsc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print(f'NÃO VOTA.')
    elif idade >= 18:
        print('VOTO OBRIGATÓRIO!')
    else:
        print('VOTO OPCIONAL.')


voto(int(input('Em que ano você nasceu? ')))
