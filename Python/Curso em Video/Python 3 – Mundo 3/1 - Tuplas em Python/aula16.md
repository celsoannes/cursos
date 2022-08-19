# Aula 16

## Tuplas
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

### Variáveis Compostas (Tuplas)

* `()` Tuplas - são imutáveis
* `[]` Listas
* `{}` Dicionários

#### Prática

>```py
>lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
>print(lanche)
>```
>```py
>('Hambúrger', 'Suco', 'Pizza', 'Pudim')
>```

##### Fatiamentos

>```py
>lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
>print(lanche[2])
>```
>```py
>Pizza
>```

>```py
>lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
>print(lanche[-3])
>```
>```py
>Suco
>```

>```py
>lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
>print(lanche[1:3])
>```
>```py
>('Suco', 'Pizza')
>```

>```py
>lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
>print(lanche[2:])
>```
>```py
>('Pizza', 'Pudim')
>```

>```py
>lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
>print(lanche[:2])
>```
>```py
>('Hambúrger', 'Suco')
>```

>```py
>lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
>print(lanche[-2:])
>```
>```py
>('Pizza', 'Pudim')
>```

##### Usando ``for``

>```py
>lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
>for comida in lanche:
>    print(f'Eu vou comer {comida}')
>print('Comi pra caramba!')
>```
>```py
>Eu vou comer Hambúrger
>Eu vou comer Suco
>Eu vou comer Pizza
>Eu vou comer Pudim
>Comi pra caramba!
>```

>```py
>lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
>for cont in range(0, len(lanche)):
>    print(f'Eu vou comer {lanche[cont]}')
>print('Comi pra caramba!')
>```
>```py
>Eu vou comer Hambúrger
>Eu vou comer Suco
>Eu vou comer Pizza
>Eu vou comer Pudim
>Eu vou comer Batata Frita
>Comi pra caramba!
>```

>```py
>lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
>for pos, comida in enumerate(lanche):
>    print(f'Eu vou comer {comida} na posição {pos}')
>print('Comi pra caramba!')
>```
>```py
>Eu vou comer Hambúrger na posição 0
>Eu vou comer Suco na posição 1
>Eu vou comer Pizza na posição 2
>Eu vou comer Pudim na posição 3
>Eu vou comer Batata Frita na posição 4
>Comi pra caramba!
>```

Colocar em ordem
>```py
>lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
>print(sorted(lanche))
>```
>```py
>['Batata Frita', 'Hambúrger', 'Pizza', 'Pudim', 'Suco']
>```

Juntar Tuplas
>```py
>a = (2, 5, 4)
>b = (5, 8, 1, 2)
>c = a + b
>print(c)
>```
>```py
>(2, 5, 4, 5, 8, 1, 2)
>```

`count` contar quantas vezes o valor informado aparece na Tupla
>```py
>a = (2, 5, 4)
>b = (5, 8, 1, 2)
>c = a + b
>print(c.count(5))
>```
>```py
>2
>```

`index` retorna a posição em que se enontra o valor informado
>```py
>a = (2, 5, 4)
>b = (5, 8, 1, 2)
>c = a + b
>print(c.index(8))
>```
>```py
>4
>```

`del` apaga uma Tupla

>```py
>pessoa = ('Gustavo', 39, 'M', 99.88)
>del(pessoa)
>```