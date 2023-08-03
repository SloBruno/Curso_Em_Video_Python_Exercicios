lista = []

while True:
    num = int(input('Digite um Valor:'))
    lista.append(num)
    print('Número adicionado com sucesso...')
    print()
    continuar = str(input('Deseja Continuar? [s/n]:')).lower().strip()

    if continuar == 's':
        continue

    elif continuar == 'n':
        break

copia1 = lista[:]
copia2 = lista[:]
impar = []
par = []

for element in copia1:
    if element // 2 == 0:
        par = element
    else:
        impar = element

