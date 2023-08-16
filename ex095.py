jogadores = list()

while True:
    total = 0
    print('-' * 25)
    jogador = dict()
    gols = list()
    jogador['nome'] = input('Nome do Jogador:')
    partidas = int(input(f'Quantas Partidas {jogador["nome"]} jogou?'))

    for i in range(partidas):
        gol = int(input(f'Quantos gols na partida {i+1}?'))
        gols.append(gol)
        total += gol

    jogador['gols'] = gols
    jogador['total'] = total

    jogadores.append(jogador.copy())
    jogador.clear()
    continuar = input('Deseja Continuar? [S/N]:').upper().strip()

    if continuar == 'N':
        break


print('-=-'*30)

print('cod      nome     gols       total')

for c, v in enumerate(jogadores):
    nome = v['nome']
    score = v['gols']
    total = v['total']
    print(f'{c}     {nome}      {score}     {total}')

print('-' * 25)

while True:
    levantamento = int(input('Mostrar dados de qual jogador? [999 para parar]:'))
    if levantamento != 999 and levantamento in range(len(jogadores)):
        print(f"-- LEVANTAMENTO do jogador {jogadores[levantamento]['nome']}:")
        for c, i in enumerate(jogadores[levantamento]['gols']):
            print(f'No jogo {c+1} fez {i} gols.')
    elif levantamento == 999:
        break
    else:
        print('Jogador não existente')

print('<Programa Finalizado>')
