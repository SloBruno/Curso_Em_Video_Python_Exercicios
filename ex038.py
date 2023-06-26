## Comparação de Dois Números Inteiros

a = int(input("Primeiro Valor:"))
b = int(input("Segundo Valor:"))

if a > b:
    print("O {} é maior que o {}." .format(a, b))
elif b > a:
    print('O {} é maior que o {}.' .format(b, a))
else:
    print('Os dois valores são iguais.')
