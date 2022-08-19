# Desafio:      108
# Enunciado:    Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.


print('====== DESAFIO 108 ======')
import moeda108
num = float(input('Digite o preço: R$'))

print(f'A metade de R${moeda108.moeda(num)} é R${moeda108.moeda(moeda108.metade(num))}')
print(f'O dobro de R${moeda108.moeda(num)} é R${moeda108.moeda(moeda108.dobro(num))}')
print(f'Aumentando 10%, temos R${moeda108.moeda(moeda108.aumentar(num))}')
