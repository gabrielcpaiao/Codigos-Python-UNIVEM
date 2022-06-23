'''
8. Elabore um programa em Python que leia duas matrizes A (mxn) e B (pxq) e
calcule e mostre a matriz Python que é a soma de A com B (caso a soma seja possível).

from random import randint
print("Informe as dimensões das matrizes A e B")
print("A")
m = int(input("Quantidade de linhas  >> "))
n = int(input("Quantidade de colunas >> "))

print("B")
p = int(input("Quantidade de linhas  >> "))
q = int(input("Quantidade de colunas >> "))

print("=" * 50)

if m == p and n == q:
    print("Matriz A")
    A = []
    for i in range(m):
        A.append([])
        for j in range(n):
            A[i].append(randint(1,50))
            print(f"{A[i][j]:2}",end=" ")
        print()

    print("*" * 50)
    print("Matriz B")
    B = []
    for i in range(p):
        B.append([])
        for j in range(q):
            B[i].append(randint(1, 50))
            print(f"{B[i][j]:2}", end=" ")
        print()

    print("*" * 50)
    print("Matriz C (Soma de A + B)")
    C = []
    for i in range(p):
        C.append([])
        for j in range(q):
            C[i].append(A[i][j] + B[i][j])
            print(f"{C[i][j]:2}", end=" ")
        print()
else:
    print("Dimensões inválidas para a realização da soma das matrizes!!")
'''
from random import randint

m = int(input("Digite o número de linhas da matriz A: "))
n = int(input("Digite o número de colunas da matriz A: "))
print()
p = int(input("Digite o número de linhas da matriz B: "))
q = int(input("Digite o número de colunas da matriz B: "))

a = [0]*m
b = [0]*m
if m==p and n==q:
    for i in range(m):
        a[i] = [0]*m
        b[i] = [0]*m
        for j in range(n):
            a[i][j] = randint(1,10)
            b[i][j] = randint(1,10)

for i in range(m):
    for j in range(n):
        print(f"{a[i][j]}", end=" ")
    print()
print()
for i in range(p):
    for j in range(q):
        print(f"{b[i][j]}", end=" ")
    print()