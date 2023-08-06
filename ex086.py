matriz = [list(), list(), list()]

for i in range(0, 3):
    valor = int(input(f'Digite um valor para [0, {i}]:'))
    matriz[0].append(valor)

for i in range(0, 3):
    valor = int(input(f'Digite um valor para [1, {i}]:'))
    matriz[1].append(valor)

for i in range(0, 3):
    valor = int(input(f'Digite um valor para [2, {i}]:'))
    matriz[2].append(valor)

print(f'{matriz[0]}\n'
      f'{matriz[1]}\n'
      f'{matriz[2]}')






