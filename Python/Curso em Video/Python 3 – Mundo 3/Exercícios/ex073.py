# Título:       Exercício 73 – Tuplas com Times de Futebol
# Desafio:      073
# Requisito:    Aula 16
# Enunciado:    Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Internacional.

print('====== EXERCÍCIO 073 ======')
times = ('Santos', 'Atlético-MG', 'Corinthias', 'Cuiabá', 'Internacional', 'Avaí', 'Bragantino', 'Palmeiras', 'Flamengo', 'Coritiba', 'São Paulo', 'Botafogo', 'Fluminence', 'América-MG', 'Ceará SC', 'Athletico-PR', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Internacional esta na {times.index("Internacional")+1}ª posição')