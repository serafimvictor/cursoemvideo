# Crie um programa que leia dois valores e mostre um menu na tela.

opcao = 0
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
while opcao != 5:
    print('''\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  [ 1 ] Somar
  [ 2 ] Multiplicar
  [ 3 ] Maior
  [ 4 ] Novos números
  [ 5 ] Sair do programa \n''')
    opcao = int(input('>>>> Qual é sua opção? '))
    if opcao == 1:
        print('A soma de {} + {} é igual a {}'.format(primeiro, segundo, primeiro + segundo))
    elif opcao == 2:
        print('O produto de {} x {} é igual a {}'.format(primeiro, segundo, primeiro * segundo))
    elif opcao == 3:
        if primeiro > segundo:
            print('O maior número entre {} e {} é o {}'.format(primeiro, segundo, primeiro))
        elif primeiro < segundo:
            print('O maior número entre {} e {} é o {}'.format(primeiro, segundo, segundo))
        elif primeiro == segundo:
            print('Os números são iguais.')
    elif opcao == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Você saiu do programa! Volte sempre :)')
    else:
        print('Opção inválida! Tente de novo...')
