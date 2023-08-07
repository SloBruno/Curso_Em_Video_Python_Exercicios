# Sorteador Mega Sena

from random import randint
from time import sleep

print('-=-' * 20)
print('Gerador de Jogo da Mega-Sena'.center(57))
print('-=-'*20)

palpites = []
jogo = []

jogos = int(input('Quantos jogos você deseja gerar?'))

for i in range(0, jogos):
    jogo = []
    while len(jogo) < 6:
        sorte = randint(1, 60)
        if sorte not in jogo:
            jogo.append(sorte)
    ordem = sorted(jogo)
    palpites.append(ordem)

# Print

print()
print(f'----- Sorteando {jogos} jogos... -----')

for c, nums in enumerate(palpites):
        sleep(1)
        print(f'{c+1}° Jogo: {nums}')

sleep(0.5)
print(f'------- <<< Boa Sorte >>> -------')


