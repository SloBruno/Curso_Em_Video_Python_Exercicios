alunos = dict()

alunos['Nome'] = str(input('Nome do Aluno:'))
alunos['Média'] = float(input('Média do Aluno:'))

media = alunos['Média']

if media >= 7:
    alunos['Situação'] = 'Aprovado'
elif 5 <= media < 7:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Reprovado'

for k, v in alunos.items():
    print(f'{k} é igual a {v}.')
