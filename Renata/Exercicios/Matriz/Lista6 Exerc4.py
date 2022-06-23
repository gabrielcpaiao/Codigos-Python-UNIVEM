from random import randint
m = [0]*10
for i in range(10):
    m[i] = [0]*10
    menor = 50
    for j in range(10):
        m[i][j] = randint(1,50)
        if m[i][j]<menor:
            menor = m[i][j]
    print(f"O menor valor da linha {i+1} é: {menor}")
for i in range(10):
    for j in range(10):
        print(f"{m[i][j]:^5}", end=" ")
    print()