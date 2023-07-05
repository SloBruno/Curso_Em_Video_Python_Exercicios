# Analisador de Triângulo 2.0

print("-=-"*10)
print('   Analisador de Triângulo')
print("-=-"*10)

retaum = float(input('Valor do segmento da primeira reta:'))
retadois = float(input('Valor do segmento da segunda reta:'))
retatrês = float(input('Valor do segmento da terceira reta:'))

ce = retadois+retatrês
cr = retadois+retaum
ct = retaum+retatrês

if ce > retaum and cr > retatrês and ct > retadois:
    print('Pode formar um triângulo', end=' ')
    if retaum == retadois == retatrês:
        print("equilátero")
    elif retaum != retadois != retatrês and retatrês != retaum:
        print("escaleno")
    else:
        print("Isósceles")

else:
    print('Não pode formar um triângulo')




