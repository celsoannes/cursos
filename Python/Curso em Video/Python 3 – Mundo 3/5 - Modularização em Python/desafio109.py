# Desafio:      109
# Enunciado:    Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


print('====== DESAFIO 108 ======')
import moeda109
num = float(input('Digite o preço: R$'))

print(f'A metade de R${moeda109.moeda(num)} é R${moeda109.moeda(moeda109.metade(num), f=False)}')
print(f'O dobro de R${moeda109.moeda(num)} é R${moeda109.moeda(moeda109.dobro(num))}')
print(f'Aumentando 10%, temos R${moeda109.moeda(moeda109.aumentar(num))}')
