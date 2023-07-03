#Conversão de Bases Numéricas

print("""Digite 1 para Conversão em Binário;
Digite 2 para Conversão em Octal;
Digite 3 para Conversão em Hexádecimal;
""")

esc = int(input('Escolha:'))
num = int(input('Valor para Conversão:'))

bin = "{:b}" .format(num)
oc = "{:o}" .format(num)
hex = "{:x}" .format(num)

if esc == 1:
    print(bin)
elif esc == 2:
    print(oc)
elif esc == 3:
    print(hex)
else:
    print('Função não disponível')
