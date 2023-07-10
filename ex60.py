num = int(input("Digite um número para saber seu fatorial: "))
fatorial = 1

while num >= 1:
    fatorial *= num
    num -= 1

print(fatorial)

for i in range(num, 1, -1):
    fatorial *= num
    num -= 1
print(fatorial)
