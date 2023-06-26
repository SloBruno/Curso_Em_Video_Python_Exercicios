h = float(input('Qual é a largura da sua parede?'))
l = float(input('Qual é a altura da sua parede?'))
area = h*l
tinta = area/2

print('Sua parede mede {} metros quadrados. \nVocê precisa de {:.1f} galões de tinta para pintar a parede'.format(area, tinta))
