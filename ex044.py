#Desconto por Método de pagamento

print("{:=^40}" .format(" Loja do Bruno "))

preço = float(input("Digite o preço do produto:"))
print("Tipo de Pagamento\n1 - À vista\n2 - Parcelado no Cartão")

tipo = int(input("Escolha:"))

if tipo == 1:
    print("Método de Pagamento\n1 - Dinheiro/Cheque\n2 - Cartão")
    método = int(input("Escolha:"))
elif tipo == 2:
    parcela = int(input("Em quantas parcelas?"))
else:
    print("Escolha inexistente.")

if tipo == 1 and método == 1:
    print("Você ganhou 10% de desconto! O produto custa agora R${}." .format(preço*0.9))
elif tipo == 1 and método == 2:
    print("Você ganhou 5% de desconto! O produto custa agora R${}." .format(preço*0.95))

if tipo == 2 and parcela == 2:
    print("O produto custa R${}." .format(preço))
elif tipo == 2 and parcela >= 3:
    print("O produto terá um acréscimo de 20% de juros. O produto custa agora R${}." .format(preço*1.2))
elif tipo == 2 and parcela < 2:
    print("Você ganhou 5% de desconto! O produto custa agora R${}." .format(preço*0.95))
