# Desafio:      041
# Enunciado:    A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER


print('====== DESAFIO 041 ======')
from datetime import datetime
nascimento = int(input('Ano de nascimento: '))
categoria = (datetime.today().year - nascimento)
if categoria <= 9:
    print('O atleta possui {} anos, categoria: MIRIM'.format(categoria))
elif categoria > 9 and categoria <= 14:
    print('O atleta possui {} anos, categoria: INFANTIL'.format(categoria))
elif categoria > 14 and categoria <= 19:
    print('O atleta possui {} anos, categoria: JUNIOR'.format(categoria))
elif categoria == 20:
    print('O atleta possui 20 anos, categoria: SÊNIOR')
else:
    print('O atleta possui {} anos, categoria MASTER'.format(categoria))
