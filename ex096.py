# Cálculo de Área
def area(l, c):
    print(f'A área de um terreno {l}x{c}m. é de {l*c}m².')


print('Área de um Terreno\n'
      '------------------')


largura = float(input('Largura(m):'))
comprimento = float(input('Comprimento(m):'))
area(largura, comprimento)
