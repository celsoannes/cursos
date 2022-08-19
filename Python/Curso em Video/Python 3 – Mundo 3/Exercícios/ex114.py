# Título:       Exercício 114 – Site está acessível?
# Desafio:      114
# Requisito:    Aula 23
# Enunciado:    Crie um código em Python que teste se o site pudim está acessível pelo computador usado.


print('====== EXERCÍCIO 114 ======')
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não esta acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    #print(site.read())