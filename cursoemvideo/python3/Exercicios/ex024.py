# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

### Resolução aula
# cid = str(input('Em que cidade você nasceu? ')).strip()
# print(cid[:5].upper() == 'SANTO')


cidade = str(input('Em que cidade você nasceu? ')).strip()
cidade = cidade.split()
print('SANTO' in cidade[0].upper())
