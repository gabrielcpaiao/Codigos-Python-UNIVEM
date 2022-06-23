xicara = int(input("Digite a quantia disponível de xícaras de farinha de trigo: "))
ovo = int(input("Digite a quantia disponível de ovo: "))
leite = int(input("Digite a quantia disponível de colheres de leite: "))
a = xicara//2
b = ovo//3
c = leite//5
if(a<b and a<c):
    print(f"A quantidade de bolos possíveis de serem feitos é {a}")
elif (b<c):
    print(f"A quantidade de bolos possíveis de serem feitos é {b}")
else:
    print(f"A quantidade de bolos possíveis de serem feitos é {c}")