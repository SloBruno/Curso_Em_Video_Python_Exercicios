#Soma dos pares

soma = 0
for i in range(1, 7):
    num = int(input("Digite um número inteiro:"))
    if num % 2 == 0:
     soma += num
print(soma)
