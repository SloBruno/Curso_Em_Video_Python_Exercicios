valor = float(input('Dê um valor em metros:'))
km = valor/1000
hm = valor/100
dam = valor/10
dm=valor*10
cm = valor*100
mm = valor*1000

print('{}m é igual a: \n{}km.\n{}hm.\n{}dam.\n{}dm.\n{}cm.\n{}mm.' .format(valor, km, hm, dam, dm, cm, mm))

