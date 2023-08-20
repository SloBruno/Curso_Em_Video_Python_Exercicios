# Sortear e Somar

from random import randint

numeros = list()


def sorteia():
    for i in range(0, 5):
        num = randint(1, 10)
        numeros.append(num)
    print(f'Os números sorteados foram {numeros}.')


def somar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos números pares sorteados é {soma}.')



sorteia()
somar()