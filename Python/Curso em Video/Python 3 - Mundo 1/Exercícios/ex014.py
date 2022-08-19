# Título:       Exercício 14 – Conversor de Temperaturas
# Desafio:      014
# Requisito:    Aula 07
# Enunciado:    Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('====== EXERCÍCIO 014 ======')
celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = (celsius * 9/5) + 32
print('A temperatura de {}°C equivalem a {}°F'.format(celsius, fahrenheit))
