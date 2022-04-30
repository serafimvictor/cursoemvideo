# Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
# e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

pessoa = dict()
anoatual = date.today().year

pessoa['nome'] = str(input('Nome: ')).strip()
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = anoatual - nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    aposentadoria = (35 - (anoatual - pessoa['contratacao'])) + pessoa['idade']
    #Aula usou 
    #aposentadoria = pessoa['idade'] + ((pessoa['contratacao'] + 35) - anoatual)
    pessoa['aposentadoria'] = aposentadoria

print('-=' * 30)
for key, value in pessoa.items():
    print(f' - {key}: {value}')