# Sequência de Fibonacci

termos = int(input("Quantos números da sequência de Fibonacci você deseja ver?"))

quant = 0
t1 = 0
t2 = 1
print('0', end='; ')
print('1', end='; ')
while quant <= termos:
      t3 = t1+t2
      print(t3, end='; ')
      t1 = t2
      t2 = t3
      quant += 1

