# Contador Personalizado
from time import sleep
lista = []
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
    print(f'-=-=-Contador de {inicio} até {fim}, de {passo} em {+passo}-=-=-')
    if passo < 0:
        for k in range(inicio, fim-1, passo):
            print(k, end=' ')
    elif inicio > fim:
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ')


contador(90, 80, -1)

