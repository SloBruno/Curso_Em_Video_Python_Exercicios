# Jogo do Par ou Ímpar

from random import randint

print(f'==========Vamos jogar Par ou Ímpar!==========')
print()

par = "Par"
ímpar = "Ímpar"
count = 0
perdeu = False

while True:

    esc = int(input("Digite 1 para ímpar e 2 para par:"))
    pc = randint(0, 10)
    player = int(input("Escolha um número:"))
    soma = pc+player
    soma2 = pc+player

    if (soma2) % 2 == 0:
        soma2 = par
    else:
        soma2 = ímpar
    print()
    if soma2 == par and esc == 1:
        print(f"Eu escolhi {pc} e você {player}. O total foi de {soma}; Deu {soma2}!")
        print("Perdeu")
        break
    elif soma2 == par and esc == 2:
        print(f"Eu escolhi {pc} e você {player}. O total foi de {soma}; Deu {soma2}!")
        print("Ganhou")
        count += 1
    elif soma2 == ímpar and esc == 1:
        print(f"Eu escolhi {pc} e você {player}. O total foi de {soma}; Deu {soma2}!")
        print("Ganhou")
        count += 1
    elif soma2 == ímpar and esc == 2:
        print(f"Eu escolhi {pc} e você {player}. O total foi de {soma}; Deu {soma2}!")
        print('Perdeu')
        break
print()
print(f"Obrigado por Jogar Comigo! Você ganhou {count} vezes consecutivas.")


