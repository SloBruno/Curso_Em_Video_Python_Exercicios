# Progressão Aritmética 2.0

a1 = int(input("Digite o primeiro termo da p.a.:"))
r = int(input("Digite a razão da p.a.:"))
termo = a1
cont = 1

while cont <= 10:
        print('{} => ' .format(termo), end="")
        termo += r
        cont += 1

print("Fim")

