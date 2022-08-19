# Aula 23

## Tratamento de Erros e Exceções

Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura `try` `except` no Python de uma forma simples.


![except](exceções.png)

* `try` -  tentará executar o código
* `except` - irá executar esta sessão do código em caso de erro
* `else` - executará este bloco de programação em caso de sucesso
* `finally` - sempre executará este bloco, importante para fechar um banco de dados, fechar um arquivo aberto

>```py
>try:
>    a = int(input('Numerador: '))
>    b = int(input('Denominador: '))
>    r = a / b
>except Exception as erro:
>    print('Infelizmente tivemos um problema :(')
>    print(f'Problema encontrado foi {erro.__class__}')
>else:
>    print(f'O resultado é {r:.1f}')
>finally:
>    print('Volte sempre! Muito Obrigado!')
>```
>```py
>Numerador: 9
>Denominador: 0
>Infelizmente tivemos um problema :(
>Problema encontrado foi <class 'ZeroDivisionError'>
>Volte sempre! Muito Obrigado!
>```

Um mesmo `try` pode ter vários `except`:

![except](exceções2.png)

```py
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrador foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')
```

### Dividir um número por letras

```py
Numerador: 7
Denominador: alicate
Tivemos um problema com os tipos de dados que você digitou.
Volte sempre! Muito Obrigado!
```

### Erro de divisão por zero:

```py
Numerador: 7
Denominador: 0
Não é possível dividir um número por zero!
Volte sempre! Muito Obrigado!
```

### Não informando valor (vazio)

```py
Numerador: 
Tivemos um problema com os tipos de dados que você digitou.
Volte sempre! Muito Obrigado!
```

### Interrompento a execução do programa (CTRL+C)

```py
Numerador: 200
Denominador: O usuário preferiu não informar os dados!
Volte sempre! Muito Obrigado!
```
