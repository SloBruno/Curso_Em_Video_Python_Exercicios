# Tabuada V 3.0

while True:
    num = int(input("Quer ver a tabuada de que valor?"))

    if num < 0:
        break

    print('=' * 20)
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")
    print('=' * 20)
print("Fim")
