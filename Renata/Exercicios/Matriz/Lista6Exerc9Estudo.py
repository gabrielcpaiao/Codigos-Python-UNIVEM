'''
Elabore um programa em Python que declare uma matriz quadrada de 10 linhas por 10
colunas e verifique se a matriz é simétrica em relação à diagonal principal. A matriz
simétrica é aquela em que todos os elementos A( i , j) = A( j , i) para quaisquer valores de i e j.
Assim, A[2,1] deverá ser igual a A[1,2], e A[3,5] deverá ser igual a A[5,3] e assim por
diante. Imprimir mensagem “Matriz Simétrica” ou “Matriz não Simétrica”.
'''
from random import randint
m = [0]*10
for i in range(10):
    m[i] = [0]*10
    for j in range(10):
        if i == j:
            m[i][j] = 0
        else:
            m[i][j] = 1
print()
for i in range(10):
    for j in range(10):
        print(f"{m[i][j]:^2}", end=" ")
    print()

simetrica = True
for i in range(10):
    for j in range(i+1,10):
        if m[i][j] != m[j][i]:
            simetrica = False
            break
    if not simetrica:
        break


if simetrica:
    print(f"Matriz simétrica!")
else:
    print("Matriz não simétrica.")