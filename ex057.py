# Validação de dados

sexo = str(input("Informe seu Sexo [M/F]:")).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo [M/F]:")).upper().strip()[0]
print("Sexo {} registrado com sucesso." .format(sexo))
