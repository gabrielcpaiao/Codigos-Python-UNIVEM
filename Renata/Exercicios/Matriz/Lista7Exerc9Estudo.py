'''
Elabore um programa em Python que gere uma matriz aleatória (9x9), com números entre 0 e
10, imprima-a. Após, peça o quadrante desejado e imprima os elementos desse quadrante.
'''
from random import randint
m = [0]*9
for i in range(9):
    m[i] = [0]*9
    for j in range(9):
        m[i][j] = randint(1,5)
        if i == 4 or j == 4:
            m[i][j] = 0

print("A matriz gerada é: ")
print()
for i in range(9):
    for j in range(9):
        print(f"{m[i][j]:^2}",end=" ")
    print()
print()
x = int(input("Digite um quadrante (1 a 4) a ser imprimido na tela: "))
print()
if x == 1:
    for i in range(0,4):
        for j in range(5,9):
            print(f"{m[i][j]:^2}",end=" ")
        print()
if x == 2:
    for i in range(0,4):
        for j in range(0,4):
            print(f"{m[i][j]:^2}",end=" ")
        print()
if x == 3:
    for i in range(5,9):
        for j in range(0,4):
            print(f"{m[i][j]:^2}",end=" ")
        print()
if x == 4:
    for i in range(5,9):
        for j in range(5,9):
            print(f"{m[i][j]:^2}",end=" ")
        print()