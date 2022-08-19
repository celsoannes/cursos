# Desafio:      073
# Enunciado:    Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#
# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição da tabela esta o time do Internacional


print('====== DESAFIO 073 ======')
brasileirão = ('Santos', 'Atlético-MG', 'Corinthias', 'Cuiabá', 'Internacional', 'Avaí', 'Bragantino', 'Palmeiras', 'Flamengo', 'Coritiba', 'São Paulo', 'Botafogo', 'Fluminence', 'América-MG', 'Ceará SC', 'Athletico-PR', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')

print('TOP 5 do Brasileirão:')
for i in range(0, 5):
    print(f'{i+1}º colocado {brasileirão[i]}')
print('-' * 30)
print('Na lanterna do Brasileirão')
for i in range(16, 20):
    print(f'{i+1}º colocado {brasileirão[i]}')
print('-' * 30)
print('Times participantes do Brasileirão')
print(sorted(brasileirão))
print('=' * 30)
internacional = brasileirão.index('Internacional')
print(f'O Internacional se enconta na {internacional+1}º posição da tabela')
