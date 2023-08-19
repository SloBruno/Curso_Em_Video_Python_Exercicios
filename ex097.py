# Print Formatado

def mensagem(txt):
    tamanho = len(txt)
    print('~'*tamanho)
    print(f'{txt}')
    print('~' * tamanho)


texto = str(input('Digite uma mensagem:'))
mensagem(texto)
