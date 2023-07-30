# N° Aleatórios em Tupla

from random import randint
aleatorio = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))

ordem = sorted(aleatorio)
menor = ordem[0]
maior = ordem[4]


print(f'A sequência sorteada foi: {aleatorio}\n'
      f'O menor valor sorteado foi {menor}\n'
      f'O maior valor sorteado foi {maior}\n')
