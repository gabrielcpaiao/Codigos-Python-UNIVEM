'''
. Faça um programa em Python que gere uma matriz 10x3 com números aleatórios de 1 a 9, onde
cada linha representa os lados de um triangulo. Imprima para cada linha, qual tipo ele é:
equilátero (todos lados iguais), isósceles (2 lados iguais) ou escaleno (3 lados diferentes). Não
precisa validar se forma um triângulo
'''
from random import randint
m = [0]*10
for i in range(10):
    m[i] = [0]*3
    for j in range(3):
        m[i][j] = randint(1,9)

for i in range(10):
    for j in range(3):
        print(f"{m[i][j]:^2}", end=" ")
    print()
print()
for i in range(10):
    if m[i][0] != m[i][1] != m[i][2]:
        print(f"O {i+1}º triângulo é escaleno!")
    elif m[i][0] == m[i][1] == m[i][2]:
        print(f"O {i+1}º triângulo é equilátero!")
    elif m[i][0] == m[i][1] or m[i][0] == m[i][2] or m[i][1] == m[i][2]:
        print(f"O {i+1}º triângulo é isóceles!")