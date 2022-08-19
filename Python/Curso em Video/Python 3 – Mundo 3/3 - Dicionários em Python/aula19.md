# Aula 19

## Dicionários

### Teoria

Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

```py
filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
         }
```

#### Valor:

>```py
>print(filme.values())
>```
>```py
>dict_values(['Star Wars', 1977, 'George Lucas'])
>```


#### Chave

>```py
>print(filme.keys())
>```
>```py
>dict_keys(['titulo', 'ano', 'diretor'])
>```


#### Item:
>```py
>print(filme.items())
>```
>```py
>dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])
>```


##### Lendo o dicionario em uma estrutura de repetição
>```py
>for k, v in filme.items():
>    print(f'O {k} é {v}')
>```
>```py
>O titulo é Star Wars
>O ano é 1977
>O diretor é George Lucas
>```

#### Juntando listas, tuplas e dicionários

Estrutura de Lista com dicionários dentro

```py
locadora = [
    {'titulo':'Star Wars',
     'ano':1977,
     'diretor':'George Lucas'},
    {'titulo':'Avengers',
     'ano':2012,
     'diretor':'Joss Whedon'},
    {'titulo':'Matrix',
     'ano':1999,
     'diretor':'Wachowski'},
]
```

>```py
>print(locadora[0]['ano'])
>```
>```py
>1977
>```

>```py
>print(locadora[2]['titulo'])
>```
>```py
>Matrix
>```

### Prática

```py
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

O Gustavo tem 22 anos.
```

#### Mostrar as chaves: `keys`
```py
print(pessoas.keys())

dict_keys(['nome', 'sexo', 'idade'])
```

#### Mostrar os valores: `values`

```py
print(pessoas.values())

dict_values(['Gustavo', 'M', 22])
```

#### Mostrar os itens: `items`
```py
print(pessoas.items())

dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
```

#### Acessando chave, valores e itens através de laços

##### Buscando por chaves `key`

>```py
>pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
>for k in pessoas.keys():
>    print(k)
>```
>```py
>nome
>sexo
>idade
>```

##### Buscando por valores `values`

>```py
>pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
>for k in pessoas.values()
>    print(k)
>```
>```py
>Gustavo
>M
>22
>```

##### Buscando por itens `ìtems`

Não se usa `enumerate` em dicionários
 
>```py
>pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
>for k, v in pessoas.items():
>    print(f'{k} = {v}')
>```
>```py
>nome = Gustavo
>sexo = M
>idade = 22
>```

#### Apagando um elemento:

>```py
>pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
>del pessoas['sexo']
>for k, v in pessoas.items():
>    print(f'{k} = {v}')
>```
>```py
>nome = Gustavo
>idade = 22
>```


#### Modificando um elemento
>```py
>pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
>pessoas['nome'] = 'Leandro'
>for k, v in pessoas.items():
>    print(f'{k} = {v}')
>```
>```py
>nome = Leandro
>sexo = M
>idade = 22
>```


#### Adicionando um elemento

>```py
>pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
>pessoas['peso'] = 98.5
>for k, v in pessoas.items():
>    print(f'{k} = {v}')
>```
>```py
>nome = Gustavo
>sexo = M
>idade = 22
>peso = 98.5
>```


### Criando um dicionário dentro de uma lista
```py
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paula', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
```

Mostrando `estado1`
>```py
>print(estado1)
>```
>```py
>{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
>```

Mostrando `estado2`
>```py
>print(estado2)
>```
>```py
>{'uf': 'São Paula', 'sigla': 'SP'}
>```

Mostrando a lista `brasil`
>```py
>print(brasil)
>```
>```py
>[{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paula', 'sigla': 'SP'}]
>```

Mostrando o primeiro estado adicionado:
>```py
>print(brasil[0])
>```
>```py
>{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
>```

Mais exemplos:
>```py
>print(brasil[0]['uf'])
>```
>```py
>Rio de Janeiro
>```

>```py
>print(brasil[1]['sigla'])
>```
>```py
>SP
>```


#### Como copiar elementos sem fazer fatiamento em um dicionário `copy`

>```py
>estado = dict()
>brasil = list()
>for c in range(0, 3):
>    estado['uf'] = str(input('Unidade Federativa: '))
>    estado['sigla'] = str(input('Sigla do Estado: '))
>    brasil.append(estado.copy())
>print(brasil)
>```
>```py
>Unidade Federativa: Minas
>Sigla do Estado: MG
>Unidade Federativa: Acre
>Sigla do Estado: AC
>Unidade Federativa: Goias
>Sigla do Estado: GO
>[{'uf': 'Minas', 'sigla': 'MG'}, {'uf': 'Acre', 'sigla': 'AC'}, {'uf': 'Goias', 'sigla': 'GO'}]
>```
