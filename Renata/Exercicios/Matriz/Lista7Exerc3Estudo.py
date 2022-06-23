'''
Faça um programa em Python que gere uma matriz 5x5 com valores entre 1 e 50. Imprima a
matriz e troque uma linha por outra linha coluna informada pelo usuário. Mostre a matriz após
a troca.
'''
from random import randint
m = [0]*5
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        m[i][j] = randint(1,10)
        print(f"{m[i][j]:^2}",end=" ")
    print()
print()
linha = int(input("Digite o número de uma linha para trocar: "))
linha1 = int(input("Digite o número de outra linha para trocar: "))

for i in range(5):
    m[linha][i],m[linha1][i] = m[linha1][i],m[linha][i]
print()
print("Matriz modificada: ")
for i in range(5):
    for j in range(5):
        print(f"{m[i][j]:^2}",end=" ")
    print()