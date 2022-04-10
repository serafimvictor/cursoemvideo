## Uso de break em while

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

## fstrings para print pode substituir .format()

nome = str(input('Seu nome: ')).strip()
idade = int(input('Sua idade: '))
salario = float(input('Ganha quanto? R$'))
print(f'O {nome} tem {idade} anos e recebe R${salario:.2f}.') # usando fstring (Python3.6+)
print('O {} tem {} anos e ganha R${:.2f}.'.format(nome, idade, salario)) # Usando format
print('O %s tem %d anos e ganha R$%g.' % (nome, idade, salario)) # Python 2