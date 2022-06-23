'''
 Os elementos de uma matriz M quadrada de ordem 5x5 são dados aij, onde:
i*j, se i ≠ j
i+j, se i = j
Faça um programa em Python que determine e imprima M
'''
m = [0]*5
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        if i != j:
            m[i][j] = i*j
        else:
            m[i][j] = i+j

for i in range(5):
    for j in range(5):
        print(f"{m[i][j]:^2}",end=" ")
    print()