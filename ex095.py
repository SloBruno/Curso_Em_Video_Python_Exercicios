jogadores = list()
total = 0

while True:
    print('-' * 25)
    jogador = dict()
    gols = list()
    jogador['nome'] = str(input('Nome do Jogador:'))
    partidas = int(input(f'Quantas Partidas {jogador["nome"]} jogou?'))

    for i in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {i+1}?'))
        gols.append(gol)
        total += gol

    jogador['gols'] = gols
    jogador['total'] = total

    jogadores.append(jogador.copy())
    jogador.clear()
    continuar = str(input('Deseja Continuar? [S/N]:')).upper().strip()

    if continuar == 'N':
        break
    else:
        continue


print('-=-'*30)


print('cod      nome     gols       total')

for c, v in enumerate(jogadores):
    nome = v.get('nome')
    score = v.get('gols')
    total = v.get('total')
    print(f'{c}     {nome}      {score}     {total}')
    total = 0

print('-' * 25)


while True:
    levantamento = int(input('Mostrar dados de qual jogador? [999 para parar]:'))
    if levantamento != 999:
        print(f"-- LEVANTAMENTO do jogador {jogadores[levantamento]['nome']}:")
        for c, i in enumerate(jogadores[levantamento]['gols']):
            print(f'No jogo {c} fez {i} gols.')
    else:
        break

print('<Programa Finalizado>')







