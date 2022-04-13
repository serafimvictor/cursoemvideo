# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também 
# indique o menor e o maior valor que estão na tupla.
from random import randint
from time import sleep
num = (randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50))

print('Atenção para o sorteio...')
print(f'Nós sorteamos os valores:', end = ' ')
for n in num:
    print(n, end = ' ')
    
print(f'\nO maior valor é {sorted(num)[-1]}')
print(f'O menor valor é {sorted(num)[0]}')

## Usado na aula
print(f'\nO maior valor é {max(num)}')
print(f'O menor valor é {min(num)}')
