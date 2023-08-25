# Ficha do Jogador

def ficha(jogador='<desconhecido>', gols=0):
    nome = str(input('Nome do jogador:'))
    g = str(input('Quantidade de gols:'))

    if g.isnumeric():
        gols = int(g)

    else:
        g = 0
        gols = g

    if nome.strip() == '':
        print(f'O jogador {jogador} fez {gols} gol(s) no campenato.')


    else:
        jogador = nome
        print(f'O jogador {jogador} fez {gols} gol(s) no campenato.')


ficha()
