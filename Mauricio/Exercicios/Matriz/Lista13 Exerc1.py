from random import randint
m = [0]*8
for i in range(8):
    m[i] = [0]*8

lin = int(input(f"Digite a posição da linha para a peça (Torre): "))
col = int(input(f"Digite a posição da coluna para a peça (Torre): "))

for i in range(8):
    for j in range(8):
        if i+1 == lin or j+1 == col:
            m[i][j] = 1
for i in range(8):
    for j in range(8):
        print(f"{m[i][j]:^2}", end=" ")
    print()