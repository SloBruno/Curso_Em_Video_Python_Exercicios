# Maior e menor peso

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa:' .format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('A pessoa mais leve pesa {}kg' .format(menor))
print('A pessoa mais pesada pesa {}kg' .format(maior))

