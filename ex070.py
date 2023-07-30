# Estatísticas em Produtos

total = 0
caro = 0
barato = 0

while True:
    nome = str(input("Nome do Produto:"))
    barato = nome
    preço = float(input("Preço do Produto: R$"))

    continuar = str(input("Você deseja continuar? [S/N]:")).strip().upper()[0]

    while continuar != "S" and continuar != "N":
        continuar = ("Você deseja continuar? [S/N]:").strip().upper()[0]

    if continuar == "S":
        total += preço
        if preço > 1000:
            caro += 1
            if nome < barato:
                barato = nome
    elif continuar == "N":
        total += preço
        if preço > 1000:
            caro += 1
            if nome < barato:
                barato = nome
        break

print(f"O total da compra é de R${total:.2f}\n"
      f"{caro} produto(s) custam mais de R$1000.\n"
      f"{barato.capitalize().strip()} é o produto mais barato.\n ")



