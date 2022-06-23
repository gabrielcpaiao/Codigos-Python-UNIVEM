from random import randint
m = [0]*4
for i in range(4):
    m[i] = [0]*6
    for j in range(6):
        m[i][j] = randint(1,10)
        print(f"{m[i][j]:^2}",end=" ")
    print()
print()
print("Matriz transposta: ")
print()
v = [0]*6
for i in range(6):
    v[i] = [0]*4
    for j in range(4):
        v[i][j] = m[j][i]
        print(f"{v[i][j]:^2}",end=" ")
    print()