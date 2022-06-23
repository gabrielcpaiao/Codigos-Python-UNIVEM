'''
2. Faça um programa em Python que gere uma matriz M[10][10] com
números aleatórios de 1 a 50 e copie para um vetor de 10 elementos,
os números da diagonal principal. Imprima a matriz e o vetor.
'''
from random import randint
print("Matriz gerada")
m = []
for i in range(10):
    m.append([])
    for j in range(10):
        m[i].append(randint(1,50))
        print(f"{m[i][j]:2}", end = " ")
    print()

v = []
for i in range(10):
    v.append(m[i][i])
print("Diagonal Principal >>",*v)