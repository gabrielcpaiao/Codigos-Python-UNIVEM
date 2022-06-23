#Gabriel Costa Paião  1ºAno, 1º Termo. Ciência da computação. RA: 61876-4
#MDC de dois números:
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
cont = 2
fatores = []
print()
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

x = menor
y = maior % menor


while maior % menor != 0:
    maior, menor = menor,(maior%menor)
print(f"O MDC de {n1} e {n2} é: {menor}")





'''while n1 == n2 ==1:
    if n1%cont == 0 and n2%cont!= 0:
        n1 = n1/cont
        cont += 1
    elif n2%cont == 0 and n1%cont != 0:
        n2 = n2/cont
        cont += 1
    elif n1%cont == 0 and n2%cont == 0:
        n1 = n1 / cont
        cont += 1
        n2 = n2 / cont
        fatores.append(cont)
    else:
        cont += 1
print(fatores)
produto = 1
for i in range(len(fatores)):
    produto *= fatores[i]
print(f"O MDC de {n1} e {n2} é: {produto}")'''