from random import randint
m = [0]*5
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        m[i][j] = randint(1,2)
for i in range(5):
    for j in range(5):
        print(f"{m[i][j]:^5}", end=" ")
    print()
print()
simetria = True
for i in range(5):
    for j in range(5):
        if m[i][j] != m[j][i]:
            simetria = False
            break
if simetria:
    print("Esta matriz é simétrica")
else:
    print("Esta matriz não é simétrica")
'''
for i in range(5):
    for j in range(5):
        if m[i][j] != m[j][i]:
            print("Esta matriz não é simétrica")
            break
'''
'''
t = [0]*5
for j in range(5):
    t[j] = [0]*5
    for i in range(5):
        t[j][i] = m[i][j]
        print(f"{t[j][i]:^5}",end=" ")
    print()
'''