'''
Faça um programa em Python que gere as 5 notas (de 0 a 10) de 10 atletas em uma competição.
Armazene em uma matriz 10x5. Após, calcule a média de cada atleta descartando a maior e
menor nota obtida e diga qual atleta venceu a competição, ou seja, o número da linha
'''
from random import randint
m = [0]*10
resposta = []

for i in range(10):
    m[i] = [0]*5
    for j in range(5):
        x = randint(1,10)
        if x not in m[i]:
            m[i][j] = x
print()
for i in range(10):
    for j in range(5):
        print(f"{m[i][j]:^2}",end=" ")
    print()
print()
for i in range(10):
    soma = 0
    maior = 0
    menor = 10
    for j in range(5):
        if m[i][j] > maior:
            maior = m[i][j]
        elif m[i][j] < menor:
            menor = m[i][j]
        soma += m[i][j]
    x = (soma - menor - maior)//3
    resposta.append(x)
print()
print(f"Notas dos atletas: {resposta}")
print()
maior = 0
for i in range(10):
    if resposta[i] > maior:
        maior = resposta[i]
        posicao = i

print(f"O {posicao}º atleta foi quem obteve a maior nota!")