'''
Faça um programa em Python que gere uma matriz 10 x 10 de inteiros e crie funções para
calcular e retornar o maior elemento de uma determinada coluna (informada por parâmetro) e o
menor elemento de uma determinada linha (informada por parâmetro). Peça a coluna e a linha,
chame os respectivos métodos e mostre o resultado
'''
from random import randint

m = [0]*10
print("A matriz gerada é: ")
for i in range(10):
    m[i] = [0]*10
    for j in range(10):
        m[i][j] = randint(1,10)
        print(f"{m[i][j]:^2}", end=" ")
    print()

def maiorElementoColuna():
    print("Digite a coluna para qual deseja encontrar o maior elemento: ")
    numColuna = int(input())
    maior = 0
    for i in range(10):
        if m[i][numColuna] > maior:
            maior = m[i][numColuna]
    return print(f"O maior elemento da coluna {numColuna} é: {maior}")

print()
maiorElementoColuna()

def menorElementorLinha():
    print("Digite a linha para qual deseja encontrar o menor elemento: ")
    numLinha = int(input())
    menor = 11
    for i in range(10):
        if m[numLinha][i] < menor:
            menor = m[numLinha][i]
    return print(f"O menor elemento da linha {numLinha} é: {menor}")

menorElementorLinha()