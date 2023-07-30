# Análise de dados em tuplas

primeiro = int(input("Digite o primeiro valor:"))
segundo = int(input("Digite outro valor:"))
terceiro = int(input("Digite mais um valor:"))
quarto = int(input("Digite o último valor:"))

tupla = (primeiro, segundo, terceiro, quarto)

nove = tupla.count(9)

if 3 in tupla:
    tres = tupla.index(3)
    temtres = f'O valor 3 está na posição {tres+1}'
else:
    temtres = 'O número três não foi digitado'

pares = tuple(valor for valor in tupla if valor % 2 == 0)

if not pares:
    a = str(f'Não foram digitados valores pares')
if pares:
    a = str(f'Os valores pares digitados foram: {pares}')

print(f'O valor 9 aparece {nove} vez(es).\n'
      f'{temtres}. \n'
      f'{a}.')
