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

# Formatação Matriz

for linha in matriz:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
    print()





