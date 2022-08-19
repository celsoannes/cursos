#direita = 'DIREITA'
#print('Alinhado à: {:>20}.'.format(direita))

#esquerda = "ESQUERDA"
#print('Alinhado à : {:<20}.'.format(esquerda))

#centro = 'CENTRO'
#print('Alinhado ao: {:^20}.'.format(centro))

#centro = 'CENTRO'
#print('Alinhado ao: {:=^20}.'.format(centro))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potência {}\n'.format(di, e))

# Colocando na mesma linha:
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))