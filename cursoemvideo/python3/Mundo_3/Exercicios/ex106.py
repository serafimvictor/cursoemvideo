# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep


c = ('\033[m',   # 0 - Sem cor
     '\033[42m', # 1 - Fundo verde
     '\033[41m', # 2 - Fundo Vermelho
     '\033[46m', # 3 - Fundo Azul
     '\033[40m', # 4 - Fundo branco
    )

def ajuda(com):
    titulo(f'Acessando o manual do comando "{com}"', 3)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(1.5)


def titulo(msg, cor=0):
    print(c[cor], end='')
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Main APP
comando = ''
while True:
    titulo('Sistema de Ajuda - PyHelp', 1)

    comando = str(input('Função ou Biblioteca >>> ')).strip()
    
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('Programa encerrado, Obrigado!', 2)
