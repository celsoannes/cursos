# Título:       Exercício 32 – Ano Bissexto
# Desafio:      032
# Requisito:    Aula 10
# Enunciado:    Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#
# BISSEXTO: 2016
# NÃO BISSEXTO: 1700, 1900

print('====== EXERCÍCIO 032 ======')
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))