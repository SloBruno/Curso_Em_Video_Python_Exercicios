media = 0
maior_idade_h = 0
maior_idade_m = 0
nome_homem_mais_velho = ""
mulheres_menos_20 = 0

for i in range(1, 5):
    print('------{}ª Pessoa------' .format(i))
    nome = str(input("Nome:"))
    idade = int(input("Idade:"))
    media += idade / 4
    sexo = str(input("Sexo [M/F]:"))

    if sexo == 'm' or sexo == 'M':
        if i == 1:
            maior_idade_h = idade
            nome_homem_mais_velho = nome
        else:
            if idade > maior_idade_h:
                maior_idade_h = idade
                nome_homem_mais_velho = nome

    elif sexo == 'f' or sexo == 'F':
        if idade < 20:
            mulheres_menos_20 += 1

print("A média de idade do grupo é de {} anos.".format(media))
print("{} é o homem mais velho e tem {} anos de idade.".format(nome_homem_mais_velho, maior_idade_h))
print("{} mulheres têm menos de 20 anos.".format(mulheres_menos_20))
