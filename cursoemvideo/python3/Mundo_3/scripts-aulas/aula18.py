teste = []
teste.append('Victor')
teste.append(24)
galera = list()
galera.append(teste[:])
teste[0] = 'Natã'
teste[1] = '17'
galera.append(teste[:])
print(galera)

##########################################

galera2 = [['Natã', 17], ['Hyago', 15], ['Luiz', 47], ['Victor', 24]]
print(galera2[0])
print(galera2[3][0])
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos.')

##########################################

gente = list()
dado = list()
maior = menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    gente.append(dado[:])
    dado.clear()
for p in gente:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} pessoas maiores de idade e {menor} pessoas com menos de 21 anos.')