# Desafio:      104
# Enunciado:    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)


print('====== DESAFIO 104 ======')


def leiaInt(txt):
    num = input(txt)
    if num.isnumeric():
        return num
    else:
        print('\33[0;31mErro! Digite um número inteiro válido.\033[m')
        exit()


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
