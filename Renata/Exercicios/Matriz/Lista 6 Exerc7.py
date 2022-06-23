from random import randint
v = [0]*4
for i in range(4):
    v[i] = [0]*6
    for j in range(6):
        v[i][j] = randint(1,50)
print("A matriz gerada é: ")
print()
for i in range(4):
    for j in range(6):
        print(f"{v[i][j]:^5}", end=" ")
    print()
print()
print("A matriz transposta é: ")
print()
t = [0]*6
for i in range(6):
    t[i] = [0]*4
    for j in range(4):
        t[i][j] , v[j][i] = v[j][i], t[i][j]
        print(f"{t[i][j]:^5}", end=" ")
    print()