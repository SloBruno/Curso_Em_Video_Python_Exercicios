from math import sin, cos, tan

gr = int(input('Quanto é o ângulo?'))

seno = sin(gr)
cosseno = cos(gr)
tangente = tan(gr)

print('O seno de {}° é {} \nO cosseno de {}° é {} \nA tangente de {}° é {}'.format(gr, seno, gr, cosseno, gr, tangente))
