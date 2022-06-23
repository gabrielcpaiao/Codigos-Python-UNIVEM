'''
Elabore um programa em Python que leia duas matrizes A (mxn) e B (pxq) e calcule e
mostre a matriz Python que é a soma de A com B (caso a soma seja possível).
'''
a = [0]*5
b = [0]*5
for i in range(5):
    a[i] = [0]*5
    b[i] = [0]*5
    for j in range(5):
        a[i][j] = int(input())
        b[i][j] = int(input())

for i in range(5):
    for j in range(5):
        print(f"{a[i][j]:^2}",end=" ")
    print()
print()
for i in range(5):
    for j in range(5):
        print(f"{b[i][j]:^2}",end=" ")
    print()

c = [0]*5
for i in range(5):
    c[i] = [0]*5
    for j in range(5):
        c[i][j] = (a[i][j])+(b[i][j])

print()
for i in range(5):
    for j in range(5):
        print(f"{c[i][j]:^2}",end=" ")
    print()