from random import randint
m = [0]*5
print("A matriz gerada é: ")
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        m[i][j] = randint(1,50)
        print(f"{m[i][j]:^2}", end=" ")
    print()
print(m)
#Trocar elementos diagonal principal pela secundária
for i in range(5):
    m[i][i], m[i][4-i] = m[i][4-i], m[i][i]


print()
print("A matriz trocada suas diagonais é:")
for i in range(5):
    for j in range(5):
        print(f"{m[i][j]:^2}", end=" ")
    print()