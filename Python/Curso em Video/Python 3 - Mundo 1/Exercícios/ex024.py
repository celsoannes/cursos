# Título:       Exercício 24 – Verificando as primeiras letras de um texto
# Desafio:      024
# Requisito:    Aula 09
# Enunciado:    Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

print('====== EXERCÍCIO 024 ======')
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
