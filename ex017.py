from math import hypot

ca = float(input('Digite o comprimento do cateto adjacente:'))
co = float(input('Digite o comprimento do cateto oposto:'))
hip = hypot(ca, co)

print('O valor da Hipotenusa é {}' .format(hip))


