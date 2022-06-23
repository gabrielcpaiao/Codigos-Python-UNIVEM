#o numero ao quadrado
#o npumero vezes ele +1
#o numero ao quadrado +1
N = int(input())
x = 1
cont = 1
while (cont<=(N*2)/2):
    print(f"{x} {x**2} {x**3}")
    print(f"{x} {(x**2)+1} {(x**3)+1}")
    x+=1
    cont += 1