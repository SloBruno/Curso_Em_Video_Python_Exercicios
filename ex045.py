#Jokenpô

from random import randrange
from time import sleep
print("{:=^40}" .format(" JOKENPÔ "))

print("Escolhas:\n[1] Pedra\n[2] Papel\n[3] Tesoura")
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

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")

print("-=" * 25)
print("O computador escolheu", pc, "e você escolheu", escolha)
print("-=" * 25)

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
