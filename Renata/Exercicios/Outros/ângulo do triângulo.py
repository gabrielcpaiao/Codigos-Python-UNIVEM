
print("Digite os valores de três ângulos de um triângulo")
a = float(input())
b = float(input())
c = float(input())
if (a+b+c!=180 or a==0 or b==0 or c==0):
    print("Os respectivos valore não formam um triângulo")
elif (a==90 or b==90 or c==90):
    print("O triângulo em questão é retângulo")
elif a<90 and b<90 and c<90:
    print("O triângulo em questão é acutângulo")
else:
    print("O triângulo em questão é obtusângulo")