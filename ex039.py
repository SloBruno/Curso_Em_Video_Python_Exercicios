## Alistamento Militar

idade = int(input('Digite sua idade:'))

if idade < 18:
    print('Falta {} ano(s) para você se alistar.' .format(18 - idade))
elif idade > 18:
    print('Você já se alistou (ou devereria ter) há {} ano(s).' .format(idade-18))
else:
    print('Você deve se alistar este ano.')
