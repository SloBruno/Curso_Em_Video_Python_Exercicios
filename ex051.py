#Progressão Aritmética

a1 = int(input("Digite o primeiro termo da p.a.:"))
r = int(input("Digite a razão da p.a.:"))

for i in range(1, 10):
    print(a1 + (i-1)*r)
