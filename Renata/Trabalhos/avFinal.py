#Gabriel Costa Paião (RA: 61876-4). UNIVEM 2021. Ciência da Computação (1º ano 1º etapa).

from random import randint

v = [0]*4
for i in range(4):
    v[i] = randint(1,4)

print(v)

x = [0]*10

for a in range(10):
    x[a] = [0] * 4
    cont = 1
    while 1 <= cont <= 4:
        print(f"Digite o {cont}º número entre um e quatro [1,4]: ")
        n = int(input())
        print()
        if 1 <= n <= 4:
            x[a][cont-1] = n
            cont += 1
        else:
            print("Número inválido. Digite um valor entre 1 e 4.")
    print()
    print(f"Números que o usuário digitou:")
    print(f"{x[a][0]} {x[a][1]} {x[a][2]} {x[a][3]}")
    print()
    posicao = 0
    qntd = 0
    Valores = v.copy()
    for c in range(4):
        if x[a][c] in Valores:
            Valores.remove(x[a][c])
            qntd += 1
        if x[a][c] == v[c]:
            posicao += 1
    print(f"Você acertou {qntd} números dos 4 sorteados e acertou a posição de {posicao} destes números.")
    print()

    ganhou = True

    if qntd == posicao == 4:
        ganhou = False
        break

if ganhou:
    print("Você não conseguiu acertar os 4 números nas posições corretas!!")