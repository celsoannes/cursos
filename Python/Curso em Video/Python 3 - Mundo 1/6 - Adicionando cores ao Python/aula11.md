# Aula 11

## Cores no Terminal

Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

### ANSI
Escape Sequence

``` py
print('\033[0:33:44[mOlá, Mundo')
```

* `0` - STYLE
* `33` - TEXT
* `44`- BACKGROUND

#### Codigos para estilo

##### STYLE 
* `0` - sem estilo nenhum
* `1` - coloca em negrito (`bold`)
* `4` - coloca em sublinhado (`underline`) 
* `7` - inverte as configurações, o que é fundo vai para letra, o que é letra vai para fundo (`negative`)

##### TEXT

* <font color='white'>30</font> - branco
* <font color='red'>31</font> - vermelho
* <font color='green'>32</font> - verde
* <font color='yellow'>33</font> - amarelo
* <font color='blue'>34</font> - azul
* <font color='magenta'>35</font> - magenta
* <font color='cyan'>36</font> - ciano
* <font color='gray'>37</font> - cinza

##### BACKGROUND
* <font style='background-color:white'>40</font> - branco
* <font style='background-color:red'>41</font> - vermelho
* <font style='background-color:green'>42</font> - verde
* <font style='background-color:yellow'>43</font> - amarelo
* <font style='background-color:blue'>44</font> - azul
* <font style='background-color:magenta'>45</font> - magenta
* <font style='background-color:cyan'>46</font> - ciano
* <font style='background-color:grey'>47</font> - cinza


* <font style='background-color:red' color='white'><b>Teste<b/></font> `\033[0:30:41mTeste[m`

* <font style='background-color:blue' color='yellow'><b>Teste</b></font> `\033[0:33:44mTeste[m`
* <font style='background-color:yellow' color='magenta'><b>Teste</b></font> `\033[0:35:43mTeste[m`
* <font style='background-color:green' color='white'><b>Teste</b></font> `\033[30:42mTeste[m`
* <font style='background-color:black' color='white'><b>Teste</b></font> `\033mTeste[m`
* <font style='background-color:white' color='black'><b>Teste</b></font> `\033[7:30mTeste[m`