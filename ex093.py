jogador = dict()
gols = list()
total = 0

jogador['nome'] = str(input('Nome do Jogador:'))
partidas = int(input('Quantas partidas ele jogou?'))

for i in range (0, partidas):
    gol = int(input('Quantos gols na partida {}?' .format(i)))
    gols.append(gol)
    total += gol

jogador['gols'] = gols
jogador['total'] = total

print('-=-'*25)

print(jogador)

print('-=-'*25)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=-'*25)

nome = jogador['nome']
print(f'O jogador {nome} jogou {partidas} partidas.')

for i in range(0, partidas):
        print(f'     =>Na partida {i}, fez {gols[i]} gols.')
print(f'Foi um total de {total} gols.')
