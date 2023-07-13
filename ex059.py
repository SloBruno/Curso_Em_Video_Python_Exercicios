# Menu de Opções

a = float(input('Digite um valor:'))
b = float(input('Digite outro valor:'))

exit = False

while not exit:

    print()

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

    escolha = int(input('>>>>>>Escolha:'))
    print()

    if escolha == 1:
        print('{} + {} = {}' .format(a, b, a+b))
    elif escolha == 2:
        print('{} * {} = {}' .format(a, b, a*b))
    elif escolha == 3:
        if a > b:
            print('O número {} é o maior' .format(a))
        else:
            print('O número {} é o maior'.format(b))
    elif escolha == 4:
        a = int(input('Digite um valor:'))
        b = int(input('Digite outro valor:'))
    elif escolha == 5:
        exit = True
print('Fim do Programa')
