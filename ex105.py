# Analisando e gerando dicionários

def notas(*nota, sit=False):

    """
        -> Função para analisar resultados de um aluno
    :param nota: Notas do aluno
    :param sit: (opcional) Mostra situação do aluno
    :return: dicionário com várias informações sobre um aluno

    """
    dicionario = dict()

    total = len(nota)
    dicionario['Total'] = total

    maior = sorted(nota)[-1]
    dicionario['Maior'] = maior
    menor = sorted(nota)[0]
    dicionario['Menor'] = menor

    soma = 0
    for v in nota:
        soma += v
    media = soma / total
    dicionario['Média'] = media

    situacao = ''

    if sit:
        if media >= 7:
            situacao = 'Boa'
        elif 6 <= media < 7:
            situacao = 'Razoável'
        else:
            situacao = 'Ruim'
        dicionario['Situação'] = situacao

    return dicionario



resultado = notas(5, 6, 7, 6, sit=True)
print(resultado)



