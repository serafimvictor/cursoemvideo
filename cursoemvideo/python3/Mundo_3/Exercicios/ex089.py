# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

aluno = list()

while True:
    nome = str(input('Nome do aluno: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    aluno.append([nome, [n1, n2], media])
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    while opcao[0] not in 'SN':
        opcao = str(input('Não entendi... Quer continuar? [S/N] ')).strip().upper()
    if opcao[0] == 'N':
            break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for n, a in enumerate(aluno):
    print(f'{n:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    notas = int(input('Deseja ver a nota de qual aluno? [999 encerra] '))
    if notas == 999:
        break
    print(f'As notas de {aluno[notas][0]} foram: ',end='')
    print(aluno[notas][1])
print('Volte sempre')