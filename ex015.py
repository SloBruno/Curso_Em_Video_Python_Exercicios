km = float(input('Quantos quilômetros você rodou com o carro?'))
dia = float(input('Quantos dias você ficou com o carro?'))
preço = ((dia*60) + (km*0.15))

print('Você terá que pagar R${:.2f}' .format(preço))
