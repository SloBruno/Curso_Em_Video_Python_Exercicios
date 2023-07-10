# Progressão Aritmética 2.0

a1 = int(input("Digite o primeiro termo da p.a.:"))
r = int(input("Digite a razão da p.a.:"))
termos = int(input('Quantos termos deve ter a p.a.?'))
termo = 1

while termo <= termos:
        print(a1 + (termo - 1) * r)
        termo += 1
