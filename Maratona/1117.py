while True:
    n1 = float(input())
    if (n1<0 or n1>10):
        print("nota invalida")
    else:
        break
while True:
    n2 = float(input())
    if (n2<0 or n2>10):
        print("nota invalida")
    else:
        break
med = (n1 + n2)/2
print(f"media = {med:.2f}")