# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

num = float(input('Digite um valor: R$'))
print(f'A metade de {num} é igual a {moeda.metade(num):.2f}')
print(f'O dobro de {num} é igual a {moeda.dobro(num):.2f}')
while True:
    opcao = str(input('Deseja alterar o número: [S/N] ')).strip().upper()
    if opcao[0] == 'N':
        break
    elif opcao[0] not in 'SN':
        print('Não entendi...')
    elif opcao[0] == 'S':
        alternativa = str(input('Deseja aumentar ou diminuir? ')).strip().upper()
        if alternativa[0] == 'A':
            qtde = int(input('Deseja aumentar quantos %? '))
            num = moeda.aumentar(num, qtde)
            print(f'Aumentando {qtde} teremos {num}')
        elif alternativa[0] == 'D':
            qtde = int(input('Deseja diminuir quantos %? '))
            num = moeda.diminuir(num, qtde)
            print(f'Diminuindo {qtde} teremos {num}')
        else:
            print('Não entendi...')
print(f'Programa finalizado, obrigado!')
