#Número Primo

num = int(input("Digite um número para saber se ele é primo ou não:"))

primo = 0

for i in range (1, (num+1)):
  if num % i == 0:
      primo += 1

if num == 2:
    print("É primo")
else:
    print("Não é um número primo.")
