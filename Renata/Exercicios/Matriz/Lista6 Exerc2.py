from random import randint
m = [0]*10
soma = 0
for i in range(10):
    m[i] = [0]*10
    for j in range(10):
        m[i][j] = randint(1, 50)
        soma += m[i][j]
for i in range(10):
    for j in range(10):
        print(f"{m[i][j]:^5}", end=" ")
    print()
print(f"A média dos elementos é: {soma/100}")