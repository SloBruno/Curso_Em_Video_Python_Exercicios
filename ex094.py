pessoas = list()
pessoa = dict()
mulheres = list()
maiores = dict()

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
        maiores = v.copy()

print(f'O grupo tem {quant} pessoas.\n'
      f'A média de idade é de {media :.2f} anos.\n'
      f'As mulheres são {mulheres}\n', end='')

print(f'Lista das pessoas com idade acima da média:')
for k, v in maiores.items():
    print()
    print(k, '=', v, ';', end='')



