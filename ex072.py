# Número por Extenso

extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
"treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

posição = int(input('Digite um número entre 0 e 20:'))

while True:
    if posição in range(0, 21):
        print(f'Você digitou o número {extenso[posição]}.')
        break

    else:
        posição = int(input(f'Tente novamente. Digite um número entre 0-20:'))


