jogador = dict()
gols = list()
total = 0

jogador['nome'] = str(input('Nome do Jogador:'))
partidas = int(input(f'Quantas Partidas {jogador["nome"]} jogou?'))

for i in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {i+1}?'))
    gols.append(gol)
    total += gol

jogador['gols'] = gols
jogador['total'] = total

print('-=-'*30)

print(jogador)

print('-=-'*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=-'*30)

nome = jogador['nome']

print(f'O jogador {nome} jogou {partidas} partidas')

for n, m in enumerate(gols):
    print(f'    =>Na partida {n}, fez {m} gols')
print(f'Foi um total de {total} gols')



