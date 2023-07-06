#Soma dos número ímpares, múltiplos de 3, 1-500
soma = 0
for i in range(1,500, 2):
    if i % 3 == 0:
        soma += i
print(soma)

