## Categoria

from datetime import date

nascimento = int(input('Digite o ano de nascimento do Atleta:'))
atual = date.today().year
idade = atual - nascimento

print("Idade:", idade)

if idade <= 9:
    print("Categoria Mirim")
elif 9 < idade <= 14:
    print("Categoria Infantil")
elif 14 < idade <= 19:
    print("Categoria Júnior")
elif 19 < idade <= 25:
    print("Categoria Sênior")
else:
    print("Categoria Master")
