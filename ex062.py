# Progressão Aritmética 3.0

a1 = int(input("Digite o primeiro termo da p.a.:"))
r = int(input("Digite a razão da p.a.:"))
termos = 10
termo = a1

cont = 1
mais = 1
total = 0
mais = 10

while mais != 0:
        total += mais
        while cont <= total:
                print('{} => '.format(termo), end="")
                termo += r
                if mais != 0:
                        cont += 1
        print("Pausa")
        mais = int(input("Quantos termos a mais você quer?"))
print("Fim, foram printados {} termos" .format(total))





