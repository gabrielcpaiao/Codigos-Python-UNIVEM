
'''
Gerar um matriz 5x5 com números aleatórios de 1 a 99, sem números repetidos

from random import randint
matriz = []
vetor = []
i = 0
while len(matriz) != 5:
    matriz.append([])
    while len(matriz[i]) != 5:
        n = randint(1,99)
        if n not in vetor:
            vetor.append(n)
            matriz[i].append(n)
    i += 1
print(vetor)
for i in range(5):
    for j in range(5):
        print(f"{matriz[i][j]:2}",end=" ")
    print()

#Outra solução
vetor = []
while len(vetor) != 25:
    n = randint(1,99)
    if n not in vetor:
        vetor.append(n)

matriz = []
c = 0
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(vetor[c])
        c += 1
print(vetor)
for i in range(5):
    for j in range(5):
        print(f"{matriz[i][j]:2}",end=" ")
    print()


6. Elabore um programa em Python que gere uma matriz 5x5 e
calcule e mostre a diagonal principal e a secundária.

from random import randint

mat = []
for i in range(5):
    mat.append([])
    for j in range(5):
        mat[i].append(randint(1,50))
        print(f"{mat[i][j]:2}",end = " ")
    print()

print("Diagonal Principal")
for i in range(5):
    print(f"{mat[i][i]:2}", end=" ")

#Imprimindo a diagonal principal com a saída na diagonal

for i in range(5):
    for j in range(5):
        if i == j:
            print(f"{mat[i][i]:2}", end=" ")
        else:
            print("  ", end=" ")
    print()

print("\nDiagonal Secundária")
for i in range(5):
    print(f"{mat[i][4-i]:2}", end=" ")

#Imprimindo a diagonal secundária com a saída na diagonal

for i in range(5):
    for j in range(5):
        if i + j == 4:
            print(f"{mat[i][i]:2}", end=" ")
        else:
            print("  ", end=" ")
    print()

print("\nTriângulo superior direito em relação a diagonal principal")
for i in range(4):
    for j in range(i+1,5):
        print(f"{mat[i][j]:2}", end=" ")

#Imprimindo o triângulo mostrando na posição do triângulo

for i in range(4):
    for j in range(5):
        if j > i:
            print(f"{mat[i][j]:2}", end=" ")
        else:
            print("  ", end=" ")
    print()
'''

from random import randint
v = [0]*5
for i in range(5):
    v[i] = [0]*5
    for j in range(5):
        v[i][j] = randint(1,50)

for i in range(5):
    for j in range(5):
        print(f"{v[i][j]:^5}",end=" ")
    print()
#diagonal principal e secundária
print()
for i in range(5):
    for j in range(5):
        if i==j:
            print(f"{v[i][j]:2}", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
for i in range(5):
    for j in range(5):
        if i+j==4:
            print(f"{v[i][j]:2}", end=" ")
        else:
            print(" ", end=" ")
    print()