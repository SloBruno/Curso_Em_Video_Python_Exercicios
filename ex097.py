# Print Formatado

def escreva(txt):
    tamanho = len(txt) + 4
    print('~'*tamanho)
    print(f'  {txt}')
    print('~' * tamanho)


texto = str(input('Digite uma mensagem:'))
escreva(texto)
