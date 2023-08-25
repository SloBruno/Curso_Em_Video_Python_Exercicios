# Função Fatorial

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: Número a ser calculado
    :param show: (opcional) Mostar ou não a conta
    :return: O valor do fatorial de um número n
    """

    numeros = list()

    conta = 1
    for i in range(n, 0, -1):
        numeros.append(i)
        conta *= i

    if show:
        for num in numeros:
            print(num, end=' ')
            if num > 1:
                print(' x ', end='')
            else:
                print('=', end=' ')

        return conta


print(fatorial(5, True))
# help(fatorial)
