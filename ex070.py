# Estatísticas em Produtos

total = 0
caro = 0

while True:
    nome = str(input("Nome do Produto:"))
    preço = float(input("Preço do Produto: R$"))

    continuar = ("Você deseja continuar? [S/N]:").strip().upper()[0]

    while continuar != "S" and continuar != "N":
        continuar = ("Você deseja continuar? [S/N]:").strip().upper()[0]

    if continuar == "S":
        total += preço
    if preço > 1000:
        caro += 1



