# Aula 20

## Funções (Parte 1)
Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando `def` em Python e como utilizá-lo com parâmetros simples e múltiplos.


### Teoria
>```py
>def título(txt):
>    print('-' * 30)
>    print(txt)
>    print('-' * 30)
>título('      CURSO EM VÍDEO      ')
>```
>```py
>------------------------------
>      CURSO EM VÍDEO    
>------------------------------

### Prática

>```py
>def soma(a, b):
>    s = a + b
>    print(s)
>
>
>soma(4, 5)
>```
>```py
>9
>```

OBS.: Deixar sempre dois espaços vazios ao final de uma função.

Outra maneira de fazer a mesma conta:

>```py
>def soma(a, b):
>    s = a + b
>    print(s)
>
>
>soma(b=4, a=5)
>```
>```py
>9
>```

##### Empacotamento/Desempacotamento usando tuplas

>```py
>def contador(* núm):
>    tam = len(núm)
>    print(f'Recebi os valores {núm} e são ao todo {tam} números')
>    
>
>contador(2, 1, 7)
>contador(8, 0)
>contador(4, 4, 7, 6, 2)
>```
>```py
>Recebi os valores (2, 1, 7) e são ao todo 3 números
>Recebi os valores (8, 0) e são ao todo 2 números
>Recebi os valores (4, 4, 7, 6, 2) e são ao todo 5 números
>```

##### Passando uma lista

>```py
>def dobra(lst):
>    pos = 0
>    while pos < len(lst):
>        lst[pos] *= 2
>        pos += 1
>
>
>valores = [6, 3, 9, 1, 0, 2]
>dobra(valores)
>print(valores)
>```
>```py
>[12, 6, 18, 2, 0, 4]
>```


