#Financiamento

casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário?'))
anos = int(input('Em quantos anos deseja comprar a casa?'))

meses = (anos*12)
valor = (casa/meses)
minimo = (salario*1.3)

print('O valor da prestação mensal é de R${:.2f}' .format(valor))

if valor <= minimo:
    print('Empréstimo Aprovado!')
else:
    print('Empréstimo Negado.')


