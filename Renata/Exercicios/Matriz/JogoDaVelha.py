print("Para o jogador 1, será utilizado X.")
print("Para o jogador 2, será utilizado y.")
print()
print("Início: ")
m = [0]*3
for i in range(3):
    m[i] = [0]*3
    for j in range(3):
        print(f"{m[i][j]:^2}",end=' ')
    print()

while True:
    print()
    while True:
        print("Digite valores entre 1 e 3.")
        jogador1Linha = int(input("Para o jogador 1 digite a coordenada da linha: "))
        jogador1Colunaa = int(input("Para o jogador 1 digite a coordenada da coluna: "))
        if m[jogador1Linha-1][jogador1Colunaa-1] != 'X' and m[jogador1Linha-1][jogador1Colunaa-1] != 'Y':
            m[jogador1Linha-1][jogador1Colunaa-1] = 'X'
            break
        else:
            print("Esta posição já está ocupada!")
    print()
    for i in range(3):
        for j in range(3):
            print(f"{m[i][j]:^2}", end=' ')
        print()
    print()
    if (m[0][0] =='X' and m[0][1] =='X' and m[0][2] =='X') or (m[1][0] =='X' and m[1][1] =='X' and m[1][2] =='X') or (m[2][0] =='X' and m[2][1] =='X' and m[2][2] =='X'):
        print("O jogador 1 ganhou!")
        break
    elif (m[0][0] =='Y' and m[0][1] =='Y' and m[0][2] =='Y') or (m[1][0] =='Y' and m[1][1] =='Y' and m[1][2] =='Y') or (m[2][0] =='Y' and m[2][1] =='Y' and m[2][2] =='Y'):
        print("O jogador 2 ganhou!")
        break
    elif (m[0][0] =='X' and m[1][0] =='X' and m[2][0] =='X') or (m[0][1] =='X' and m[1][1] =='X' and m[2][1] =='X') or (m[0][2] =='X' and m[1][2] =='X' and m[2][2] =='X'):
        print("O jogador 1 ganhou!")
        break
    elif (m[0][0] =='Y' and m[1][0] =='Y' and m[2][0] =='Y') or (m[0][1] =='Y' and m[1][1] =='Y' and m[2][1] =='Y') or (m[0][2] =='Y' and m[1][2] =='Y' and m[2][2] =='Y'):
        print("O jogador 2 ganhou!")
        break
    elif (m[0][0] =='X' and m[1][1] =='X' and m[2][2] =='X'):
        print("O jogador 1 ganhou!")
        break
    elif (m[0][0] =='Y' and m[1][1] =='Y' and m[2][2] =='Y'):
        print("O jogador 2 ganhou!")
        break
    while True:
        print("Digite valores entre 1 e 3.")
        jogador2Linha = int(input("Para o jogador 2 digite a coordenada da linha: "))
        jogador2Colunaa = int(input("Para o jogador 2 digite a coordenada da coluna: "))
        if m[jogador2Linha-1][jogador2Colunaa-1] != 'X' and m[jogador2Linha-1][jogador2Colunaa-1] != 'Y':
            m[jogador2Linha-1][jogador2Colunaa-1] = 'Y'
            break
        else:
            print("Esta posição já está ocupada!")
    print()
    for i in range(3):
        for j in range(3):
            print(f"{m[i][j]:^2}", end=' ')
        print()
    if (m[0][0] =='X' and m[0][1] =='X' and m[0][2] =='X') or (m[1][0] =='X' and m[1][1] =='X' and m[1][2] =='X') or (m[2][0] =='X' and m[2][1] =='X' and m[2][2] =='X'):
        print("O jogador 1 ganhou!")
        break
    elif (m[0][0] =='Y' and m[0][1] =='Y' and m[0][2] =='Y') or (m[1][0] =='Y' and m[1][1] =='Y' and m[1][2] =='Y') or (m[2][0] =='Y' and m[2][1] =='Y' and m[2][2] =='Y'):
        print("O jogador 2 ganhou!")
        break
    elif (m[0][0] =='X' and m[1][0] =='X' and m[2][0] =='X') or (m[0][1] =='X' and m[1][1] =='X' and m[2][1] =='X') or (m[0][2] =='X' and m[1][2] =='X' and m[2][2] =='X'):
        print("O jogador 1 ganhou!")
        break
    elif (m[0][0] =='Y' and m[1][0] =='Y' and m[2][0] =='Y') or (m[0][1] =='Y' and m[1][1] =='Y' and m[2][1] =='Y') or (m[0][2] =='Y' and m[1][2] =='Y' and m[2][2] =='Y'):
        print("O jogador 2 ganhou!")
        break
    elif (m[0][0] =='X' and m[1][1] =='X' and m[2][2] =='X'):
        print("O jogador 1 ganhou!")
        break
    elif (m[0][0] =='Y' and m[1][1] =='Y' and m[2][2] =='Y'):
        print("O jogador 2 ganhou!")
        break