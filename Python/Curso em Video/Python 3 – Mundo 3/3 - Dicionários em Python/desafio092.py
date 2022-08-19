# Desafio:      092
# Enunciado:    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.


print('====== DESAFIO 092 ======')
from _datetime import date
carteira = {
    'nome': str(input('Nome: ')),
    'idade': (date.today().year - int(input('Ano de Nascimento: '))),
    'ctps': int(input('Carteira de Trabalho (0 não tem): '))
}
if carteira['ctps'] != 0:
    carteira['contratação'] = int(input('Ano de Contratação: '))
    carteira['salário'] = float(input('Salário: R$'))
    carteira['aposentadoria'] = (30 - (date.today().year - carteira['contratação'])) + carteira['idade']
    #carteira['aposentadoria'] = (30 - (date.today().year - carteira['contratação']))

for k, v in carteira.items():
    print(f'{k} tem o valor {v}')
