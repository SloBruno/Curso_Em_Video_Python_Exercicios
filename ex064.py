# Tratando Vários Valores

soma = 0
num = 0
trig = 0


while trig != 999:
    trig = int(input('Digite um número [999 para parar]:'))
    if trig != 999:
        soma += trig
        num += 1

print("{} números forma digitados e a soma entre eles é {}." .format(num, soma))

