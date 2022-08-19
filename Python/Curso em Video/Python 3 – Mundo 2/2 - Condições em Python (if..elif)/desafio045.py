# Desafio:      045
# Enunciado:    Crie um programa que faça o computador jogar Jokenpô com você.


print('====== DESAFIO 045 ======')

from random import randint
from time import sleep
escolha = randint(1, 3)
if escolha == 1:
    cpu = str('pedra')
elif escolha == 2:
    cpu = str('papel')
else:
    cpu = str('tesoura')

p1 = str(input('Digite para jogar Jokenpô: Pedra, Papel ou Tesoura\n: ')).lower()
print('\nJo..')
sleep(1)
print('ken..')
sleep(1)
print('PO!\n')

if cpu == p1:
    print('Empate. Os dois escolheram {}'.format(cpu.upper()))
elif ( cpu == 'pedra' and p1 == 'tesoura' ) or ( cpu == 'papel' and p1 == 'pedra' ) or ( cpu == 'tesoura' and p1 == 'papel' ):
    print('Xiii. Você perdeu eu escolhi {}'.format(cpu.capitalize()))
else:
    print('Parabéns, você ganhou! Eu escolhi {}'.format(cpu.capitalize()))