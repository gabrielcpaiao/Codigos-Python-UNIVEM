#Trabalho 2. Gabriel Costa Paião   RA: 61876-4  (UNIVEM, Ciência da computação, 1º Ano, 1º Etapa)
from random import randint
v = []*10
cont = 1
while (cont<=11):
    v.append(randint(1, 1000))
    cont +=1
print("O vetor gerado é: ")
print(v)
print("O vetor ordenado é:")
v.sort()
print(v)
while True:
    print("Digite um valor: ")
    x = int(input())
    for i in range (10):
        if x < v[i]:
            v.insert(i, x)
            break
        elif v[i] < x < v[i+1]:
            v.insert(i+1,x)
            break
    if x > v[10]:
        v.append(x)
    print(v)
    continuar = int(input("Caso queira rodar novamente digite um (1): "))
    if continuar!=1:
        break