'''
Escreva um programa em Python que gere uma matriz M[5][5], com números aleatórios entre 1
e 50. Imprima a matriz. A seguir, troque os elementos da diagonal principal com os elementos
da diagonal secundária. Imprima a nova matriz.
'''
from random import randint
m = [0]*5
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        m[i][j] = randint(1,50)
        print(f"{m[i][j]:^3}", end=" ")
    print()

print()
print("Ao trocar as diagonais de lugar, temos:")
for i in range(5):
    m[i][i],m[i][4-i] = m[i][4-i],m[i][i]
    for j in range(5):
        print(f"{m[i][j]:^3}", end=" ")
    print()