import math
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = (b**2)-4*(a)*(c)
if(a<0):
    print("Não é equação de segundo grau.")
elif(delta==0):
    x1 = (-b + math.sqrt(delta)) / 2 * a
    print(f"A raíz desta equação é: {x1}")
elif(delta>0):
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print(f"As raízes desta equação é: {x1} e {x2}")
else:
    print("Esta equação não possui raízes reais")