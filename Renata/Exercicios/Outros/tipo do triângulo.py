print("Digite os valores de três lados de um triângulo")
a = float(input())
b = float(input())
c = float(input())
if (a>b+c) or (b>a+c) or (c>a+b):
    print("Os respectivos valore não formam um triângulo")
elif a==b==c:
    print("O triângulo em questão é equilátero")
elif a!=b!=c:
    print("O triângulo em questão é escaleno")
else:
    print("O triângulo em questão é isóceles")
