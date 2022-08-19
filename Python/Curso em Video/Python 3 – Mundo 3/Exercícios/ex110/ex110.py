# Título:       Exercício 110 – Reduzindo ainda mais seu programa
# Desafio:      110
# Requisito:    Aula 22
# Enunciado:    Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.


print('====== EXERCÍCIO 110 ======')
import moeda
p = float(input('Digite o preço: R$'))
moeda.resumo(p)
