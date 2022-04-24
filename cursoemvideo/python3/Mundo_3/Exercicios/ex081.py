# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
cont = 0

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    cont += 1
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao[0] not in 'SN':
        opcao = str(input('Não entendi, quer continuar? [S/N] ')).strip().upper()
    if opcao[0] == 'N':
        break
print(f'Você digitou {cont} números.')
## print(f'Você digitou {len(lista)} números.') // usado na aula

lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista}')

cinco = lista.count(5)
if cinco == 0:
    print('O número 5 não está na lista.')
if cinco >= 1:
    print(f'O valor 5 está na lista e foi digitado {cinco} vezes.')

### Aula
# if 5 in lista:
#     print('O valor 5 ta na lista')
# else:
#     print('Não tem 5 na lista')
