frase = str(input('Qual é a frase?'))
minúsculo = frase.lower().strip()
a = minúsculo.count('a')
b = minúsculo.find('a')+1
c = minúsculo.rfind('a')+1

print('A letra "A" aparece {} vezes na frase.\n'
      'A letra "A" aparece pela primeira vez na posição {}.\n'
      'A letra "A" aparece na posição {} pela última vez. ' .format(a, b, c))
