'''
 Faça um programa em Python que gere 20 elementos aleatórios (entre 1 e 50)
armazenando no vetor A e crie outros 2 vetores B e C. O vetor B deve ter apenas os
números pares e o vetor C deve conter apenas os números ímpares. Imprima os três
vetores.
'''
from random import randint
a = [0]*20
for i in range(20):
    a[i] = randint(1,50)
b = []
c = []
for i in range(20):
    if a[i]%2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])

print(a)
print(b)
print(c)