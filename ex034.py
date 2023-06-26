salario = float(input('Digite o salário para saber o aumento:'))

aumentoum = salario + (salario * 15/100)
aumentodois = salario + (salario * 10/100)

if salario > 1250 :
    print('O novo salário será de R${}' .format(aumentodois))
else:
    print('O novo salário será de R${}' .format(aumentoum))
