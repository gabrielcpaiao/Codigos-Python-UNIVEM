from random import randint
m = [0]*10
for i in range(10):
    m[i] = [0]*10
    for j in range(10):
        m[i][j] = randint(1,50)
for i in range(10):
    menor = 51
    for j in range(10):
        if m[j][i]< menor:
            menor = m[j][i]
    print(f"O menor número da coluna {i+1} é: {menor}")
for i in range(10):
    for j in range(10):
        print(f"{m[i][j]:^5}", end=" ")
    print()