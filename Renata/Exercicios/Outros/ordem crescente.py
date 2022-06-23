#meu:
print("Digite três valores diferentes")
a = int(input())
b = int(input())
c = int(input())
if (a>c):
    a,c = c,a
if (c>b):
    c,b = b,c

if (a-b<0 and a-c<0 and b-c<0):
    print(f"{a} é o menor valor entre eles, {b} é o do meio e {c} é o maior")
elif (a-b<0 and a-c<0 and c-b<0):
    print(f"{a} é o menor valor entre eles, {c} é o do meio e {b} é o maior")
elif (a-b<0 and a-c<0 and b-c<0):
    print(f"{a} é o menor valor entre eles, {c} é o do meio e {b} é o maior")

#Professora:
print("Informe 3 valores")
a = int(input("1º >> "))
b = int(input("2º >> "))
c = int(input("3º >> "))
print(f"Números informados: {a} - {b} - {c}")

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(f"Números ordenados:  {a} - {b} - {c}")
