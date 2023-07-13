# Vários números com Flag

soma = 0
count = 0

while True:
    num = int(input("Digite úm número [999 para parar]:"))
    if num == 999:
        break
    soma += num
    count += 1

print(f'Você digitou {count} números e a soma entre eles é {soma}')
