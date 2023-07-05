## Média e Status

notaum = float(input('Digite a primeira nota:'))
notadois = float(input('Digite a segunda nota:'))
media = (notaum+notadois)/2

print("A média é {:.1f}" .format(media))
if media < 5:
    print('\033[0;31mAluno Reprovado.\033[m')
elif  5 < media < 6.9:
    print('\033[0;33mAluno em Recuperação.\033[m')
else:
    print('\033[0;32mAluno Aprovado.\033[m')
