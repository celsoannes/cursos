# Aula 17

## Listas (Parte 1)

Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

### Criando uma lista

>```py
>num = [2, 5, 9, 1]
>print(num)
>```
>```py
>[2, 5, 9, 1]
>```

### Subistituindo um valor de uma lista

>```py
>num = [2, 5, 9, 1]
>num [2] = 3
>print(num)
>```
>```py
>[2, 5, 3, 1]
>```

### Adicionando novos valores em uma lista com `append`

>```py
>num = [2, 5, 9, 1]
>num.append(7)
>print(num)
>```
>```py
>[2, 5, 9, 1, 7]
>```

### Ordenando os valores de uma lista

>```py
>num = [2, 5, 9, 1]
>num.sort()
>print(num)
>```
>```py
>[1, 2, 5, 9]
>```

### Ordenando de maneira reversa uma lista

>```py
>num = [2, 5, 9, 1]
>num.sort(reverse=True)
>print(num)
>```
>```py
>[9, 5, 2, 1]
>```


### Verificar número de elementos de uma lista

>```py
>num = [2, 5, 9, 1]
>print(f'{len(num)}')
>```
>```py
>4
>```

### Adicionar valores em uma lista com `insert`

Insere na posição `2` o número `0`

>```py
>num = [2, 5, 9, 1]
>num.insert(2, 0)
>print(num)
>```
>```py
>[2, 5, 0, 9, 1]
>```

### Removendo elementos com `pop`

Se não for informado um parametro para `pop` ele eliminará o ultimo da lista

>```py
>num = [2, 5, 9, 1]
>num.pop()
>print(num)
>```
>```py
>[2, 5, 9]
>```

Quando passado um parametro `pop` ele eliminara o valor da posição informada

>```py
>num = [2, 5, 9, 1]
>num.pop(2)
>print(num)
>```
>```py
>[2, 5, 1]
>```

### Removendo elementos com `remove`

>```py
>num = [2, 5, 9, 1]
>num.remove(2)
>print(num)
>```
>```py
>[5, 9, 1]
>```

### Criando uma lista vazia e preenchendo depois

>```py
>valores = []
>valores.append(5)
>valores.append(9)
>valores.append(4)
>print(valores)
>```
>```py
>[5, 9, 4]
>

Outro exemplo:

>```py
>valores = list()
>for cont in range(0, 5):
>    valores.append(int(input('Digite um valor: ')))
>for c, v, in enumerate(valores):
>    print(f'Na posição {c} encontrei o valor {v}!')
>print('Cheguei ao final da lista.')
>```
>```py
>Digite um valor: 4
>Digite um valor: 8
>Digite um valor: 9
>Digite um valor: 1
>Digite um valor: 3
>Na posição 0 encontrei o valor 4!
>Na posição 1 encontrei o valor 8!
>Na posição 2 encontrei o valor 9!
>Na posição 3 encontrei o valor 1!
>Na posição 4 encontrei o valor 3!
>Cheguei ao final da lista.
>```

### Fazendo a ligação de uma lista

>```py
>a = [2, 3, 4, 7]
>b = a
>b[2] = 8
>print(f'Lista A: {a}')
>print(f'Lista B: {b}')
>```
>```py
>Lista A: [2, 3, 8, 7]
>Lista B: [2, 3, 8, 7]
>```

### Fazendo uma cópia de uma lista

>```py
>a = [2, 3, 4, 7]
>b = a[:]
>b[2] = 8
>print(f'Lista A: {a}')
>print(f'Lista B: {b}')
>```
>```py
>Lista A: [2, 3, 4, 7]
>Lista B: [2, 3, 8, 7]
>
