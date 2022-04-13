# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('victor', 'paralelepipedo', 'dicionario', 'contundido',
'confuso', 'raul', 'myllena', 'vasco', 'ganhador', 'vencedor')

for p in palavras:
    print(f'\nEm {p.upper()} temos as vogais: ', end = '')
    for l in p:
        if l in 'aeiou':
            print(l, end =' ')
