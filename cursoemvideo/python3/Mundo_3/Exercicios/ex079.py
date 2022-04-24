# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    num = int(input('Digite um número: '))
    if num in lista:
        print('Já tem esse número, não vou colocar')
    else:
        lista.append(num)
    opcao = str(input('Você quer continuar? [S/N] ')).strip().upper()
    if opcao[0] not in 'SN':
        opcao = str(input('Não entendi... Quer continuar? [S/N] ')).strip().upper()
    if opcao[0] == 'N':
        break
print('-' * 60)
print(sorted(lista))
## Aula
# lista.sort()
# print(lista)
