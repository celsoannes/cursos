# Desafio:      039
# Enunciado:    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

import datetime
print('====== DESAFIO 039 ======')
nascimento = int(input('Informe o ano de nascimento: '))
ano = datetime.datetime.today().year
alistamento = ano - nascimento
if alistamento < 18:
    print('Você ainda irá se alistar.\nFaltam {} anos para você se alistar'.format(18 - alistamento))
elif alistamento == 18:
    print('Você deve se alistar este ano')
else:
    print('Já passou o tempo do seu alistamento\nJá se passaram {} anos do seu alistamento.'.format(alistamento - 18))
