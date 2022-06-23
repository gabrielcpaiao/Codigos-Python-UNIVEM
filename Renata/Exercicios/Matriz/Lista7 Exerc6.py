'''
7. Faça um programa em Python que gere as 5 notas (de 0 a 10) de 10 atletas em
uma competição. Armazene em uma matriz 10x5. Após, calcule a média de cada atleta
descartando a maior e menor nota obtida e diga qual atleta venceu a competição,
ou seja, o número da linha.
'''
from random import randint
notas = []
for i in range(10):
    notas.append([])
    for j in range(5):
        notas[i].append(randint(0,10))
    notas[i].sort()
    media = 0
    for j in range(1,4):
        media += notas[i][j]
    media /= 3
    notas[i].append(media)

maiorMedia = notas[0][5]
linha = 0
for i in range(1,10):
    if notas[i][5] > maiorMedia:
        maiorMedia = notas[i][5]
        linha = i
print(" N1  N2  N3  N4  N5     Média")
for i in range(10):
    for j in range(5):
        print(f"{notas[i][j]:3}", end= " ")
    if i == linha:
        print(f" >> {notas[i][5]:.2f} >> CAMPEÃO!!")
    else:
        print(f" >> {notas[i][5]:.2f}")
'''
from random import randint
m = [0]*10
print("Notas de cada aluno: ")
for i in range(10):
    m[i] = [0]*5
    for j in range(5):
        m[i][j] = randint(0,10)
        print(f"{m[i][j]:^2}", end=" ")
    print()
print()
r = []
maior = 0
menor = 10
for i in range(10):
    soma = 0
    for j in range(5):
        if (m[i][j] > maior):
            maior = m[i][j]
        if m[i][j] < menor:
            menor = m[i][j]
        if (m[i][j] != maior) or (m[i][j] != menor):
            soma += m[i][j]
    r[i] = soma

print(r)
print()
print("O atleta que venceu a competição foi: ")
maior = 0
for i in range(10):
    if m[i]> maior:
        maior = m[i]
print(maior)