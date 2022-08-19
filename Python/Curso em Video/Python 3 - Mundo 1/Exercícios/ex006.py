# Título:       Exercício 6 – Dobro, Triplo, Raiz Quadrada
# Desafio:      006
# Requisito:    Aula 07
# Enunciado:    Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada

print('====== EXERCÍCIO 006 ======')
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
#r = n ** (1/2)
r = pow(n, (1/2))
print('O dibro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
