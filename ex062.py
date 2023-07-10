# Progressão Aritmética 3.0

a1 = int(input("Digite o primeiro termo da p.a.:"))
r = int(input("Digite a razão da p.a.:"))
termos = 10
termo = a1

cont = 1

while cont <= termos:
        print('{} => '.format(termo), end="")
        termo += r
        cont += 1

mais = int(input("Quantos termos a mais você quer?"))
count = mais

for i in range (1, count):
        a1 = termo
        termo += r
        print('{} => '.format(termo), end="")


