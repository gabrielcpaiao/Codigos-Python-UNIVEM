'''
9. Elabore um programa em Python que declare uma matriz quadrada de
10 linhas por 10 colunas e verifique se a matriz é simétrica em relação à
diagonal principal. A matriz simétrica é aquela em que todos os elementos
A( i , j)  =  A( j , i)  para quaisquer valores de i e j. Assim, A[2,1]
deverá ser igual a A[1,2], e A[3,5] deverá ser igual a A[5,3] e assim por diante.
Imprimir mensagem “Matriz Simétrica” ou “Matriz não Simétrica”.
'''

mat = []
print("\nMatriz gerada")
for i in range(3):
    mat.append([])
    for j in range(3):
        mat[i].append(int(input(f"[{i}][{j}] >> ")))

for i in range(3):
    for j in range(3):
        print("[{:2}] ".format(mat[i][j]), end='')
    print()

simetrica=True
for i in range(3):
    for j in range(3):
        if (mat[i][j]!=mat[j][i]):
            simetrica=False
            break
    if not simetrica:
        break
if simetrica:
    print("\nMatriz simétrica em relação a Diagonal Principal")
else:
    print("\nMatriz não simétrica em relação a Diagonal Principal")