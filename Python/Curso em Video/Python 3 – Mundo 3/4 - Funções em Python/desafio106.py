# Desafio:      106
# Enunciado:    Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.


print('====== DESAFIO 105 ======')


def pyHelp(comando):
    msg = f"Acessando o manual do comando '{comando}'"
    t = len(msg) + 2
    print('\033[0:35:43m~' * t)
    print(f'{msg:^{t}}')
    print('~' * t)
    print('\033[7:30m')
    help(f'{msg}')
    #print(msg)


while True:
    cmd = str(input('Função ou Biblioteca > '))
    if cmd.lower() == 'fim':
        break
    pyHelp(cmd)
