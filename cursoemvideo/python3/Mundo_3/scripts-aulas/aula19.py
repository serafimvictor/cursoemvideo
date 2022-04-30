pessoas = {'nome': 'Victor', 'sexo': 'M', 'idade': 24}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['nome'] = 'Natã' # alterando um valor
pessoas['peso'] = 55 # Adicionando k/v
for k, v in pessoas.items():
    print(f'{k} = {v}')

#############################################################################
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil) # Mostra a lista com todos os dicts
print(brasil[0]) # Mostra o primeiro dict da lista
print(brasil[0]['uf']) # Mostra o UF do primeiro dict da lista

#############################################################################

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: ')).strip()
    estado['sigla'] = str(input('Sigla do Estado: ')).strip().upper()
    brasil.append(estado.copy()) # A cópia diferente da lista '[:]' é com .copy
for estado in brasil:
    print(e)
    for k, v in estado.items():
        print(f'{k} = {v}.')
    for v in estado.values():
        print(v, end=' ')
    print()