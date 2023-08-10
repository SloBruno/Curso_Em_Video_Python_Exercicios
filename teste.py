import psutil
import time
import matplotlib.pyplot as plt


# Função para obter o uso de dados da rede
def get_network_usage():
    network_stats = psutil.net_io_counters()
    return network_stats.bytes_sent, network_stats.bytes_recv


# Tempo total para monitorar (em segundos)
tempo_total = 30

# Intervalo de coleta (em segundos)
intervalo = 1

# Listas para armazenar os dados coletados
tempos = []
dados_enviados = []
dados_recebidos = []

# Coleta de dados
tempo_atual = 0
dados_enviados_anterior, dados_recebidos_anterior = get_network_usage()

while tempo_atual < tempo_total:
    tempo_atual += intervalo
    dados_enviados_atual, dados_recebidos_atual = get_network_usage()

    taxa_enviados = ((dados_enviados_atual - dados_enviados_anterior) * 8) / (intervalo * 1000)  # kbit/s
    taxa_recebidos = ((dados_recebidos_atual - dados_recebidos_anterior) * 8) / (intervalo * 1000)  # kbit/s

    tempos.append(tempo_atual)
    dados_enviados.append(taxa_enviados)
    dados_recebidos.append(taxa_recebidos)

    dados_enviados_anterior = dados_enviados_atual
    dados_recebidos_anterior = dados_recebidos_atual

    time.sleep(intervalo)

# Geração do gráfico
plt.plot(tempos, dados_enviados, label='Dados Enviados')
plt.plot(tempos, dados_recebidos, label='Dados Recebidos')
plt.title('Uso de Dados da Rede')
plt.xlabel('Tempo (segundos)')
plt.ylabel('Uso de Dados (kbit/s)')
plt.legend()
plt.grid(True)

# Salvar o gráfico como um arquivo de imagem
plt.savefig('uso_de_dados.png')  # O nome do arquivo pode ser alterado conforme necessário

# Exibir o gráfico na janela de visualização
plt.show()
