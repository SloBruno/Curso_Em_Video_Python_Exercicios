##Grupo da maioridade

from datetime import date
atual = date.today().year

menor = 0
maior = 0

for i in range(1, 8):
    ano = int(input("Ano de nascimento:"))
    idade = atual-ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('{} pessoas são maiores de idade e {} pessoas são menores de idade' .format(maior, menor))
