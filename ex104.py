# Validação de dados

def leia_int(texto):

    while True:
        n = input(texto)

        if n.isdigit():
            int(n)
            return n
            break

        else:
            print("Erro! Digite apenas valores inteiros.")

n = leia_int("Digite um número inteiro:")
print(f"Você digitou o número {n}.")

