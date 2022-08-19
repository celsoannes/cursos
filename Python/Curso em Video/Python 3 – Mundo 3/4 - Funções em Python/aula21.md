# Aula 21

## Funções (Parte 2)

Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre `Interactive Help` em Python, o uso de `docstrings` para documentar nossas funções, **Argumentos opcionais** para dar mais dinamismo em funções Python, **Escopo de variáveis** e **Retorno de resultados**.

### `Interactive Help`

No console digite: `help()`, agora é possivel digitar qualquer comando, função ou biblioteca interna que ele irá trazer o manual completo.

```py
  >? input
Help on built-in function input in module builtins:
input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
```

Para sair digite `quit` que você voltará para o console do python.

O mesmo comando também pode ser usado dentro de um programa python:

>```py
>help(input)
>```
>```py
>Help on built-in function input in module builtins:
>
>input(prompt=None, /)
>    Read a string from standard input.  The trailing newline is stripped.
>    
>    The prompt string, if given, is printed to standard output without a
>    trailing newline before reading input.
>    
>    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
>    On *nix systems, readline is used if available.
>```


Também é possivel imprimir o doc interno dentro de um comando:

>```py
>print(input.__doc__)
>```
>```py
>Read a string from standard input.  The trailing newline is stripped.
>
>
>The prompt string, if given, is printed to standard output without a
>trailing newline before reading input.
>
>If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
>On *nix systems, readline is used if available.
>```

### `Docstrings`
Cria um manual para uma função customizada:

>```py
>def contador(i, f, p):
>    """
>    -> Faz uma contagem e mostra na tela.
>    :param i: inicio da contagem
>    :param f: fim da contagem
>    :param p: passo da contagem
>    :return: sem retorno
>    """>
>
>    c = i
>    while c<= f:
>        print(f'{c}', end='..')
>        c += p
>    print('FIM!')
>
>
>help(contador)
>```
>```py
>contador(i, f, p)
>    -> Faz uma contagem e mostra na tela.
>    :param i: inicio da contagem
>    :param f: fim da contagem
>    :param p: passo da contagem
>    :return: sem retorno
>```


### Parâmetros Opcionais

Quando é possivel nomear os parametros ou colocar nenhum deles

>```py
>def somar(a=0, b=0, c=0):
>    """
>    -> Faz a soma de três valores e mostra o resultado na tela
>    :param a: o primeiro valor
>    :param b: o segundo valor
>    :param c: o terceiro valor
>    :return: 
>    """
>    s = a + b + c
>    print(f'A soma vale {s}')
>
>
>somar(3, 2, 5)
>somar(8, 4)
>somar()
>```
>```py
>A soma vale 10
>A soma vale 12
>A soma vale 0
>```


### Escopo de variáveis

É o local onde uma variável vai existir e onde a variável não vai mais existir.

>```py
>def funcao():
>    n1 = 4
>    print(f'N1 dentro vale {n1}')
>
>
>n1 = 2
>funcao()
>print(f'N1 fora vale {n1}')
>```
>```py
>N1 dentro vale 4
>N1 fora vale 2
>```

Definindo uma variável como global dentro de uma função:

>```py
>def funcao():
>    global n1
>    n1 = 4
>    print(f'N1 dentro vale {n1}')
>
>
>n1 = 2
>funcao()
>print(f'N1 fora vale {n1}')
>```
>```py
>N1 dentro vale 4
>N1 fora vale 4
>```


### Retornando de Valores

Útil quando é necessário pegar o retorno para um uso customizado

>```py
>def somar(a=0, b=0, c=0)
>    s = a + b + c
>    return s
>
>
>r1 = somar(3, 2, 5)
>r2 = somar(2, 2)
>r3  = somar(6)
>print(f'Os resultados foram {r1}, {r2}, {r3}')
>```
>```py
>Os resultados foram 10, 4, 6
>```