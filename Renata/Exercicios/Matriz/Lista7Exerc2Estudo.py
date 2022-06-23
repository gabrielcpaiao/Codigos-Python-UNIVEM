'''
Faça um programa em Python que gere uma matriz M[10][10] com números aleatórios de 1 a 50
e copie para um vetor de 10 elementos, os números da diagonal principal. Imprima a matriz e o
vetor.
'''
from random import randint
m = [0]*10
v = [0]*10
for i in range(10):
    m[i] = [0]*10
    for j in range(10):
        x = randint(1,10)
        m[i][j] = x
        print(f"{m[i][j]:^2}",end=" ")
        if i == j:
            v[i] = x
    print()
print()
print(f"Os valores da diagonal principal são: {v}")