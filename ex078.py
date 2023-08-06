lista = []

for i in range(0, 5):
    valor = int(input('Digite um número:'))
    lista.append(valor)

ordem = sorted(lista)

menor = ordem[0]
maior = ordem[-1]

print(f'Sua Lista: {lista}\n'
      f'Maior valor: {maior}\n'
      f'Menor Valor: {menor}')
