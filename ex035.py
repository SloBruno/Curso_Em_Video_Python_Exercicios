print("-=-"*10)
print('   Analisador de Triângulo')
print("-=-"*10)

retaum = float(input('Valor do segmento da primeira reta:'))
retadois = float(input('Valor do segmento da segunda reta:'))
retatrês = float(input('Valor do segmento da terceira reta:'))

ce = retadois+retatrês
cr = retadois+retaum
ct = retaum+retatrês

if ce>retaum and cr>retatrês and ct > retadois:
    print('Pode formar um Triângulo')
else:
    print('Não pode formar um triângulo')




