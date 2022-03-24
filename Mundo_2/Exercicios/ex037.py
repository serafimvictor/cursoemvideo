# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

# Recebendo valor e definindo escolha
numero = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

escolha = int(input('Sua opção: '))

# Conversão do número e cortando os 2 primeiros caracteres
binario = bin(numero)[2:]
hexa = str(hex(numero)[2:])
octal = oct(numero)[2:]

# Definindo condições
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, binario))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, octal))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hexa))
else:
    print('\033[31mOpção inválida!')
