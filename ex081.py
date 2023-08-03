lista = []

while True:
    num = int(input('Digite um Valor:'))
    lista.append(num)
    print('Número adicionado com sucesso')

    continuar = str(input('Deseja Continuar? [s/n]:')).lower().strip()

    if continuar == 's':
        continue

    elif continuar == 'n':
        break

quant = len(lista)
ordem = sorted(lista, reverse=True)

temcinco = lista.count(5)

if temcinco > 0:
    temcinco = 'O valor 5 foi digitado.'
else:
    temcinco = 'O valor 5 não foi digitado.'

print(f'Valores inseridos: {lista}\n'
      f'Foram digitados {quant} números.\n'
      f'Lista em forma decrescente: {ordem}.\n'
      f'{temcinco}')

