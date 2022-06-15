# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(fr):
    while True:
        num = str(input(fr))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[31mErro!\033[m Por favor, digite um número inteiro')
    return num

n = leiaInt('Digite um número: ')
print(f'Obrigado, você digitou o número inteiro: {n}.')
