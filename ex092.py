import datetime

dados = dict()

dados['Nome'] = str(input('Digite o nome:'))
ano_nascimento = int(input('Digite o ano de nascimento:'))
ano_atual = datetime.date.today()
anoatual = ano_atual.year
idade = anoatual - ano_nascimento
dados['Idade'] = idade
dados['CTPS'] = int(input('Número da Carteira de Trabalho:'))

if dados['CTPS'] == 0:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    dados['Contratação'] = int(input('Ano da Contratação:'))
    anos = dados['Contratação']
    anos_1 = anoatual-anos
    aposentadoria = 35 - anos_1
    aposentadoriax = idade+aposentadoria
    dados['Aposentadoria'] = aposentadoriax
    dados['Salário'] = int(input('Sálario: R$'))

    for k, v in dados.items():
        print(f'{k} tem o valor {v}')



