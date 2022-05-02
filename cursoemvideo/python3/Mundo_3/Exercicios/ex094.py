# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas 
# B) A média de idade C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

pessoaslist = list()
pessoa = dict()
mulheres = list()
velhos = list()
idade = 0

while True:
    pessoa['Nome'] = str(input('Nome: ')).strip()
    
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while pessoa['Sexo'][0] not in 'MF':
        pessoa['Sexo'] = str(input('Não reconhecido... Sexo [M/F]: ')).strip().upper()
    
    pessoa['Idade'] = int(input('Idade: '))
    idade += pessoa['Idade']
    pessoaslist.append(pessoa.copy())
    
    if pessoa['Sexo'][0] == 'F':
        mulheres.append(pessoa.copy())

    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    while opcao[0] not in 'SN':
        opcao = str(input('Não entendi... Quer continuar? [S/N] ')).strip().upper()
    if opcao[0] == 'N':
        break
media = idade / len(pessoaslist)

print()
print('-=' * 30)
print(f'Foram cadastradas {len(pessoaslist)} pessoas na lista.')
print(f'A média de idade é de {media:.0f} anos.')
print(f'Foram cadastradas {len(mulheres)} mulheres. Sendo elas:')
for p in mulheres:
    print(f" - {p['Nome']}")
for v in pessoaslist:
    if v["Idade"] > media:
        velhos.append(v.copy())
print(f'Foram cadastradas {len(velhos)} pessoas acima da média de idade({media:.0f} anos). Sendo elas:')
for p in velhos:
    print(f" - {p['Nome']} com {p['Idade']} anos.")
