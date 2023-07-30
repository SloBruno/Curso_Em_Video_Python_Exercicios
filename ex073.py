#Tabela Brasileirão

times = ("Botafogo", "Grêmio", "Flamengo", "Palmeiras","Athletico-PR", "São Paulo", "Fluminense", "Bragantino",
         "Fortaleza", "Internacional", "Cruzeiro", "Cuiabá", "Atlético-MG", "Santos", "Corinthians", "Goiás", "Bahia",
         "Coritiba", "América-MG", "Vasco")

primeros_5 = times[0:5]
ultimos_4 = times[-5:-1]
ordem = sorted(times)
procurado = 'Flamengo'
posição_procurado = times.index('Flamengo') + 1

print(f'5 primeiros colocados: {primeros_5}\n'
      f'Zona de Rebaixamento: {ultimos_4}\n'
      f'Tabela em Ordem Alfabética: {ordem}\n'
      f'Posição do Flamenago: {posição_procurado}\n')
