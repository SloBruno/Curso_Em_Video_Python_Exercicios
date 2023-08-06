pessoas = list()
dados = []
maiorpeso = 0
menorpeso = 0
contador = 0

while True:
    nome = str(input('Nome da pessoa:'))
    dados.append(nome)
    peso = float(input('Peso da pessoa [kg]:'))
    if contador == 0:
        menorpeso = peso
        contador += 1
    else:
        if peso < menorpeso:
            menorpeso = peso

    dados.append(peso)

    pessoas.append(dados[:])

    dados.clear()

    if peso >= maiorpeso:
        maiorpeso = peso

    continuar = str(input('Deseja continuar? [s/n]:')).lower().strip()

    if continuar == 's':
        continue
    elif continuar == 'n':
        break

maispesado = list()
maisleve = list()

for dado in pessoas:
    ape = dado[0]
    quilo = dado[1]
    if quilo == maiorpeso:
        maispesado.append(dado[0])
    if quilo == menorpeso:
        maisleve.append(dado[0])

quant = len(pessoas)



print(f'Há {quant} pessoas cadastrada.\n'
      f'As pessoas mais pesadas são: {maispesado} com {maiorpeso}kg.\n'
      f'As pessoas mais leves são: {maisleve} com {menorpeso}kg.')
