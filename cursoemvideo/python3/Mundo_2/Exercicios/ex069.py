# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre: A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

contidade = 0 # Contador de idade
chomens = 0 # Contador de Homens
cmulher = 0 # Contador de Mulheres com menos de 20

while True:
    print('-' * 60)
    print('{:^60}'.format('CADASTRE UMA PESSOA'))
    print('-' * 60)
    idade = int(input('Idade: '))

    if idade >= 18: # Contador de +18
        contidade = contidade + 1
    
    sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Opção inválida. Sexo: [F/M] ')).strip().upper()[0]
    
    if sexo == 'M': # Contador de homens
        chomens += 1
    
    if sexo == 'F' and idade < 20: # Contador de mulheres -20
        cmulher += 1
    
    opcao = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Não entendi. Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'''{'-' * 60}
Das pessoas que você cadastrou, tem:
{contidade} pessoas com mais de 18 anos.
{chomens} homens cadastrados.
{cmulher} mulheres cadastradas com menos de 20 anos.
''')
