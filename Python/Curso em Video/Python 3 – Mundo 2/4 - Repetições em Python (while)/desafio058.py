# Desafio:      058
# Enunciado:    Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

print('====== DESAFIO 058 ======')
from random import randint
cpu = randint(0, 11)
p1 = 12
cont = 0
while cpu != p1:
    p1 = int(input('Adivinhe o número que armazenei em memória: '))
    cont += 1
print('Acertou depois de {} tentativas'.format(cont))
