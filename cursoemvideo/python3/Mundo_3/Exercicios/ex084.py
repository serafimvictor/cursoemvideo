# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre: 
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
infos = list()
pesados = list()
leves = list()
cont = maior = menor = 0

while True:
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    peso = float(input('Digite seu peso em Kg: '))
    if cont == 0:
        maior = peso
        menor = peso
    if peso >= maior:
        maior = peso
    if peso < menor:
        menor = peso
    infos.append(nome)
    infos.append(peso)
    pessoas.append(infos[:])
    cont += 1
    infos.clear()
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao[0] not in 'SN':
        opcao = str(input('Não entendi... Deseja continuar? [S/N] ')).strip().upper()
    if opcao[0] == 'N':
        print('Ok, finalizando.')
        break
for p in pessoas:
    if p[1] == maior:
        pesados.append(p[0])
    if p[1] == menor:
        leves.append(p[0])

print('=' * 50)
print(f'Você cadastrou {cont} pessoas na lista.') # Poderia usar len(pessoas)
print(f'O maior peso foi {maior}Kg. Peso de {pesados}')
print(f'O menor peso foi {menor}Kg. Peso de {leves}')
