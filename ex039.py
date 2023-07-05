## Alistamento Militar

from datetime import date

nascimento = int(input('Digite o ano de nascimento:'))
atual = date.today().year
idade = atual - nascimento

print("Você tem", idade,'anos.')

if idade < 18:
    print('Falta {} ano(s) para você se alistar.' .format(18 - idade))
elif idade > 18:
    print('Você já se alistou (ou devereria ter) há {} ano(s).' .format(idade-18))
    print("Seu alistamento foi em", (atual-idade) + 18)
else:
    print('Você deve se alistar este ano.')
