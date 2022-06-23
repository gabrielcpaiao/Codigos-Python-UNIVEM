'''
Outro exerc
Faça um programa para gerar automaticamente números entre 1 e 75 de uma cartela de bingo. Sabendo que cada cartela deverá conter 5 linhas de
5 números, cartelas nas quais cada coluna contém 5 números e é associada a uma letra da palavra BINGO. Os números são dispostos nas 5 colunas
da cartela, divididos em grupos de 15 (por exemplo, na coluna B só aparecerão os números de 1 a 15) . O ponto central é o coringa. Gere estes
dados de modo a não ter números repetidos dentro das cartelas. O programa deve exibir na tela a cartela gerada.
'''

'''
from random import randint
from termcolor import colored

b = []
fim = 0
for i in range(5):
    ini = fim + 1
    fim = (i+1) * 15
    b.append([])
    while len(b[i]) != 5:
        numero = randint(ini, fim)
        if numero not in b[i]:
            b[i].append(numero)
bingo = []
for i in range(5):
    bingo.append([])
    for j in range(5):
        bingo[i].append(b[j][i])
print(colored(" B  I  N  G  O","red"))
bingo[2][2] = colored(" X","red")
for i in range(5):
    for j in range(5):
        print(f"{bingo[i][j]:2}", end=" ")
    print()

#outra solução

bingo = [0] * 5
for i in range(5):
    bingo[i] = [0] * 5

fim = 0
for i in range(5):
    b = []
    ini = fim + 1
    fim = (i+1) * 15
    while len(b) != 5:
        numero = randint(ini, fim)
        if numero not in b:
            b.append(numero)
    for j in range(5):
        bingo[j][i] = b[j]

print(colored("  B   I   N   G   O","red"))
bingo[2][2] = colored(" X ","red")
for i in range(5):
    for j in range(5):
        if j == 0:
            print(f"|{bingo[i][j]:3}|", end="")
        else:
            print(f"{bingo[i][j]:3}|", end="")
    print()
'''