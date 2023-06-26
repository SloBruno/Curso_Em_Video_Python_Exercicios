## Categoria

from datetime import date

nascimento = int(input('Digite o ano de nascimento do Atleta:'))
atual = date.today().year
idade = atual - nascimento


print(idade)