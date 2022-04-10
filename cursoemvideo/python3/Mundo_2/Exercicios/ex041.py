# A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.

from datetime import date

nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    classif = 'MIRIM'
elif idade <= 14:
    classif = 'INFANTIL'
elif idade <= 19:
    classif = 'JÚNIOR'
elif idade <= 25:
    classif = 'SÊNIOR'
elif idade > 25:
    classif = 'MASTER'

print('Classificação: {}'.format(classif))
