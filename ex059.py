# Menu de Opções

exit = False

while not exit:

    print()
    a = int(input('Digite um valor:'))
    b = int(input('Digite outro valor:'))

    print('-='*15)
    print('       Menu de Opções')
    print('-='*15)
    print()
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    print()

    escolha = int(input('Escolha:'))
    print()

    if escolha == 1:
        print('A soma é {}' .format(a+b))
    elif escolha == 2:
        print('O produto é {}'.format(a * b))
    elif escolha == 3:
        if a > b:
            print('O número {} é o maior' .format(a))
        else:
            print('O número {} é o maior'.format(b))
    elif escolha == 4:
        continue
    elif escolha == 5:
        exit = True

