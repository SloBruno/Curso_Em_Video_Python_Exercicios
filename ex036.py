casa = float(input('Qual é o valor da casa?'))
salario = float(input('Qual é o seu salário?'))
anos = int(input('Em quantos anos deseja comprar a casa?'))

meses = (anos*12)
valor = (casa/meses)


print('O valor da prestação mensal é de R${}' .format(valor))

if valor <= salario*1.3:
    print('Empréstimo Aprovado!')
else:
    print('Empréstimo Negado.')


