# Desafio:      042
# Enunciado:    Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes


print('====== DESAFIO 042 ======')
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print('Os segmentos acima formam um Triângulo Equilátero!')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2:
        print('Os segmentos acima formam um Triângulo Isóceles!')
    else:
        print('Os segmentos acima formam um Triângulo Escaleno!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')