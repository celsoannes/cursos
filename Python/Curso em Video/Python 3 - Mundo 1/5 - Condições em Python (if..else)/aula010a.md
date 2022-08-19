# Aula 10

## Condições (Parte 1)
Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

```
carro.siga()
```

* `carro` - é o objeto
* `siga()` - é o método

### Condições Simples e Compostas

#### Composta

``` py
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('carro novo')
else
    print('carro velho')
print('--FIM--')
```

#### Simplificada

``` py
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo<=3 else' carro velho')
print('--FIM--')
```