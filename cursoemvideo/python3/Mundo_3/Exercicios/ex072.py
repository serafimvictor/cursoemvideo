# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, 
# de zero até vinte. Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.
# Desafio EXTRA: Fazer o programa perguntar se quer continuar

cont = 0
extenso = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
'dezesste', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0<= num <= 20:
            break
        print(f'Errado! ', end = '')
    print(f'Você digitou o número {extenso[num]}')
    cont += 1
    opcao = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if opcao not in 'SN':
        opcao = str(input('Não entendi. Você quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Paramos por aqui, você verificou {cont} números.')
