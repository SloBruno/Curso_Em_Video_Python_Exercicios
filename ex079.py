list = []

while True:
        valor = (int(input('Digite um valor:')))
        if valor in list:
            print('O valor já foi inserido. Não irei cadastrar novamente...')
        else:
            list.append(valor)
            print('Valor Cadastrado com sucesso...')

        continuar = str(input(('Deseja continuar [s]/[n]:'))).lower().strip()

        if continuar == 's':
            continue
        else:
            break

ordem = sorted(list)
menor = ordem[0]
maior = ordem[-1]

print(f'A lista cadastrada foi {ordem}.\n'
      f'O menor valor é {menor}.\n'
      f'O maior valor é {maior}.')





