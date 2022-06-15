# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas, – A maior nota, – A menor nota, – A média da turma, – A situação (opcional)

def notas(*nota, sit=False):
    """
    ---> Função criada para receber N quantidade de notas e retornar:
    – Quantidade de notas, – A maior nota, – A menor nota, – A média da turma, – A situação (opcional)
    :param *nota: Recebe quantas notas forem necessárias e inputa numa tupla
    :param sit: Se Falso, mostra somente a quantidade, maior e menor nota e a média, quando True, exibe a situação da turma
    :return: Retorna um dicionário com: – Quantidade de notas, – A maior nota, – A menor nota, – A média da turma, – A situação (opcional)
    """
    turma = dict()
    media = 0
    
    turma['total_notas'] = len(nota)

    turma['maior'] = max(nota)
    
    turma['menor'] = min(nota)

    for k in nota:
        media += k
    media = media / turma['total_notas']
    turma['media'] = media
    # turma['media'] = sum(nota) / len(nota) # Usado em aula

    if sit:
        if turma['media'] <= 4:
            situacao = 'RUIM'
        elif 4 < turma['media'] < 6.9:
            situacao = 'RAZOÁVEL'
        elif turma['media'] >= 7:
            situacao = 'BOA'
        turma['situação'] = situacao
    return turma

n = notas(6, 5.5, 10, 5)
#help(notas)
print(n)
