#Adivinhe um número

from random import randint
from time import sleep

print('-=-'*20)
num = int(input('Vamos Jogar! Escolha um número entre 0 e 5:'))
print('-=-'*20)

sort = randint(0, 5)

print('Processando...')
sleep(2)

if sort == num:
    print('Eu escolhi {} e você também! Parabéns, você ganhou.' .format(sort))
else:
    print('Eu escolhi {} e você escolheu {}. Você perdeu.' .format(sort, num))

print('Obrigado por jogar comigo!')
