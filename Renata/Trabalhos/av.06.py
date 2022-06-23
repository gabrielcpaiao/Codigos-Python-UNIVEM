#Gabriel Costa Paião (RA: 61876-4). Ciência da computação 1ºano, 1º etapa.
from random import randint
m = [0]*10
for i in range(10):
    m[i] = [0]*10
    for j in range(10):
        m[i][j] = randint(0,9)
print("A matriz gerada é: ")
print()
for i in range(10):
    for j in range(10):
        print(f"{m[i][j]:^2}", end=" ")
    print()
print()
print("Digite um número de três algorismos: ")
while True:
    n = int(input())
    if n<100 or n>1000:
        print("Digite um número válido.")
    else:
        break

print()

c = n//100
d = (n%100)//10
u = n%10

#Linhas esquerda para direita
for p in range(10):
    for q in range(8):
        if (m[p][q] == c) and (m[p][q+1] == d) and (m[p][q+2] == u):
            print(f"{p}{q} {p}{q+1} {p}{q+2}")

#Linhas direita para esquerda
for p in range(10):
    for q in range(7, -1, -1):
        if (m[p][q+2] == c) and (m[p][q+1] == d) and (m[p][q] == u):
            print(f"{p}{q+2} {p}{q+1} {p}{q}")

#Colunas cima para baixo
for p in range(10):
    for q in range(8):
        if (m[q][p] == c) and (m[q+1][p] == d) and (m[q+2][p] == u):
            print(f"{q}{p} {q+1}{p} {q+2}{p}")

#Colunas baixo para cima
for p in range(10):
    for q in range(7, -1, -1):
        if (m[q+2][p] == c) and (m[q+1][p] == d) and (m[q][p] == u):
            print(f"{q+2}{p} {q+1}{p} {q}{p}")

'''
#Professora:
from random import randint
m = []
for i in range(10):
    m.append([])
    for j in range(10):
        m[i].append(randint(0,9))
        print(f"{m[i][j]:2}",end=" ")
    print()

while True:
    num = int(input("\nInforme um número de 3 dígitos >> "))
    if num in range(100,1000):
        break
    print("Número inválido!! Informe novamente...")

c = num // 100
d = num % 100 // 10
u = num % 10

existe = False
for i in range(10):
    for j in range(10):
        if m[i][j] == c:
            if j < 8 and m[i][j+1] == d and m[i][j+2] == u:
                print(f"Linha: {i} Colunas: {j} {j+1} {j+2}")
                existe = True
                break
            if j > 1 and m[i][j-1] == d and m[i][j-2] == u:
                print(f"Linha: {i} Colunas: {j} {j -1} {j - 2}")
                existe = True
                break
            if i > 1 and m[i-1][j] == d and m[i-2][j] == u:
                print(f"Coluna: {j} Linhas: {i} {i - 1} {i - 2}")
                existe = True
                break
            if i < 8 and m[i+1][j] == d and m[i+2][j] == u:
                print(f"Coluna: {j} Linhas: {i} {i + 1} {i + 2}")
                existe = True
                break
    if existe:
        break
if not existe:
    print("Número não encontrado!!")
'''