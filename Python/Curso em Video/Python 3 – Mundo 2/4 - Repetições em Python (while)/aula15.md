# Aula 15

##Interrompendo repetições while

Nessa aula, vamos aprender como utilizar a instrução `break` e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o `break` no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.

Além disso, vamos aprender como trabalhar com as novas `fstrings` do Python.

### Prática

#### Looping infinito
 ```py
cont = 1
 while True:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')
 ```

#### Usando break

```py
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
```

```py
Digite um número: 1
Digite um número: 2
Digite um número: 3
Digite um número: 4
Digite um número: 999
A soma vale 10

Process finished with exit code 0
```

### Usando f-strings

```py
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
```

```py
Digite um número: 1
Digite um número: 2
Digite um número: 3
Digite um número: 4
Digite um número: 5
Digite um número: 999
A soma vale 15
```

#### Exemplos de fstring (interpolação)

>```py
>nome = 'José'
>idade = 33
>print(f'O {nome} tem {idade} anos.') #PYTHON 3.6+
>print('O {} tem {} anos.'.format(nome, idade)) # PYTHON 3
>print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2
>```
>```py
>O José tem 33 anos.
>O José tem 33 anos.
>O José tem 33 anos.
>```

>```py
>nome = 'José'
>idade = 33
>salário = 987.3
>print(f'O {nome} tem {idade} anos  e ganha R${salário:.2f}')
>```
>```py
>O José tem 33 anos  e ganha R$987.30
>```