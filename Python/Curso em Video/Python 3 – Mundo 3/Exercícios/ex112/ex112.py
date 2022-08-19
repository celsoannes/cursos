# Título:       Exercício 112 – Entrada de dados monetários
# Desafio:      112
# Requisito:    Aula 22
# Enunciado:    Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.


print('====== EXERCÍCIO 112 ======')
from utilidadescev import moeda
from utilidadescev import dado
p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)
