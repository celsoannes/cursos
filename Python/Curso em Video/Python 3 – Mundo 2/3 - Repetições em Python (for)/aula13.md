# Aula 13

## Laços de Repetição

###  Estrutura de repetição `for`

Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:

### Teoria

``` py
for c in range(0, 4):

print(c)

print(‘Acabou’)
```

### Prática

* Contagem progresiva: `aula13a.py`
``` py
for i in range(0, 6):
    print(i)
print('FIM')
```

```py
0
1
2
3
4
5
FIM
```

* Contagem Regressiva: `aula13b.py`

``` py
for i in range(0, 6):
    print(i)
print('FIM')
```

```py
0
1
2
3
4
5
FIM
```

* Contar para trás: `aula13c.py`

``` py
for i in range(6, 0, -1):
    print(i)
print('FIM')
```

```py
6
5
4
3
2
1
FIM
```

* Contagem com salto `aula13d.py`

``` py
for i in range(0, 7, 2):
    print(i)
print('FIM')
```

```py
0
2
4
6
FIM
```

* Lendo valores para criar um laço: `aula13e.py`

```py
i = int(input('Início: '))
f = int(input('Fin: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
```
```py
Início: 0
Fin: 100
Passo: 10
0
10
20
30
40
50
60
70
80
90
100
FIM
```

`aula13f.py`
```py
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
```

```py
Digite um valor: 1
Digite um valor: 2
Digite um valor: 3
Digite um valor: 4
O somatório de todos os valores foi 10
```