# Desafio:      032
# Enunciado:    Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
#
# Critérios para definir o ano bissexto
#
# Para podermos entender melhor, vamos realizar o cálculo do ano bissexto para verificar quais dos anos descritos abaixo encaixam-se nessa categoria. Antes disso, precisamos saber quais são os critérios que o definem, ou seja:
#
# Para ser bissexto, o ano deve ser:
# 1. Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
# 2. Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
# 3. Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.
#
# De acordo com os critérios estabelecidos acima, vamos determinar se o ano de 2015 ou 2016 é bissexto. Para isso, existem três situações preestabelecidas:
# 1ª situação: Se o ano de 2015 ou 2016 for uma divisão exata em relação a 4, deveremos verificar, em seguida, se não é divisível por 100. Se não for, o ano será bissexto;
# 2ª situação: Se o ano de 2015 ou 2016 não for divisível por 4, então deveremos verificar se ele é divisível por 400. Se também não for divisível, o ano de 2015 não será bissexto;
# 3ª situação: Se o ano de 2015 ou 2016 não for divisível por 4, então devemos verificar se ele é divisível por 400. Caso seja, o ano de 2015 é bissexto.

print('====== DESAFIO 032 ======')
ano = int(input('Digite um ano: '))
if (ano % 4) == 0:
    if (ano % 100) == 0:
        print('{} é divisível por quatro e é divisível por 100.'.format(ano))
        print('{} não é bissexto.'.format(ano))
    else:
        print('{} é divisível por quatro e não é divisível por 100.'.format(ano))
        print('{} é bissexto.'.format(ano))
else:
    if (ano % 400) == 0:
        print('{} não é divisível por quatro e é divisível por 400.'.format(ano))
        print('{} é bissexto.'.format(ano))
    else:
        print('{} não é divisível por quatro e não é divisível por 400.'.format(ano))
        print('{} não é bissexto.'.format(ano))
