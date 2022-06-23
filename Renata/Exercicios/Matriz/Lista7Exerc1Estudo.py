'''
 Escreva um programa em Python que gere uma matriz M[10][10] com números aleatórios de 1
a 50, peça um número de uma linha qualquer, entre 0 e 9, e copie os elementos dessa linha para
um vetor. Imprima a matriz e o vetor.
'''
from random import randint
m = [0]*10
v = [0]*10
for i in range(10):
    m[i] = [0]*10
    for j in range(10):
        m[i][j] = randint(1,10)
        print(f"{m[i][j]:^2}",end=" ")
    print()
print()
linha = int(input("Digite uma linha que deseja guardar os elementos: "))

for i in range(10):
    v[i] = m[linha][i]
print(f"Os valores da linha guardada são: {v}")