# Crie um programa que tenha uma tupla única com 
# nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

pep = ('Notebook', 998.46, 'Pneu', 202.3, 'Impressora', 184.7, 'Relógio', 52, 'Mouse', 192.35, 
'Mousepad', 62.1, 'Monitor', 863.9, 'Speaker', 121.3, 'Pulseira', 329, 'Headset', 199.68)

print('=' * 45)
print(f'{" TABELA DE PREÇOS ":^40}')
print('=' * 45)

for itens in range( 0, len(pep)):
    if itens % 2 == 0:
        print(f'{pep[itens]:.<35}', end = '')
    elif itens % 2 != 0:
        print(f'R${pep[itens]:>7.2f}')
print('=' * 45)
