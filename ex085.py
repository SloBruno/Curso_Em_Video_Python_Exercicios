numeros = [list(), list()]

for i in range(0, 7):
    num = int(input(f'Digite o {i+1}° número:'))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

pares = sorted(numeros[0])
impares = sorted(numeros[1])

print(f'Valores pares: {pares}.\n'
      f'Valores ímpares: {impares}.')
