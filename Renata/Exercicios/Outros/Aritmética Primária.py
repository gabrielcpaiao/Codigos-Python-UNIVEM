a = int(input ("digite o primeiro número de até 3 algarismos >> "))

a1= a//100
a2= a % 100//10
a3= a % 10

b = int(input ("digite o segundo número de até 3 algarismos >> "))

b1= b//100
b2= b % 100//10
b3= b % 10

cont = 0

if a1 + b1 > 9:
    cont +=1


if a2 + b2 > 9:
    cont +=1


if a3 + b3 > 9:
    cont +=1



print(cont)