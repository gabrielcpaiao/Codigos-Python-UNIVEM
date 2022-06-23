from random import randint
m = [0]*4
for i in range(4):
    m[i] = [0]*6
    for j in range(6):
        m[i][j] = randint(1,10)
for i in range(4):
    for j in range(6):
        print(f"{m[i][j]:^5}", end=" ")
    print()
print()
t = [0]*6
for j in range(6):
    t[j] = [0]*4
    for i in range(4):
        t[j][i] = m[i][j]
        print(f"{t[j][i]:^5}",end=" ")
    print()