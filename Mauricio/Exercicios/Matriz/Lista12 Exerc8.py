m = [0]*8
for i in range(8):
    m[i] = [0]*8
    for j in range(8):
        if (i+j)%2==0:
            m[i][j] = 0
        else:
            m[i][j] = 1
for i in range(8):
    for j in range(8):
        print(f"{m[i][j]:^5}", end=" ")
    print()
print()
print()
#outro
for i in range(8):
    m[i] = [0]*8
    for j in range(8):
        m[i][j] = (i+j)%2
for i in range(8):
    for j in range(8):
        print(f"{m[i][j]:^5}", end=" ")
    print()