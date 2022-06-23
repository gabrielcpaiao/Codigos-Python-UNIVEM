'''
4. Faça um programa em Python que gere uma matriz 5x5 com valores entre 1 e 50.
Imprima a matriz e troque uma linha por uma coluna informada pelo usuário.
Mostre a matriz após a troca.
'''
from random import randint

print("Matriz gerada...")
M = [0] * 5
for i in range(5):
    M[i] = [0] * 5
    for j in range(5):
        M[i][j] = randint(1,50)
        print(f"{M[i][j]:2}", end=" ")
    print()

print("=" * 50)

while True:
    linha = int(input("Informe a linha que deseja trocar >> "))
    if linha in range(5):
        break
    print("Valor de linha inválida!! Digite um valor entre 0 e 4...")

while True:
    coluna = int(input("Informe a coluna que deseja trocar >> "))
    if coluna in range(5):
        break
    print("Valor de coluna inválida!! Digite um valor entre 0 e 4...")

#for i in range(5):
#    M[linha][i], M[i][coluna] = M[i][coluna], M[linha][i]

l = []
c = []
for i in range(5):
    l.append(M[linha][i])
    c.append(M[i][coluna])
for i in range(5):
    M[linha][i] = c[i]
    M[i][coluna] = l[i]

print("=" * 50)

print("Matriz alterada...")
for i in range(5):
    for j in range(5):
        print(f"{M[i][j]:2}", end=" ")
    print()