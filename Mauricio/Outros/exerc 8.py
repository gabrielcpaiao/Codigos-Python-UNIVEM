print("Digite o primeiro valor: ")
a = float(input())
print("Digite o segundo valor: ")
b = float(input())
print("Digite o terceiro valor: ")
c = float(input())
if (c<a<b):
    a,b,c=b,c,a
elif (c<b<a):
    a,c=c,a
elif (b<)


#se na varial a n esta o menor valor, troca ela(variavel). TROCA A COM B OU A COM C
#Professor:
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
print("A = ", a, "B = ", b, "C= ",c)