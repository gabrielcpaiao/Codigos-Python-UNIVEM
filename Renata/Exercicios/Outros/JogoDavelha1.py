#do italo
'''arr, cur, winner = [[0] * 3 for i in range(3)], 1, False
while not winner and (0 in arr[0] or 0 in arr[1] or 0 in arr[2]):
    for line in arr:
        print("|", end=" ")
        for c in line: print(" " if not c else "X" if c == 1 else "O", end=" | ")
        print("\b ")

    while True:
        y, x = map(int, input(f"Y,X JOGADOR {cur} >> ").split())
        if not 0 <= y <= 2 or not 0 <= x <= 2: print("Entrada invalida!")
        elif arr[y][x]: print("Posição já escolhida antes")
        else: break
    arr[y][x] = 1 if cur == 1 else -1
    varr = [[arr[j][i] for j in range(3)] for i in range(3)]
    sums = [arr[0][0] + arr[1][1] + arr[2][2], arr[0][2] + arr[1][1] + arr[2][0], sum(arr[0]), sum(arr[1]),
            sum(arr[2]), sum(varr[0]), sum(varr[1]), sum(varr[2])]

    if 3 in sums or -3 in sums:
        winner = True
        break
    else: cur = 2 if cur == 1 else 1
for line in arr:
    print("|", end=" ")
    for c in line: print(" " if not c else "X" if c == 1 else "O", end=" | ")
    print("\b ")

print("Empate" if not winner else f"Jogador {cur} ganhou")'''

#meu Gabriel Paião
