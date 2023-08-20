# Contador Personalizado
from time import sleep


def contador(inicio, fim, passo):
    print(f'-=-=-Contador de 1 a 10-=-=-')
    for i in range(1, 11):
        sleep(0.4)
        print(i, end=' ')
    print()
    print(f'-=-=-Contador de 10 até 0, de 2 em 2-=-=-')
    for j in range(10, -1, -2):
        sleep(0.4)
        print(j, end=' ')
    print()
    print('-=-=-Contador Personalizado-=-=-=-')
    inicio = int(input('Início:'))
    fim = int(input('Fim:'))
    passo = int(input('Passo:'))
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print(f'-=-=-Contador de {inicio} até {fim}, de {passo} em {passo}-=-=-')
    if passo < 0:
        for k in range(inicio, fim-1, passo):
            sleep(0.4)
            print(k, end=' ')
    elif inicio > fim:
        for c in range(inicio, fim-1, -passo):
            sleep(0.4)
            print(c, end=' ')
    else:
        for q in range(inicio, fim + passo, passo):
            sleep(0.4)
            print(q, end=' ')






contador(0, 0, 0)

