'''
Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) sem
números repetidos. Imprima o vetor.
'''
from random import randint
a = []
for i in range(10):
    x = randint(1,50)
    if x not in a:
        a.append(x)

print(a)