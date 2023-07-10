# Adivinhe um número 2.0

from random import randint

ganhou = False
pal = 1
sort = randint(0, 10)

print('-=-' * 20)
print('Vamos Jogar! Escolha um número entre 0 e 10:')
palpite = int(input("Qual é o seu palpite:"))
print('-=-' * 20)

while not ganhou:
    if palpite < sort:
        ganhou = False
        pal += 1
        print('Mais... Tente novamente.')
        palpite = int(input("Qual é o seu palpite:"))
    elif palpite > sort:
        ganhou = False
        pal += 1
        print('Menos... Tente novamente.')
        palpite = int(input("Qual é o seu palpite:"))
    if palpite == sort:
        ganhou = True
print('Eu escolhi {} e você também! Parabéns, você ganhou com {} palpites.'.format(sort,  pal))
