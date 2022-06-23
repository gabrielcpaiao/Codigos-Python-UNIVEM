from random import randint
m = [0]*10
for i in range(10):
    soma = 0
    m[i] = [0]*10
    for j in range(10):
        m[i][j] = randint(1, 50)
        soma += m[i][j]
    print(f"A soma da {i+1}º linha é: {soma}")
for i in range(10):
    for j in range(10):
        print(f"{m[i][j]:^5}", end=" ")
    print()