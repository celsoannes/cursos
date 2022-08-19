# Aula 08

Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.


## Utilizando Módulos

### Módulo `math`

* `ceil` - arredonda um número para cima
* `floor` - arredonda um número para baixo
* `trunc` - elimina da virgula para frente sem fazer arredondamento
* `pow` - faz a potencia de um número o mesmo que `**` faz
* `sqrt` - faz a raiz quadrada de um número
* `factorial` - faz a fatorial de um número

### Exemplo:

`import math` - importa todos os módulos
``` py
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
```

`from math import sqrt` - importa apenas a função de raiz quadrada
``` py
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))
```

`from math import sqrt, ceil` -  importa apenas as funções sqrt e ceil