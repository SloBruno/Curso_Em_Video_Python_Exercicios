lista = list(str(input('Digite a expressão:')))

abertos = lista.count('(')
fechados = lista.count(')')

if abertos != fechados:
    print('Expressão inválida')
else:
    print('Expressão válida')
