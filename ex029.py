velo = float(input("Qual é a velocidade do carro?"))
multa = (velo-80)*7

if velo > 80:
    print('Você está a cima da velocidade permitida. \n'
          'Você foi multado em R${:.2f}' .format(multa))


print('Tenha um bom dia, dirija com cuidado.')
