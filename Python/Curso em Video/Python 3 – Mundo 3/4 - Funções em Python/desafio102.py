# Desafio:      102
# Enunciado:    Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


print('====== DESAFIO 102 ======')


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n
    """
    fatorial = 1
    msg = ''
    for c in range(n, 0, -1):
        fatorial = (fatorial * c)
        if show is True:
            msg += f'{c}'
            if c != 1:
                msg += ' x '
            else:
                msg += ' = '
    msg += f'{fatorial}'
    return msg


print(fatorial(5))
#help(fatorial)
