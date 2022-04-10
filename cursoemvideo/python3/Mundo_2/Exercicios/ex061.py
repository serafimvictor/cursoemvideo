# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('''{}
    10 TERMOS DE UMA PA
{} 
'''.format('=' * 25, '=' * 25))
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
print('{}'.format(primeiro), end = ' -> ')
while cont != 10:
    termo = termo + razao
    print(termo, end = ' -> ')
    cont = cont + 1
print('Acabou!')

## Aula

# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão da PA: '))
# termo = primeiro
# cont = 1
# while cont <= 10:
#     print('{} -> '.format(termo), end = '')
#     termo += razao
#     cont += 1
# print('Fim')
