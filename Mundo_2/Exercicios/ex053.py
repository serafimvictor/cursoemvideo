# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

from socket import J1939_MAX_UNICAST_ADDR


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
frasejunta = ''.join(palavras)
inverso = ''
## Ao invés de for, pode ser usado desta forma:
# inverso = frasejunta[::-1]
for letras in range(len(frasejunta) - 1, -1, -1):
    inverso = inverso + frasejunta[letras]
print('O inverso de {} é {}.'.format(frasejunta, inverso))
if inverso == frasejunta:
    print('Temos um palíndromo!')
else:
    print('Não é palíndromo!')
