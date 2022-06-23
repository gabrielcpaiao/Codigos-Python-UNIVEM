'''
Na teoria dos sistemas, define-se como elem... por Renata Aparecida de Carvalho Paschoal
Renata Aparecida de Carvalho Paschoal22:12
Na teoria dos sistemas, define-se como elemento minimax de uma matriz o menor elemento da linha onde se encontra o maior elemento
 da matriz. Escreva um programa em Python que gere uma matriz 10 X 10 de números aleatórios entre 1 e 99, imprima a matriz e enco
 ntre seu elemento minimax, imprimindo-o e mostrando também sua posição.
No exemplo acima:
Minimax = 2, na linha 2, coluna 1
'''
'''
from random import randint
M = [0] * 10
for i in range(10):
    M[i] = [0] * 10
    for j in range(10):
        M[i][j] = randint(1,99)
        print(f"{M[i][j]:2}", end=" ")
    print()

maior = M[0][0]
linha = 0
col = 0
for i in range(10):
    for j in range(10):
        if M[i][j] > maior:
            maior = M[i][j]
            linha = i
            col = j

print(f"O maior elemento da matriz é {maior} e se encontra na posição [{linha}][{col}]")

menor = M[linha][0]
col = 0
for i in range(10):
    if M[linha][i] < menor:
        menor = M[linha][i]
        col = i

print(f"Minimax da matriz é {menor} e se encontra na posição [{linha}][{col}]")
'''

from random import randint
m = [0]*5
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        m[i][j] = randint(1,99)
        print(f"{m[i][j]:^2}", end=" ")
    print()
print()
maior = 0
for i in range(5):
    for j in range(5):
        if m[i][j]> maior:
            maior = m[i][j]
            gravador = i

print()
print(f"O maior número dessa matriz é: {maior}")
print()

menor = 99
for i in range(5):
    if m[gravador][i] < menor:
        menor = m[gravador][i]
print()
print(f"O menor número da linha que está o maior número é: {menor}")
