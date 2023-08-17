from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
ranking = dict()

jogadores['jodador_um'] = randint(1, 6)
jogadores['jodador_dois'] = randint(1, 6)
jogadores['jodador_tres'] = randint(1, 6)
jogadores['jodador_quatro'] = randint(1, 6)

print('Valores Sorteados')

for k, v in jogadores.items():
    sleep(0.7)
    print(f'O {k} tirou {v}')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)


print('-=-=-=-=-=Ranking-=-=-=-=-=')

for i, v in enumerate(ranking):
    print(f'    {i+1}° Lugar: {v[0]} com o número {v[1]}')
    sleep(1)





