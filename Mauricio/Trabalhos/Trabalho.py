import random
vitoriaA = 0
vitoriaB = 0
vitoriaC = 0
while(True):
    a = random.randint(1, 2)
    A = print(f"O PRIMEIRO jogador escolheu {a}")
    b = random.randint(1, 2)
    B = print(f"O SEGUNDO jogador escolheu {b}")
    c = random.randint(1, 2)
    C = print(f"O TERCEIRO jogador escolheu {c}")
    if(a==b and a!=c):
        vitoriaC += 1
        print("Nesta rodada o vencedor foi o TERCEIRO jogador")
        if(vitoriaC == 3):
            print("O TERCEIRO jogador conseguiu fazer 3 vitórias antes dos outros jogadores. Ele é o vencedor!")
            break
    elif(a==c and a!=b):
        vitoriaB += 1
        print("Nesta rodada o vencedor foi o SEGUNDO jogador")
        if (vitoriaB==3):
            print("O SEGUNDO jogador conseguiu fazer 3 vitórias antes dos outros jogadores. Ele é o vencedor!")
            break
    elif(b==c and b!=a):
        vitoriaA += 1
        print("Nesta rodada o vencedor foi o PRIMEIRO jogador")
        if(vitoriaA==0):
            print("O PRIMEIRO jogador conseguiu fazer 3 vitórias antes dos outros jogadores. Ele é o vencedor!")
            break
    elif (a==b==c):
        print("Deu empate. Jogue novamente!")