# Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável

def escreva(frase):
    tam = len(frase) + 4
    print('~' * tam)
    print(f'{frase:^{tam}}')
    print('~' * tam)


txt = str(input('Digite uma frase: ')).strip()
escreva(txt)
