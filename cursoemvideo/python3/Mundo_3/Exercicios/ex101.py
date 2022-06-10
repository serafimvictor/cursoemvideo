# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ap):
    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if 16 > idade:
        return f'Voce tem {idade} anos de idade: Voto NEGADO!'
    elif 16 <= idade < 18 or idade >= 63:
        return f'Voce tem {idade} anos de idade: Voto OPCIONAL!'
    else:
        return f'Voce tem {idade} anos de idade: Voto OBRIGATORIO!'


print('--' * 20)
nascimento = int(input('Ano de nascimento: '))
print(voto(nascimento))
