# Aula 18

## Listas (Parte 2)

Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

### Variáveis Compostas

#### Uma lista principal com várias listas internas #1
>```py
>teste = list()
>teste.append('Gustavo')
>teste.append('40')
>galera = list()
>galera.append(teste[:])
>teste[0] = 'Maria'
>teste[1] = 22
>galera.append(teste[:])
>print(galera)
>```
>```py
>[['Gustavo', '40'], ['Maria', 22]]
>```

#### Uma lista principal com várias listas internas #2

>```py
>galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
>print(galera)
>```
>```py
>[['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
>```

#### Mostrando apenas dados do João:
>```py
>galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
>print(galera[0])
>```
>```py
>['João', 19]

#### Pegando apenas primeiro item de João:
>```py
>galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
>print(galera[0][0])
>```
>```py
>João
>```

#### Mostrando os valores da lista com `for`

>```py
>galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
>for p in galera:
>    print(f'{p[0]} tem {p[1]} anos de idade.')
>```
>```py
>João tem 19 anos de idade.
>Ana tem 33 anos de idade.
>Joaquim tem 13 anos de idade.
>Maria tem 45 anos de idade.
>```

#### Criando lista secundaria com dados teporarios

>```py
>galera = list()
>dado = list()
>for c in range(0, 3):
>    dado.append(str(input('Nome: ')))
>    dado.append(int(input('Idade: ')))
>    galera.append(dado[:])
>    dado.clear()
>print(galera)
>```
>```py
>Nome: Pedro
>Idade: 22
>Nome: Maria
>Idade: 33
>Nome: Claudia
>Idade: 55
>[['Pedro', 22], ['Maria', 33], ['Claudia', 55]]
>```
