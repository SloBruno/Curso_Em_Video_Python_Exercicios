# Validação de dados

import cores


def leia_int(texto):

    while True:
        n = input(texto)

        if n.isnumeric():
            int(n)
            return n
            break

        else:
            print(f" {cores.VERMELHO}Erro! Digite apenas valores inteiros.{cores.RESET}")


res = leia_int("Digite um número inteiro:")
print(f"Você digitou o número {res}.")

