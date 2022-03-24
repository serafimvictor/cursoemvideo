# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, date.today().year))

if idade < 18:
    falta = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(falta))
    print('Seu alistamento será em {}.'.format(anoatual + falta))
elif idade > 18:
    idadealistar = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(idadealistar))
    print('Seu alistamento foi em {}.'.format(anoatual - idadealistar))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
