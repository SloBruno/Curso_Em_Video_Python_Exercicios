alunos = []

while True:

    nome = str(input('Nome do Aluno:'))
    alunos.append(nome)
    nota_um = float(input('Nota 1:'))
    alunos.append(nota_um)
    nota_dois = float(input('Nota 2:'))
    alunos.append(nota_dois)


    continuar = str(input('Deseja Continuar? [s/n]:')).lower().strip()

    if continuar == 's':
        continue
    else:
        break

print(alunos)