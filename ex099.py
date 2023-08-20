# Finçãoo que descobre o maior valor

def maior(*valores):
    print('-=-'*15)
    tamanho = len(valores)
    print(f'Valores informados: {valores}.')
    print(f'Foram informados {tamanho} valores ao todo.')
    lista = list(valores)
    ordem = lista.sort(reverse=True)
    maior = lista[0]
    print(f'O maior valor digitado foi {maior}.')
    print('-=-'*15)


maior(2, 9, 4, 7, 1)