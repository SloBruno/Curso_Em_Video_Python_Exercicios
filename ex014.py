celsius = float(input('Digite a temperatura em C°:'))
fah = (celsius*1.8+32)
kelvin = (celsius+273.15)

print('{}C° é igual a: \n{:.2f} Graus Fahrenheit. \n{:.2f} Graus Kelvin.' .format(celsius, fah, kelvin))
