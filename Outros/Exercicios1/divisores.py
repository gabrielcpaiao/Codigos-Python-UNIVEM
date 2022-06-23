#Gabriel Costa Paião  1ºAno, 1º Termo. Ciência da computação. RA: 61876-4
#Divisores de um número:
N = int(input())
cont = 1
while (cont<=N):
    div = N%cont
    if (div==0):
        print(cont)
    cont+=1
