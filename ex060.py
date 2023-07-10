num = int(input("Digite um número para saber seu fatorial: "))
i = num
fatorial = 1
print("{}! = " .format(num), end="")
while i > 0:
    print("{}" .format(i, i), end='')
    print(" X " if i > 1 else " = ", end='')
    fatorial = fatorial*i
    i -= 1

print(fatorial)


