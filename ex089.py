alunos = []


while True:

    nome = str(input('Nome do Aluno:'))
    notaum = int(input('Nota 1:'))
    notadois = int(input('Nota 2:'))

    aluno = [nome, [notaum, notadois]]
    alunos.append(aluno)

    continuar = str(input('Deseja Continuar? [s/n]:')).lower().strip()

    if continuar == 's':
        continue
    else:
        break


print('-=-' * 20)

for c, aluno in enumerate(alunos):
    nome_aluno = aluno[0]
    notas = aluno[1]
    nota_um = notas[0]
    nota_dois = notas[1]
    print(f'N°      NOME        MÉDIA\n'
          f'{c}      {nome_aluno}         {(nota_um+nota_dois)/2} ')

print('-=-' * 20)


while True:

    dequal = int(input('De qual aluno você deseja ver a nota?(999 interrompe):'))

    if dequal == 999:
        break
    else:
        print(alunos[dequal][1])
print('Obrigado')
