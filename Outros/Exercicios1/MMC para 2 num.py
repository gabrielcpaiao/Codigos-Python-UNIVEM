#Gabriel Costa Paião  1ºAno, 1º Termo. Ciência da computação. RA: 61876-4
#MMC de dois números:
n1 = int(input())
copn1 = n1
n2 = int(input())
copn2 = n2
cont = 2

resultado = []
while n1 != 1 and n2 != 1:
    if n1 % cont == 0 and n2 % cont == 0:
        resultado.append(cont)
        n1 = n1/cont
        n2 = n2/cont
    elif n1 % cont == 0 and n2 % cont != 0:
        resultado.append(cont)
        n1 = n1/cont
    elif n1 % cont != 0 and n2 % cont == 0:
        resultado.append(cont)
        n2 = n2/cont
    else:
        cont += 1

print(resultado)
x = 1
for i in range(len(resultado)):
    x *= resultado[i]
print(f"O MMC de {copn1} e de {copn2} é igual a: {x}")

'''cont = 2
while n2 != 1:
    if n2 % cont == 0:
        resultado.append(cont)
        n2 = n2/cont
    else:
        cont += 1
print(resultado)
x = 1
for i in range(len(resultado)):
    x *= resultado[i]
print(f"O MMC de {copn1} e de {copn2} é igual a: {x}")'''