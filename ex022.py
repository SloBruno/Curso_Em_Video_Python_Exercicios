nome = str((input("Nome Completo:")))

up = nome.upper()
low = nome.lower()
let = nome.split()
joi = ''.join(let)
cou = len(joi)
qua = len(let[0])


print('Nome com todas as letras maiúsculas:', up)
print('Nome com todas as letras minúsculas:', low)
print('Quantidade de letras:', cou)
print('Quantida de letras do primeiro nome:', qua)


