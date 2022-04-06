# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
maior = 0
menor = 0
for n in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(n)))
    idade = date.today().year - ano
    if idade >= 21:
        maior = maior + 1
    elif idade < 21:
        menor = menor + 1
print('Neste grupo temos {} pessoa(s) na maioridade e {} menores de idade.'.format(maior, menor))
