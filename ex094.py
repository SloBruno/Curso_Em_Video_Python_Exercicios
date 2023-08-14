pessoas = list()
pessoa = dict()
mulheres = list()
maiores = list()

while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['sexo'] = str(input('Sexo [M/F]:')).upper().strip()
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade:'))

    pessoas.append(pessoa.copy())
    pessoa.clear()

    continuar = str(input('Deseja continuar [S/N]')).upper().strip()

    if continuar == 'N':
        break
    else:
        continue

print('-=-'*25)

quant = len(pessoas)
soma_idade = 0

for v in pessoas:
    idade = v['idade']
    soma_idade += idade

media = soma_idade/quant

for v in pessoas:
    idade = v['idade']
    if idade > media:
        maior = v['nome']
        maiores.append(maior)
        maior = v['idade']
        maiores.append(maior)

print(f'O grupo tem {quant} pessoas.\n'
      f'A média de idade é de {media :.2f} anos.\n'
      f'As mulheres são {mulheres}\n', end='')
for v in maiores:
    print(v, 'tem a idade acima da média com', end='')
    print(v, 'anos de idade.')
    # print(f'{v} está acima da média com {v+1} anos de idade')

