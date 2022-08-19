# Desafio:      040
# Enunciado:    Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#
# - Média abaixo de 5.0:
#   REPROVADO
# - Média entre 5.0 e 6.9
#   RECUPERAÇÃO
# - Média 7.0 ou superior:
#   APROVADO


print('====== DESAFIO 040 ======')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
if média < 5.0:
    print('Sua média foi {}, você foi \033[1:31mREPROVADO!\033[m'.format(média))
elif média >= 5.0 and média <= 6.9:
    print('Sua média foi {}, você esta em \033[1:33mRECUPERAÇAO!\033[m'.format(média))
else:
    print('Sua média foi {}. Parabéns! Você \033[1:32mPASSOU!\033[m'.format(média))
