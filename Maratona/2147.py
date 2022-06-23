#Galopeira
C = int(input())
centesimo = 0.01
for i in range(C):
    soma = 0
    vet = []
    while True:
        galopeira = input().split()
        vet.append(galopeira)
        soma += centesimo
        if len(vet)>=9:
            if vet[-1] == str("a"):
                break
    if ((soma*1000)%10)>=5:
        round(soma+0.005)
        print(f"{soma:.2f}")
    else:
        print(f"{soma:.2f}")