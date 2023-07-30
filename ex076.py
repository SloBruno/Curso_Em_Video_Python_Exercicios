# Listagem de Preços

listagem = ('Mouse', 122.9, 'Teclado', 315, 'Monitor', 799.90, 'HeadSet', 425.90)

print('-=-' * 15)
print('             Listagem de Preço')
print('-=-' * 15)
for cont in range(0, len(listagem), 2):
    print(f'{listagem[cont]}............R$', end='')
    cont += 1
    print(listagem[cont])
print('-=-' * 15)


