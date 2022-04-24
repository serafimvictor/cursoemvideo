# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e ímpares, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = list()
pares = list()
impares = list()

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
        print('Esse número é par!')
    else:
        impares.append(numero)
        print('Esse número é impar!')
    opcao = str(input('Quer adicionar mais números? [S/N] ')).strip().upper()
    if opcao[0] not in 'SN':
        opcao = str(input('Não entendi, quer adicionar mais números? [S/N] ')).strip().upper()
    if opcao[0] == 'N':
        break
#### Aula
# for i, v in enumerate(lista):
#     if v % 2 == 0:
#         pares.append(v)
#     else:
#         impares.append(v)

print('=' * 55)
print(f'A lista gerada é: {lista}')
print(f'Da lista gerada, esses são pares: {pares}')
print(f'E esses são os números ímpares: {impares}')
