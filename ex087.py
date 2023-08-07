matriz = [list(), list(), list()]

# Construção Matriz

for i in range(0, 3):
    valor = int(input(f'Digite um valor para [0, {i}]:'))
    matriz[0].append(valor)

for j in range(0, 3):
    valor = int(input(f'Digite um valor para [1, {j}]:'))
    matriz[1].append(valor)

for k in range(0, 3):
    valor = int(input(f'Digite um valor para [2, {k}]:'))
    matriz[2].append(valor)

# Soma Valores Pares Matriz

pares = 0

for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0:
            pares += elemento

# Soma dos valores da terceira coluna

soma_terceira_coluna = 0

for linha in matriz:
    terceiro_elemento = linha[2]
    soma_terceira_coluna += terceiro_elemento

# Maior Valor Segunda linha

for linha in matriz:
    segunda_linha = matriz[1]

ordem = sorted(segunda_linha)
maior_valor = ordem[-1]

# Matriz

print('-=-' * 20)

for linha in matriz:
    for element in linha:
        print(f'[ {element} ]', end='')
    print()

print('-=-' * 20)

# Print

print(f'A soma dos valores pares é {pares}.\n'
      f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.\n'
      f'O maior valor da segunda linha é {maior_valor}.\n')
