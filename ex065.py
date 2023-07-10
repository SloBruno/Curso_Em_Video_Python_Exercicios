#  Maior e menor valores.

esc = "S"
num = 0
soma = 0
quant = 0
maior = 0
menor = 0

while esc == 'S':

    num = int(input("Digite um número:"))

    if quant == 0:
        maior = num
        menor = num
        quant += 1

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    soma += num
    esc = str(input("Deseja continuar? [S/N]:")).upper().strip()
    quant += 1



media = soma/(quant-1)
print("A média entre os valores digitados é {:.2f}, O maior e o menor valor são respectivamente {} e {} " .format(media, maior, menor))
