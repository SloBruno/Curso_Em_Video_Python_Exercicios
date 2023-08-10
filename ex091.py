from random import randint
from time import sleep

jogadores = dict()
ranking = list()

jogadores['jodador_um'] = randint(1, 6)
jogadores['jodador_dois'] = randint(1, 6)
jogadores['jodador_tres'] = randint(1, 6)
jogadores['jodador_quatro'] = randint(1, 6)

print('-=-=-=-=-=Ranking-=-=-=-=-=')

for k, v in jogadores.items():
    sleep(0.7)
    print(f'O {k} tirou {v}')


