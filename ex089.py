alunos = []
nomes = []
notas = []
contador = 0

while True:

    nome = str(input('Nome do Aluno:'))
    nomes.append(nome)
    notaum = int(input('Nota 1:'))
    notas.append(notaum)
    notadois = int(input('Nota 2:'))
    notas.append(notadois)
    nomes.append(notas[:])
    alunos.append(nomes[:])
    nomes.clear()
    notas.clear()
    continuar = str(input('Deseja Continuar? [s/n]:')).lower().strip()

    if continuar == 's':
        continue
    else:
        break

# Média

print('-=-' *20)
print(f'N° NOME       MÉDIA')

print(alunos[0, 1])
