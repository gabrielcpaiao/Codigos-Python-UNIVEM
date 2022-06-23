m = [0]*2
soma = 0
for i in range(2):
    m[i] = [0]*3
    for j in range(3):
        m[i][j] = int(input(f"[{i}][{j}]: "))
for i in range(2):
    for j in range(3):
        print(f"{m[i][j]:^3}", end=" ")
        soma += m[i][j]
    print()
print(f"A soma de todos os elementos é: {soma}")