# Ficha do Jogador

def ficha(jogador='<desconhecido>', gols=0):
    jogador = str(input('Nome do jogador:'))
    gols = int(input('Quantidade de gols:'))

    if jogador.strip() == '':
        jogador = '<desconhecido>'
        print(f'O jogador {jogador} fez {gols} gols no campenato.')


    else:
        jogador = str(input('Nome do jogador:'))
        gols = int(input('Quantidade de gols:'))
        print(f'O jogador {jogador} fez {gols} gols no campenato.')

ficha(jogador, gols)


