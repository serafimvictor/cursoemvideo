def metade(num):
    met = num * 0.5
    return f'R${met:.2f}'


def dobro(num):
    dob = num * 2
    return f'R${dob:.2f}'


def aumentar(num=0, qtde=0):
    num2 = num * (qtde / 100)
    aum = num + num2
    return f'R${aum:.2f}'


def diminuir(num=0, qtde=0):
    num2 = num * (qtde / 100)
    dim = num - num2
    return f'R${dim:.2f}'


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


