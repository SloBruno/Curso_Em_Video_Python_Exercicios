valor = int(input("Quantos reais você deseja sacar? R$ "))

de1 = 0
de10 = 0
de20 = 0
de50 = 0

while valor >= 50:
    de50 += 1
    valor -= 50

while valor >= 20:
    de20 += 1
    valor -= 20

while valor >= 10:
    de10 += 1
    valor -= 10

while valor >= 1:
    de1 += 1
    valor -= 1

print(f"Total de {de1} notas de um real")
print(f"Total de {de10} notas de dez reais")
print(f"Total de {de20} notas de vinte reais")
print(f"Total de {de50} notas de cinquenta reais")
