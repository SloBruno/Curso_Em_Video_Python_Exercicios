# Análise de dados do grupo

maior = 0
homem = 0
mulher = 0
continuar = True

while True:

    if continuar:

        print("-------Cadastro de Usuário-------")

        idade = int(input("Idade:"))

        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]

        while sexo != "M" and sexo != "F":
            sexo = str(input("Sexo: [M/F]")).strip().upper()[0]

        if idade > 18:
            maior += 1
        if sexo == 'M':
            homem += 1
        if sexo == 'F' and idade < 20:
            mulher += 1

    parafrente = str(input('Deseja Continuar [S/N]')).upper().strip()[0]

    while parafrente != "S" and parafrente != "N":
        parafrente = str(input('Deseja Continuar [S/N]')).upper().strip()[0]

    if parafrente == 'S':
        continuar = True
    elif parafrente == 'N':
        continuar = False

    if not continuar:
        break

print(f"""Há {maior} pessoas com mais de 18 anos cadastradas'
Há {homem} homens cadastrados.
Há {mulher} mulheres com menos de 20 anos cadastradas.""")





