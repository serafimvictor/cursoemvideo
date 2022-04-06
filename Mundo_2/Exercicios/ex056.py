# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idmedia = 0
maior = 0
contm = 0
hvelho = ''

for p in range(1, 5):
    print('{} {}º PESSOA {}'.format('-' * 10, p, '-' * 10))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    idmedia = idmedia + idade
    if p == 1 and sexo == 'M':
        maior = idade
    if sexo == 'M' and idade > maior:
        hvelho = nome
        maior = idade
    if sexo == 'F' and idade < 20:
        contm = contm + 1
media = idmedia / 4
print('A média de idade do pessoal lido é de {:.1f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, hvelho))
print('Ao todo temos {} mulher(es) com menos de 20 anos.'.format(contm))
