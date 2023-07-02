#Jokenpô

from random import randrange
print("Escolhas:\n1 - Pedra\n2 - Papel\n3 - Tesoura")
escolha = int(input("Qual é a sua escolha?"))

if escolha == 1:
    escolha = 'Pedra'
elif escolha == 2:
    escolha= 'Papel'
elif escolha == 3:
    escolha = 'Tesoura'

pc = randrange(1, 3)

if pc == 1:
    pc = 'Pedra'
elif pc == 2:
    pc = 'Papel'
elif pc == 3:
    pc = 'Tesoura'

print("O computador escolheu", pc,"e você escolheu", escolha)

if escolha == pc:
    print("Empatou!")
elif escolha == "Pedra" and pc == "Papel":
    print("Você Perdeu!")
elif escolha == "Pedra" and pc == "Tesoura":
    print("Você Venceu!")
elif escolha == "Papel" and pc == "Pedra":
    print("Você Venceu!")
elif escolha == "Papel" and pc == "Tesoura":
    print("Você Perdeu!")
elif escolha == "Tesoura" and pc == "Pedra":
    print("Você Perdeu!")
elif escolha == "Tesoura" and pc == "Papel":
    print("Você Venceu!")
