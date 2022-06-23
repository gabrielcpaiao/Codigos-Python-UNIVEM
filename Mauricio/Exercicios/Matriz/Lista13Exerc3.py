m = [0]*8
for i in range(8):
    m[i] = [0]*8

lin = int(input(f"Digite a posição da linha para a peça (Cavalo): "))
lin -= 1
col = int(input(f"Digite a posição da coluna para a peça (Cavalo): "))
col -= 1
print()
#2 vertical 1 horizontal
#2 horizontal 1 vertical
for i in range(8):
    for j in range(8):
        if (i== lin-2 or i==lin+2) and (j==col-1 or j==col+1):
            m[i][j] = 1
        if (i == lin-1 or i== lin+1) and (j==col-2 or j == col+2):
            m[i][j] = 1

print()
for i in range(8):
    for j in range(8):
        print(f"{m[i][j]:^2}", end=" ")
    print()