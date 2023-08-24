# Biblioteca para facilitar o uso de cores no Terminal

# Cores ANSI

#Estilo

RESET = "\033[0m"
NEGRITO = "\033[1m"
ITALICO = "\033[3m"
SUBLINHADO = "\033[4m"

# Cores do texto
PRETO = "\033[30m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CYANO = "\033[36m"
BRANCO = "\033[37m"

# Cores do fundo
BG_PRETO = "\033[40m"
BG_VERMELHO = "\033[41m"
BG_VERDE = "\033[42m"
BG_AMARELO = "\033[43m"
BG_AZUL = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYANO = "\033[46m"
BG_BRANCO = "\033[47m"

# Funções para imprimir texto colorido
def print_colorido(texto, cor):
    print(cor + texto + RESET)

def print_colorido_estilizado(texto, cor, estilo):
    print(cor + estilo + texto + RESET)

def print_com_fundo(texto, cor_texto, cor_fundo):
    print(cor_texto + cor_fundo + texto + RESET)

