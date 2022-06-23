print("Digite o primeiro valor: ")
a = float(input())
print("Digite o segundo valor: ")
b = float(input())
print("Digite o terceiro valor: ")
c = float(input())
if (a>b or a>c):
    if (b<c):
        a,b=b,a
    else:
        a,c=c,a
if (b>c):
    b,c=c,b
print("A= ",a,"B= ",b,"C= ",c)
