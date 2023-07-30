# Vogais

palavras = ('abacaxi', 'banana', 'carro', 'dado', 'elefante', 'futebol', 'girassol', 'hamburguer', 'ilustracao', 'janela')

vogais = ('a', 'e', 'i', 'o', 'u')

for termo in palavras:
    for letras in termo:
        if letras in vogais:
            print(f'Na palavra {termo.upper()}, as vogais são: {letras}')
    print('')