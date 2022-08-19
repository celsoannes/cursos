# Desafio:      105
# Enunciado:    Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


print('====== DESAFIO 105 ======')


def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    boletin = dict()
    boletin['total'] = len(n)
    boletin['maior'] = max(n)
    boletin['menor'] = min(n)
    boletin['média'] = sum(n) / boletin['total']
    if sit:
        if boletin['média'] < 6:
            boletin['situação'] = 'RUIM'
        else:
            boletin['situação'] = 'BOA'
    print(boletin)


resp = notas(5.5, 9.5, sit=False)
#help(notas)