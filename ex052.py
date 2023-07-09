num = int(input("Digite um número para saber se ele é primo ou não:"))
primo = True

for i in range(2, num):
    if num % i == 0:
        primo = False
        break

if primo:
    print("É primo")
else:
    print("Não é primo")
