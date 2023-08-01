# Vogais

palavras = ('abacaxi', 'banana', 'carro', 'dado', 'elefante', 'futebol', 'girassol', 'hamburguer', 'ilustracao', 'janela')

vogais = ('a', 'e', 'i', 'o', 'u')

for termo in palavras:
    print(f'Na palavra {termo.upper()}, as vogais são:', end='')
    for letras in termo:
        if letras in vogais:
            print(letras, end=' ')
    print('')
