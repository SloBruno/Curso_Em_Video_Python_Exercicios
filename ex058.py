# Adivinhe um número 2.0

from random import randint

ganhou = False
pal = 1

while not ganhou:
    sort = randint(0, 10)
    print('-=-' * 20)
    num = int(input('Vamos Jogar! Escolha um número entre 0 e 10:'))
    print('-=-' * 20)
    if num != sort:
        ganhou = False
        pal += 1
        print('Eu escolhi {} e você {}. Você perdeu. Tente novamente.'.format(sort, num))
    if num == sort:
        ganhou = True
print('Eu escolhi {} e você também! Parabéns, você ganhou com {} palpites.'.format(sort,  pal))
