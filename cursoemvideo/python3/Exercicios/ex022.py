# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
# pnome = nome.split()[0]
snome = nome.split()
#pnome = snome[0]
tnome = ''.join(snome)

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(tnome)))
# print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) - Usado na aula
print('Seu primeiro nome é {} e ele tem {} letras'.format(snome[0], len(snome[0])))
# print('Seu primeiro nome é {} e ele tem {} letras'.format(pnome, nome.find(' '))) - Usado na aula
