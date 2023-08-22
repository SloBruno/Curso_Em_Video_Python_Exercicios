# Função para Votação

import datetime


def voto(ano_nascimento):
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 18:
        return idade, 'NÃO VOTA!'
    elif idade >= 65:
        return idade, 'VOTO NÃO OBRIGATÓRIO!'
    else:
        return idade, 'VOTO OBRIGATÓRIO!'


r1 = voto(int(input('Digite o ano de nascimento:')))
print(f'Com {r1[0]} anos, {r1[1]}')
