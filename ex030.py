num = int(input('Digíte um número pra saber se ele é par ou ímpar:'))
teste = num % 2

if teste == 0:
    print('O número {} é par!' .format(num))
else:
    print('O número {} é ímpar!' .format(num))
