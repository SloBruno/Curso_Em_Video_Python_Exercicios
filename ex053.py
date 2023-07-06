# É palíndromo?

frase = str(input("Digite uma frase para saber se é palíndromo ou não:"))

semesp = frase.strip()
semesp = frase.replace(" ", "")
carac = len(semesp)
invert = frase[::-1]

if frase == invert:
    print("É palíndromo")
else:
    print("Não é palíndromo")
