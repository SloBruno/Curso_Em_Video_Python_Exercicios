pessoas = list()
pessoa = dict()

while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['sexo'] = str(input('Sexo [M/F]:'))
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
    for i in v['idade']:
        soma_idade += i

media = soma_idade/quant

print(f'O grupo tem {quant} pessoas.'
      f'A média de idade é de {media} anos.')
