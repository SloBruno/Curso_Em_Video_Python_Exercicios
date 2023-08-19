# Cálculo de Área

print('Área de um Terreno\n'
      '------------------')
def area(l, c):
    print(f'A área de um terreno {l}x{c} é de {l*c}m².')


largura = float(input('Largura(m):'))
comprimento = float(input('Comprimento(m):'))
area(largura, comprimento)
