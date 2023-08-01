# Tabela Brasileirão

times = ("Botafogo", "Grêmio", "Flamengo", "Palmeiras","Athletico-PR", "São Paulo", "Fluminense", "Bragantino",
         "Fortaleza", "Internacional", "Cruzeiro", "Cuiabá", "Atlético-MG", "Santos", "Corinthians", "Goiás", "Bahia",
         "Coritiba", "América-MG", "Vasco")

print(f'Tabela do Brasileirão: {times}')

primeros_5 = times[0:5]
ultimos_4 = times[-5:-1]
ordem = sorted(times)
procurado = str(input('Qual time você deseja saber a posição?'))
posição_procurado = times.index(procurado) + 1

print(f'5 primeiros colocados: {primeros_5}\n'
      f'Zona de Rebaixamento: {ultimos_4}\n'
      f'Tabela em Ordem Alfabética: {ordem}\n'
      f'Posição do {procurado}: {posição_procurado}°\n')
