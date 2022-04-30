# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.
# 0 ~ 4.9 Reprovado, 5 ~ 6.9 recuperação, 7+ aprovado

aluno = dict()

aluno['Nome'] = str(input('Nome: ')).strip()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
elif aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é {v}')
