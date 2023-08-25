# Função para Votação

def voto(ano_nascimento):
    import datetime

    ano_atual = datetime.date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return idade, 'NÃO VOTA!'
    elif idade >= 65 or 16 <= idade < 18:
        return idade, 'VOTO OPCIONAL!'
    else:
        return idade, 'VOTO OBRIGATÓRIO!'


r1 = voto(int(input('Digite o ano de nascimento:')))
print(f'Com {r1[0]} anos, {r1[1]}')
