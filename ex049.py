#Tabuada 2.0

num = int(input("Digite um número para saber sua tabuada:"))

for i in range(1, 11):
    mult = i * num
    print("{} x {} = {}" .format(num, i, mult))
