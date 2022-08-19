def moeda(n=0, f=True):
    if f:
        return f'{n:.2f}'
    return n


def aumentar(n):
    return ((n * 10) / 100) + n


#def diminuir(n):


def dobro(n):
    return n * 2


def metade(n):
    return n / 2
