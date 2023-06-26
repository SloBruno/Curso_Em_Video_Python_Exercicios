dist = float(input('Qual é a distância da viagem?'))

if dist <= 200:
    print('Sua viagem vai custar R${:.2f}' .format(dist*0.5))
else:
    print('Sua viagem vai custar R${:.2f}' .format(dist*0.45))





