from random import randint
m = [0]*9
for i in range(9):
    m[i] = [0]*9
    for j in range(9):
        m[i][j] = randint(0,10)
        print(f"{m[i][j]:^2}", end=" ")
    print()
print()
print("Digite um número entre 0 e 4: ")
while True:
    n = int(input())
    if 1<=n<=4:
        break
if n ==1:
    for i in range(4):
        for j in range(4):
            print(f"{m[i][j]:^2}", end=" ")
        print()

if n ==2:
    for i in range(4):
        for j in range(5, 9):
            print(f"{m[i][j]:^2}", end=" ")
        print()

if n ==3:
    for i in range(5, 9):
        for j in range(4):
            print(f"{m[i][j]:^2}", end=" ")
        print()

if n ==4:
    for i in range(5, 9):
        for j in range(5, 9):
            print(f"{m[i][j]:^2}", end=" ")
        print()

'''
9. Elabore um programa em Python que gere uma matriz aleatória (9x9),
com números entre 0 e 10, imprima-a. Após, peça o quadrante desejado
e imprima os elementos desse quadrante.

from random import randint

from termcolor import colored

m = [0] * 9
for i in range(9):
    m[i] = [0] * 9
    for j in range(9):
        m[i][j] = randint(0,10)
        if i == 4 or j == 4:
            print(colored(f"{m[i][j]:2}","blue"),end=" ")
        else:
            print(f"{m[i][j]:2}",end=" ")
    print()

while True:
    quadrante = int(input("\nInforme o quadrante [1-4] >> "))
    if quadrante in range(1,5):
        break
    print("Valor inválido!! Digite novamente...")

if quadrante == 1:
    for i in range(4):
        for j in range(4):
            print(f"{m[i][j]:2}", end=" ")
        print()
elif quadrante == 2:
    for i in range(4):
        for j in range(5,9):
            print(f"{m[i][j]:2}", end=" ")
        print()
elif quadrante == 3:
    for i in range(5,9):
        for j in range(4):
            print(f"{m[i][j]:2}", end=" ")
        print()
else:
    for i in range(5,9):
        for j in range(5,9):
            print(f"{m[i][j]:2}", end=" ")
        print()
'''