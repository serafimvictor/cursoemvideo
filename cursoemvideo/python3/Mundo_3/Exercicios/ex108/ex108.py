# Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
# que consiga mostrar os números como um valor monetário formatado.import moeda

import moeda

num = float(input('Digite um valor: R$'))
print(f'A metade de {moeda.moeda(num)} é igual a {moeda.metade(num)}')
print(f'O dobro de {moeda.moeda(num)} é igual a {moeda.dobro(num)}')
while True:
    opcao = str(input('Deseja alterar o valor? [S/N] ')).strip().upper()
    if opcao[0] == 'N':
        break
    elif opcao[0] not in 'SN':
        print('Não entendi...')
    elif opcao[0] == 'S':
        alternativa = str(input('Deseja aumentar ou diminuir? ')).strip().upper()
        if alternativa[0] == 'A':
            qtde = int(input('Deseja aumentar quantos %? '))
            num = moeda.aumentar(num, qtde)
            print(f'Aumentando {qtde}% teremos {num}')
        elif alternativa[0] == 'D':
            qtde = int(input('Deseja diminuir quantos %? '))
            num = moeda.diminuir(num, qtde)
            print(f'Diminuindo {qtde}% teremos {num}')
        else:
            print('Não entendi...')
print(f'Programa finalizado, obrigado!')
