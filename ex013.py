sal = float(input('Qual é o seu salário?'))
desc = float(input("Qual é o percentual de aumento?"))
aum = sal*(desc/100)
fn = sal+aum

print('Com o aumento de {}%, o salário custará {:.2f}' .format(desc, fn))
