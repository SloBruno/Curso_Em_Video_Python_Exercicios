# Ficha do Jogador

def ficha(jogador='<desconhecido>', gols=0):
    jogador = str(input('Nome do jogador:'))
    gols = str(input('Quantidade de gols:'))

    if gols == '':
        gols = 0

    else:
        int(gols)

    if jogador.strip() == '':
        jogador = '<desconhecido>'
        print(f'O jogador {jogador} fez {gols} gols no campenato.')


    else:
        print(f'O jogador {jogador} fez {gols} gols no campenato.')



ficha()


