m = [0]*5
for i in range(5):
    m[i] = [0]*5
    for j in range(5):
        if i==0 or j==0:
            m[i][j] = 0
        else:
            m[i][j] = (i*j)
for i in range(5):
    for j in range(5):
        print(f"{m[i][j]:^5}", end=" ")
    print()